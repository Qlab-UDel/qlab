#  BLAST vsl Analysis
#  Violet Kozloff
#  Last updated February 27th
#  Adapted from mturk_vsl by An Nguyen
#  This script analyses reaction time for vsl files from the online session of the BLAST experiment
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------

# Set directory
setwd("/Volumes/data/projects/blast/data/online_sl/blast_adult")
# NOTE: Comment out the above line and use this one for children
# setwd("/Volumes/data/projects/blast/data/online_sl/blast_child")
# NOTE: This is the path for SPOLI
# setwd("/Volumes/data-1/projects/spoli/raw_sl_data/")

# Install packages
install.packages("reshape")
library("reshape")
install.packages("DescTools")
library("DescTools")


# Remove objects in environment
rm(list=ls())

# Output path
output_path <- ("/Volumes/data/projects/blast/data_summaries/blast_online_adult/breakdown/")
# output_path <- ("/Volumes/data-1/projects/blast/data_summaries/blast_online_child/")


# Extract data from files ------------------------------------------------------------

# Read in the entropy key
vsl_entropy_key <- read.csv("/Volumes/data/projects/blast/data/online_sl/entropy_keys/vsl_entropy_key.csv")
vsl_entropy_key <- (vsl_entropy_key[c("target_type","target_order","target_occurance_order","alien_target")])

# Ask user for input on how many files are expected (i.e. how many participants are there?)
correct_total_files <- as.integer(readline("How many total participants should there be for this file type? Enter this into the console. If you are not sure, check the qlab_participant_checklist.   "))

# List input files
vsl_files <- list.files(pattern="*vsl.csv")

# Confirm that all files are present. If not, alert user
if(length(vsl_files)!=correct_total_files){
  stop(print(paste("Found", length(vsl_files), "files. You indicated that there are", correct_total_files, "participants. Please check files in folder against the qlab_participant_checklist.")))
}


# Initialize variable to hold data
vsl <- NULL

# Extract relevant data and combine it
for (file in vsl_files){
  # Select only relevant columns
  extracted_data <- read.csv(file)[c("rt", "trial_index", "targ","key_press", "stimulus")]  
  # Create a column populated with the participant ID based on the file name
  extracted_data["part_id"] <- substr(basename(file), 1, 11)
  # Change target and stimulus to string
  extracted_data["targ"] <- as.character(extracted_data$targ)
  extracted_data["stimulus"] <- as.character(extracted_data$stimulus)
  # The keypress value recorded as "rt" in the raw files is not the vsltime. Rename the column. See below for details on how to use this value.
  colnames(extracted_data)[colnames(extracted_data)=="rt"] <- "press_time"
  # Standardize stimulus names and types
  extracted_data$stimulus<- tolower(gsub(".jpg","", extracted_data$stimulus))
  extracted_data$stimulus<- tolower(gsub(".png","", extracted_data$stimulus))
  extracted_data$stimulus<- gsub("../../images/","",extracted_data$stimulus)
  extracted_data$press_time<-as.numeric(extracted_data$press_time)
  # Identify blank keypresses
  extracted_data[which(extracted_data$press_time==-1),]$press_time<-NA
  # Identify preceding and following stimuli
  extracted_data$prev_stim <- append(NA, (head(extracted_data$stimulus, -1)))
  extracted_data$next_stim <- append(extracted_data$stimulus[-1], NA)
  vsl<-rbind(vsl,extracted_data)
}

# List all the participants
all_ids<- unique(vsl$part_id)


# Calculate and summarize true reaction times ------------------------------------------------------------

# Set boundaries for the exposure phase. These correspond to the first and last trial numbers
# NOTE: Due to some variation between files, include the lowest and highest trial numbers across all files
exp_phase_start <-12
exp_phase_end <-298

# Extract exposure phase
exp_phase <- vsl[which(vsl$trial_index<=exp_phase_end & vsl$trial_index>=exp_phase_start),]

# Internal check: Make sure that there are 286 stimuli per participant
# NOTE: Unlike vsl and vsl, which have 576, these ones have 286
# Initialize variables
total_stimuli <- NULL
# Find the number of stimuli for each participant
for(check_id in unique(exp_phase$part_id)){
  total_stimuli <- append(total_stimuli, length(which(exp_phase$part_id==check_id)))}
stimulus_check <- (cbind(all_ids, total_stimuli))

# Identify participants with too few/many targets and alert user if present
if(! all(unique (total_stimuli) == "286")){
  # Create error message alerting user
  print(" The following participant(s) has an incorrect number of extracted trials:")
  # List the participants with the wrong number of targets
  print(paste("", stimulus_check[which(total_stimuli!="286")]))
  print(" Please check the number of targets in the following input files.")
  print(" If the participant saw too few or too many stimuli, exclude them from analysis and alert the lab member maintaining bluehost.")
  print(" If the wrong number of stimuli was extracted, adjust the values of exp_phase_start and exp_phase_end.")
  # Open a new window showing the user the number of targets for each participant
  View(stimulus_check)
  stop()}

# # Extract the row numbers for all lines in which the stimulus is the target
# targets <- which(exp_phase$targ==exp_phase$stimulus)
# 
# # Set the number of targets expected per participant
# correct_total_targets <- 24
# 
# # Internal check: Make sure that there are the right number of targets per participant
# # Initialize variables
# target_rows <-(exp_phase[targets,])
# total_targets <- NULL
# # Find the number of targets for each participant
# for(check_id in unique(exp_phase$part_id)){
#   total_targets <- append(total_targets, length(which(target_rows$part_id==check_id)))}
# target_check <- (cbind(all_ids, total_targets))
# 
# # Identify participants with too few/many targets and alert user if present
# if(! all(unique (total_targets) == correct_total_targets)){
#   # Create error message alerting user
#   print(" The following participant(s) has an incorrect number of extracted targets:")
#   # List the participants with the wrong number of targets
#   print(paste("", target_check[which(total_targets!=correct_total_targets)]))
#   print(" Please check the number of targets in the following input files.")
#   print(" If the participant saw too few or too many targets, exclude them from analysis and alert the lab member maintaining bluehost.")
#   print(" If the wrong number of targets was extracted, adjust exp_phase_start + exp_phase_end.")
#   # Open a new window showing the user the number of targets for each participant
#   View(target_check)
#   stop()}
# 
# 
# # Extract the response time and trial number when stimulus is the target------------------
# 
# # A valid response time comes from:
# #   - A keypress during the 1000 ms prior to the target stimulus presentation (anticipation)
# #   - A keypress during the 1000 ms after the target stimulus is presented (on-target)
# 
# # TO DO: For visual, make sure it's only during the preceding trial or the target
# 
# # Variables to extract
# id <- NULL
# trial <- NULL
# reaction_time <- NULL
# exp_phase$type <- NA
# 
# # # Note: these variables aren't necessary, but they are useful for understanding and troubleshooting RT calculations for each case
# # target <- NULL
# # this_preceding_trial_press <-NULL
# # preceding_trial_press <-NULL
# # this_target_trial_press <-NULL
# # target_trial_press <-NULL
# # type <- NULL
# 
# # Calculate true reaction times
# for (i in targets){
#   
#   # Isolate variables used for calculations
#   # Current trial
#   this_trial <- exp_phase[i,][,"trial_index"]
#   # List of all  targets' trials
#   trial <- append(trial, this_trial)
#   # Current id
#   id <- append(id,exp_phase[i,]$part_id)
#   # Keypress time recorded from preceding trial
#   {if(this_trial>exp_phase_start) {
#     this_preceding_trial_press <- exp_phase[i-1,][,"press_time"]}
#     else {
#       this_preceding_trial_press <- NA}}
#   
#   # Press time recorded for current target
#   this_target_trial_press <- exp_phase[i,][,"press_time"]
#   
#   # NOTE: Uncomment this section for troubleshooting the number of targets/ RTs
#   
#   # # List of all target stimuli
#   # target <- append(target, as.character(exp_phase[i,]$targ))
#   # # List of keypress time for trials preceding all targets
#   # preceding_trial_press <- append (preceding_trial_press, this_preceding_trial_press)
#   # # List of press times for all targets
#   # target_trial_press <- append(target_trial_press, this_target_trial_press)
# 
#   # Anticipation, positive RT from preceding trial 
#   if (!is.na(exp_phase[i-1,]$press_time > 0) & (exp_phase[i-1,]$press_time > 0)){
#     reaction_time <- append(reaction_time, (this_preceding_trial_press-480))
#     exp_phase[i,]$type <- "hit_before"
#     # type <- rbind(type, "hit_before")
#   }
#   
#   # On-target, positive RT from target trial
#   else if (!is.na(exp_phase[i,]$press_time > 0) & exp_phase[i,]$press_time > 0){
#     reaction_time <- append(reaction_time, (exp_phase[i,][,"press_time"]))
#     exp_phase[i,]$type <- "hit_during"
#     # type <- rbind(type, "hit_during")
#   }
#   
#   # Misses
#   else {
#     reaction_time <- append(reaction_time, NA)
#     exp_phase[i,]$type <- "miss"
#     # type <- rbind(type, "miss")
#   }
# }
# 
# # exp_targets now contains all targets from the exposure phase and their true RTs (includes any response within 480 ms of a target)
# exp_targets <- data.frame(trial,reaction_time,id)
# 
# # # NOTE: If you are missing RTs or they seem inaccurate, uncomment all variables above, as well as the following section, to help troubleshoot
# # # This one shows you all of the lines with targets
# #  exp_targets_check1 <- exp_phase[which(exp_phase$targ==exp_phase$stimulus),]
# # # This shows the details of lines with targets
# #  exp_targets_check2 <- data.frame(id, trial,reaction_time, type, preceding_trial_press, target_trial_press)
# 
# 
# # Find the number of RTs for each participant
# 
# # Initialize variables
# total_rts <- NULL
# 
# # Check RTs
# for(check_id in all_ids){
#   total_rts <- append(total_rts, length(which(exp_targets$id==check_id)))}
# rt_check <- (cbind(all_ids, total_rts))
# # Idenitify participants with too few/many RTs and alert user if present
# if(! all(unique (total_rts) == correct_total_targets)){
#   # Create error message alerting user
#   print(" The following participant(s) has an incorrect number of reaction times:")
#   # List the participants with the wrong number of RTs
#   print(paste("", rt_check[which(total_rts!=correct_total_targets)]))
#   print(" Please check the reaction time calculations as indicated in line 260 before continuing.")
#   # Open a new window showing the user the number of RTs for each participant
#   View(rt_check)
#   stop()}
# 
# # Reindex the targets from 1 to the expected number of targets for each participant
# targ_index <- rep(1:correct_total_targets,length(exp_targets$trial)/correct_total_targets)
# exp_targets$targ_index <- targ_index
# 
# # Find reaction time slopes and mean reaction times and write them to NAS ------------------------------------
# 
# # Internal check: make sure that all RTs are valid, ie. fall within 1 SOA of the stimulus
# check_rts_1 <- exp_targets[which(exp_targets$reaction_time!=-1 & exp_targets$reaction_time>1000),]
# check_rts_2 <- exp_targets[which(exp_targets$reaction_time< -1000),]
# 
# # Alert the user of invalid RTs
# if(length(check_rts_1[,1]) | length(check_rts_2[,1]) !=0){
#   # Create error message alerting user
#   print("One or more participants has an invalid reaction time. Please check the reaction time calculations.")
#   # Open a new window showing the user the RTs for each participant
#   View(exp_targets)
#   stop()}
# 
# # Find all the false alarms
# exp_phase[which(
#   # The participant pressed
#   !is.na(exp_phase$press_time)
#   # It was not during a target
#   & exp_phase$stimulus!=exp_phase$targ
#   # It was not directly before a target
#   & exp_phase$next_stim!=exp_phase$targ
#   # Change their type 
# ),]$type<-"false_alarm"
# 
# # Find all the correct rejections
# exp_phase[which(
#   # The participant did not press
#   is.na(exp_phase$press_time)
#   # It was not during a target
#   & exp_phase$stimulus!=exp_phase$targ
#   # It was not directly before a target
#   & exp_phase$next_stim!=exp_phase$targ
#   # Change their type 
# ),]$type<-"corr_rej"
# 
# # -----------------------------------
# 
# 
# 
# #analysis on RT
# # Numbers might change file to file. May have an extra blank stimulus before it.
# # TO DO: Check that these chunks are generally correct
# fam_block <- vsl[which(vsl$trial_index<=300 & vsl$trial_index>=13),]
# fam_block <- fam_block[!(fam_block$stimulus=="../../vsl_audio/sound_instruct/vsl_instr7.wav"),]
# fam_block$targ <- paste(fam_block$targ)
# fam_block$stimulus <- paste(fam_block$stimulus)
# 
# rt_col <- NULL
# id <- NULL
# trial <- NULL
# target <- NULL
# 
# #Extract the row number in which the stimulus is the target
# row_number <- which(fam_block$targ==fam_block$stimulus)
# 
# #Extract the response time and trial number when stimulus is the target
# for (i in row_number){
#   rt_col <- append(rt_col,fam_block[i,][,"rt"])
#   trial <- append(trial,fam_block[i,][,"trial_index"])
#   id <- append(id,paste(fam_block[i,]$part_id))
#   if (fam_block[i-1,][,"rt"]!=-1){
#     rt_col[(match(i,row_number))] <- -(1000-fam_block[i-1,][,"rt"])
#     
#   }}
# 
# fam_trial <- data.frame(unlist(trial),unlist(rt_col),id)
# colnames(fam_trial) <- c("trial","rt_col","id")
# 
# #Re-index the trial number of the response so that it ranges from 1-24 (because there are 24 stimuli in total)
# reindex <- rep(1:total_vsl_trial,length(fam_trial$trial)/24)
# fam_trial$reindex <- reindex
# 
# hit_rate <- NULL
# miss_rate <- NULL
# correct_rejection <- NULL
# false_alarm <- NULL
# mean_rt <- NULL
# rt_slope <- NULL
# timeline <- c(rep("first half",total_vsl_trial/2),rep("second half",total_vsl_trial/2))
# timeline <- rep(timeline,length(fam_trial$trial)/24)
# fam_trial$timeline <- timeline
# mean_table <- fam_trial[which(fam_trial$rt_col!=-1 & fam_trial$rt_col<1000 & fam_trial$rt_col>-1000), ] #only accept answers in range of -1000 < x < 1000
# 
# # TO DO: Fix this
# # exclude people who only have one rt point, so rvslope cannot be computed
# # mean_table <- mean_table[mean_table$id!="mvslAG1213",]
# 
# #vsl2
# #mean_table <- mean_table[mean_table$id!="A1FDP7EMSL9T9F",]
# #mean_table <- mean_table[mean_table$id!="mvslen0591",]
# #mean_table <- mean_table[mean_table$id!="mvslmd1085",]
# 
# list_vsl_id <- unique(mean_table$id)
# 
# #Extract the mean response time, rt slope, hit rate, miss rat, correct rejection, and false alarm for each participant
# for(id in list_vsl_id){
#   mean_rt<-append(mean_rt,round(mean(mean_table$rt_col[mean_table$id==id]),digits=3))
#   rt_slope <-append(rt_slope,round(summary(lm(mean_table$rt_col[mean_table$id==id]~mean_table$reindex[mean_table$id==id]))$coefficient[2,1],digits=3))
#   hit_rate<-append(hit_rate,round(sum(!is.na(mean_table$rt_col[mean_table$id==id]))/total_vsl_trial,digits =2))
#   miss_rate<-append(miss_rate,round(sum(fam_trial$rt_col[fam_trial$id==id]==-1)/total_vsl_trial,digits=2))
#   correct_rejection <- append(correct_rejection, round(sum(fam_block$rt[fam_block$par_id==id]==-1 & fam_block$targ[fam_block$par_id==id]!=fam_block$stimulus[fam_block$par_id==id])/264,digits=2)) #264 is the total number of stimuli in the familiarization block
#   false_alarm <- append(false_alarm, round(sum(fam_block$rt[fam_block$par_id==id]!=-1 & fam_block$targ[fam_block$par_id==id]!=fam_block$stimulus[fam_block$par_id==id])/264,digits=2))
# }
# 
# subj_table <- data.frame(list_vsl_id,mean_rt, rt_slope,hit_rate, miss_rate,correct_rejection,false_alarm)
# #dprime<-NULL
# #for (i in seq(from=1,to=length(subj_table$list_vsl_id),by=1)){dprime<-append(dprime,qnorm(subj_table[i,]$hit_rate-0.00000001)-qnorm(subj_table[i,]$false_alarm+0.000000001))} #minus 0.000000001 to avoid perfect hit rate
# #subj_table$dprime <- round(dprime,3)
# 
# # TO DO: What is this?
# #lowerbound <- mean(subj_table$rt_slope) - 2.5*sd(subj_table$rt_slope)
# #upperbound <- mean(subj_table$rt_slope) + 2.5*sd(subj_table$rt_slope)
# #subj_table <- subj_table[subj_table$rt_slope>=lowerbound,]
# #subj_table <- subj_table[subj_table$rt_slope<=upperbound,]




# Calculate and summarize individual accuracies ------------------------------------------------------------

#Extract the testing phase
#test block
# TO DO: Check that these are the right lines
vsl$targ <- paste(vsl$targ)
vsl$stimulus <- paste(vsl$stimulus)
test_block <- vsl[which(vsl$stimulus==""),]
test_block <- test_block[which((test_block$key_press==49)|(test_block$key_press==50)),]

#Internal check: this should be exactly 32 (32 forced choices per participant)
# View(length(test_block$targ)/length(unique(test_block$part_id)))
ans <- NULL
keyv <- NULL
subj <- NULL

#Extract rows in which the participant gives a response
row_numberv <- which(test_block$key_press != -1 & test_block$stimulus == "")
for (i in row_numberv){
  ans<-append(ans,test_block[i,]$key_press)
  subj <- append(subj,paste(test_block[i,]$part_id))
}

# Create a data frame that contains the participants' responses
vsl_accuracy <- data.frame(ans,subj)
vsl_accuracy <- vsl_accuracy[!(vsl_accuracy$ans==32),]

keyv<- NULL

i=0

language = list(1,1,2,1,1,1,2,2,2,2,1,1,1,2,2,1,2,2,1,1,2,1,2,1,2,1,2,1,1,2,2,2)
keyv <- rep(language, times = length(unique(vsl_accuracy$subj)))

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(vsl_accuracy$subj)

vsl_accuracy$key <- keyv

#Substitute the key press (49,50) with the answer (1,2)
vsl_accuracy$ans <- gsub(50,2,vsl_accuracy$ans)
vsl_accuracy$ans <- gsub(49,1,vsl_accuracy$ans)

#Loop through and count the correct answer
corr <- NULL
for (i in seq(from=1,to=length(vsl_accuracy$ans),by=1)) {corr<-append(corr,as.numeric(vsl_accuracy[i,]$ans==vsl_accuracy[i,]$key))}
vsl_accuracy$corr <- corr



# Entropy

# Find the triplet type (each triplet gets coded with a value from A-D)
triplet_type <- rep(vsl_entropy_key$target_type, times = length(unique(vsl_accuracy$subj)))
# Find the order for the triplet (the triplet either appeared first or second, with respect to the foil)
triplet_order <- rep(vsl_entropy_key$target_order, times = length(unique(vsl_accuracy$subj)))
# Find the occurance for the triplet (each triplet occurs between 7 and 9 times. Number each occurance.)
triplet_occurance <- rep(vsl_entropy_key$target_occurance_order, times = length(unique(vsl_accuracy$subj)))
# Find the image triplet (which three images make up the triplet)
image_triplet <- rep(vsl_entropy_key$alien_target, times = length(unique(vsl_accuracy$subj)))

vsl_accuracy$triplet_type <- triplet_type
vsl_accuracy$triplet_order <- triplet_order
vsl_accuracy$triplet_occurance <- triplet_occurance
vsl_accuracy$image_triplet <- image_triplet


# Entropy
vsl_entropy_wide<- cast(vsl_accuracy, subj~corr+triplet_type, value = "image_triplet", fun.aggregate = length)


#Caculate Entropy for each target type by group and by task
vsl_entropy_by_triplet <- data.frame()

# vsl Entropy for each target type
for (i in 1:nrow(vsl_entropy_wide)) {
  vsl_entropy_by_triplet[i,"vsl_a_entropy"] <- Entropy(vsl_entropy_wide[i,c("0_A","1_A")])
}

for (i in 1:nrow(vsl_entropy_wide)) {
  vsl_entropy_by_triplet[i,"vsl_b_entropy"] <- Entropy(vsl_entropy_wide[i,c("0_B","1_B")])
}

for (i in 1:nrow(vsl_entropy_wide)) {
  vsl_entropy_by_triplet[i,"vsl_c_entropy"] <- Entropy(vsl_entropy_wide[i,c("0_C","1_C")])
}

for (i in 1:nrow(vsl_entropy_wide)) {
  vsl_entropy_by_triplet[i,"vsl_d_entropy"] <- Entropy(vsl_entropy_wide[i,c("0_D","1_D")])
}

for (i in 1:nrow(vsl_entropy_wide)) {
  vsl_entropy_by_triplet[i,"part_id"] <- vsl_entropy_wide[i,c("subj")]
}

vsl_entropy_by_triplet$mean_entropy <- round(rowMeans(vsl_entropy_by_triplet[,1:4], na.rm = FALSE, dims = 1), 3)

write.csv(vsl_entropy_by_triplet[,5:6], paste0(output_path, "online_vsl_entropy_adults.csv"))


# Count how many answers were correct for each participant
subj_corr <- NULL
for (id in acc_id) {subj_corr <- append(subj_corr,round(sum(vsl_accuracy$corr[vsl_accuracy$subj==id])/32,digits=3))}
vsl_acc_table <- data.frame(acc_id,subj_corr)

write.csv(vsl_acc_table, "/Volumes/data/projects/blast/data_summaries/blast_online_child/breakdown/online_vsl_accuracies.csv")
#write.csv(vsl_acc_table, "/Volumes/data/projects/blast/data_summaries/blast_online_adult/breakdown/online_vsl_accuracies.csv")

