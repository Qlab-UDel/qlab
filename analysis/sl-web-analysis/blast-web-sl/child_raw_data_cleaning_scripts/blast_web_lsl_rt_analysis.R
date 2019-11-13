#  BLAST LSL RT Analysis
#  Jojo Hu
#  Last updated Sep 29th 2019 
#  Adapted from blast_web_ssl from Violet Kozloff
#  This script analyses reaction time for lsl files from the online session of the BLAST experiment
#  ****************************************************************************



install.packages("stringr")
library("stringr")
#LSL RT Slope Analysis ----------------------------------------------
input_path <- "/Volumes/data/projects/blast/data_summaries/blast_online_child_lsl_clean/predictable_lsl/"
input_path2 <- "/Volumes/data/projects/blast/data_summaries/blast_online_child_lsl_clean/"
output_path <- "/Volumes/data/projects/blast/data_summaries/blast_online_child/breakdown/"

#Include all data from predictable 2 alternative force choice and random 2 afc
#RT slope and Mean RT are only analyzed for the online but not the offline portion of the task
lsl_files <- list.files(path = input_path, pattern = "*lsl.csv")
lsl_files2 <- list.files(path = input_path2, pattern = "*lsl.csv")
lsl_files <- append(lsl_files, lsl_files2)

lsl_all <- NULL
loop_index = 0

for (file in lsl_files) {
  loop_index = loop_index + 1
  if(file %in% lsl_files2) {
  lsl <- read.csv(paste0(input_path2, file))
  } else {
    lsl <- read.csv(paste0(input_path, file))
  }
  #put in participant ID for each file
  lsl$par_id <-
  str_extract(as.character(file), "\\S+(?=.csv)")
  
  # Identify preceding and following stimuli
  #The column has to be character type for the append function to work
 lsl$stim_disp <- as.character(lsl$stim_disp)
 
 lsl$two_stim_before <-
    append(NA, (append(NA, head(
      lsl$stim_disp, -2
    )))) 
  lsl$prev_stim <-
    append(NA, (head(lsl$stim_disp, -1)))
  lsl$next_stim <-
    append(lsl$stim_disp[-1], NA)
  lsl$two_stim_later <-
    append(append((tail(
      lsl$stim_disp, -2
    )), NA), NA)
  
  # Combine data from current file
  lsl_all <- rbind(lsl_all, lsl)
}


# Internal check: Make sure that there are 576 stimuli per participant--------------------------------
# Initialize variables
total_stimuli <- NULL

# List all the participants
all_ids<- unique(lsl_all$par_id)

# Find the number of stimuli for each participant
for(check_id in all_ids) {
  # TO DO: return this at the end
  total_stimuli <-
    append(total_stimuli, length(which(lsl_all$par_id == check_id)))
}

stimulus_check <- (cbind(all_ids, total_stimuli))

# Extract the row numbers for all lines in which the stimulus is the target--------------------

#To do: fix this in the cleaning script. Currently, some key presses time were logged onto the
#wrong displayed stimulus. It should be for the last matched stimulus between keypress and displayed
#Check jspsych to see why two key presses for the same trial was ever recorded

removed_wrong_keypress_time <- which(lsl_all[,"col1"] < lsl_all[, "time"])
lsl_all[removed_wrong_keypress_time, "col1"] <- NA
print(lsl_all[removed_wrong_keypress_time, c(1:8)])

#Internal check: Make sure that there are the right number of targets per participant---------------------------
targets = list()

for (i in 1:length(all_ids)) {
current_matched <- 
  lsl_all[which(lsl_all$par_id %in% all_ids[i]), ]$stim_disp %in% 
  lsl_all[which(lsl_all$par_id %in% all_ids[i]), ][1, "target"]
row_names_orig <-
  row.names(lsl_all[which(lsl_all$par_id %in% all_ids[i]), ][current_matched,])
targets[[i]] <- row_names_orig
#To do: Internal check: Make sure that there are the right number of targets per participant
row <- data.frame(row_names_orig)
nrow(row) == 24
colnames(row)[colnames(row)=="row_names_orig"] <- all_ids[i]
}
#To Do: alert users when targets are not 24
#cbind returns (24 target trials * subject numbers) columns here
#if cbind fails, then some participant does not have 24 targets
check_stimuli_num_for_each_subject = do.call(cbind, targets)
#Cbind to make a list
#Cbind is crucial to maintain the order of trials for each participant
targets = do.call(cbind, targets)

# Extract the response time and trial number when stimulus is the target------------------

# A valid response time comes from:
#   - A keypress during the 1000 ms prior to the target stimulus presentation (anticipation)
#   - A keypress during the 1000 ms after the target stimulus is presented (on-target)
#   - A keypress during the 1000 ms after the following stimulus is presented (delay)

# Variables to extract
trial <- list()
id <- list()
list_num = 0
reaction_time <- NULL
type <- NULL
lsl_all$type <- NA

lsl_all$col1 <- as.numeric(lsl_all$col1)
lsl_all$time <- as.numeric(lsl_all$time)
lsl_all$X <- as.numeric(lsl_all$X)

# Calculate true reaction times-----------------------------------------------------------
for (i in targets) {
  i <- as.numeric(i)
  list_num = list_num + 1
  # Isolate variables used for calculations
  # Current trial
  this_trial <- lsl_all[i,"X"]
  # List of all  targets' trials
  trial[[list_num]] <- this_trial
  # Current id
  id[[list_num]] <- lsl_all[i,]$par_id
  # Keypress time recorded from preceding trial
  #For visual tasks, the reaction time needs to be calculated from key press time - stimuli onset time
  this_preceding_trial_press <- lsl_all[i-1, "col1"]-lsl_all[i-1, "time"]
   
  # Press time recorded for current target
  this_target_trial_press <- lsl_all[i, "col1"]-lsl_all[i, "time"]
  
  
  # # NOTE: Uncomment this section for troubleshooting the number of targets/ RTs
  # # # Press time recorded for following trial
  #  {if(this_trial<lsl_all_end){
  #    this_following_trial_press <- lsl_all[i+1,][,"press_time"]}
  #   else {
  #     this_following_trial_press <- NA}}
  #  # List of all target stimuli
  #  target <- append(target, as.character(lsl_all[i,]$targ))
  # # # List of keypress time for trials preceding all targets
  #  preceding_trial_press <- append (preceding_trial_press, this_preceding_trial_press)
  #  # List of press times for all targets
  #  target_trial_press <- append(target_trial_press, this_target_trial_press)
  #  # List of press times for trials following all targets
  #  following_trial_press <- append(following_trial_press, this_following_trial_press)
  
  # Anticipation, positive RT from preceding trial: 
  
  if (!is.na(lsl_all[i-1,]$col1 > 0) & (lsl_all[i-1,]$col1 > 0)){
    reaction_time <- append(reaction_time, (this_preceding_trial_press-1000))
    lsl_all[i,]$type <- "hit_before"
    type <- rbind(type, "hit_before")
  }
  
  # On-target, positive RT from target trial)
  else if (!is.na(lsl_all[i,]$col1 > 0) & lsl_all[i,]$col1 > 0){
    reaction_time <- append(reaction_time, (this_target_trial_press))
    lsl_all[i,]$type <- "hit_during"
    type <- rbind(type, "hit_during")
  }
  
  # Delay, positive RT from following trial
  # else if ( !is.na(this_trial< lsl_all_end & lsl_all[i+1,]$press_time > 0) & (this_trial< lsl_all_end & lsl_all[i+1,]$press_time > 0)){
  else if (!is.na(lsl_all[i+1,]$col1 > 0) & (lsl_all[i+1,]$col1 > 0)){
    reaction_time <- append(reaction_time, (1000+(lsl_all[i+1, "col1"]-lsl_all[i+1, "time"])))
    lsl_all[i,]$type <- "hit_after"
    type <- rbind(type, "hit_after")
  }
  
  # Misses
  else {
    reaction_time <- append(reaction_time, NA)
    lsl_all[i,]$type <- "miss"
    type <- rbind(type, "miss")
  }
}

# exp_targets now contains all targets from the exposure phase and their true RTs (includes any response within 480 ms of a target)
#file that contains reaction time for each trial for each individual
trial = do.call(rbind, trial)
id = do.call(rbind, id)
exp_targets <- data.frame(trial,reaction_time,id)

# # NOTE: If you are missing RTs or they seem inaccurate, uncomment all variables above, as well as the following section, to help troubleshoot
# This shows all lsl_all lines pulled out as targets
#  exp_targets_check1 <- lsl_all[which(lsl_all$targ==lsl_all$stimulus),]
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

correct_total_targets = 24

if(! all(unique (total_rts) == correct_total_targets) & (! all(unique (total_rts) == 24))){
  # Create error message alerting user
  print(" The following participant(s) has an incorrect number of reaction times:")
  # List the participants with the wrong number of RTs
  print(paste("", rt_check[which(total_rts!=correct_total_targets)]))
  print(" Please check the reaction time calculations as indicated in line 260 before continuing.")
  # Open a new window showing the user the number of RTs for each participant
  View(rt_check)
  stop()}

# Reindex the targets from 1 to the expected number of targets for each participant
#What is targ_index?
targ_index <- NULL

for (i in total_rts) {
  targ_index <- append(targ_index, rep(1:i))
  }
exp_targets$targ_index <- targ_index

write.csv(exp_targets, paste0(output_path, "rt_by_trial/blast_lsl_rt_by_trial.csv"))

# Find reaction time slopes and mean reaction times and write them to NAS ------------------------------------

# Internal check: make sure that all RTs are valid, ie. fall within 1 SOA of the stimulus
check_rts_1 <- exp_targets[which(exp_targets$reaction_time!=-1 & exp_targets$reaction_time>2000),]
check_rts_2 <- exp_targets[which(exp_targets$reaction_time< -1000),]

# Alert the user of invalid RTs
if(length(check_rts_1[,1]) | length(check_rts_2[,1]) !=0){
  # Create error message alerting user
  print("One or more participants has an invalid reaction time. Please check the reaction time calculations above.")
  # Open a new window showing the user the RTs for each participant
  View(exp_targets)
  stop()}

#To do: come back to these and check cor_rej and FA
# Find all the false alarms
lsl_all[which(
  # The participant pressed
  !is.na(lsl_all$col1)
  # It was not during a target
  & lsl_all$stim_disp!=lsl_all$target
  # It was not directly before a target
  & (lsl_all$next_stim!=lsl_all$target | is.na(lsl_all$next_stim))
  # It was not directly after a target
  & (lsl_all$prev_stim!=lsl_all$target | is.na(lsl_all$prev_stim))
  # Change their type 
),]$type<-"false_alarm"


# Find all the correct rejections
lsl_all[which(
  # The participant did not press
  is.na(lsl_all$col1)
  # It was not during a target
  & lsl_all$stim_disp!=lsl_all$target
  # It was not directly before a target
  & (lsl_all$next_stim!=lsl_all$target | is.na(lsl_all$next_stim))
  # It was not directly after a target
  & (lsl_all$prev_stim!=lsl_all$target | is.na(lsl_all$prev_stim))
  # Change their type 
),]$type<-"corr_rej"


# Initialize variables for RT calculations
mean_rt <- list()
loop_index = 0
current_id <- list()
rt_slope <- list()
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

#Calculate mean RT, D Prime--------------------------------------------------------------------------
# Extract the mean response time and rt slope for each participant
for(id in (all_ids)) {
  loop_index = loop_index + 1
  #Record id
  current_id[[loop_index]] <- id
  #extract id's data
  this_id <- lsl_all[which(lsl_all$par_id == id), ]
  #Mean RT
  mean_rt[[loop_index]] <-
    round(mean(exp_targets$reaction_time[exp_targets$id == id], na.rm = TRUE), digits = 3)
  # Find this participant's number of hits, misses, correct rejections, and false alarms
  this_hit <-
    length(this_id[which((
      this_id$type == "hit_before" |
        this_id$type == "hit_during" |
        this_id$type == "hit_after"
    ) & this_id$par_id == id
    ), 1])
  
  #Calculate RT Slope-----------------------------------------------------------------------------------------------------
  # If there are enough hits to find RT slope, calculate it
  if (this_hit > 1) {
    #extract each id's individual rt by trial
    rt_by_trial <- exp_targets[which(exp_targets$id == id), "reaction_time"]
    #scale the rt based on mean and sd
    scaled_rt_by_id <- scale(rt_by_trial)
    #save the scaled rt to a new column
    exp_targets[which(exp_targets$id == id), "scaled_rt"]<- scaled_rt_by_id
    
    rt_slope[[loop_index]] <-
      round(summary(
        lm(exp_targets$scaled_rt[exp_targets$id == id] ~ exp_targets$targ_index[exp_targets$id == id])
      )$coefficient[2, 1], digits = 3)
  } else {
    # Otherwise, record that there are too few hits
    rt_slope[[loop_index]] <- "too few hits"
  }
  #Calculate miss, false alarm, correct rejection----------------------------------------------------------------------
  this_miss <-
    length(this_id[which((this_id$type == "miss") &
                           this_id$par_id == id), 1])
  this_corr_rej <-
    length(this_id[which((this_id$type == "corr_rej") &
                           this_id$par_id == id), 1])
  this_false_alarm <-
    length(this_id[which((this_id$type == "false_alarm") &
                           this_id$par_id == id), 1])
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

all_ids <- do.call(rbind, current_id)
colnames(all_ids) <- "all_ids"
mean_rt <- do.call(rbind, mean_rt)
colnames(mean_rt) <- "mean_rt"
scaled_rt_slope <- do.call(rbind, rt_slope)
colnames(scaled_rt_slope) <- "scaled_rt_slope"

#----------------------------------------------------------------------------------------------------------------------

indiv_rts <- cbind(all_ids, mean_rt, scaled_rt_slope, d_prime, this_targets, hits, hit_rate, misses, miss_rate, corr_rej, corr_rej_rate, false_alarms, false_alarm_rate, distractors, total_disc, resp_acc, total_stimuli)


# Remove any extra columns that are only helpful for internal checks
# Tidy up column names
colnames(indiv_rts)[colnames(indiv_rts)=="all_ids"] <- "par_id"

# Write RT, RT slope results and save them to NAS
# NOTE: This is for children files
write.csv(indiv_rts, paste0(output_path, "blast_online_children_lsl_indiv_rts.csv"))


