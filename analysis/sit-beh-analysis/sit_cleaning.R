#  SIT RT Slope Cleaning
#  Violet Kozloff
#  Adapted from cleaning files produced by An Nguyen
#  Last modified July 3rd, 2019
#  This script cleans files from the SIT experiment
#  NOTE: Before starting, "first_targ" and "second_targ" columns must be manually added to each raw data file
#        These values come from the corresponding .log file on NAS data/projects/sit/visual_inter/data/
#        "first_targ" comes from the line "Created firstTarget_image"; "second_targ" from "Created secondTarget_image"
#        A future version of this script should automatically extract these values.
#  NOTE: This script generates warnings when the value 'F' cannot be found in a column. 
#        While this does not affect the output, a future version of this script should account for this case.  
#  ****************************************************************************


# Prepare files ------------------------------------------------------------

# Set working directory
setwd("/Volumes/data/projects/completed_projects/sit/analysis/")

# Remove objects in environment
rm(list=ls())


# Clean ll files with an lsl test phase --------------------------------------------------------------------------------

# Find ll files
setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/original/ll_original")
ll_files <- list.files(pattern=("*.csv"))
ll_output <- ("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/ll_clean")

# Clean ll files and put output on NAS under /Volumes/data/projects/completed_projects/sit/analysis/data/clean/ll_clean
for (file in ll_files) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("PartID", "trialnum", "expName", "condition", "l_block_trial_loop.thisTrialN", "image","first_targ", "second_targ","l_block_trial_key_resp.rt","lsl_question_key_resp.corr", "letter6",	"letter5",	"letter4",	"letter3",	"letter2",	"letter1",	"corrAns")
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
  names(newdata) <- gsub ("letter6", "sixth2AFC", names(newdata))
  names(newdata) <- gsub ("letter5", "fifth2AFC", names(newdata))
  names(newdata) <- gsub ("letter4", "fourth2AFC", names(newdata))
  names(newdata) <- gsub ("letter3", "third2AFC", names(newdata))
  names(newdata) <- gsub ("letter2", "second2AFC", names(newdata))
  names(newdata) <- gsub ("letter1", "first2AFC", names(newdata))
  names(newdata) <- gsub ("corrAns", "triplet_position", names(newdata))
  
  # Write file
  write.csv(newdata, paste('/Volumes/data/projects/completed_projects/sit/analysis/data/clean/ll_clean/clean2_', basename(file), sep=""))
}


# Clean lv files with an lsl test phase --------------------------------------------------------------------------------

# Find lv files
setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/original/lv_original")
lv_files <- list.files(pattern=("*.csv"))
lv_output <- ("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/lv_clean")

for (file in lv_files) {
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
  write.csv(newdata, paste('/Volumes/data/projects/completed_projects/sit/analysis/data/clean/lv_clean/clean_', basename(file), sep=""))
}


# Clean vl files --------------------------------------------------------------------------------

# Find vl files
setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/original/vl_original")
vl_files <- list.files(pattern=("*.csv"))
vl_output <- ("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vl_clean")

# create a new file containing only the relevant columns in the output folder
for (file in vl_files) {
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
  write.csv(newdata, paste('/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vl_clean/clean_', basename(file), sep=""))
}


# Clean vv files --------------------------------------------------------------------------------

# Find vv files
setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/original/vv_original")
vv_files <- list.files(pattern=("*.csv"))
vv_output <- ("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vv_clean")

# create a new file containing only the relevant columns in the output folder
for (file in vv_files) {
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
  write.csv(newdata, paste('/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vv_clean/clean_', basename(file), sep=""))
}

