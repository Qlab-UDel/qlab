#  SIT ACCURACY ANALYSIS
#  Violet Kozloff
#  April 17, 2018
#  This script analyzes structured and random blocks across two visual tasks, letters and images.
#  It measures the mean reaction time and the slope of the reaction time for each participant for each condition.
#  It also runs an ANOVA to compare reaction time slope between tasks, modalities, and domains.
# NOTE: Does not remove points outside 2.5 stdev of mean
# NOTE: relevant columns pre-selected through this experiment's version of fmri_data_cleaning.Rmd
#  ****************************************************************************


# ******************** I. PREPARE FILES *************************

# Prepare workspace ------------------------------------------------------------------------------------------------------

# Move to folder from GitHub (Mac when folder is on desktop)
setwd("/Users/qlab_macbook/Documents/qlab/analysis/sit-analysis/")

# Remove objects in environment
rm(list=ls())


# Prepare paths for files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#For use on Mac 
input_path <- ("../../../sit_data/clean/")


# List all files---------------------------------------------------------------------------------------------------------------------------------------------------------------------

files <- list.files(path=input_path, pattern = ".csv")

#Remove the underscores in file names
all_files <- gsub("_", "", files)

# Read in auditory files and combine them into one data frame--------------------------------------------------------------------------------------------------------------------------------------------

# Prepare auditory_data_frame to hold the files you're reading in
complete_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(input_path, file, sep="")))
    #complete_data_frame <- merge(complete_data_frame, read_file)
}

# Combine each file with the previous files into auditory_data_frame
for (file in all_files){complete_data_frame <- append(complete_data_frame, list(eval(parse(text=file))))}
#complete_data_frame <- do.call(rbind.data.frame, complete_data_frame)
complete_data_frame <- do.call(merge (complete_data_frame))#, by.x=c("part_id"))






# List files---------------------------------------------------------------------------------------------------------------------------------------------------------------------

all_files <- list.files(path=input_path, pattern = ".csv")

files <- gsub("_", "", all_files)


# Read in auditory files and combine them into one data frame--------------------------------------------------------------------------------------------------------------------------------------------

# Prepare auditory_data_frame to hold the files you're reading in
complete_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in all_files)
{
  assign(
    gsub("_", "", file),
    read.csv(paste(input_path, file, sep="")))
}

# Combine each file with the previous files into auditory_data_frame
for (file in all_files){complete_data_frame <- append(complete_data_frame, list(eval(parse(text=file))))}
complete_data_frame <- do.call(rbind.data.frame, complete_data_frame)






# combine rt columns for lv and vl df$x <- paste(df$n,df$s)


# ******************** II. FIND ACCURACY *************************

# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(complete_data_frame$PartID)

# List unique tasks for this condition
list_tasks <- lapply(unique(complete_data_frame$task), as.character)

# Separate ll, lv, vl, vv
ll <- (complete_data_frame[ which(complete_data_frame$expName=="ll"),])
lv <- (complete_data_frame[ which(complete_data_frame$expName=="lv"),])
vl <- (complete_data_frame[ which(complete_data_frame$expName=="vl"),])
vv <- (complete_data_frame[ which(complete_data_frame$expName=="vv"),])

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
modality1 <- NULL
modality2 <- NULL
task<- NULL


# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  for (t in list_tasks){
    if (t=="ll"){
      modality1 <- append (modality1, "linguistic")
      modality2 <- append (modality2, "linguistic")}
   if (t=="lv"){
      modality1 <- append (modality1, "linguistic")
      modality2 <- append (modality2, "non-linguistic")}
   if (t=="vl"){
      modality1 <- append (modality1, "non-linguistic")
      modality2 <- append (modality2, "linguistic")}
   if (t=="vv"){
      modality1 <- append (modality1, "non-linguistic")
      modality2 <- append (modality2, "non-linguistic")}
    part_id <- append(part_id, id)
    task <- append(task, as.character(t))
    accuracy <- append(accuracy, round(mean(complete_data_frame[ which(complete_data_frame$PartID==id 
                                                                       & complete_data_frame$task== t), ]$key_resp.corr), digits =3))
  }
}

# Combine data for each participant
indiv_auditory_accuracies <- data.frame(part_id, task, domain, modality, accuracy)


# ******************** III. FIND VISUAL ACCURACY *************************

# visual: Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(visual_data_frame$PartID)

# List unique tasks for this condition
list_tasks <- lapply(unique(visual_data_frame$task), as.character)

# Separate lsl and vsl
lsl <- (visual_data_frame[ which(visual_data_frame$task=="lsl"),])
vsl <- (visual_data_frame[ which(visual_data_frame$task=="vsl"),])

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
domain <- NULL
modality <- NULL
type <- NULL
task<- NULL

# visual_data_frame$accuracy <- as.factor(visual_data_frame$accuracy)


# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  for (t in list_tasks){
    if (t=="LSL"){
      modality <- append (modality, "linguistic")}
    if (t=="VSL")
    {modality <- append (modality, "non-linguistic")}
    part_id <- append(part_id, id)
    domain <- append(domain, "visual")
    task <- append(task, as.character(t))
    accuracy <- append(accuracy, round(mean(visual_data_frame[ which(visual_data_frame$PartID==id 
                                                                     & visual_data_frame$task== t), ]$key_resp.corr), digits =3))
  }
}

# Combine data for each participant
indiv_visual_accuracies <- data.frame(part_id, task, domain, modality, accuracy)

# Combine individual visual and auditory accuracies into one data frame
indiv_accuracies <- data.frame(rbind(indiv_auditory_accuracies, indiv_visual_accuracies))

# Write individual accuracies to output file
setwd("../output_files/")
write.csv(indiv_accuracies, "4_runs_pilot_accuracy_indiv.csv")

