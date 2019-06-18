#  SIT RT Slope Cleaning
#  Violet Kozloff
#  April 8th 2018 
#  This script cleans files from the SIT experiment
#  NOTE: Before starting, manually add columns to each file that contain "first_targ" and "second_targ."
#  These values come from the corresponding .log file on NAS data/projects/sit/visual_inter/data/
#  "first_targ" comes from the line "Created firstTarget_image"; "second_targ" from "Created secondTarget_image"
#  ****************************************************************************


# Prepare files ------------------------------------------------------------

# Set working directory
setwd("/Users/vkozloff/Documents/qlab/analysis/sl-psychopy-analysis/sit-beh-analysis")

# Remove objects in environment
rm(list=ls())

# Set up file paths
ll_input <- ("/Users/vkozloff/Documents/sit_data/original/ll_original/")
lv_input <- ("/Users/vkozloff/Documents/sit_data/original/lv_original/")
vl_input <- ("/Users/vkozloff/Documents/sit_data/original/vl_original/")
vv_input <- ("/Users/vkozloff/Documents/sit_data/original/vv_original/")
ll_output <- ("/Users/vkozloff/Documents/sit_data/clean/ll_clean/")
lv_output <- ("/Users/vkozloff/Documents/sit_data/clean/lv_clean/")
vl_output <- ("/Users/vkozloff/Documents/sit_data/clean/vl_clean/")
vv_output <- ("/Users/vkozloff/Documents/sit_data/clean/vv_clean/")
ll_files<- list.files(path = ll_input, pattern="*.csv")
lv_files<- list.files(path = lv_input, pattern="*.csv")
vl_files<- list.files(path = vl_input, pattern="*.csv")
vv_files<- list.files(path = vv_input, pattern="*.csv")


# Clean files with an lsl test phase --------------------------------------------------------------------------------

# create a new file containing only the relevant columns in the output folder
ll_clean <- function(file) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("PartID", "trialnum", "expName", "condition", "l_block_trial_loop.thisTrialN", "image","first_targ", "second_targ","l_block_trial_key_resp.rt","lsl_question_key_resp.corr")
  newdata <- current_file[value]
  # Make sure that F is not marked as False
  newdata$first_targ[newdata$first_targ == FALSE] <- 'f_not_false'
  newdata$second_targ[newdata$second_targ == FALSE] <- 'f_not_false'
  # Put all data in lowercase
  names(newdata) <- tolower(names(newdata))
  # Standardize "corr_resp" column across runs
  names(newdata)[names(newdata) == 'lsl_question_key_resp.corr'] <- 'corr_resp'
  # Simplify loop names
  names(newdata)[names(newdata) == 'l_block_trial_loop.thistrialn'] <- 'this_l_loop'
  # Simplify RT names
  names(newdata)[names(newdata) == 'l_block_trial_key_resp.rt'] <- 'l_rt'
  # Separate words by underscore
  names(newdata) <- gsub ("partid", "part_id", names(newdata))
  names(newdata) <- gsub ("expname", "exp_name", names(newdata))
  names(newdata) <- gsub ("trialnum", "trial_num", names(newdata))
  # Define targets by condition
  names(newdata) <- gsub ("first_targ", "structured_targ", names(newdata))
  names(newdata) <- gsub ("second_targ", "random_targ", names(newdata))
  # Define targets by condition
  names(newdata) <- gsub ("first_targ", "structured_targ", names(newdata))
  names(newdata) <- gsub ("second_targ", "random_targ", names(newdata))
  # Write file
  this_path<-file.path(ll_output, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all ll files
for (file in ll_files)
{
  ll_clean(paste0(ll_input,file))
}

ll_output_files <- list.files(path = ll_output, pattern="*.csv")


# create a new file containing only the relevant columns in the output folder
lv_clean <- function(file) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("PartID", "expName", "trialnum", "condition", "l_block_trial_loop.thisTrialN", "v_block_trials.thisTrialN", "image","first_targ", "second_targ","l_block_trial_key_resp.rt", "v_block_trial_key_resp.rt","lsl_question_key_resp.corr")
  newdata <- current_file[value]
  # Make sure that F is not marked as False
  newdata$first_targ[newdata$first_targ == FALSE] <- 'f_not_false'
  # Put all data in lowercase
  names(newdata) <- tolower(names(newdata))
  # Standardize "corr_resp" column across runs
  names(newdata)[names(newdata) == 'lsl_question_key_resp.corr'] <- 'corr_resp'
  # Simplify loop names
  names(newdata)[names(newdata) == 'l_block_trial_loop.thistrialn'] <- 'this_l_loop'
  names(newdata)[names(newdata) == 'v_block_trials.thistrialn'] <- 'this_v_loop'
  # Simplify RT names
  names(newdata)[names(newdata) == 'l_block_trial_key_resp.rt'] <- 'l_rt'
  names(newdata)[names(newdata) == 'v_block_trial_key_resp.rt'] <- 'v_rt'
  # Separate words by underscore
  names(newdata) <- gsub ("partid", "part_id", names(newdata))
  names(newdata) <- gsub ("expname", "exp_name", names(newdata))
  names(newdata) <- gsub ("trailname", "trial_name", names(newdata))
  # Define targets by condition
  names(newdata) <- gsub ("first_targ", "structured_targ", names(newdata))
  names(newdata) <- gsub ("second_targ", "random_targ", names(newdata))
  # Write file
  this_path<-file.path(lv_output, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all lv files
for (file in lv_files)
{
  lv_clean(paste0(lv_input,file))
}


# Clean files with a vsl test phase --------------------------------------------------------------------------------

# create a new file containing only the relevant columns in the output folder
vl_clean <- function(file) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("PartID", "trialnum", "expName", "condition", "l_block_trial_loop.thisTrialN", "v_block_trials.thisTrialN", "image","first_targ", "second_targ","l_block_trial_key_resp.rt","v_block_trial_key_resp.rt", "vsl_question_key_resp.corr")
  newdata <- current_file[value]
  # Make sure that F is not marked as False
  newdata$second_targ[newdata$second_targ == FALSE] <- 'f_not_false'
  # Put all data in lowercase
  names(newdata) <- tolower(names(newdata))
  # Standardize "corr_resp" column across runs
  names(newdata)[names(newdata) == 'vsl_question_key_resp.corr'] <- 'corr_resp'
  # Simplify loop names
  names(newdata)[names(newdata) == 'l_block_trial_loop.thistrialn'] <- 'this_l_loop'
  names(newdata)[names(newdata) == 'v_block_trials.thistrialn'] <- 'this_v_loop'
  # Simplify RT names
  names(newdata)[names(newdata) == 'l_block_trial_key_resp.rt'] <- 'l_rt'
  names(newdata)[names(newdata) == 'v_block_trial_key_resp.rt'] <- 'v_rt'
  # Separate words by underscore
  names(newdata) <- gsub ("partid", "part_id", names(newdata))
  names(newdata) <- gsub ("expname", "exp_name", names(newdata))
  names(newdata) <- gsub ("trialnum", "trial_num", names(newdata))
  # Define targets by condition
  names(newdata) <- gsub ("first_targ", "structured_targ", names(newdata))
  names(newdata) <- gsub ("second_targ", "random_targ", names(newdata))
  # Write file
  this_path<-file.path(vl_output, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all vl files
for (file in vl_files)
{
  vl_clean(paste0(vl_input,file))
}

newdata <- NULL

# create a new file containing only the relevant columns in the output folder
vv_clean <- function(file) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("PartID", "expName", "trialnum", "condition", "v_block_trials.thisTrialN", "image", "first_targ", "second_targ","v_block_trial_key_resp.rt", "vsl_question_key_resp.corr")
  newdata <- current_file[value]
  # Standardize "corr_resp" column across runs
  names(newdata)[names(newdata) == 'vsl_question_key_resp.corr'] <- 'corr_resp'
  # Put all data in lowercase
  names(newdata) <- tolower(names(newdata))
  # Simplify loop names
  names(newdata)[names(newdata) == 'v_block_trials.thistrialn'] <- 'this_v_loop'
  # Simplify RT names
  names(newdata)[names(newdata) == 'v_block_trial_key_resp.rt'] <- 'v_rt'
  # Separate words by underscore
  names(newdata) <- gsub ("partid", "part_id", names(newdata))
  names(newdata) <- gsub ("expname", "exp_name", names(newdata))
  names(newdata) <- gsub ("trialnum", "trial_num", names(newdata))
  # Rename target names
  names(newdata) <- gsub ("first_targ", "structured_targ", names(newdata))
  names(newdata) <- gsub ("second_targ", "random_targ", names(newdata))
  # Write file
  this_path<-file.path(vv_output, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all vv files
for (file in vv_files)
{
  vv_clean(paste0(vv_input,file))
}

