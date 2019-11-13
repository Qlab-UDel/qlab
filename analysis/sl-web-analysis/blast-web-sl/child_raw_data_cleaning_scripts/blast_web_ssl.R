#  BLAST SSL Analysis
#  Jojo Hu
#  Last updated Sep 29th 2019 
#  Adapted from mturk_ssl by An Nguyen and blast_web_ssl from Violet Kozloff
#  This script analyses reaction time, accuracy and entropy for ssl files from the online session of the BLAST experiment
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------

# Set directory

install.packages("reshape")
library("reshape")
install.packages("DescTools")
library("DescTools")

# Remove objects in environment
rm(list=ls())

# Directory for children
#setwd("/Volumes/data/projects/spoli/raw_sl_data")
# Directory for adults
#setwd("/Volumes/data/projects/blast/data/online_sl/blast_adult/")
# NOTE: Try this one if the previous one has the "cannot change working directory" error
setwd("/Volumes/data/projects/blast/data/online_sl/blast_child")
# For SPOLI
# setwd("/Volumes/data-1/projects/spoli/raw_sl_data")

#Input path
input_path <- ("/Volumes/data/projects/blast/data/online_sl/blast_child/")
#input_path <- ("/Volumes/data/projects/spoli/raw_sl_data/")
#Since June 11th 2019, the test phase of all SL tasks have been changed to a balanced design
#New answer keys should be used
input_path2 <- ("/Volumes/data/projects/blast/data/online_sl/blast_child/counterbalance_2afc_sl_data/")
#input_path2 <- ("/Volumes/data/projects/spoli/raw_sl_data/counterbalance_2afc_sl_data/")
# Output path for adults
# output_path <- ("/Volumes/data/projects/blast/data_summaries/blast_online_adult/breakdown/")
# NOTE: Try this one if you can't connect to this output path
output_path <- ("/Volumes/data/projects/blast/data_summaries/blast_online_child/breakdown/")
#output_path <- ("/Volumes/data/projects/spoli/data_summaries/breakdown/")


# Read in the entropy key
ssl_entropy_key <-
  read.csv("/Volumes/data/projects/blast/data/online_sl/entropy_keys/ssl_entropy_key.csv")
ssl_entropy_key <-
  (ssl_entropy_key[c("target_type",
                     "target_order",
                     "target_occurance_order",
                     "syllable_target")])

# Read in the entropy key
ssl_entropy_key_bal <-
  read.csv("/Volumes/data/projects/blast/data/online_sl/balanced2afc_entropy_keys/ssl_bal_entropy.csv")
ssl_entropy_key_bal <-
  (ssl_entropy_key_bal[c("target_type",
                         "answer_key",
                         "syllable_target")])



# Extract data from files ------------------------------------------------------------

# Ask user for input on how many files are expected (i.e. how many participants are there?)
#correct_total_files <- as.integer(readline("How many total participants should there be for this file type? Enter this into the console. If you are not sure, check the qlab_participant_checklist.   "))

# List input files
ssl_files <- list.files(pattern="*ssl.csv")

# Confirm that all files are present. If not, alert user
# if(length(ssl_files)!=correct_total_files) {
#   stop(print(
#     paste(
#       "Found",
#       length(ssl_files),
#       "files. You indicated that there are",
#       correct_total_files,
#       "participants. Please check files in folder against the qlab_participant_checklist."
#     )
#   ))
# }

# Initialize variable to hold data
ssl <- NULL

# Extract relevant data and combine it
for (file in ssl_files) {
  # Select only relevant columns
  extracted_data <-
    read.csv(file)[c("rt", "trial_index", "targ", "key_press", "stimulus")]
  # Create a column populated with the participant ID based on the file name
  extracted_data["part_id"] <- substr(basename(file), 1, 11)
  # Change target and stimulus to string
  extracted_data["targ"] <- as.character(extracted_data$targ)
  extracted_data["stimulus"] <-
    as.character(extracted_data$stimulus)
  # The keypress value recorded as "rt" in the raw files is not the true reaction time. Rename the column. See below for details on how to use this value.
  colnames(extracted_data)[colnames(extracted_data) == "rt"] <-
    "press_time"
  # Standardize stimulus names and types
  extracted_data$stimulus <-
    gsub(".wav", "", extracted_data$stimulus)
  extracted_data$stimulus <-
    gsub("sound/", "", extracted_data$stimulus)
  extracted_data$press_time <- as.numeric(extracted_data$press_time)
  # Identify blank keypresses
  extracted_data[which(extracted_data$press_time == -1000),]$press_time <-
    NA
  # Identify preceding and following stimuli
  extracted_data$two_stim_before <-
    append(NA, (append(NA, head(
      extracted_data$stimulus, -2
    ))))
  extracted_data$prev_stim <-
    append(NA, (head(extracted_data$stimulus, -1)))
  extracted_data$next_stim <-
    append(extracted_data$stimulus[-1], NA)
  extracted_data$two_stim_later <-
    append(append((tail(
      extracted_data$stimulus, -2
    )), NA), NA)
  # Combine data from current file
  ssl <- rbind(ssl, extracted_data)
}

#RT analysis--------------------------------------------------------------------------------------------------------------
# Calculate true keypress times.
# NOTE: There is a 100 ms pause at the beginning of the trial, between when the trial starts and when the stimulus appears. 
# Keypresses recorded during the 100 ms pause are actually responses to the previous stimulus.
# These help figure out how many negative values were used in calculating a keypress, versus how many were from a second keypress for the same stimulus

calculated <-NULL
removed <- NULL
negatives <- 0

for (i in 2:length(ssl$press_time)) {
  # Identify negative keypress values following NAs. Use them to calculate the preceding stimuli's response times
  #380+100+negative RT time = real RT for the NA trial
  if (ssl[i, ]$press_time < 0 &
      is.na(ssl[i - 1, ]$press_time) & !is.na(ssl[i, ]$press_time)) {
    ssl[i - 1, ]$press_time <- 480 + (ssl[i, ]$press_time)
    calculated <-
      append(calculated, (paste(i, ":", ssl[i, ]$press_time)))
    ssl[i, ]$press_time <- NA
    negatives <- negatives + 1
  }
  
  # Identify negative keypress values following valid keypresses. Remove the duplicates.
  else if (ssl[i,]$press_time <0 & !is.na(ssl[i-1,]$press_time) & !is.na(ssl[i,]$press_time)){
    removed <- append(removed, (paste(i, ":", ssl[i,]$press_time)))
    ssl[i,]$press_time<- NA
    negatives <- negatives +1
  }
}

# List all the participants
all_ids<- unique(ssl$part_id)


# Calculate and summarize true reaction times ------------------------------------------------------------

# Set boundaries for the exposure phase. These correspond to the first and last trial numbers
# NOTE: Due to some variation between files, include the lowest and highest trial numbers across all files

exp_phase_start <-10
exp_phase_end <-585

# Extract exposure phase
exp_phase <- ssl[which(ssl$trial_index<=exp_phase_end & ssl$trial_index>=exp_phase_start),]

# Remove extra instructions present in some files
exp_phase <- exp_phase[!(exp_phase$stimulus=="ssl_instr7"),]
exp_phase <- exp_phase[!(exp_phase$stimulus=="ssl_instr8"),]

# Internal check: Make sure that there are 575 or 576 stimuli per participant
# Note: Some early SSL files previously only had 575 stimuli, so there could be 575 or 576 targets.
# Initialize variables
total_stimuli <- NULL
# Find the number of stimuli for each participant
for(check_id in unique(exp_phase$part_id)){
# TO DO: return this at the end
  total_stimuli <- append(total_stimuli, length(which(exp_phase$part_id==check_id)))}
stimulus_check <- (cbind(all_ids, total_stimuli))

# Identify participants with too few/many targets and alert user if present
# NOTE: For SSL specifically, the 575 or 576 is an acceptable number of stimuli because an earlier version of the task only have 575.
if((! all(unique (total_stimuli) == c(575, 576))) & (! all(unique (total_stimuli) == c(576, 575)))){
  # Create error message alerting user
  print(" The following participant(s) has an incorrect number of extracted trials:")
  # List the participants with the wrong number of targets
  print(paste("", stimulus_check[which(total_stimuli!="576"&total_stimuli!="575")]))
  print(" Please check the number of targets in the following input files.")
  print(" If the participant saw too few or too many stimuli, exclude them from analysis and alert the lab member maintaining bluehost.")
  print(" If the wrong number of stimuli was extracted, adjust the values of exp_phase_start and exp_phase_end.")
  # Open a new window showing the user the number of targets for each participant
  View(stimulus_check)
  stop()}

# Make sure that no extra stimuli from the instructions phases carried over into the exposure phase at the beginning/ end of the block
for(id in unique(exp_phase$part_id)){
  # Find the exposure phase for this participant
  this_exp_phase <- exp_phase[(which(exp_phase$part_id==id)),]
  # Find the highest and lowest trials from this participant
  this_first_trial <- min(this_exp_phase$trial_index)
  this_last_trial <- max(this_exp_phase$trial_index)
  # for the first 2 exposure trials for this participant, remove any stimuli that came from two trials before (during the previous instruction block)
  this_exp_phase[which(this_exp_phase$trial==this_first_trial),]$two_stim_before <- NA
  this_exp_phase[which(this_exp_phase$trial==this_first_trial+1),]$two_stim_before <- NA
  # for the first exposure trial for this participant, remove any stimuli that came from the previous trial (during the previous instruction block)
  this_exp_phase[which(this_exp_phase$trial==this_first_trial),]$prev_stim <- NA
  # for the last exposure trial for this participant, remove any stimuli that came from the following trial (during the previous instruction block)
  this_exp_phase[which(this_exp_phase$trial==this_last_trial),]$next_stim <- NA
  # for the last 2 exposure trials for this participant, remove any stimuli that came from two trials before (during the previous instruction block)
  this_exp_phase[which(this_exp_phase$trial==(this_last_trial-1)),]$two_stim_later <- NA
  this_exp_phase[which(this_exp_phase$trial==this_last_trial),]$two_stim_later <- NA
  # Update the exposure phase with the corrected data
  exp_phase[(which(exp_phase$part_id==id)),] <- this_exp_phase
}


# Extract the row numbers for all lines in which the stimulus is the target
#Why does this command work here but not in lsl and vsl? How come only the target for the pariticipant is extracted?
targets <- which(exp_phase$targ==exp_phase$stimulus)

# Set the number of targets expected per participant
# Note: Some early SSL files previously only had 575 stimuli, so the final target was cut off. For this reason, there could be 47 or 48 targets.
correct_total_targets <- c(48, 47)

# Internal check: Make sure that there are the right number of targets per participant
# Initialize variables
target_rows <-(exp_phase[targets,])
total_targets <- NULL
# Find the number of targets for each participant
for(check_id in unique(exp_phase$part_id)){
  total_targets <- append(total_targets, length(which(target_rows$part_id==check_id)))}
target_check <- (cbind(all_ids, total_targets))

# Identify participants with too few/many targets and alert user if present
# NOTE: There may be only files with 48 targets, or some with 47 and others with 48, depednding on your dataset
if(! all(unique (total_targets) == correct_total_targets) & (! all(unique (total_targets) == 48)) ){
  # Create error message alerting user
  print(" The following participant(s) has an incorrect number of extracted targets:")
  # List the participants with the wrong number of targets
  print(paste("", target_check[which(total_targets!=correct_total_targets)]))
  print(" Please check the number of targets in the following input files.")
  print(" If the participant saw too few or too many targets, exclude them from analysis and alert the lab member maintaining bluehost.")
  print(" If the wrong number of targets was extracted, adjust exp_phase_start + exp_phase_end.")
  # Open a new window showing the user the number of targets for each participant
  View(target_check)
  stop()}

# Extract the response time and trial number when stimulus is the target------------------

# A valid response time comes from:
#   - A keypress during the 480 ms prior to the target stimulus presentation (anticipation)
#   - A keypress during the 480 ms after the target stimulus is presented (on-target)
#   - A keypress during the 480 ms after the following stimulus is presented (delay)

# TO DO: For visual, make sure it's only during the preceding trial or the target

# Variables to extract
id <- NULL
trial <- NULL
reaction_time <- NULL
type <- NULL
exp_phase$type <- NA

# # # Note: these variables aren't necessary, but they are useful for understanding and troubleshooting RT calculations for each case
#  target <- NULL
#  this_preceding_trial_press <-NULL
#  preceding_trial_press <-NULL
#  this_target_trial_press <-NULL
#  target_trial_press <-NULL
#  following_trial_press <-NULL
#  this_following_trial_press <-NULL

# Calculate true reaction times
for (i in targets){
  
  # Isolate variables used for calculations
  # Current trial
  this_trial <- exp_phase[i,][,"trial_index"]
  # List of all  targets' trials
  trial <- append(trial, this_trial)
  # Current id
  id <- append(id,exp_phase[i,]$part_id)
  # Keypress time recorded from preceding trial
  {if(this_trial>exp_phase_start) {
    this_preceding_trial_press <- exp_phase[i-1,][,"press_time"]}
    else {
      this_preceding_trial_press <- NA}}
  
  # Press time recorded for current target
  this_target_trial_press <- exp_phase[i,][,"press_time"]
  
  # # NOTE: Uncomment this section for troubleshooting the number of targets/ RTs
  # # # Press time recorded for following trial
  #  {if(this_trial<exp_phase_end){
  #    this_following_trial_press <- exp_phase[i+1,][,"press_time"]}
  #   else {
  #     this_following_trial_press <- NA}}
  #  # List of all target stimuli
  #  target <- append(target, as.character(exp_phase[i,]$targ))
  # # # List of keypress time for trials preceding all targets
  #  preceding_trial_press <- append (preceding_trial_press, this_preceding_trial_press)
  #  # List of press times for all targets
  #  target_trial_press <- append(target_trial_press, this_target_trial_press)
  #  # List of press times for trials following all targets
  #  following_trial_press <- append(following_trial_press, this_following_trial_press)
  
  # Anticipation, positive RT from preceding trial: )
  if (!is.na(exp_phase[i-1,]$press_time > 0) & (exp_phase[i-1,]$press_time > 0)){
    reaction_time <- append(reaction_time, (this_preceding_trial_press-480))
    exp_phase[i,]$type <- "hit_before"
    type <- rbind(type, "hit_before")
  }
  
  # On-target, positive RT from target trial)
  else if (!is.na(exp_phase[i,]$press_time > 0) & exp_phase[i,]$press_time > 0){
    reaction_time <- append(reaction_time, (exp_phase[i,][,"press_time"]))
    exp_phase[i,]$type <- "hit_during"
    type <- rbind(type, "hit_during")
  }
  
  # Delay, positive RT from following trial
  # else if ( !is.na(this_trial< exp_phase_end & exp_phase[i+1,]$press_time > 0) & (this_trial< exp_phase_end & exp_phase[i+1,]$press_time > 0)){
  else if (!is.na(exp_phase[i+1,]$press_time > 0) & (exp_phase[i+1,]$press_time > 0)){
    reaction_time <- append(reaction_time, (480+exp_phase[i+1,][,"press_time"]))
    exp_phase[i,]$type <- "hit_after"
    type <- rbind(type, "hit_after")
  }
  
  # Misses
  else {
    reaction_time <- append(reaction_time, NA)
    exp_phase[i,]$type <- "miss"
    type <- rbind(type, "miss")
  }
}

# exp_targets now contains all targets from the exposure phase and their true RTs (includes any response within 480 ms of a target)
exp_targets <- data.frame(trial,reaction_time,id)

# # NOTE: If you are missing RTs or they seem inaccurate, uncomment all variables above, as well as the following section, to help troubleshoot
# This shows all exp_phase lines pulled out as targets
#  exp_targets_check1 <- exp_phase[which(exp_phase$targ==exp_phase$stimulus),]
# # This shows the details of lines with targets
#  exp_targets_check2 <- data.frame(id, trial,reaction_time, type, preceding_trial_press, target_trial_press, following_trial_press)

# Find the number of RTs for each participant

# Initialize variables
total_rts <- NULL
# Check RTs
for(check_id in all_ids){
  total_rts <- append(total_rts, length(which(exp_targets$id==check_id)))}
rt_check <- (cbind(all_ids, total_rts))

# Idenitify participants with too few/many RTs and alert user if present
# NOTE: Depending on the data set, may or may not have participants with only 47 RTs
if(! all(unique (total_rts) == correct_total_targets) & (! all(unique (total_rts) == 48))){
  # Create error message alerting user
  print(" The following participant(s) has an incorrect number of reaction times:")
  # List the participants with the wrong number of RTs
  print(paste("", rt_check[which(total_rts!=correct_total_targets)]))
  print(" Please check the reaction time calculations as indicated in line 260 before continuing.")
  # Open a new window showing the user the number of RTs for each participant
  View(rt_check)
  stop()}

# Reindex the targets from 1 to the expected number of targets for each participant

targ_index <- NULL

for (i in total_rts) 
{targ_index <- append(targ_index, rep(1:i),1)}
exp_targets$targ_index <- targ_index

# Find reaction time slopes and mean reaction times and write them to NAS ------------------------------------

# Internal check: make sure that all RTs are valid, ie. fall within 1 SOA of the stimulus
check_rts_1 <- exp_targets[which(exp_targets$reaction_time!=-1 & exp_targets$reaction_time>960),]
check_rts_2 <- exp_targets[which(exp_targets$reaction_time< -480),]

# Alert the user of invalid RTs
if(length(check_rts_1[,1]) | length(check_rts_2[,1]) !=0){
  # Create error message alerting user
  print("One or more participants has an invalid reaction time. Please check the reaction time calculations above.")
  # Open a new window showing the user the RTs for each participant
  View(exp_targets)
  stop()}


# Find all the false alarms
exp_phase[which(
  # The participant pressed
  !is.na(exp_phase$press_time)
  # It was not during a target
  & exp_phase$stimulus!=exp_phase$targ
  # It was not directly before a target
  & (exp_phase$next_stim!=exp_phase$targ | is.na(exp_phase$next_stim))
  # It was not directly after a target
  & (exp_phase$prev_stim!=exp_phase$targ | is.na(exp_phase$prev_stim))
  # Change their type 
),]$type<-"false_alarm"


# Find all the correct rejections
exp_phase[which(
  # The participant did not press
  is.na(exp_phase$press_time)
  # It was not during a target
  & exp_phase$stimulus!=exp_phase$targ
  # It was not directly before a target
  & (exp_phase$next_stim!=exp_phase$targ | is.na(exp_phase$next_stim))
  # It was not directly after a target
  & (exp_phase$prev_stim!=exp_phase$targ | is.na(exp_phase$prev_stim))
  # Change their type 
),]$type<-"corr_rej"


# TO DO: For visual, it also counts as false alarm if it's during the following trial
# Initialize variables for RT calculations
mean_rt <- NULL
rt_slope <- NULL
# Initialize variables for response accuracy calculations
hits <- NULL
hit_rate <- NULL
misses <- NULL
miss_rate <- NULL
false_alarms <- NULL
false_alarm_rate <- NULL
corr_rej <- NULL
corr_rej_rate <- NULL
resp_acc<-NULL
keep <- NULL
distractors <- NULL
d_prime <- NULL
total_disc <- NULL
targets <- NULL
this_targets <- NULL

# Extract the mean response time and rt slope for each participant
for(id in (all_ids)) {
  this_id <- exp_phase[which(exp_phase$part_id == id), ]
  mean_rt <-
    append(mean_rt, round(mean(exp_targets$reaction_time[exp_targets$id == id], na.rm =
                                 TRUE), digits = 3))
  # Find this participant's number of hits, misses, correct rejections, and false alarms
  this_hit <-
    length(this_id[which((
      this_id$type == "hit_before" |
        this_id$type == "hit_during" |
        this_id$type == "hit_after"
    ) & this_id$part_id == id
    ), 1])
  # If there are enough hits to find RT slope, calculate it
  if (this_hit > 1) {
    #extract each id's individual rt by trial
    rt_by_trial <- exp_targets[which(exp_targets$id == id), "reaction_time"]
    #scale the rt based on mean and sd
    scaled_rt_by_id <- scale(rt_by_trial)
    #save the scaled rt to a new column
    exp_targets[which(exp_targets$id == id), "scaled_rt"]<- scaled_rt_by_id
    #Calculate rt slope
    rt_slope <-
      append(rt_slope, round(summary(
        lm(exp_targets$scaled_rt[exp_targets$id == id] ~ exp_targets$targ_index[exp_targets$id ==
                                                                                      id])
      )$coefficient[2, 1], digits = 3))
  }
  # Otherwise, record that there are too few
  else {
    rt_slope <- append(rt_slope, "too few hits")
  }
  this_miss <-
    length(this_id[which((this_id$type == "miss") &
                           this_id$part_id == id), 1])
  this_corr_rej <-
    length(this_id[which((this_id$type == "corr_rej") &
                           this_id$part_id == id), 1])
  this_false_alarm <-
    length(this_id[which((this_id$type == "false_alarm") &
                           this_id$part_id == id), 1])
  # TO DO: Add to SSL, LSL, VSL
  total_disc <-
    append (total_disc,
            (this_hit + this_miss + this_corr_rej + this_false_alarm))
  # Store these values for all participants
  hits <- append (hits, this_hit)
  misses <- append (misses, this_miss)
  corr_rej <- append(corr_rej, this_corr_rej)
  false_alarms <- append (false_alarms, this_false_alarm)
  # Find the d-prime
  this_d_prime <-
    qnorm(this_hit / (this_hit + this_miss)) - qnorm(this_false_alarm / (this_false_alarm +
                                                                           this_corr_rej))
  d_prime <- append (d_prime, this_d_prime)
  # Find the rates of each
  this_distractors <- this_false_alarm + this_corr_rej
  distractors <- append (distractors, this_distractors)
  this_targets <- this_hit + this_miss
  targets <- append (targets, this_targets)
  hit_rate <-
    append(hit_rate, round(this_hit / this_targets, digits = 3))
  miss_rate <-
    append (miss_rate, round(this_miss / this_targets, digits = 3))
  false_alarm_rate <-
    append(false_alarm_rate, round(this_false_alarm / (this_distractors), digits = 3))
  corr_rej_rate <-
    append(corr_rej_rate, round(this_corr_rej / (this_distractors), digits = 3))
  this_resp_acc <-
    round((this_corr_rej + this_hit) / (this_distractors + 48), digits = 3)
  resp_acc <- append(resp_acc, this_resp_acc)
}

indiv_rts <- cbind(all_ids, mean_rt, rt_slope, d_prime, this_targets, hits, hit_rate, misses, miss_rate, corr_rej, corr_rej_rate, false_alarms, false_alarm_rate, distractors, total_disc, resp_acc, total_stimuli)


# Remove any extra columns that are only helpful for internal checks
# Tidy up column names
colnames(indiv_rts)[colnames(indiv_rts)=="all_ids"] <- "par_id"
colnames(indiv_rts)[colnames(indiv_rts)=="rt_slope"] <- "scaled_rt_slope"

# Write individual RT results and save them to NAS
# NOTE: This is for adult files
#write.csv(indiv_rts, paste0(output_path, "online_adult_tsl_indiv_rts.csv"))
write.csv(indiv_rts, paste0(output_path, "blast_online_children_ssl_indiv_rts.csv"))
#Save rt by trial data
write.csv(exp_targets, paste0(output_path, "rt_by_trial/blast_ssl_rt_by_trial.csv"))
# TO DO: Add this for children



# TO DO: Fix this for 479 or 480. Also SSL is messy and sometimes there are a weird number of them
# Identify participants with too few/many discrimintations and alert user if present
# if(! all(unique (total_disc) == "480")){
#   # Create error message alerting user
#   print(" The following participant(s) has an incorrect number of discriminations:")
#   # List the participants with the wrong number of targets
#   # TO DO: Make sure SSL, LSL, and VSL don't say 576 here
#   print(paste("", indiv_rts[which(total_disc!="480")]))
#   print(" Please check how discriminations are categorized for this participant in exp_phase$type.")
#   # Open a new window showing the user the number of targets for each participant
#   View(indiv_rts)
#   stop()}




# Note: Uncomment this to find and exclude participants with unusually high/ low RT slopes
# Find values for 2.5 standard deviations within the mean
# lowerbound <- mean(mean(gsub(indiv_rts$rt_slope, "low hits", NA), na.rm = TRUE)) - 2.5*sd(gsub(indiv_rts$rt_slope, "low hits", NA), na.rm = TRUE)
# lowerbound <- mean(mean(gsub(indiv_rts$rt_slope, "low hits", NA), na.rm = TRUE)) + 2.5*sd(gsub(indiv_rts$rt_slope, "low hits", NA), na.rm = TRUE)
# Check whose RT slope is unusually low
# too_low <- indiv_rts[indiv_rts$rt_slope<=lowerbound,]
# Check whose rt slope is unusually high
# too_high <- indiv_rts[indiv_rts$rt_slope>=upperbound,]
# Remove participants with unusual RT slopes
# indiv_rts <- indiv_rts[indiv_rts$press_time_slope>=lowerbound,]
# indiv_rts <- indiv_rts[indiv_rts$press_time_slope<=upperbound,]

# Remove any extra columns that are only helpful for internal checks
# Tidy up column names
#colnames(indiv_rts)[colnames(indiv_rts)=="all_ids"] <- "part_id"

# Write individual RT results and save them to NAS
# NOTE: This is for adult files
#write.csv(indiv_rts, paste0(output_path, "online_adult_ssl_indiv_rts.csv"))

# write.csv(indiv_rts, paste0(output_path, "online_child_ssl_indiv_rts.csv"))
# TO DO: Add this for children

#End of RT analysis----------------------------------------------------------------------------------------



# Calculate and summarize individual accuracies ------------------------------------------------------------

#List the ssl files after June 11th, 2019 with counterbalanced target-foils in the test phase
#Extract the ids for balanced lsl
ssl_files_balanced <- list.files(path=input_path2, pattern="*ssl.csv")
ssl_bal_id <- str_extract(ssl_files_balanced, "\\S+(?=_ssl.csv)")
#List the files that are not counterbalanced which are collected before June 11th, 2019
ssl_files_unbal <- ssl_files[!(ssl_files %in% ssl_files_balanced)]
ssl_unb_id <- str_extract(ssl_files_unbal, "\\S+(?=_ssl.csv)")

#Extract the data for participants who did unbalanced design
ssl_unb <- ssl[which(ssl$part_id %in% unlist(ssl_unb_id)),]

#Extract the test phase
test_block <- ssl_unb[(ssl_unb$stimulus=="silence" & !ssl_unb$key_press==-1),]


#Internal check: this should be exactly 32 (32 forced choices per participant)
forced_choice_rows <- test_block[(test_block$stimulus=="silence" & !test_block$key_press==-1),]

# Initialize variables
total_2afc_rows <- NULL
# # Check how many trials each participant saw
# for(check_id in all_ids){
#   total_2afc_rows <- append(total_2afc_rows, length(which(forced_choice_rows$id==check_id)))}
# forced_check <- (cbind(all_ids, total_rts))
# # Idenitify participants with too few/many RTs and alert user if present
# if(! all(unique (total_rts) == correct_total_targets)){
#   # Create error message alerting user
#   print(" The following participant(s) has an incorrect number of reaction times:")
#   # List the participants with the wrong number of RTs
#   print(paste("", rt_check[which(total_rts!=correct_total_targets)]))
#   print(" Please check the reaction time calculations as indicated in line 260 before continuing.")
#   # Open a new window showing the user the number of RTs for each participant
#   View(forced_check)
#   stop()}

ans <- NULL
keyv <- NULL
subj <- NULL
cond<- NULL

#Extract rows in which the participant gives a response
#targetsv is just row number for the test block
targetsv <- which(test_block$key_press != -1 & test_block$stimulus=="silence")
for (i in targetsv){
  ans<-append(ans,test_block[i,]$key_press)
  subj <- append(subj,paste(test_block[i,]$part_id))
}

# Create a data frame that contains the participants' responses
ssl_accuracy <- data.frame(ans,subj)

keyv<- NULL

i=0


language = list(1,1,2,1,1,1,2,2,2,2,1,1,1,2,2,1,2,2,1,1,2,1,2,1,2,1,2,1,1,2,2,2)

# Combine the answer keys for the two language conditions that the participant saw
keyv <- rep(language, times = length(unique(ssl_accuracy$subj)))

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(ssl_accuracy$subj)

ssl_accuracy$key <- keyv

#Substitute the key press (37,39) with the answer (1,2)
ssl_accuracy$ans <- gsub(37,1,ssl_accuracy$ans)
ssl_accuracy$ans <- gsub(39,2,ssl_accuracy$ans)


# Entropy

# Find the triplet type (each triplet gets coded with a value from A-D)
triplet_type <- rep(ssl_entropy_key$target_type, times = length(unique(ssl_accuracy$subj)))
# Find the order for the triplet (the triplet either appeared first or second, with respect to the foil)
triplet_order <- rep(ssl_entropy_key$target_order, times = length(unique(ssl_accuracy$subj)))
# Find the occurance for the triplet (each triplet occurs between 7 and 9 times. Number each occurance.)
triplet_occurance <- rep(ssl_entropy_key$target_occurance_order, times = length(unique(ssl_accuracy$subj)))
# Find the syllable triplet (which three syllables make up the triplet)
syllable_triplet <- rep(ssl_entropy_key$syllable_target, times = length(unique(ssl_accuracy$subj)))

ssl_accuracy$triplet_type <- triplet_type
ssl_accuracy$triplet_order <- triplet_order
ssl_accuracy$triplet_occurance <- triplet_occurance
ssl_accuracy$syllable_triplet <- syllable_triplet

#Loop through and mark each answer as correct or incorrect
corr <- NULL
for (i in seq(from = 1,
              to = length(ssl_accuracy$ans),
              by = 1)) {
  corr <-
    append(corr, as.numeric(ssl_accuracy[i, ]$ans == ssl_accuracy[i, ]$key))
}
ssl_accuracy$corr <- as.integer(corr)



#Check stimuli and answer keys in the test phase against the entropy key---------------------------------
#Extract the testing phase--------------------------------------------------------------------------------

test_phase<- list()
loop_index = 0

for (id in ssl_unb_id) {
  loop_index = loop_index +1
  this_id_ssl <- ssl_unb[which(ssl_unb$part_id %in% id),]
  test_phase_index <- which(this_id_ssl$stimulus == "silence")
  test_phase_start<- test_phase_index[1]
  test_phase_end <- test_phase_index[length(test_phase_index)]
  test_phase_this_id <- this_id_ssl[test_phase_start:test_phase_end,]
  # Extract exposure phase
  test_phase[[loop_index]] <- test_phase_this_id
}

test_phase <- do.call(rbind, test_phase)


#Check whether the answer keys match the answer keys from the entropy keys----------------------------------------------------------- 
#Answer keys in the Entropy keys are always correct
test_phase_stim <- list()
loop_index = 0 
test_phase_id <- unique(ssl_unb$part_id)
trial_index <- seq(from = 1, to = 192,  by = 1)

for (id in test_phase_id) {
  loop_index = loop_index + 1
  #Extract data for current id
  this_id_data <- test_phase[which(test_phase$part_id %in% id),]
  #Extract the rows that have the silence stimuli, ssl test phase starts and ends with silence
  row_white <- which(this_id_data$stimulus == "silence")
  #Extract the test phase trials for the current participant
  stim_test <- this_id_data[row_white[1]:row_white[length(row_white)], c("part_id", "stimulus")]
  #Remove the silence stimulus
  stim_test <- stim_test[which(stim_test$stimulus != "silence"),]
  #Add in trial number
  stim_test$trial_index <- trial_index
  #Extract only the stimuli column and split into triplets
  current_id_stim <- stim_test$stimulus
  current_id_triplet <- split(current_id_stim, ceiling(seq_along(current_id_stim)/3))
  #Combine the splitted triplets into a column
  current_id_triplet <- do.call(rbind, current_id_triplet)
  #Paste the three individual stimuli in a triplet into a column
  current_id_triplet <- data.frame(current_id_triplet)
  current_id_triplet$triplet <- with(current_id_triplet, paste(X1, X2, X3, sep = "_"))
  #format the triplet column into lower case to match with the entropy file
  current_id_triplet$triplet <- paste0("syllable", current_id_triplet$triplet)
  #Extract triplets in the entropy file and insert an empty row every other row into the entropy key
  #Doing this will allow comparing 64 trials (targets + foils) with 32 trials (from entropy key)
  #First double all rows in lsl_entropy_keys
  doubled_entropy_key <- ssl_entropy_key[rep(1:nrow(ssl_entropy_key),1,each=2),]
  #Then make every other row's target triplet empty
  doubled_entropy_key[c(seq(2, dim(doubled_entropy_key)[1], by=2)), "syllable_target"] <- NA
  #Check the triplets of the current id's data against entropy key
  #Every other rowsin doubled_entropy_key shows the target triplet, so if every other row yeilds TRUE, then answer will be 1
  check_every_other_row <- 
    as.numeric(current_id_triplet$triplet %in% doubled_entropy_key$syllable_target)
  #Extract every other row and sub 0 with 2
  current_id_key <- check_every_other_row[seq(1, length(check_every_other_row), 2)]
  current_id_key <- gsub(0, 2, current_id_key)
  #Check current id's answer keys against the correct answer keys 
  current_id_correct_key <- sum(as.numeric(current_id_key == ssl_entropy_key$target_order))
  #Save the result into a list
  test_phase_stim[[loop_index]] <- data.frame(id, current_id_correct_key)
}

test_phase_stim <- do.call(rbind, test_phase_stim)

if (mean(test_phase_stim$current_id_correct_key) != 32) {
  print(test_phase_stim)
  print("Check subject IDs that do not have 32. They are not supposed to be in the counterbalanced group.")
  stop()
}

#---------------------------------------------------------------------------------------------------------------


# Entropy
ssl_entropy_wide <-
  cast(ssl_accuracy,
       subj ~ corr + triplet_type,
       value = "syllable_triplet",
       fun.aggregate = length)


#Caculate Entropy for each target type by group and by task
ssl_entropy_by_triplet <- data.frame()

# SSL Entropy for each target type
for (i in 1:nrow(ssl_entropy_wide)) {
  ssl_entropy_by_triplet[i,"ssl_a_entropy"] <- Entropy(ssl_entropy_wide[i,c("0_A","1_A")])
  ssl_entropy_by_triplet[i,"ssl_b_entropy"] <- Entropy(ssl_entropy_wide[i,c("0_B","1_B")])
  ssl_entropy_by_triplet[i,"ssl_c_entropy"] <- Entropy(ssl_entropy_wide[i,c("0_C","1_C")])
  ssl_entropy_by_triplet[i,"ssl_d_entropy"] <- Entropy(ssl_entropy_wide[i,c("0_D","1_D")])
  ssl_entropy_by_triplet[i,"part_id"] <- ssl_entropy_wide[i,c("subj")]
}


ssl_entropy_by_triplet$mean_entropy <- round(rowMeans(ssl_entropy_by_triplet[,1:4], na.rm = FALSE, dims = 1), 3)


# Count the correct answers for each participant
subj_corr <- NULL
for (id in acc_id) {
  subj_corr <-
    append(subj_corr, round(sum(ssl_accuracy$corr[ssl_accuracy$subj == id]) /
                              32, digits = 3))
}

ssl_acc_table <- data.frame(acc_id, subj_corr)

#Why remove outliners here???
# lowerbound <- mean(ssl_acc_table$subj_corr) - 2.5*sd(ssl_acc_table$subj_corr)
# upperbound <- mean(ssl_acc_table$subj_corr) + 2.5*sd(ssl_acc_table$subj_corr)
# 
# # Internal check: whose mean rt is unusually low?
# too_low <- ssl_acc_table[ssl_acc_table$subj_corr<=lowerbound,]
# # Internal check: whose data is unusually high?
# too_high <- ssl_acc_table[ssl_acc_table$subj_corr>=upperbound,]

#End of unbalanced accuracy analysis-----------------------------------------------------------------------------------




#Analyze accuracy for participants (after June 11th, 2019) who did the balanced test phase----------------------------------------------------------------
# Calculate and summarize individual accuracies ------------------------------------------------------------

#List the ssl files after June 11th, 2019 with counterbalanced target-foils in the test phase
#Extract the ids for balanced ssl
ssl_files_balanced <- list.files(path=input_path2, pattern="*ssl.csv")
ssl_bal_id <- str_extract(ssl_files_balanced, "\\S+(?=_ssl.csv)")

#Extract the data for participants who did balanced design
ssl_bal <- ssl[which(ssl$part_id %in% unlist(ssl_bal_id)),]


#Extract the test phase
test_block <- ssl_bal[(ssl_bal$stimulus=="silence" & !ssl_bal$key_press==-1),]


#Internal check: this should be exactly 32 (32 forced choices per participant)
forced_choice_rows <- test_block[(test_block$stimulus=="silence" & !test_block$key_press==-1),]

# Initialize variables
total_2afc_rows <- NULL
# # Check how many trials each participant saw
# for(check_id in all_ids){
#   total_2afc_rows <- append(total_2afc_rows, length(which(forced_choice_rows$id==check_id)))}
# forced_check <- (cbind(all_ids, total_rts))
# # Idenitify participants with too few/many RTs and alert user if present
# if(! all(unique (total_rts) == correct_total_targets)){
#   # Create error message alerting user
#   print(" The following participant(s) has an incorrect number of reaction times:")
#   # List the participants with the wrong number of RTs
#   print(paste("", rt_check[which(total_rts!=correct_total_targets)]))
#   print(" Please check the reaction time calculations as indicated in line 260 before continuing.")
#   # Open a new window showing the user the number of RTs for each participant
#   View(forced_check)
#   stop()}

ans <- NULL
keyv <- NULL
subj <- NULL
cond<- NULL

#Extract rows in which the participant gives a response
#targetsv is just row number for the test block
targetsv <- which(test_block$key_press != -1 & test_block$stimulus=="silence")
for (i in targetsv){
  ans<-append(ans,test_block[i,]$key_press)
  subj <- append(subj,paste(test_block[i,]$part_id))
}

# Create a data frame that contains the participants' responses
ssl_accuracy <- data.frame(ans,subj)

keyv<- NULL

i=0


language = list(2,1,1,2,1,2,2,1,1,2,2,1,2,1,2,1,1,2,1,2,2,1,2,1,1,2,2,1,1,2,1,2)

# Combine the answer keys for the two language conditions that the participant saw
keyv <- rep(language, times = length(unique(ssl_accuracy$subj)))

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(ssl_accuracy$subj)

ssl_accuracy$key <- keyv

#Substitute the key press (37,39) with the answer (1,2)
ssl_accuracy$ans <- gsub(37,1,ssl_accuracy$ans)
ssl_accuracy$ans <- gsub(39,2,ssl_accuracy$ans)


# Entropy

# Find the triplet type (each triplet gets coded with a value from A-D)
triplet_type <- rep(ssl_entropy_key_bal$target_type, times = length(unique(ssl_accuracy$subj)))
# Find the order for the triplet (the triplet either appeared first or second, with respect to the foil)
triplet_order <- rep(ssl_entropy_key_bal$answer_key, times = length(unique(ssl_accuracy$subj)))
# Find the syllable triplet (which three syllables make up the triplet)
syllable_triplet <- rep(ssl_entropy_key_bal$syllable_target, times = length(unique(ssl_accuracy$subj)))

ssl_accuracy$triplet_type <- triplet_type
ssl_accuracy$triplet_order <- triplet_order
ssl_accuracy$syllable_triplet <- syllable_triplet

#Loop through and mark each answer as correct or incorrect
corr <- NULL
for (i in seq(from = 1,
              to = length(ssl_accuracy$ans),
              by = 1)) {
  corr <-
    append(corr, as.numeric(ssl_accuracy[i, ]$ans == ssl_accuracy[i, ]$key))
}
ssl_accuracy$corr <- as.integer(corr)



#Check stimuli and answer keys in the test phase against the entropy key---------------------------------
#Extract the testing phase--------------------------------------------------------------------------------

test_phase<- list()
loop_index = 0

for (id in ssl_bal_id) {
  loop_index = loop_index +1
  this_id_ssl <- ssl_bal[which(ssl_bal$part_id %in% id),]
  test_phase_index <- which(this_id_ssl$stimulus == "silence")
  test_phase_start<- test_phase_index[1]
  test_phase_end <- test_phase_index[length(test_phase_index)]
  test_phase_this_id <- this_id_ssl[test_phase_start:test_phase_end,]
  # Extract exposure phase
  test_phase[[loop_index]] <- test_phase_this_id
}

test_phase <- do.call(rbind, test_phase)


#Check whether the answer keys match the answer keys from the entropy keys----------------------------------------------------------- 
#Answer keys in the Entropy keys are always correct
test_phase_stim <- list()
loop_index = 0 
test_phase_id <- unique(ssl_bal$part_id)
trial_index <- seq(from = 1, to = 192,  by = 1)

for (id in test_phase_id) {
  loop_index = loop_index + 1
  #Extract data for current id
  this_id_data <- test_phase[which(test_phase$part_id %in% id),]
  #Extract the rows that have the silence stimuli, ssl test phase starts and ends with silence
  row_white <- which(this_id_data$stimulus == "silence")
  #Extract the test phase trials for the current participant
  stim_test <- this_id_data[row_white[1]:row_white[length(row_white)], c("part_id", "stimulus")]
  #Remove the silence stimulus
  stim_test <- stim_test[which(stim_test$stimulus != "silence"),]
  #Add in trial number
  stim_test$trial_index <- trial_index
  #Extract only the stimuli column and split into triplets
  current_id_stim <- stim_test$stimulus
  current_id_triplet <- split(current_id_stim, ceiling(seq_along(current_id_stim)/3))
  #Combine the splitted triplets into a column
  current_id_triplet <- do.call(rbind, current_id_triplet)
  #Paste the three individual stimuli in a triplet into a column
  current_id_triplet <- data.frame(current_id_triplet)
  current_id_triplet$triplet <- with(current_id_triplet, paste(X1, X2, X3, sep = "_"))
  #format the triplet column into lower case to match with the entropy file
  current_id_triplet$triplet <- paste0("syllable", current_id_triplet$triplet)
  #Extract triplets in the entropy file and insert an empty row every other row into the entropy key
  #Doing this will allow comparing 64 trials (targets + foils) with 32 trials (from entropy key)
  #First double all rows in lsl_entropy_keys
  doubled_entropy_key <- ssl_entropy_key_bal[rep(1:nrow(ssl_entropy_key_bal),1,each=2),]
  #Then make every other row's target triplet empty
  doubled_entropy_key[c(seq(2, dim(doubled_entropy_key)[1], by=2)), "syllable_target"] <- NA
  #Check the triplets of the current id's data against entropy key
  #Every other rowsin doubled_entropy_key shows the target triplet, so if every other row yeilds TRUE, then answer will be 1
  check_every_other_row <- 
    as.numeric(current_id_triplet$triplet %in% doubled_entropy_key$syllable_target)
  #Extract every other row and sub 0 with 2
  current_id_key <- check_every_other_row[seq(1, length(check_every_other_row), 2)]
  current_id_key <- gsub(0, 2, current_id_key)
  #Check current id's answer keys against the correct answer keys 
  current_id_correct_key <- sum(as.numeric(current_id_key == ssl_entropy_key_bal$answer_key))
  #Save the result into a list
  test_phase_stim[[loop_index]] <- data.frame(id, current_id_correct_key)
}

test_phase_stim <- do.call(rbind, test_phase_stim)

if (mean(test_phase_stim$current_id_correct_key) != 32) {
  print(test_phase_stim)
  print("Check subject IDs that do not have 32. They are not supposed to be in the counterbalanced group.")
  stop()
}

#---------------------------------------------------------------------------------------------------------------


# Entropy
ssl_entropy_wide_bal <-
  cast(ssl_accuracy,
       subj ~ corr + triplet_type,
       value = "syllable_triplet",
       fun.aggregate = length)


#Caculate Entropy for each target type by group and by task
ssl_entropy_by_triplet_bal <- data.frame()

# SSL Entropy for each target type
for (i in 1:nrow(ssl_entropy_wide_bal)) {
  ssl_entropy_by_triplet_bal[i,"ssl_a_entropy"] <- Entropy(ssl_entropy_wide_bal[i,c("0_A","1_A")])
  ssl_entropy_by_triplet_bal[i,"ssl_b_entropy"] <- Entropy(ssl_entropy_wide_bal[i,c("0_B","1_B")])
  ssl_entropy_by_triplet_bal[i,"ssl_c_entropy"] <- Entropy(ssl_entropy_wide_bal[i,c("0_C","1_C")])
  ssl_entropy_by_triplet_bal[i,"ssl_d_entropy"] <- Entropy(ssl_entropy_wide_bal[i,c("0_D","1_D")])
  ssl_entropy_by_triplet_bal[i,"part_id"] <- ssl_entropy_wide_bal[i,c("subj")]
}


ssl_entropy_by_triplet_bal$mean_entropy <- round(rowMeans(ssl_entropy_by_triplet_bal[,1:4], na.rm = FALSE, dims = 1), 3)


# Count the correct answers for each participant
subj_corr <- NULL
for (id in acc_id) {
  subj_corr <-
    append(subj_corr, round(sum(ssl_accuracy$corr[ssl_accuracy$subj == id]) /
                              32, digits = 3))
}

ssl_acc_table_bal <- data.frame(acc_id, subj_corr)

#---------------------------------------------------------------------------------------------------------------
#End of balanced test phase accuracy analysis-----------------------------------------------------------------------------------------------------------------------------------

ssl_acc_table <- rbind(ssl_acc_table, ssl_acc_table_bal)

ssl_entropy_by_triplet <- rbind(ssl_entropy_by_triplet, ssl_entropy_by_triplet_bal)

ssl_entropy_wide <- rbind(ssl_entropy_wide, ssl_entropy_wide_bal)

#Save raw entropy by triplet counts
write.csv(ssl_entropy_wide,
          paste0(output_path, "entropy_by_triplet/blast_ssl_entropy_raw_sums.csv"))
#Save entropy by triplet type
write.csv(ssl_entropy_by_triplet,
          paste0(output_path, "entropy_by_triplet/blast_ssl_entropy_by_triplet.csv"))
#Save mean entropy 
write.csv(ssl_entropy_by_triplet[,5:6], 
          paste0(output_path, "blast_online_children_ssl_entropy.csv"))
#Save accuracy
write.csv(ssl_acc_table, paste0(output_path, "blast_online_children_ssl_accuracies.csv"))





