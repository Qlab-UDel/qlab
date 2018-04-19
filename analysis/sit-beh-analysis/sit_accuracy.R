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
setwd("/Users/qlab_macbook/Documents/qlab/analysis/sit-beh-analysis/")

# Remove objects in environment
rm(list=ls())


# Prepare paths for files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#For use on Mac 
ll_input <- ("../../../sit_data/clean/ll_clean/")
lv_input <- ("../../../sit_data/clean/lv_clean/")
vl_input <- ("../../../sit_data/clean/vl_clean/")
vv_input <- ("../../../sit_data/clean/vv_clean/")

# Read in ll files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

ll_underscore_files <- list.files(path=ll_input, pattern = ".csv")

#Remove the underscores in file names
ll_files <- gsub("_", "", ll_underscore_files)

# Prepare data_frame to hold the files you're reading in
ll_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in ll_underscore_files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(ll_input, file, sep="")))
}

# Combine each file with the previous files into ll_data_frame
for (file in ll_files){ll_data_frame <- append(ll_data_frame, list(eval(parse(text=file))))}
ll_data_frame <- do.call(rbind.data.frame, ll_data_frame)


# Read in lv files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

lv_underscore_files <- list.files(path=lv_input, pattern = ".csv")

#Remove the underscores in file names
lv_files <- gsub("_", "", lv_underscore_files)

# Prepare data_frame to hold the files you're reading in
lv_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in lv_underscore_files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(lv_input, file, sep="")))
}

# Combine each file with the previous files into lv_data_frame
for (file in lv_files){lv_data_frame <- append(lv_data_frame, list(eval(parse(text=file))))}
lv_data_frame <- do.call(rbind.data.frame, lv_data_frame)


# Read in vl files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

vl_underscore_files <- list.files(path=vl_input, pattern = ".csv")

#Remove the underscores in file names
vl_files <- gsub("_", "", vl_underscore_files)

# Prepare data_frame to hold the files you're reading in
vl_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in vl_underscore_files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(vl_input, file, sep="")))
}

# Combine each file with the previous files into vl_data_frame
for (file in vl_files){vl_data_frame <- append(vl_data_frame, list(eval(parse(text=file))))}
vl_data_frame <- do.call(rbind.data.frame, vl_data_frame)


# Read in vv files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

vv_underscore_files <- list.files(path=vv_input, pattern = ".csv")

#Remove the underscores in file names
vv_files <- gsub("_", "", vv_underscore_files)

# Prepare data_frame to hold the files you're reading in
vv_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in vv_underscore_files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(vv_input, file, sep="")))
}

# Combine each file with the previous files into vv_data_frame
for (file in vv_files){vv_data_frame <- append(vv_data_frame, list(eval(parse(text=file))))}
vv_data_frame <- do.call(rbind.data.frame, vv_data_frame)




# ******************** II. FIND lv ACCURACY *************************

# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(lv_data_frame$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task<- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "lv")
  #accuracy <- append(accuracy, round(mean(lv_data_frame[ which(lv_data_frame$PartID==id), ]$corr_resp, na.rm=TRUE), digits =3),)
  accuracy <- append(accuracy, round(mean(lv_data_frame[which(lv_data_frame$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
  }
  
# Combine data for each participant
indiv_lv_accuracies <- data.frame(part_id, task, accuracy)

# ******************** III. FIND ll ACCURACY *************************

# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(ll_data_frame$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task<- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "ll")
  #accuracy <- append(accuracy, round(mean(ll_data_frame[ which(ll_data_frame$PartID==id), ]$corr_resp, na.rm=TRUE), digits =3),)
  accuracy <- append(accuracy, round(mean(ll_data_frame[which(ll_data_frame$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_ll_accuracies <- data.frame(part_id, task, accuracy)

# ******************** IV. FIND vv ACCURACY *************************

# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(vv_data_frame$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task<- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "vv")
  #accuracy <- append(accuracy, round(mean(vv_data_frame[ which(vv_data_frame$PartID==id), ]$corr_resp, na.rm=TRUE), digits =3),)
  accuracy <- append(accuracy, round(mean(vv_data_frame[which(vv_data_frame$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_vv_accuracies <- data.frame(part_id, task, accuracy)


# ******************** V. FIND vl ACCURACY *************************

# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(vl_data_frame$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task<- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "vl")
  #accuracy <- append(accuracy, round(mean(vl_data_frame[ which(vl_data_frame$PartID==id), ]$corr_resp, na.rm=TRUE), digits =3),)
  accuracy <- append(accuracy, round(mean(vl_data_frame[which(vl_data_frame$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_vl_accuracies <- data.frame(part_id, task, accuracy)

View(indiv_ll_accuracies)
View(indiv_lv_accuracies)

# Write individual accuracies to output file
#setwd("../output_files/")
#write.csv(indiv_accuracies, "4_runs_pilot_accuracy_indiv.csv")

