#  SIT ACCURACY EXTRACTION
#  Violet Kozloff
#  Adapted from analysis scripts by An Nguyen
#  Last modified October 4th, 2019
#  This script finds two-alternative forced-choice task accuracies for statistical learning tasks involving structured and random triplets of letters and images
#  NOTE: relevant columns have been pre-selected through sit_cleaning.R
#  ****************************************************************************



# ******************** I. PREPARE FILES *************************


# Prepare workspace ------------------------------------------------------------------------------------------------------

# Install packages
install.packages("reshape")
install.packages("dplyr")
install.packages("corrplot")
library ("plyr")
library("reshape")
library("dplyr")
library("corrplot")

# Remove objects in environment
rm(list=ls())

# Read in picture vocabulary scores --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
picture_vocab <- read.csv("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vocab_clean/vocab_clean.csv")


# Read in ll files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/ll_clean")
ll_files <- list.files(pattern=("*.csv"))
ll_data <- NULL

for (file in ll_files)
{
  current_file <- read.csv(file)
  ll_data <- rbind.fill (ll_data, current_file)
}

# Read in lv files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/lv_clean")
lv_files <- list.files(pattern=("*.csv"))
lv_data <- NULL

for (file in lv_files)
{
  current_file <- read.csv(file)
  lv_data <- rbind.fill (lv_data, current_file)
}

# Read in vl files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vl_clean")
vl_files <- list.files(pattern=("*.csv"))
vl_data <- NULL

for (file in vl_files)
{
  current_file <- read.csv(file)
  vl_data <- rbind.fill (vl_data, current_file)
}


# Read in vv files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vv_clean")
vv_files <- list.files(pattern=("*.csv"))
vv_data <- NULL

for (file in vv_files)
{
  current_file <- read.csv(file)
  vv_data <- rbind.fill (vv_data, current_file)
}

# Set working directory
setwd("/Volumes/data/projects/completed_projects/sit/analysis")


# ******************** FIND ACCURACY FOR LV FILES *************************

# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(lv_data$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task <- NULL
same_or_diff <-NULL
test_phase <- NULL

# For each participant, extract id
# Assign domain, same_or_diff, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "lv")
  same_or_diff <- append(same_or_diff, "different")
  test_phase <- append (test_phase, "lsl")
  accuracy <- append(accuracy, round(mean(lv_data[which(lv_data$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_lv_accuracies <- data.frame(part_id, task, same_or_diff, test_phase, accuracy)

# TEST: There should be 32 entries
length(indiv_lv_accuracies$part_id)

# TEST: All entries should all have an accuracy value
View(indiv_lv_accuracies)



# ******************** III. FIND ll ACCURACY *************************


# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(ll_data$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task <- NULL
same_or_diff <-NULL
test_phase <- NULL

# For each participant, extract id
# Assign domain, same_or_diff, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "ll")
  same_or_diff <- append(same_or_diff, "same")
  test_phase <- append (test_phase, "lsl")
  accuracy <- append(accuracy, round(mean(ll_data[which(ll_data$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_ll_accuracies <- data.frame(part_id, task, same_or_diff, test_phase, accuracy)

# TEST: There should be 32 entries
length(indiv_ll_accuracies$part_id)

# TEST: All entries should all have an accuracy value
 View(indiv_ll_accuracies)



# ******************** V. FIND VL ACCURACY *************************


# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(vl_data$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task<- NULL
same_or_diff <-NULL
test_phase <- NULL

# For each participant, extract id
# Assign domain, same_or_diff, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "vl")
  same_or_diff <- append(same_or_diff, "different")
  test_phase <- append (test_phase, "vsl")
  accuracy <- append(accuracy, round(mean(vl_data[which(vl_data$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_vl_accuracies <- data.frame(part_id, task, same_or_diff, test_phase, accuracy)

# TEST: There should be 32 entries
length(indiv_vl_accuracies$part_id)

# TEST: All entries should all have an accuracy value
View(indiv_vl_accuracies)



# ******************** IV. FIND vv ACCURACY *************************


# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(vv_data$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task<- NULL
same_or_diff <- NULL
test_phase <- NULL

# For each participant, extract id
# Assign domain, same_or_diff, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "vv")
  same_or_diff <- append(same_or_diff, "same")
  test_phase <- append(test_phase, "vsl")
  accuracy <- append(accuracy, round(mean(vv_data[which(vv_data$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_vv_accuracies <- data.frame(part_id, task, same_or_diff, test_phase, accuracy)

# TEST: There should be 32 entries 
length(indiv_vv_accuracies$part_id)

# TEST: All entries should all have an accuracy value
View(indiv_vv_accuracies)


# Summarize individual accuracies  ------------------------------------------------------------------------------------------------

# Bind different accuracy data frames
indiv_accuracies <- rbind(indiv_ll_accuracies, indiv_lv_accuracies, indiv_vl_accuracies, indiv_vv_accuracies)

write.csv(indiv_accuracies, "/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_accuracy_long.csv")


# Create a wide form version of the data
indiv_accuracies_wide <- cast(indiv_accuracies, part_id ~ task, mean, value = 'accuracy')
indiv_accuracies_wide<- merge(indiv_accuracies_wide, picture_vocab, by = "part_id", all=TRUE)

# Mark by same or different group
colnames(indiv_accuracies_wide)[9] <- "same_or_diff"
all_same <- indiv_accuracies_wide[ which(indiv_accuracies_wide$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- indiv_accuracies_wide[ which(indiv_accuracies_wide$lv>0), ]
all_diff$same_or_diff <- ("different")
indiv_accuracies_wide <- rbind(all_same, all_diff)

write.csv(indiv_accuracies_wide, "/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_accuracy_vocab_wide.csv")


# Find group-level mean accuracy accross tasks------------------------------------------------------------------------------------

# Remove one participant with incomplete accuracy data
indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_054"),]

# Set up variables
group_accuracy <- NULL
mean_accuracy <- NULL
task <- NULL

# Find mean ll accuracy across participants
all_ll<-subset(indiv_accuracies, task=="ll")
task <- append (task, paste ("ll"))
mean_accuracy <- append (mean_accuracy, round(mean(all_ll$accuracy), digits = 3))

# Find mean lv accuracy across participants
all_lv<-subset(indiv_accuracies, task=="lv")
task <- append (task, paste ("lv"))
mean_accuracy <- append (mean_accuracy, round(mean(all_lv$accuracy), digits = 3))

# Find mean vl accuracy across participants
all_vl<-subset(indiv_accuracies, task=="vl")
task <- append (task, paste ("vl"))
mean_accuracy <- append (mean_accuracy, round(mean(all_vl$accuracy), digits = 3))

# Find mean vv accuracy across participants
all_vv<-subset(indiv_accuracies, task=="vv")
task <- append (task, paste ("vv"))
mean_accuracy <- append (mean_accuracy, round(mean(all_vv$accuracy, na.rm=TRUE), digits = 3))

# Find mean accuracy across all lsl tests
all_lsl<-rbind(all_ll, all_lv)
task <- append (task, paste ("lsl_test_phase"))
mean_accuracy <- append (mean_accuracy, round(mean(all_lsl$accuracy), digits = 3))

# Find mean accuracy across all vsl tests
all_vsl<-rbind(all_vl, all_vv)
task <- append (task, paste ("vsl_test_phase"))
mean_accuracy <- append (mean_accuracy, round(mean(all_vsl$accuracy, na.rm=TRUE), digits = 3))

# Find mean accuracy across all "same condition"
all_same<-rbind(all_ll, all_vv)
task <- append (task, paste ("same_condition"))
mean_accuracy <- append (mean_accuracy, round(mean(all_same$accuracy, na.rm=TRUE), digits = 3))

# Find mean accuracy across all "different condition"
all_different<-rbind(all_lv, all_vl)
task <- append (task, paste ("different_condition"))
mean_accuracy <- append (mean_accuracy, round(mean(all_different$accuracy), digits = 3))

# Combine group accuracies into one data frame
group_accuracy <- data.frame(cbind(task, mean_accuracy))

write.csv(group_accuracy, "/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_mean_accuracies.csv")

