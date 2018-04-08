#  RT Slope 4 runs data Cleaning
#  Violet Kozloff
#  March 15th 2018 
#  This script cleans the auditory and visual files from the 4-run pilot for reaction time slope analysis
# NOTE: Does not include f008_visual_3.csv (missing from NAS)
# NOTE: f008_auditory_2.csv has been adapted to be more standard format
#  ****************************************************************************

# Prepare files ------------------------------------------------------------

# Move to folder from GitHub (Mac when folder is on desktop)
setwd("/Users/jasinskagroup/Desktop/QLAB/psychopy_sl_beh-master/rt_slope/4_runs/scripts")

# Remove objects in environment
rm(list=ls())

# Set up auditory input file path
old_auditory_input_path <- ("../original_data/auditory/old_format")
new_auditory_input_path <- ("../original_data/auditory/new_format")
old_auditory_files<- list.files(path=old_auditory_input_path, pattern="*.csv")
new_auditory_files<- list.files(path=new_auditory_input_path, pattern="*.csv")

# Set up auditory input file path
old_auditory_input_path <- ("../original_data/auditory/old_format")
new_auditory_input_path <- ("../original_data/auditory/new_format")
# select only files containing a trial session
old_auditory_files_2<- list.files(path=old_auditory_input_path, pattern="*2.csv")
old_auditory_files_4<- list.files(path=old_auditory_input_path, pattern="*4.csv")
old_auditory_files <- c(old_auditory_files_2, old_auditory_files_4)
new_auditory_files_2<- list.files(path=new_auditory_input_path, pattern="*2.csv")
new_auditory_files_4<- list.files(path=new_auditory_input_path, pattern="*4.csv")
new_auditory_files <- c(new_auditory_files_2, new_auditory_files_4)

# Set up visual input file path
old_visual_input_path <- ("../original_data/visual/old_format")
new_visual_input_path <- ("../original_data/visual/new_format")
# select only files containing a trial session
old_visual_files_2<- list.files(path=old_visual_input_path, pattern="*2.csv")
old_visual_files_4<- list.files(path=old_visual_input_path, pattern="*4.csv")
old_visual_files <- c(old_visual_files_2, old_visual_files_4)
new_visual_files_2<- list.files(path=new_visual_input_path, pattern="*2.csv")
new_visual_files_4<- list.files(path=new_visual_input_path, pattern="*4.csv")
new_visual_files <- c(new_visual_files_2, new_visual_files_4)

# Set up auditory ouput file path
auditory_output_path <- "../cleaned_data/auditory/"

# Set up visual output file path
visual_output_path <- "../cleaned_data/visual/"


# Clean old format auditory files --------------------------------------------------------------------------------

# create a new file containing only the relevant columns in the output folder
auditory_cleaning_old <- function(file) {
  current_file <- read.csv(file)
  value <- c("soundFile","trialnum","condition","random_block_key_resp.rt","random_block_key_resp.keys","structured_block_key_resp.rt","structured_block_key_resp.keys","starget","Run","PartID","ttarget","expName")
  newdata <- current_file[value]
  this_path<-file.path(auditory_output_path, basename(file))
  write.csv(newdata, file=(this_path))
  }

# Apply function to all auditory files
for (file in old_auditory_files)
{
  auditory_cleaning_old(paste0(old_auditory_input_path,file))
}


# Clean new format auditory files --------------------------------------------------------------------------------

# create a new file containing only the relevant columns in the output folder
auditory_cleaning_new <- function(file) {
  current_file <- read.csv(file)
  value <- c("soundFile","trialnum","condition","sound_block_key_resp.rt","sound_block_key_resp.keys","tone_block_key_resp.rt","tone_block_key_resp.keys","starget","Run","PartID","ttarget","expName")
  newdata <- current_file[value]
  this_path<-file.path(auditory_output_path, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all auditory files
for (file in new_auditory_files)
{
  auditory_cleaning_new(paste0(new_auditory_input_path,file))
}





# CLean old format visual files --------------------------------------------------------------------------------

# create a new file containing only the relevant columns in the output folder
visual_cleaning <- function(file) {
  current_file <- read.csv(file)
  value <- c("image","trialnum","condition","l_block_trial_key_resp.rt","l_block_trial_key_resp.keys","v_block_trial_key_resp.rt","v_block_trial_key_resp.keys","ltarget","Run","PartID","vtarget","expName")
  newdata <- current_file[value]
  this_path<-file.path(visual_output_path, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all visual files
for (file in old_visual_files)
{
  visual_cleaning(paste0(visual_input_path,file))
}

