#  6_RUNS ACCURACY ANALYSIS
#  Violet Kozloff
#  April 7. 2018
#  This script analyzes structured and random blocks across four tasks: auditory (speech and tones) and visual (letters and images).
#  It measures the mean reaction time and the slope of the reaction time for each participant for each condition.
#  It also runs an ANOVA to compare reaction time slope between tasks, modalities, and domains.
# NOTE: f002_auditory_6 has been modified to reflect the correct participant id
# NOTE: Does not remove points outside 2.5 stdev of mean
# NOTE: relevant columns pre-selected through this experiment's version of fmri_data_cleaning.Rmd
#  ****************************************************************************


# ******************** I. PREPARE FILES *************************

# Prepare workspace ------------------------------------------------------------------------------------------------------

# Move to folder from GitHub (Mac when folder is on desktop)
setwd("/Users/jasinskagroup/Desktop/QLAB/psychopy_sl_beh-master/accuracy/6_runs/scripts")

# Remove objects in environment
rm(list=ls())


# Prepare paths for files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#For use on Mac 
auditory_path <- ("../cleaned_data/auditory/")
visual_path <- ("../cleaned_data/visual/")


# List auditory and visual files---------------------------------------------------------------------------------------------------------------------------------------------------------------------

afiles <- list.files(path=auditory_path, pattern="*.csv")
vfiles <- list.files(path=visual_path, pattern = ".csv")

#Remove the underscores in file names
auditory_files <- gsub("_", "", afiles)
visual_files <- gsub("_", "", vfiles)


# Read in auditory files and combine them into one data frame--------------------------------------------------------------------------------------------------------------------------------------------

# Prepare auditory_data_frame to hold the files you're reading in
auditory_data_frame<-list()

# Remove the dashes in each file name read it in
for(auditory_file in afiles)
{
  assign(
    gsub("_", "", auditory_file),
    read.csv(paste(auditory_path, auditory_file, sep="")))
}

# Combine each file with the previous files into auditory_data_frame
for (afile in auditory_files){auditory_data_frame <- append(auditory_data_frame, list(eval(parse(text=afile))))}
auditory_data_frame <- do.call(rbind.data.frame, auditory_data_frame)


# Prepare auditory files for use----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rename expName column as "domain"
names(auditory_data_frame)[names(auditory_data_frame) == 'expName'] <- 'domain'


# Read in visual files and combine them into one data frame------------------------------------------------------------------------------------------------------

# Prepare visual_data_frame to hold the files you're reading in
visual_data_frame <- data.frame()
visual_data_frame<-list()

# Remove the dashes from each file name and read it in
for(visual_file in vfiles)
{
  assign(
    gsub("_", "", visual_file),
    read.csv(paste(visual_path, visual_file, sep="")))
  }

#Combine the visual files into visual_data_frame
for (vfile in visual_files){visual_data_frame <- append(visual_data_frame, list(eval(parse(text=vfile))))}
visual_data_frame <- do.call(rbind.data.frame, visual_data_frame)
  
# Rename expName column as 'domain'
names(visual_data_frame)[names(visual_data_frame) == 'expName'] <- 'domain'


# ******************** II. FIND AUDITORY ACCURACY *************************

# Auditory: Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(auditory_data_frame$PartID)

# List unique tasks for this condition
list_tasks <- lapply(unique(auditory_data_frame$task), as.character)

# Separate SSL and TSL
ssl <- (auditory_data_frame[ which(auditory_data_frame$task=="SSL"),])
tsl <- (auditory_data_frame[ which(auditory_data_frame$task=="TSL"),])

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
domain <- NULL
modality <- NULL
type <- NULL
task<- NULL

# auditory_data_frame$accuracy <- as.factor(auditory_data_frame$accuracy)


# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  for (t in list_tasks){
    if (t=="SSL"){
      modality <- append (modality, "linguistic")}
    if (t=="TSL")
      {modality <- append (modality, "non-linguistic")}
    part_id <- append(part_id, id)
    domain <- append(domain, "auditory")
    task <- append(task, as.character(t))
    accuracy <- append(accuracy, round(mean(auditory_data_frame[ which(auditory_data_frame$PartID==id 
                                                                       & auditory_data_frame$task== t), ]$key_resp.corr), digits =3))
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

setwd("../output_files/")
write.csv(indiv_accuracies, "6_runs_pilot_accuracy_indiv.csv")

