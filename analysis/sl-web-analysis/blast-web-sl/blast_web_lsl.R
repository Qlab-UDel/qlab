#  BLAST LSL Analysis
#  Violet Kozloff
#  September 10th, 2018 
#  Adapted from mturk_lsl by An Nguyen
#  This script analyses reaction time for lsl files from the online session of the BLAST experiment
#  TO DO: Double check each step of the way that everything is still relevant...
#  TO DO: Set up checks for # of rows
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------

# Set directory
setwd("/Users/vkozloff/Documents/qlab/analysis/sl-web-analysis/blast-web-sl")
# Remove objects in environment
rm(list=ls())


#importing files
# TO DO: Check this key for LSL against An's mturk one
language = list(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)

# LSL Accuracy -------------------------------------------

#Extract the testing phase
test_block <- read.csv("/Users/vkozloff/Documents/blast_adult_web_sl_data/clean/lsl_acc_clean/lsl_acc.csv")

# TO DO: Check on this
test_block <- test_block[!(test_block$stimulus=="" & test_block$key_press==-1),]
test_block <- test_block[(test_block$stimulus=="white" & !test_block$key_press==-1),]


#Internal check: this should be exactly 32 (32 forced choices per participant)
# View(length(test_block$targ)/length(unique(test_block$part_id)))

ans <- NULL
keyv <- NULL
subj <- NULL

#Extract rows in which the participant gives a response
row_numberv <- which(test_block$key_press != -1 & test_block$stimulus == "white")
for (i in row_numberv){
  ans<-append(ans,test_block[i,]$key_press)
  subj <- append(subj,paste(test_block[i,]$part_id))
}

# Create a data frame that contains the participants' responses
lsl_accuracy <- data.frame(ans,subj)
lsl_accuracy <- lsl_accuracy[!(lsl_accuracy$ans==32),]

keyv<- NULL

i=0

# Combine the answer keys for the two language conditions that the participant saw
keyv <- rep(language, times = length(unique(lsl_accuracy$subj)))

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(lsl_accuracy$subj)

lsl_accuracy$key <- keyv

#Substitute the key press (49,50) with the answer (1,2)
lsl_accuracy$ans <- gsub(50,2,lsl_accuracy$ans)
lsl_accuracy$ans <- gsub(49,1,lsl_accuracy$ans)

#Loop through and count the correct answer
corr <- NULL
for (i in seq(from=1,to=length(lsl_accuracy$ans),by=1)) {corr<-append(corr,as.numeric(lsl_accuracy[i,]$ans==lsl_accuracy[i,]$key))}
lsl_accuracy$corr <- corr
subj_corr <- NULL
for (id in acc_id) {subj_corr <- append(subj_corr,round(sum(lsl_accuracy$corr[lsl_accuracy$subj==id])/32,digits=3))}
lsl_acc_table <- data.frame(acc_id,subj_corr)



# RT Slope Analysis ----------------------------------------------

lsl <- read.csv("/Users/vkozloff/Documents/blast_adult_web_sl_data/clean/lsl_clean/lsl.csv")

lsl$stim_disp<- gsub("image/","",lsl$stim_disp)
lsl$stim_disp<- gsub(".png","",lsl$stim_disp)
lsl$stim_disp<- tolower(lsl$stim_disp)


# Find the rows when the participant responded to the target
row_number <- which(lsl$targ==lsl$stim_disp)

rt_col <- NULL
id <- NULL
trial <- NULL
for (i in row_number){
  rt_col <- append(rt_col,lsl[i,][,"time"])
  trial <- append(trial,lsl[i,][,"X"])
  id <- append(id,paste(lsl[i,]$part_id))
  if (!is.na(lsl[i+1,][,"time"])){
    rt_col[(match(i,row_number))] <- (480+lsl[i+1,][,"time"])
    # TO DO: This was formerly an "if" statement, but I don't get how any reaction could fit into both? 
    # And they're all negative otherwise?
  } 
  if (!is.na(lsl[i-1,][,"time"])){
    rt_col[(match(i,row_number))] <- (0-lsl[i+1,][,"time"])
  }
}


#analysis on RT
# Numbers might change file to file. May have an extra blank stimulus before it.
# TO DO: Check that these chunks are generally correct
fam_trial <- data.frame(unlist(trial),unlist(rt_col),id)
colnames(fam_trial) <- c("trial","rt_col","id")

#Re-index the trial number of the response so that it ranges from 1-24 (because there are 24 stimuli in total)
reindex <- rep(1:24,length(fam_trial$trial)/24)
fam_trial$reindex <- reindex

hit_rate <- NULL
miss_rate <- NULL
correct_rejection <- NULL
false_alarm <- NULL
mean_rt <- NULL
rt_slope <- NULL

# TO DO: Restricting answers in a range of -1000-1000 gives a very low number of responses. 
# Something off about the scale?
#only accept answers in range of -1000 < x < 1000
mean_table <- fam_trial[which(fam_trial$rt_col!=-1),] #& fam_trial$rt_col<1000 & fam_trial$rt_col>-1000), ] 

#TO DO: exclude data that only press 1 (so rt slope cannot be computed)

list_lsl_id <- unique(mean_table$id)
mean_table$part_id<-mean_table$id

#Extract the mean response time, rt slope, hit rate, miss rat, correct rejection, and false alarm for each participant
for(id in list_lsl_id){
  mean_rt<-append(mean_rt,round(mean(mean_table$rt_col[mean_table$part_id==id]),digits=3))
  rt_slope <-append(rt_slope,round(summary(lm(mean_table$rt_col[mean_table$part_id==id]~mean_table$reindex[mean_table$id==id]))$coefficient[2,1],digits=3))
  
  hit_rate<-append(hit_rate,round(sum(!is.na(mean_table$rt_col[mean_table$part_id==id]))/24,digits =2))
  
  miss_rate<-append(miss_rate,round(sum(is.na(fam_trial$rt_col[fam_trial$part_id==id]))/24,digits =2))
  
  correct_rejection <- append(correct_rejection,  round(sum(is.na(lsl$rt[lsl$part_id==id]) & lsl$target[lsl$par_id==id]!=lsl$stim_disp[lsl$par_id==id])/552,digits=2) )  #552 is the total number of stimuli in the familiarization block
  false_alarm <- append(false_alarm, round(sum(!is.na(lsl$rt[lsl$par_id==id]) & lsl$target[lsl$par_id==id]!=lsl$stim_disp[lsl$par_id==id])/552,digits=2) ) }

subj_table <- data.frame(list_lsl_id,mean_rt, rt_slope,hit_rate, miss_rate,correct_rejection,false_alarm)

# TO DO: Deal with all the warnings that come here? Idk why? 
# Something is funky with the rts, which seem to be the presentation times and not response times?