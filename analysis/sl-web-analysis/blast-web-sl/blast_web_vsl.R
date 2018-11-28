#  BLAST VSL Analysis
#  Violet Kozloff
#  September 10th, 2018 
#  Adapted from mturk_vsl by An Nguyen
#  This script analyses reaction time for VSL files from the online session of the BLAST experiment
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
vsl <- read.csv("../../../../blast_adult_web_sl_data/clean/vsl_clean/vsl.csv")

#analysis on RT
# Numbers might change file to file. May have an extra blank stimulus before it.
# TO DO: Check that these chunks are generally correct
fam_block <- vsl[which(vsl$trial_index<=300 & vsl$trial_index>=13),]
fam_block <- fam_block[!(fam_block$stimulus=="../../vsl_audio/sound_instruct/vsl_instr7.wav"),]
fam_block$targ <- paste(fam_block$targ)
fam_block$stimulus <- paste(fam_block$stimulus)

rt_col <- NULL
id <- NULL
trial <- NULL
target <- NULL

#Extract the row number in which the stimulus is the target
row_number <- which(fam_block$targ==fam_block$stimulus)

#Extract the response time and trial number when stimulus is the target
for (i in row_number){
  rt_col <- append(rt_col,fam_block[i,][,"rt"])
  trial <- append(trial,fam_block[i,][,"trial_index"])
  id <- append(id,paste(fam_block[i,]$part_id))
  if (fam_block[i-1,][,"rt"]!=-1){
    rt_col[(match(i,row_number))] <- -(1000-fam_block[i-1,][,"rt"])
    
  }}

fam_trial <- data.frame(unlist(trial),unlist(rt_col),id)
colnames(fam_trial) <- c("trial","rt_col","id")

#Re-index the trial number of the response so that it ranges from 1-24 (because there are 24 stimuli in total)
reindex <- rep(1:total_vsl_trial,length(fam_trial$trial)/24)
fam_trial$reindex <- reindex

hit_rate <- NULL
miss_rate <- NULL
correct_rejection <- NULL
false_alarm <- NULL
mean_rt <- NULL
rt_slope <- NULL
timeline <- c(rep("first half",total_vsl_trial/2),rep("second half",total_vsl_trial/2))
timeline <- rep(timeline,length(fam_trial$trial)/24)
fam_trial$timeline <- timeline
mean_table <- fam_trial[which(fam_trial$rt_col!=-1 & fam_trial$rt_col<1000 & fam_trial$rt_col>-1000), ] #only accept answers in range of -1000 < x < 1000

# TO DO: Fix this
# exclude people who only have one rt point, so rtslope cannot be computed
# mean_table <- mean_table[mean_table$id!="mtslAG1213",]

#vsl2
#mean_table <- mean_table[mean_table$id!="A1FDP7EMSL9T9F",]
#mean_table <- mean_table[mean_table$id!="mtslen0591",]
#mean_table <- mean_table[mean_table$id!="mtslmd1085",]

list_vsl_id <- unique(mean_table$id)

#Extract the mean response time, rt slope, hit rate, miss rat, correct rejection, and false alarm for each participant
for(id in list_vsl_id){
  mean_rt<-append(mean_rt,round(mean(mean_table$rt_col[mean_table$id==id]),digits=3))
  rt_slope <-append(rt_slope,round(summary(lm(mean_table$rt_col[mean_table$id==id]~mean_table$reindex[mean_table$id==id]))$coefficient[2,1],digits=3))
  hit_rate<-append(hit_rate,round(sum(!is.na(mean_table$rt_col[mean_table$id==id]))/total_vsl_trial,digits =2))
  miss_rate<-append(miss_rate,round(sum(fam_trial$rt_col[fam_trial$id==id]==-1)/total_vsl_trial,digits=2))
  correct_rejection <- append(correct_rejection, round(sum(fam_block$rt[fam_block$par_id==id]==-1 & fam_block$targ[fam_block$par_id==id]!=fam_block$stimulus[fam_block$par_id==id])/264,digits=2)) #264 is the total number of stimuli in the familiarization block
  false_alarm <- append(false_alarm, round(sum(fam_block$rt[fam_block$par_id==id]!=-1 & fam_block$targ[fam_block$par_id==id]!=fam_block$stimulus[fam_block$par_id==id])/264,digits=2))
}

subj_table <- data.frame(list_vsl_id,mean_rt, rt_slope,hit_rate, miss_rate,correct_rejection,false_alarm)
#dprime<-NULL
#for (i in seq(from=1,to=length(subj_table$list_vsl_id),by=1)){dprime<-append(dprime,qnorm(subj_table[i,]$hit_rate-0.00000001)-qnorm(subj_table[i,]$false_alarm+0.000000001))} #minus 0.000000001 to avoid perfect hit rate
#subj_table$dprime <- round(dprime,3)

# TO DO: What is this?
#lowerbound <- mean(subj_table$rt_slope) - 2.5*sd(subj_table$rt_slope)
#upperbound <- mean(subj_table$rt_slope) + 2.5*sd(subj_table$rt_slope)
#subj_table <- subj_table[subj_table$rt_slope>=lowerbound,]
#subj_table <- subj_table[subj_table$rt_slope<=upperbound,]

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
cond<- NULL

#Extract rows in which the participant gives a response
row_numberv <- which(test_block$key_press != -1 & test_block$stimulus == "")
for (i in row_numberv){
  ans<-append(ans,test_block[i,]$key_press)
  subj <- append(subj,paste(test_block[i,]$part_id))
  cond <- append(cond,paste(test_block[i,]$cond))
}

# Create a data frame that contains the participants' responses
vsl_accuracy <- data.frame(ans,subj,cond)
vsl_accuracy <- vsl_accuracy[!(vsl_accuracy$ans==32),]

keyv<- NULL

i=0

keyv <- rep(language, times = length(unique(vsl_accuracy$subj)))

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(vsl_accuracy$subj)


# TO DO: Stops working here
vsl_accuracy$key <- keyv

#Substitute the key press (49,50) with the answer (1,2)
vsl_accuracy$ans <- gsub(50,2,vsl_accuracy$ans)
vsl_accuracy$ans <- gsub(49,1,vsl_accuracy$ans)

#Loop through and count the correct answer
corr <- NULL
for (i in seq(from=1,to=length(vsl_accuracy$ans),by=1)) {corr<-append(corr,as.numeric(vsl_accuracy[i,]$ans==vsl_accuracy[i,]$key))}
vsl_accuracy$corr <- corr
subj_corr <- NULL
for (id in acc_id) {subj_corr <- append(subj_corr,round(sum(vsl_accuracy$corr[vsl_accuracy$subj==id])/32,digits=3))}
vsl_acc_table <- data.frame(acc_id,subj_corr)

