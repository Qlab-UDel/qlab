#  FMRI Pilot Analysis
#  Violet Kozloff
#  March 15th 
#  This script cleans the auditory and visual files from the November pilot
#  NOTE: Does not include participant 9, who did not respond in several conditions
#  NOTE: Original psychopy files have been renamed to have a letter as a leading character
# NOTE: Excludes the file 007_auditory_2, which is missing RT data
#  ****************************************************************************

#for test purposes only
setwd("/Users/jasinskagroup/Desktop/QLAB/psychopy_sl_beh-master/rt_slope/nov_pilot/scripts")

# Remove objects in environment
rm(list=ls())

# Clean auditory files ----------------------------------------------------------

# Prepare file paths
auditory_input_path <- "../original_data/auditory/"
auditory_files <- list.files(path=auditory_input_path, pattern="*.csv")
auditory_output_path <- "../cleaned_data/auditory/"

# create a new file containing only the relevant columns in the output folder
auditory_cleaning <- function(file) {
  current_file <- read.csv(file)
  value <- c("soundFile","trialnum","condition","random_block_key_resp.rt","random_block_key_resp.keys","structured_block_key_resp.rt","structured_block_key_resp.keys","starget","Run","PartID","ttarget","expName")
  newdata <- current_file[value]
  this_path<-file.path(auditory_output_path, basename(file))
  write.csv(newdata, file=(this_path))
  }

# Apply function to all auditory files
for (file in auditory_files)
{
  auditory_cleaning(paste0(auditory_input_path,file))
}


# Clean visual files ----------------------------------------------------------

# to test
rm(list=ls())

# Prepare file paths
visual_input_path <- "../original_data/visual/"
visual_files <- list.files(path=visual_input_path, pattern="*.csv")
visual_output_path <- "../cleaned_data/visual/"

# create a new file containing only the relevant columns in the output folder
visual_cleaning <- function(file) {
  current_file <- read.csv(file)
  value <- c("image","trialnum","condition","l_block_trial_key_resp.keys","l_block_trial_key_resp.rt","v_block_trial_key_resp.keys","v_block_trial_key_resp.rt","vtarget","Run","PartID","ltarget","expName")
  newdata <- current_file[value]
  this_path<-file.path(visual_output_path, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all auditory files
for (file in visual_files)
{
  visual_cleaning(paste0(visual_input_path,file))
}

