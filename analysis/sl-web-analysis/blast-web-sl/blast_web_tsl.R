#  BLAST TSL Analysis
#  Violet Kozloff
#  September 10th, 2018 
#  Adapted from mturk_tsl by An Nguyen
#  This script analyses reaction time for tsl files from the online session of the BLAST experiment
#  TO DO: Double check each step of the way that everything is still relevant...
#  TO DO: Set up checks for # of rows
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------

# Set directory
setwd("/Users/vkozloff/Documents/qlab/analysis/sl-web-analysis/blast-web-sl")
# Remove objects in environment
rm(list=ls())

language = list(1,1,2,1,1,1,2,2,2,2,1,1,1,2,2,1,2,2,1,1,2,1,2,1,2,1,2,1,1,2,2,2)

#import files
tsl <- read.csv("/Users/vkozloff/Documents/blast_adult_web_sl_data/clean/tsl_clean/tsl.csv")

#analysis on RT
# TO DO: Check this
fam_block <- tsl[which(tsl$trial_index<=598 & tsl$trial_index>=23),]
fam_block <- fam_block[!(fam_block$stimulus=="../../tone_instr/fixation_instr"),]

# Make these two columns comparable
fam_block$targ <- paste(fam_block$targ)
fam_block$stimulus <- paste(fam_block$stimulus)
fam_block$part_id <- paste(fam_block$part_id)

#Extract the row number in which the stimulus is the target
targets <- which(fam_block$targ==fam_block$stimulus)

#Internal check: this should be exactly 48 (48 targets per participant)
# View(length(fam_block[targets,]$rt)/length(unique(fam_block$part_id)))
# Internal check: if the above is not exactly 48, troubleshoot using this script
target_rows <-(fam_block[targets,])
#targets_per_participant <- NULL
# Show how many targets each participant has (should be 48 for each)
#for(test_id in unique(fam_block$part_id)){
 #targets_per_participant <- append(targets_per_participant, length(which(target_rows$part_id==test_id)))}

# Extract the response time and trial number when stimulus is the target------------------

# A valid response time comes from:
# A keypress during the 480 ms prior to the target stimulus presentation (anticipation)
# A keypress during the 480 ms after the target stimulus is presented (on-target)
# A keypress during the 480 ms following the target stimulus presentation (delay)


# Note: Each trial lasts 480 ms long, however the first 100 ms of a trial do not yet present the new stimulus
# There is a 100 second delay between the trial start and the audio stimulus
# Any keypresses during this time are recorded as negative values

# For test purposes, check the rows that fall into each case
# 1: Anticipation after the preceding stimulus has been presented but before the target trial begins
# (positive RT recorded)
case1 <- data.frame()
# 2: Anticipation after the preceding stimulus has been presented and after the target trial begins
# (negative RT recorded)
case2 <- data.frame()
# 3: On-target after the target stimulus has been presented and before the following trial begins
# (positive RT recorded)
case3 <- data.frame()
# 4: On-target after the target stimulus has been presented and after the following trial begins
# (negative RT recorded)
case4 <- data.frame()
# 5: Delay after the following stimulus has been presented and before the next trial begins
# (positive RT recorded)
case5 <- data.frame()
# 6: Delay after the following stimulus has been presented and after the next trial begins
# (negative RT recorded)
case6 <- data.frame()
# 7: Missed targets (no rt recorded)
case7 <- data.frame()

# Variables to extract
rt_col <- NULL
id <- NULL
trial <- NULL
target <- NULL

for (i in targets){
  
  # Case 1 (anticipation, positive RT from preceding trial)
  if (i>1 & fam_block[i-1,]$rt > 0){
    rt_col <- append(rt_col, (fam_block[i-1,][,"rt"]-480))
    case1 <- rbind(case1, fam_block[i-1,])    
    trial <- append(trial,paste(fam_block[i,][,"trial_index"]))
    id <- append(id,paste(fam_block[i-1,]$part_id))
  }
  
  # Case 2 (anticipation, negative RT from target trial)
  else if (i>1 & fam_block[i,]$rt < 0 & !(fam_block[i,]$rt== -1000)){
    rt_col <- append(rt_col, (fam_block[i,][,"rt"]))
    case2 <- rbind(case2, fam_block[i,])    
    trial <- append(trial,paste(fam_block[i,][,"trial_index"]))
    id <- append(id,paste(fam_block[i,]$part_id))
  }
  
  # Case 3 (on-target, positive RT from target trial)
  else if (fam_block[i,]$rt > 0){
    rt_col <- append(rt_col, (fam_block[i,][,"rt"]))
    case3 <- rbind(case3, fam_block[i,])    
    trial <- append(trial,paste(fam_block[i,][,"trial_index"]))
    id <- append(id,paste(fam_block[i,]$part_id))
  }
  
  # Case 4 (on-target, negative RT from following trial)
  else if ((i+1) <= length(fam_block$rt) & fam_block[i+1,]$rt < 0 & (!(fam_block[i+1,]$rt== -1000))){
    rt_col <- append(rt_col, (480+fam_block[i+1,][,"rt"]))
    case4 <- rbind(case4, fam_block[i+1,])    
    trial <- append(trial,paste(fam_block[i,][,"trial_index"]))
    id <- append(id,paste(fam_block[i+1,]$part_id))
  }
  
  # Case 5 (delay, positive RT from following trial)
  else if ((i+1) <= length(fam_block$rt) & fam_block[i+1,]$rt > 0 & (!(fam_block[i+1,]$rt== -1000))){
    rt_col <- append(rt_col, (480+fam_block[i+1,][,"rt"]))
    case5 <- rbind(case5, fam_block[i+1,])    
    trial <- append(trial,paste(fam_block[i,][,"trial_index"]))
    id <- append(id,paste(fam_block[i,]$part_id))
  }
  
  # Case 6 (on-target, negative RT from 2 trials later)
  else if ((!(fam_block[i+2,]$rt== -1000)) & (fam_block[i+2,]$rt < 0) 
           & ((i+2) <= length(fam_block$rt))){
    rt_col <- append(rt_col, (960+fam_block[i+2,][,"rt"]))
    case6 <- rbind(case6, fam_block[i+2,])    
    trial <- append(trial,paste(fam_block[i,][,"trial_index"]))
    id <- append(id,paste(fam_block[i,]$part_id))
  }
  
  # Case 7 (extra case for testing purposes; shows all the missed targets)
  else {
    case7 <- rbind(case7, fam_block[i,])    
  }
}

# fam_trial will now contain rts only from trials with a response to a target
fam_trial <- data.frame(unlist(trial),unlist(rt_col),id)
colnames(fam_trial) <- c("trial","rt_col","id")

# Re-index the trial number of the response so that it reflects the number of responses
hits<-NULL
for (i in (unique(fam_trial$id))){hits<- append(hits,sum(fam_trial$id==i))}
# Internal check: hits should generally be high, otherwise participants aren't really able to track
View(fam_trial[hits,])
reindex <- NULL
for (i in hits) {reindex <- append(reindex,rep(1:i,1))}     
fam_trial$reindex <- reindex

# TO DO: Exclude people who only have zero or one rt point, so rtslope cannot be computed
# Steps should be to match unique(fam_trial$id) with a
# then for any id whose a is <2, remove their data from fam_trial

# Internal check: make sure that all of these values return 0
# TO DO: For visual, only accept answers in range of -1000 < x < 1000
 test_rts_1 <- fam_trial[which(fam_trial$rt_col!=-1 & fam_trial$rt_col>960),]
 test_rts_2 <- fam_trial[which(fam_trial$rt_col== -1),]
 test_rts_3 <- fam_trial[which(fam_trial$rt_col< -480),]

 # TO DO: should check and only include anyone with over 24 hits. This participant only has 1
 fam_trial<-fam_trial[which(fam_trial$id!="blast_c_035"),]
 
 # Extract the mean response time and rt slope for each participant
 mean_rt <- NULL
 rt_slope <- NULL
 list_tsl_id <- unique(fam_trial$id)
 
 for(id in (list_tsl_id)){
   mean_rt<-append(mean_rt,round(mean(fam_trial$rt_col[fam_trial$id==id]),digits=3))
   rt_slope <-append(rt_slope,round(summary(lm(fam_trial$rt_col[fam_trial$id==id]~fam_trial$reindex[fam_trial$id==id]))$coefficient[2,1],digits=3))
 }
 
subj_table <- data.frame(list_tsl_id,mean_rt, rt_slope)

lowerbound <- mean(subj_table$rt_slope) - 2.5*sd(subj_table$rt_slope)
upperbound <- mean(subj_table$rt_slope) + 2.5*sd(subj_table$rt_slope)

# Internal check: whose mean rt is unusually low?
too_low <- subj_table[subj_table$rt_slope<=lowerbound,]
# Internal check: whose data is unusually high?
too_high <- subj_table[subj_table$rt_slope>=upperbound,]

subj_table <- subj_table[subj_table$rt_slope>=lowerbound,]
subj_table <- subj_table[subj_table$rt_slope<=upperbound,]

#Extract the testing phase
#test block
test_block <- tsl[(tsl$stimulus=="silent" & !tsl$key_press==-1),]

#Internal check: this should be exactly 32 (32 forced choices per participant)
View(length(test_block$targ)/length(unique(test_block$part_id)))

ans <- NULL
keyv <- NULL
subj <- NULL
cond<- NULL

#Internal check: this should be exactly 32 (32 forced choices per participant)
forced_choice_rows <- test_block[(test_block$stimulus=="silent" & !test_block$key_press==-1),]
View(length(forced_choice_rows$targ)/length(unique(test_block$part_id)))


#Extract rows in which the participant gives a response
#targetsv is just row number for the test block
targetsv <- which(test_block$key_press != -1 & test_block$stimulus=="silent")
for (i in targetsv){
  ans<-append(ans,test_block[i,]$key_press)
  subj <- append(subj,paste(test_block[i,]$part_id))
}

# Create a data frame that contains the participants' responses
tsl_accuracy <- data.frame(ans,subj)

keyv<- NULL

i=0

# Combine the answer keys for the two language conditions that the participant saw
keyv <- rep(language, times = length(unique(tsl_accuracy$subj)))

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(tsl_accuracy$subj)

tsl_accuracy$key <- keyv

#Substitute the key press (37,39) with the answer (1,2)
tsl_accuracy$ans <- gsub(37,1,tsl_accuracy$ans)
tsl_accuracy$ans <- gsub(39,2,tsl_accuracy$ans)


#Loop through and count the correct answer
corr <- NULL
for (i in seq(from=1,to=length(tsl_accuracy$ans),by=1)) {corr<-append(corr,as.numeric(tsl_accuracy[i,]$ans==tsl_accuracy[i,]$key))}
tsl_accuracy$corr <- corr
subj_corr <- NULL
for (id in acc_id) {subj_corr <- append(subj_corr,round(sum(tsl_accuracy$corr[tsl_accuracy$subj==id])/32,digits=3))}
tsl_acc_table <- data.frame(acc_id,subj_corr)

lowerbound <- mean(tsl_acc_table$subj_corr) - 2.5*sd(tsl_acc_table$subj_corr)
upperbound <- mean(tsl_acc_table$subj_corr) + 2.5*sd(tsl_acc_table$subj_corr)

# Internal check: whose mean rt is unusually low?
too_low <- tsl_acc_table[tsl_acc_table$subj_corr<=lowerbound,]
# Internal check: whose data is unusually high?
too_high <- tsl_acc_table[tsl_acc_table$subj_corr>=upperbound,]

