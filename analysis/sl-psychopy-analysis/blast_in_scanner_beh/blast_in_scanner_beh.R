#  ****************************************************************************
#  BLAST IN-SCANNER BEHAVIORAL ANALYSIS
#  Violet Kozloff
#  Last updated: May 29th 2019 
#  This script analyzes structured and random blocks across four tasks: auditory (speech and tones) and visual (letters and images).
#  It measures the mean reaction time and the slope of the reaction time for each participant for each condition.
#  ****************************************************************************

# ******************** I. EXTRACT AND PREPARE DATA *************************


# Prepare files ------------------------------------------------------------

# Load packages
library (plyr)
library("reshape")

# Set working directory
setwd("/Volumes/data/projects/blast/data/mri/in_scanner_behavioral/adult/sl_raw_data")
# Alternate working directory if the above throws error (depends on how NAS is mounted)
#setwd("/Volumes/data-1/projects/blast/data/mri/in_scanner_behavioral/adult/sl_raw_data")

# Set output path
output_path <- ("/Volumes/data/projects/blast/data_summaries/blast_in_lab_adult/behavioral/")
# Alternate working directory if the above throws error (depends on how NAS is mounted)
# output_path <- ("/Volumes/data-1/projects/blast/data_summaries/blast_in_lab_adult/behavioral/")

# NOTE: Try this one if you can't connect to this output path
# output_path <- ("/Volumes/data-1/projects/blast/data_summaries/blast_online_child/breakdown/")


# Remove objects in environment
rm(list=ls())


# Extract auditory data ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

auditory_files <- list.files(pattern=glob2rx("*auditory_*.csv"))

# Extract only the relevant columns of auditory data
auditory_data <- NULL 

for (file in auditory_files) {
  current_file <- read.csv(file)
  # Check that the participant responded to both types of stimuli
  if (length((current_file$sound_block_key_resp.rt))&(length(current_file$tone_block_key_resp.rt)>0)){
    value <- c("soundFile", "fam_trials_loop.thisTrialN", "trials_1.thisTrialN", "condition", "sound_block_key_resp.rt","tone_block_key_resp.rt","starget","Run","PartID","ttarget","expName")
    # If they did not respond to syllables, only extract tone response times
    } else if (length(current_file$tone_block_key_resp.rt)>0){
    value <- c("soundFile", "fam_trials_loop.thisTrialN", "trials_1.thisTrialN", "condition","tone_block_key_resp.rt","starget","Run","PartID","ttarget","expName")
    # If they did not respond to tones, only extract syllable response times
    } else if (length(current_file$sound_block_key_resp.rt)>0){
      value <- c("soundFile", "fam_trials_loop.thisTrialN", "trials_1.thisTrialN", "condition","sound_block_key_resp.rt","starget","Run","PartID","ttarget","expName")
    # If they didn't respond to either stimulus type, only extract information about the stimuli presented  
    } else {
        value <- c("soundFile", "fam_trials_loop.thisTrialN", "trials_1.thisTrialN", "condition","starget","Run","PartID","ttarget","expName")}
  current_data <- current_file[value]
  # Combine all auditory data into a single data frame
  auditory_data <- rbind.fill (auditory_data,current_data)
}

# Check for extra or incorrect targets----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Check for extra or incorrect syllable targets
if (!all(levels(unique(auditory_data$starget))==c("bi","du","pu","da"))){
  print(paste("Incorrect syllable targets identified. The syllable targets should be bi, du, pu, and da. Please check your data's syllable targets in the window labeled unique(auditory_data$starget)."))
  stop(View(unique(auditory_data$starget)))
  }

# Check for extra or incorrect tone targets
if (!all(levels(unique(auditory_data$ttarget))==c("1C","2C"))){
  print("Incorrect tone targets identified. The tone targets should be 1C and 2C. Please check your data's syllable targets in the window labeled unique(auditory_data$ttarget).")
  stop(View(unique(auditory_data$ttarget)))
}   
       

# Prepare auditory data for use----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Convert targets and soundFile from factors to atomic variables 
auditory_data$ttarget<-as.character(auditory_data$ttarget)
auditory_data$soundFile<-as.character(auditory_data$soundFile)
auditory_data$starget<-as.character(auditory_data$starget)

# Match name of image with name of target in auditory files by removing extension from end of sound_file
auditory_data$soundFile <- gsub (".wav", "", auditory_data$soundFile, ignore.case=TRUE)

# Rename columns to standard format
names(auditory_data) <- c('stimulus','syllable_trial', 'tone_trial', 'condition','syllable_keypress','tone_keypress','syllable_target','run','part_id','tone_target','modality')

# Combine all responses into one column
auditory_data$keypress <- (paste(auditory_data$tone_keypress, auditory_data$syllable_keypress))
auditory_data$keypress <- gsub("NA NA", NA, auditory_data$keypress)
auditory_data$keypress <- gsub(" NA", "", auditory_data$keypress)
auditory_data$keypress <- gsub("NA ", "", auditory_data$keypress)

# Explicitly indicate conditions
auditory_data$condition <- gsub ("R", "random", auditory_data$condition, ignore.case=TRUE)
auditory_data$condition <- gsub ("S", "structured", auditory_data$condition, ignore.case=TRUE)
auditory_data$condition <- gsub ("B", "blank", auditory_data$condition, ignore.case=TRUE)

# Explicitly state the task
auditory_data$task <- NA
auditory_data[which(auditory_data$stimulus %in% c("1A","1B","1C","2A","2B","2C","3A","3B","3C","4A","4B","4C")),]$task <- "tone"
auditory_data[which(auditory_data$stimulus %in% c("pi","tu","bi","di","ba","pu","bu","pa","da","ta","ti","du"  )),]$task <- "syllable"

# Standardize all strings into lowercase
auditory_data$stimulus <- tolower(auditory_data$stimulus)
auditory_data$tone_target <- tolower(auditory_data$tone_target)

# In the design, blank blocks were mistakenly indexed as trials 95 and on of the preceding block. Remove these indices.
auditory_data$tone_trial[which(auditory_data$tone_trial>95)] <- NA
auditory_data$syllable_trial[which(auditory_data$syllable_trial>95)] <- NA

# Index each trial within a block. Exclude trial numbers for blank blocks. Combine all trial data into one column.
auditory_data$stimulus_trial <- (paste(auditory_data$tone_trial, auditory_data$syllable_trial))
auditory_data$stimulus_trial <- gsub("NA NA", NA, auditory_data$stimulus_trial)
auditory_data$stimulus_trial <- gsub(" NA", "", auditory_data$stimulus_trial)
auditory_data$stimulus_trial <- gsub("NA ", "", auditory_data$stimulus_trial)

# Remove old columns
auditory_data$syllable_keypress <- NULL
auditory_data$tone_keypress <- NULL
auditory_data$syllable_trial <- NULL
auditory_data$tone_trial <- NULL

# Convert keypress times to milliseconds
auditory_data$keypress <- as.numeric(auditory_data$keypress)*1000



# Extract visual data ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List files
visual_files <- list.files(pattern=glob2rx("*visual_*.csv"))

# Store relevant data
visual_data <- NULL 

# Extract only the relevant columns
for (file in visual_files) {

  current_file <- read.csv(file)
  # Override default where "F" is read in as "FALSE"
  current_file$ltarget <- gsub(FALSE, "F_not_false", current_file$ltarget)
  # Extract only relevant columns
  value <- c("image", "v_block_trials.thisTrialN", "l_block_trial_loop.thisTrialN", "condition","l_block_trial_key_resp.rt","v_block_trial_key_resp.rt","ltarget","Run","PartID","vtarget","expName")
  current_data <- current_file[value]
  # Combine all visual data into a single data frame
  visual_data <- rbind.fill (visual_data,current_data)
}

# Check for extra or incorrect targets 

# Return "F_not_false" values to "F"
visual_data$ltarget <- tolower(as.character(gsub ("F_not_false", "F", visual_data$ltarget, ignore.case=TRUE)))

# Check for extra or incorrect letter targets
if (!all(unique(visual_data$ltarget)==c("f", "g", "h", "b"))){
  print(paste("Incorrect letter targets identified. The letter targets should be f, g, h, and b. Please check your data's letter targets in the window labeled unique(visual_data$ltarget)."))
  stop(View(unique(visual_data$ltarget)))
}

# Check for extra or incorrect letter targets
if (!all(unique(visual_data$vtarget)==c(3,6,15,18,24,21))){
  print(paste("Incorrect image targets identified. The image targets should be 3, 6, 15, 18, 24, and 21. Please check your data's image targets in the window labeled unique(visual_data$vtarget)."))
  stop(View(unique(visual_data$vtarget)))
}



# Prepare visual data for use  ----------------------------------------------------------------------------------------

# Remove "Alien" from beginning of vtarget names
visual_data$image <- gsub ("Alien", "", visual_data$image, ignore.case=TRUE)

# Remove extensions from end of end of target names
visual_data$image <- gsub (".bmp", "", visual_data$image, ignore.case=TRUE)
visual_data$image <- gsub (".png", "", visual_data$image, ignore.case=TRUE)

# Rename columns to standard format
names(visual_data) <- c('stimulus', 'image_trial', 'letter_trial', 'condition','letter_keypress','image_keypress','letter_target','run','part_id','image_target','modality')

# Combine all responses into one column
visual_data$keypress <- (paste(visual_data$image_keypress, visual_data$letter_keypress))
visual_data$keypress <- gsub("NA NA", NA, visual_data$keypress)
visual_data$keypress <- gsub(" NA", "", visual_data$keypress)
visual_data$keypress <- gsub("NA ", "", visual_data$keypress)
visual_data$image_keypress <- NULL
visual_data$letter_keypress <- NULL

# Explicitly indicate conditions
visual_data$condition <- gsub ("R", "random", visual_data$condition, ignore.case=TRUE)
visual_data$condition <- gsub ("S", "structured", visual_data$condition, ignore.case=TRUE)
visual_data$condition <- gsub ("B", "blank", visual_data$condition, ignore.case=TRUE)

# Explicitly state the task
visual_data$task <- NA
visual_data[which(visual_data$stimulus %in% c("1", "2", "3", "4", "5", "6", "7", "8", "9","10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24")),]$task <- "image"
visual_data[which(visual_data$stimulus %in% c("A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M")),]$task <- "letter"
 
# Standardize all strings into lowercase
visual_data$stimulus <- tolower(visual_data$stimulus)
visual_data$letter_target <- tolower(visual_data$letter_target)
visual_data$letter_target <- gsub("f_not_false", "f", visual_data$letter_target)

# Blank blocks were mistakenly indexed as trials 48 and on of the preceding block. Remove these indices.
visual_data$image_trial[which(visual_data$image_trial>48)] <- NA
visual_data$letter_trial[which(visual_data$letter_trial>48)] <- NA

# Index each trial within a block. Exclude trial numbers for blank blocks. Combine all trial data into one column.
visual_data$stimulus_trial <- (paste(visual_data$image_trial, visual_data$letter_trial))
visual_data$stimulus_trial <- gsub("NA NA", NA, visual_data$stimulus_trial)
visual_data$stimulus_trial <- gsub(" NA", "", visual_data$stimulus_trial)
visual_data$stimulus_trial <- gsub("NA ", "", visual_data$stimulus_trial)
visual_data$letter_trial <- NULL
visual_data$image_trial <- NULL

# Convert keypress times to milliseconds
visual_data$keypress <- as.numeric(visual_data$keypress)*1000



# ******************** II. FIND AUDITORY REACTION TIME MEANS AND SLOPES *************************

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Identify the rows when the target was presented
auditory_targets <- which((auditory_data$stimulus==auditory_data$tone_target) | (auditory_data$stimulus==auditory_data$syllable_target))

# Initialize variables to track participant ID, condition, modality, task, and reaction time (RT)
auditory_part_id <- NULL
auditory_condition <- NULL
auditory_modality <- NULL
auditory_task <- NULL
auditory_rt <- NULL

# Track the cases for calculating each type of reaction time

# Case 1: The participant responds during the target, which is the first trial in a block 
auditory_case1 <- NULL
# Case 2: The participant responds to the trial directly following the target, which is the first trial in a block 
auditory_case2 <- NULL
# Case 3: Anticipation of target, participant responded to stimulus directly preceding target
auditory_case3 <- NULL
# Case 4: Response to target during the target trial
auditory_case4 <- NULL
# Case 5: Delay from target, participant responded to stimulus directly following target
auditory_case5 <- NULL
# Case 6: Missed target, record NA reaction time
auditory_case6 <- NULL

# Isolate participants' response times.

# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in auditory_targets) {
  
  # Isolate the ID number, auditory_condition, auditory_modality, and auditory_task
  auditory_part_id <- append(auditory_part_id, paste(auditory_data[i,]$part_id))
  auditory_condition <- append (auditory_condition, paste(auditory_data[i,]$condition))
  auditory_modality <- append (auditory_modality, paste(auditory_data[i,]$modality))
  auditory_task <- append (auditory_task, paste(auditory_data[i,]$task))
  
  # Check if you are looking at the first trial If so, it does not have a preceeding target
  # TO DO: Check this auditory_condition
  if (auditory_data[i,]$stimulus_trial==0 & !is.na(auditory_data[1,]$keypress)){ 
    # Count the response time from the target stimulus (NA)
   auditory_rt <- append (auditory_rt, auditory_data[i,][,"keypress"])
   auditory_case1 <- append (auditory_case1, i)

  # If it's the first trial and there was no target keypress, count the response time from the following stimulus
  } else if (auditory_data[i,]$stimulus_trial==0 & (auditory_data[i,])$condition==(auditory_data[i+1,]$condition)) {
   # TO DO: test this auditory_condition
    auditory_rt <- append (auditory_rt, 480+(auditory_data[i+1,][,"keypress"]))
    auditory_case2 <- append (auditory_case2, i)
  }  
  
  # Otherwise, if the participant responded during the stimulus preceding the target, and the preceding stimulus was not also a target, and the preceding stimulus came from the same block
  else if (!is.na(auditory_data[i-1,] [,"keypress"]) & ((auditory_data[i-1,][,"tone_target"] != (auditory_data[i-1,][,"stimulus"]))) & (auditory_data[i,])$condition==(auditory_data[i-1,]$condition)){
    # Count their response time as how much sooner they responded than when the stimulus was presented (anticipation)
    auditory_rt <- append(auditory_rt, (auditory_data[i-1,][,"keypress"]-480))
    auditory_case3 <- append (auditory_case3, i)
  }
  
  # Otherwise, if the participant responded during the target
  else if (!is.na(auditory_data[i,] [,"keypress"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    auditory_rt <- append(auditory_rt, (auditory_data[i,][,"keypress"]))
    auditory_case4 <- append (auditory_case4, i)
  }
  
  # Otherwise, if the participant responded after the target, and the following target came from the same block
  else if (!is.na(auditory_data[i+1,]$keypress > 0) & (auditory_data[i+1,]$keypress > 0) & (auditory_data[i,])$condition==(auditory_data[i+1,]$condition)){
    # Count their response time as how much later they responded than when the stimulus was presented
    auditory_rt <- append(auditory_rt, (480+auditory_data[i+1,][,"keypress"]))
    auditory_case5 <- append (auditory_case5, i)
    
  # Otherwise, record the miss with a reaction time of NA
    } else {
      auditory_rt <- append(auditory_rt, NA)
      auditory_case6 <- append (auditory_case6, i)
    }
}

# Combine the reaction time data into one dataframe. Note that auditory_case_1 through auditory_case_6 are excluded. These are for hand-testing the logic of the above loop only

# exp_auditory_targets now contains all targets from the exposure phase and their true auditory_rts (includes any response within 480 ms of a target)
exp_auditory_targets <- data.frame(auditory_part_id, auditory_condition, auditory_modality, auditory_task, auditory_rt)

# Find the number of RTs for each participant
all_auditory_ids <- unique(as.character(auditory_data$part_id))

# TO DO: Account for alternating targets and keypresses (ie. target-keypress-target, or target-keypress-target-keypress)

# Initialize variables
total_syllable_rts <- NULL
total_tone_rts <- NULL
total_auditory_rts <- NULL


# Check RTs
for(check_id in all_auditory_ids){
  total_tone_rts <- append(total_tone_rts, length(which(exp_auditory_targets$auditory_part_id==check_id & exp_auditory_targets$auditory_task=="tone")))
  total_syllable_rts <- append(total_syllable_rts, length(which(exp_auditory_targets$auditory_part_id==check_id & exp_auditory_targets$auditory_task=="syllable")))
  total_auditory_rts <- append(total_auditory_rts, length(which(exp_auditory_targets$auditory_part_id==check_id)))
  }
auditory_rt_check <- (cbind(all_auditory_ids, total_tone_rts, total_syllable_rts, total_auditory_rts))


# Internal check: make sure that all RTs are valid, ie. fall within 1 SOA of the stimulus. Alert user if not.

# Alert the user of invalid RTs
check_rts_1 <- exp_auditory_targets[which(exp_auditory_targets$auditory_rt > 960),]
check_rts_2 <- exp_auditory_targets[which(exp_auditory_targets$auditory_rt < -480),]
if(length(check_rts_1[,1]) | length(check_rts_2[,1]) !=0){
  # Create error message alerting user
  print("One or more participants has an invalid reaction time. Please check the reaction time calculations above.")
  # Open a new window showing the user the RTs for each participant
  View(exp_auditory_targets)
  stop()}


# Calculate mean rt  -----------------------------------------------------------------------------------------------------

# mean reaction times
exp_auditory_mean_rts<- cast(exp_auditory_targets, auditory_part_id~auditory_condition+auditory_task, value = "auditory_rt", fun.aggregate = mean, na.rm=TRUE)


# Calculate rt slopes  -----------------------------------------------------------------------------------------------------


# Initialize column to track numbers of targets

# Reindex the targets from 1 to the expected number of targets for each participant
exp_auditory_targets$index <- NA

# Loop trhough targets and index them
for (i in unique(exp_auditory_targets$auditory_part_id)){ 
  # Identify all rows with SSL value
  total_structured_ssl <- which(exp_auditory_targets$auditory_part_id==i & exp_auditory_targets$auditory_task=="syllable" & exp_auditory_targets$auditory_condition == "structured")
  # number them from 1 to the total number of ssl
  k <- 1
  for (j in total_structured_ssl){
    exp_auditory_targets$index[j] <- k
    k <- k+1
  }
  # Identify all rows with SSL value
  total_random_ssl <- which(exp_auditory_targets$auditory_part_id==i & exp_auditory_targets$auditory_task=="syllable" & exp_auditory_targets$auditory_condition == "random")
  # number them from 1 to the total number of ssl
  k <- 1
  for (j in total_random_ssl){
    exp_auditory_targets$index[j] <- k
    k <- k+1
  }
  # Identify all rows with tsl value
  total_structured_tsl <- which(exp_auditory_targets$auditory_part_id==i & exp_auditory_targets$auditory_task=="tone" & exp_auditory_targets$auditory_condition == "structured")
  # number them from 1 to the total number of tsl
  k <- 1
  for (j in total_structured_tsl){
    exp_auditory_targets$index[j] <- k
    k <- k+1
  }
  # Identify all rows with tsl value
  total_random_tsl <- which(exp_auditory_targets$auditory_part_id==i & exp_auditory_targets$auditory_task=="tone" & exp_auditory_targets$auditory_condition == "random")
  # number them from 1 to the total number of tsl
  k <- 1
  for (j in total_random_tsl){
    exp_auditory_targets$index[j] <- k
    k <- k+1
  }
}

# Calculate reaction time slopes

# Initialize variables for RT calculations
random_ssl_rt_slope <- NULL
random_tsl_rt_slope <- NULL
structured_ssl_rt_slope <- NULL
structured_tsl_rt_slope <- NULL

# Extract the rt slope for each participant
for(id in (unique(auditory_part_id))){
  
  # Separate data by target and condition type (eg. random syllables, structured tones)
  random_ssl <- exp_auditory_targets[which(exp_auditory_targets$auditory_part_id==id & exp_auditory_targets$auditory_task=="syllable" & exp_auditory_targets$auditory_condition=="random"),]
  random_tsl <- exp_auditory_targets[which(exp_auditory_targets$auditory_part_id==id & exp_auditory_targets$auditory_task=="tone" & exp_auditory_targets$auditory_condition=="random"),]
  structured_ssl <- exp_auditory_targets[which(exp_auditory_targets$auditory_part_id==id & exp_auditory_targets$auditory_task=="syllable" & exp_auditory_targets$auditory_condition=="structured"),]
  structured_tsl <- exp_auditory_targets[which(exp_auditory_targets$auditory_part_id==id & exp_auditory_targets$auditory_task=="tone" & exp_auditory_targets$auditory_condition=="structured"),]
  
  # Calculate slopes for any target type that has two or more data points. If not, mark that there are too few hits (correctly identified targets) to calculate it
  if (!all(is.na(unique(random_ssl$auditory_rt))) & length(unique(random_ssl$auditory_rt))>1){random_ssl_rt_slope <-append(random_ssl_rt_slope,round(summary(lm(random_ssl$auditory_rt~random_ssl$index))$coefficient[2,1],digits=3))}
  else(random_ssl_rt_slope<- append(random_ssl_rt_slope, "too few hits"))
  if (!all(is.na(unique(random_tsl$auditory_rt))) & length(unique(random_tsl$auditory_rt))>1){random_tsl_rt_slope<-append(random_tsl_rt_slope,round(summary(lm(random_tsl$auditory_rt~random_tsl$index))$coefficient[2,1],digits=3))}
  else(random_tsl_rt_slope<- append(random_tsl_rt_slope, "too few hits"))
  if (!all(is.na(unique(structured_ssl$auditory_rt))) & length(unique(structured_ssl$auditory_rt))>1){structured_ssl_rt_slope <-append(structured_ssl_rt_slope,round(summary(lm(structured_ssl$auditory_rt~structured_ssl$index))$coefficient[2,1],digits=3))}
  else(structured_ssl_rt_slope<- append(structured_ssl_rt_slope, "too few hits"))
  if (!all(is.na(unique(structured_tsl$auditory_rt))) & length(unique(structured_tsl$auditory_rt))>1){structured_tsl_rt_slope <-append(structured_tsl_rt_slope,round(summary(lm(structured_tsl$auditory_rt~structured_tsl$index))$coefficient[2,1],digits=3))}
  else(structured_tsl_rt_slope<- append(structured_tsl_rt_slope, "too few hits"))
}
  
# Bind all auditory output

auditory_rt_slopes <- cbind(unique(auditory_part_id), random_ssl_rt_slope, random_tsl_rt_slope, structured_ssl_rt_slope, structured_tsl_rt_slope)
colnames(auditory_rt_check)[1] <- "auditory_part_id"
colnames(exp_auditory_mean_rts) <- c("auditory_part_id", "random_syllable_mean_rt", "random_tone_mean_rt", "structured_syllable_mean_rt", "structured_tone_mean_rt")
colnames(auditory_rt_slopes)[1] <- "auditory_part_id"
auditory_output <- merge(merge(auditory_rt_check, exp_auditory_mean_rts), auditory_rt_slopes)

# Check auditory output
auditory_output

# Write  results and save them to NAS
write.csv(auditory_output, paste0(output_path, "adult_in_scanner_behavioral.csv"))








