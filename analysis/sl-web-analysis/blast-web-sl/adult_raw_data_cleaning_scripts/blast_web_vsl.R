#  BLAST vsl Analysis
#  Jojo Hu
#  Last updated Sep 25th, 2019
#  Adapted from mturk_vsl by An Nguyen and blast_web_vsl by Violet Kozloff
#  This script analyses reaction time, accuracy and entropy for vsl files from the online session of the BLAST experiment
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------
# Install packages
install.packages("reshape")
library("reshape")
install.packages("DescTools")
library("DescTools")


# Remove objects in environment
rm(list=ls())

# Set directory
setwd("/Volumes/data/projects/blast/data/online_sl/blast_adult")
#Input path
input_path <- ("/Volumes/data/projects/blast/data/online_sl/blast_adult/")
#Since June 11th 2019, the test phase of all SL tasks have been changed to a balanced design
#New answer keys should be used
input_path2 <- ("/Volumes/data/projects/blast/data/online_sl/blast_adult/counterbalance_2afc_sl_data/")
# Output path
output_path <- ("/Volumes/data/projects/blast/data_summaries/blast_online_adult/breakdown/")



# Extract data from files ------------------------------------------------------------

# Read in the entropy key
vsl_entropy_key <-
  read.csv("/Volumes/data/projects/blast/data/online_sl/entropy_keys/vsl_entropy_key.csv")
vsl_entropy_key <-
  (vsl_entropy_key[c("target_type",
                     "target_order",
                     "target_occurance_order",
                     "alien_target")])

# Read in the entropy key for balanced test phase 
vsl_entropy_key_bal <-
  read.csv("/Volumes/data/projects/blast/data/online_sl/balanced2afc_entropy_keys/vsl_bal_entropy.csv")
vsl_entropy_key_bal <-
  (vsl_entropy_key_bal[c("target_type",
                     "answer_key",
                     "alien_target")])

# Ask user for input on how many files are expected (i.e. how many participants are there?)
#correct_total_files <- as.integer(readline("How many total participants should there be for this file type? Enter this into the console. If you are not sure, check the qlab_participant_checklist.   "))

# List input files
vsl_files <- list.files(pattern="*vsl.csv")

# # Confirm that all files are present. If not, alert user
# if(length(vsl_files)!=correct_total_files){
#   stop(print(paste("Found", length(vsl_files), "files. You indicated that there are", correct_total_files, "participants. Please check files in folder against the qlab_participant_checklist.")))
# }


# Initialize variable to hold data
vsl <- NULL

# Extract relevant data and combine it
for (file in vsl_files){
  # Select only relevant columns
  extracted_data <- read.csv(file)[c("rt", "targ","key_press", "stimulus")]  
  # Create a column populated with the participant ID based on the file name
  extracted_data["part_id"] <- substr(basename(file), 1, 11)
  # Change target and stimulus to string
  extracted_data["targ"] <- as.character(extracted_data$targ)
  extracted_data["stimulus"] <- as.character(extracted_data$stimulus)
  
  #To Do: make it consistent across all tasks
  #Change these to be consistent across lsl and vsl
  colnames(extracted_data)[colnames(extracted_data)=="rt"] <- "press_time"
  colnames(extracted_data)[colnames(extracted_data)=="targ"] <- "target"
  
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
  vsl <-rbind(vsl,extracted_data)
}

# List all the participants
all_ids<- unique(vsl$part_id)


# Calculate and summarize true reaction times ------------------------------------------------------------

# Set boundaries for the exposure phase
library("stringr")

loop_index = 0 
exp_phase <- list()

for (id in all_ids) { 
  loop_index = loop_index +1
  this_id_vsl <- vsl[which(vsl$part_id %in% id),]
  exp_phase_start <- which(str_detect(this_id_vsl$stimulus, "vsl_instr7.wav$")) + 1
  exp_phase_end <- which(str_detect(this_id_vsl$stimulus, "vsl_audio/lsl_instr6.wav$")) - 1
  # blast_a_001 - blast_a_004 used old sitmuli but not blast stimuli
  if (length(which(str_detect(this_id_vsl$stimulus, "vsl_audio/lsl_instr6.wav$"))) == 0) {
    exp_phase_end <- which(str_detect(this_id_vsl$stimulus, "vsl_audio/vsl_instr_between.wav$")) - 1
    print(id)
  }
  exp_phase_this_id <- this_id_vsl[exp_phase_start:exp_phase_end,]
  exp_phase_this_id$trial_index <- NULL
  exp_phase_this_id$trial_index <- seq(from=1, to=length(exp_phase_this_id$part_id), by=1)
  # Extract exposure phase
  exp_phase[[loop_index]] <- exp_phase_this_id
}

exp_phase <- do.call(rbind, exp_phase)

#To Do: check this chunck of script and simplify
# Internal check: Make sure that there are 286 stimuli per participant
# NOTE: Unlike vsl and vsl, which have 576, these ones have 286
# Initialize variables
total_stimuli <- NULL
# Find the number of stimuli for each participant
for(check_id in unique(exp_phase$part_id)){
  total_stimuli <- append(total_stimuli, length(which(exp_phase$part_id==check_id))-2)}
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

#Internal check: Make sure that there are the right number of targets per participant---------------------------
targets = list()

for (i in 1:length(all_ids)) {
  #Extract for the current id, the rows that are matched between displayed stimulus and target
  #This returns TRUE and FALSE values
  current_matched <- 
    exp_phase[which(exp_phase$part_id %in% all_ids[i]), ]$stimulus %in% 
    exp_phase[which(exp_phase$part_id %in% all_ids[i]), ][1, "target"]
  #Extract for the current id, the row numbers that are matched (TRUE in current_matched)
  row_names_orig <-
    row.names(exp_phase[which(exp_phase$part_id %in% all_ids[i]), ][current_matched,])
  targets[[i]] <- row_names_orig
  #To do: Internal check: Make sure that there are the right number of targets per participant
  row <- data.frame(row_names_orig)
  if (nrow(row) != 24) {
    stop()
  }
  
}
#if cbind fails, then some participant does not have 24 targets
check_stimuli_num_for_each_subject = do.call(cbind, targets)
#Append to make a list
#Cbind is crucial to keep the order of trials for each participant
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
vsl$type <- NA
#add in row numbers for the original data to match up with rows in targets
vsl$row <- NULL
vsl$row <- seq(from = 1, to = length(vsl$part_id), by = 1)
# Calculate true reaction times-----------------------------------------------------------
for (i in targets) {
  #i is character after cbinding above, change into numeric as index
  i <- as.numeric(i)
  #Initiate index count
  list_num = list_num + 1
  # Isolate variables used for calculations
  # Current row
  this_trial <- vsl[i,"row"]
  # List of all  targets' trials
  trial[[list_num]] <- this_trial
  # Current id
  id[[list_num]] <- vsl[i,]$part_id
  # Keypress time recorded from preceding trial
  #For visual tasks, the reaction time needs to be calculated from key press time - stimuli onset time
  this_preceding_trial_press <- vsl[i-1, "press_time"]
  
  # Press time recorded for current target
  this_target_trial_press <- vsl[i, "press_time"]
  
  
  # # NOTE: Uncomment this section for troubleshooting the number of targets/ RTs
  # # # Press time recorded for following trial
  #  {if(this_trial<vsl_end){
  #    this_following_trial_press <- vsl[i+1,][,"press_time"]}
  #   else {
  #     this_following_trial_press <- NA}}
  #  # List of all target stimuli
  #  target <- append(target, as.character(vsl[i,]$targ))
  # # # List of keypress time for trials preceding all targets
  #  preceding_trial_press <- append (preceding_trial_press, this_preceding_trial_press)
  #  # List of press times for all targets
  #  target_trial_press <- append(target_trial_press, this_target_trial_press)
  #  # List of press times for trials following all targets
  #  following_trial_press <- append(following_trial_press, this_following_trial_press)
  
  # Anticipation, positive RT from preceding trial: 
  
  if (!is.na(vsl[i-1,]$press_time > 0) & (vsl[i-1,]$press_time > 0)){
    reaction_time <- append(reaction_time, (this_preceding_trial_press-1000))
    vsl[i,]$type <- "hit_before"
    type <- rbind(type, "hit_before")
  }
  
  # On-target, positive RT from target trial)
  else if (!is.na(vsl[i,]$press_time > 0) & vsl[i,]$press_time > 0){
    reaction_time <- append(reaction_time, (this_target_trial_press))
    vsl[i,]$type <- "hit_during"
    type <- rbind(type, "hit_during")
  }
  
  # Delay, positive RT from following trial
  # else if ( !is.na(this_trial< vsl_end & vsl[i+1,]$press_time > 0) & (this_trial< vsl_end & vsl[i+1,]$press_time > 0)){
  else if (!is.na(vsl[i+1,]$press_time > 0) & (vsl[i+1,]$press_time > 0)){
    reaction_time <- append(reaction_time, (1000+(vsl[i+1, "press_time"])))
    vsl[i,]$type <- "hit_after"
    type <- rbind(type, "hit_after")
  }
  
  # Misses
  else {
    reaction_time <- append(reaction_time, NA)
    vsl[i,]$type <- "miss"
    type <- rbind(type, "miss")
  }
}

# exp_targets now contains all targets from the exposure phase and their true RTs (includes any response within 480 ms of a target)
#file that contains reaction time for each trial for each individual
trial = do.call(rbind, trial)
id = do.call(rbind, id)
exp_targets <- data.frame(trial,reaction_time,id)

# Find the number of RTs for each participant

# Initialize variables
total_rts <- NULL
# Check RTs
for(check_id in all_ids){
  total_rts <- append(total_rts, length(which(exp_targets$id==check_id)))}
rt_check <- (cbind(all_ids, total_rts))

# Idenitify participants with too few/many RTs and alert user if present
# NOTE: Depending on the data set, may or may not have participants with only 47 RTs



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

targ_index <- NULL

for (i in total_rts) {
  targ_index <- append(targ_index, rep(1:i))
}
exp_targets$targ_index <- targ_index


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


# Initialize variables for RT calculations
mean_rt <- list()
loop_index = 0
current_id <- list()
rt_slope <- list()
# Initialize variables for response accuracy calculations
hits <- NULL


#Calculate mean RT, D Prime--------------------------------------------------------------------------
#To Do: Add in D Prime, FA, CR, Misses, etc.


# Extract the mean response time and rt slope for each participant
for(id in (all_ids)) {
  loop_index = loop_index + 1
  #Record id
  current_id[[loop_index]] <- id
  #extract id's data
  this_id <- vsl[which(vsl$part_id == id), ]
  #Mean RT
  mean_rt[[loop_index]] <-
    round(mean(exp_targets$reaction_time[exp_targets$id == id], na.rm = TRUE), digits = 3)
  # Find this participant's number of hits, misses, correct rejections, and false alarms
  this_hit <-
    length(this_id[which((
      this_id$type == "hit_before" |
        this_id$type == "hit_during" |
        this_id$type == "hit_after"
    ) & this_id$part_id == id
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
}

all_ids <- do.call(rbind, current_id)
colnames(all_ids) <- "all_ids"
mean_rt <- do.call(rbind, mean_rt)
colnames(mean_rt) <- "mean_rt"
scaled_rt_slope <- do.call(rbind, rt_slope)
colnames(scaled_rt_slope) <- "scaled_rt_slope"

#----------------------------------------------------------------------------------------------------------------------

indiv_rts <- cbind(all_ids, mean_rt, scaled_rt_slope)

# Remove any extra columns that are only helpful for internal checks
# Tidy up column names
colnames(indiv_rts)[colnames(indiv_rts)=="all_ids"] <- "par_id"

# Write RT, RT slope results and save them to NAS

write.csv(indiv_rts, paste0(output_path, "blast_online_adult_vsl_indiv_rts.csv"))
#Save rt by trial data
write.csv(exp_targets, paste0(output_path, "rt_by_trial/blast_vsl_rt_by_trial.csv"))


#End of RT analysis------------------------------------------------------------------------------------------



# Calculate and summarize individual accuracies ------------------------------------------------------------

#List the vsl files after June 11th, 2019 with counterbalanced target-foils in the test phase
#Extract the ids for balanced vsl
vsl_files_balanced <- list.files(path=input_path2, pattern="*vsl.csv")
vsl_bal_id <- str_extract(vsl_files_balanced, "\\S+(?=_vsl.csv)")
#List the files that are not counterbalanced which are collected before June 11th, 2019
vsl_files_unbal <- vsl_files[!(vsl_files %in% vsl_files_balanced)]
vsl_unb_id <- str_extract(vsl_files_unbal, "\\S+(?=_vsl.csv)")



#Extract the data for participants who did unbalanced design
vsl_unb <- vsl[which(vsl$part_id %in% unlist(vsl_unb_id)),]


#Internal check: this should be exactly 32 (32 forced choices per participant)
# TO DO: Make this automatic so it just warns user if participant doesn't have exactly 32



#To Do: figure out what this is doing
#Is there any cases in which there is no response?
vsl_unb$targ <- paste(vsl_unb$target)
vsl_unb$stimulus <- paste(vsl_unb$stimulus)
test_block <- vsl_unb[which(vsl_unb$stimulus==""),]
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
for (i in seq(from = 1,
              to = length(vsl_accuracy$ans),
              by = 1)) {
  corr <-
    append(corr, as.numeric(vsl_accuracy[i, ]$ans == vsl_accuracy[i, ]$key))
}
vsl_accuracy$corr <- corr

#Check stimuli and answer keys in the test phase against the entropy key---------------------------------
#Extract the testing phase--------------------------------------------------------------------------------

test_phase<- list()
loop_index = 0

for (id in vsl_unb_id) {
  loop_index = loop_index +1
  this_id_vsl <- vsl_unb[which(vsl_unb$part_id %in% id),]
  test_phase_start <- which(str_detect(this_id_vsl$stimulus, "vsl_instr14.wav$")) + 1
  test_phase_end <- which(str_detect(this_id_vsl$stimulus, "lsl_instr13.wav$")) - 1
  
  # blast_a_001 = blast_a_004 used old stimuli
  if (length(which(str_detect(this_id_vsl$stimulus, "lsl_instr13.wav$"))) == 0) {
    test_phase_end <- nrow(this_id_vsl) - 1
    print(id)
  }
  
  test_phase_this_id <- this_id_vsl[test_phase_start:test_phase_end,]
  # Extract exposure phase
  test_phase[[loop_index]] <- test_phase_this_id
}

test_phase <- do.call(rbind, test_phase)


#Check whether the answer keys match the answer keys from the entropy keys----------------------------------------------------------- 
#Answer keys in the Entropy keys are always correct
test_phase_stim <- list()
loop_index = 0 
test_phase_id <- unique(vsl_unb$part_id)
trial_index <- seq(from = 1, to = 192,  by = 1)

for (id in test_phase_id) {
  loop_index = loop_index + 1
  #Extract data for current id
  this_id_data <- test_phase[which(test_phase$part_id %in% id),]
  #Extract the rows that have the NA stimuli, vsl test phase starts and ends with NA
  row_white <- which(this_id_data$stimulus == "")
  #Extract the test phase trials for the current participant
  stim_test <- this_id_data[row_white[1]:row_white[length(row_white)], c("part_id", "stimulus")]
  #Remove the NA stimulus
  stim_test <- stim_test[which(stim_test$stimulus != ""),]
  #Add in trial number
  stim_test$trial_index <- trial_index
  #Extract only the stimuli column and split into triplets
  current_id_stim <- stim_test$stimulus
  current_id_stim <- gsub("alien", "", current_id_stim)
  current_id_triplet <- split(current_id_stim, ceiling(seq_along(current_id_stim)/3))
  #Combine the splitted triplets into a column
  current_id_triplet <- do.call(rbind, current_id_triplet)
  #Paste the three individual stimuli in a triplet into a column
  current_id_triplet <- data.frame(current_id_triplet)
  current_id_triplet$triplet <- with(current_id_triplet, paste(X1, X2, X3, sep = "_"))
  #format the triplet column into lower case to match with the entropy file
  current_id_triplet$triplet <- tolower(paste0("alien", current_id_triplet$triplet))
  #Extract triplets in the entropy file and insert an empty row every other row into the entropy key
  #Doing this will allow comparing 64 trials (targets + foils) with 32 trials (from entropy key)
  #First double all rows in vsl_entropy_keys
  doubled_entropy_key <- vsl_entropy_key[rep(1:nrow(vsl_entropy_key),1,each=2),]
  #Then make every other row's target triplet empty
  doubled_entropy_key[c(seq(2, dim(doubled_entropy_key)[1], by=2)), "alien_target"] <- NA
  #Check the triplets of the current id's data against entropy key
  #Every other rowsin doubled_entropy_key shows the target triplet, so if every other row yeilds TRUE, then answer will be 1
  check_every_other_row <- 
    as.numeric(current_id_triplet$triplet %in% doubled_entropy_key$alien_target)
  #Extract every other row and sub 0 with 2
  current_id_key <- check_every_other_row[seq(1, length(check_every_other_row), 2)]
  current_id_key <- gsub(0, 2, current_id_key)
  #Check current id's answer keys against the correct answer keys 
  current_id_correct_key <- sum(as.numeric(current_id_key == vsl_entropy_key$target_order))
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

# Entropy------------------------------------------------------------------------------------------------------------------

# Find the triplet type (each triplet gets coded with a value from A-D)
triplet_type <-
  rep(vsl_entropy_key$target_type, times = length(unique(vsl_accuracy$subj)))
# Find the order for the triplet (the triplet either appeared first or second, with respect to the foil)
triplet_order <-
  rep(vsl_entropy_key$target_order, times = length(unique(vsl_accuracy$subj)))
# Find the occurance for the triplet (each triplet occurs between 7 and 9 times. Number each occurance.)
triplet_occurance <-
  rep(vsl_entropy_key$target_occurance_order, times = length(unique(vsl_accuracy$subj)))
# Find the image triplet (which three images make up the triplet)
image_triplet <-
  rep(vsl_entropy_key$alien_target, times = length(unique(vsl_accuracy$subj)))

vsl_accuracy$triplet_type <- triplet_type
vsl_accuracy$triplet_order <- triplet_order
vsl_accuracy$triplet_occurance <- triplet_occurance
vsl_accuracy$image_triplet <- image_triplet


# Entropy
vsl_entropy_wide <-
  cast(vsl_accuracy,
       subj ~ corr + triplet_type,
       value = "image_triplet",
       fun.aggregate = length)


#Caculate Entropy for each target type by group and by task
vsl_entropy_by_triplet <- data.frame()

# vsl Entropy for each target type
for (i in 1:nrow(vsl_entropy_wide)) {
  vsl_entropy_by_triplet[i, "vsl_a_entropy"] <-
    Entropy(vsl_entropy_wide[i, c("0_A", "1_A")])
  
  vsl_entropy_by_triplet[i, "vsl_b_entropy"] <-
    Entropy(vsl_entropy_wide[i, c("0_B", "1_B")])
  
  vsl_entropy_by_triplet[i, "vsl_c_entropy"] <-
    Entropy(vsl_entropy_wide[i, c("0_C", "1_C")])
  
  vsl_entropy_by_triplet[i, "vsl_d_entropy"] <-
    Entropy(vsl_entropy_wide[i, c("0_D", "1_D")])
  
  vsl_entropy_by_triplet[i, "part_id"] <-
    vsl_entropy_wide[i, c("subj")]
}



vsl_entropy_by_triplet$mean_entropy <- 
  round(rowMeans(vsl_entropy_by_triplet[,1:4], na.rm = FALSE, dims = 1), 3)


# Count how many answers were correct for each participant
subj_corr <- NULL
for (id in acc_id) {
  subj_corr <-
    append(subj_corr, round(sum(vsl_accuracy$corr[vsl_accuracy$subj == id]) /
                              32, digits = 3))
}
vsl_acc_table <- data.frame(acc_id, subj_corr)
#----------------------------------------------------------------------------------------------------------------------------------





#Calculate accuracy and entropy for participants (after June 11th, 2019) who did counterbalanced test phase---------------------------

#Extract the data for participants who did balanced design
vsl_bal <- vsl[which(vsl$part_id %in% unlist(vsl_bal_id)),]

#Internal check: this should be exactly 32 (32 forced choices per participant)
# TO DO: Make this automatic so it just warns user if participant doesn't have exactly 32



#To Do: figure out what this is doing
#Is there any cases in which there is no response?
vsl_bal$targ <- paste(vsl_bal$target)
vsl_bal$stimulus <- paste(vsl_bal$stimulus)
test_block <- vsl_bal[which(vsl_bal$stimulus==""),]
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

language = list(2,2,1,2,1,2,2,1,2,1,2,1,1,2,1,2,1,1,2,1,1,2,2,1,2,2,1,2,1,2,1,1)
keyv <- rep(language, times = length(unique(vsl_accuracy$subj)))

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(vsl_accuracy$subj)

vsl_accuracy$key <- keyv

#Substitute the key press (49,50) with the answer (1,2)
vsl_accuracy$ans <- gsub(50,2,vsl_accuracy$ans)
vsl_accuracy$ans <- gsub(49,1,vsl_accuracy$ans)

#Loop through and count the correct answer
corr <- NULL
for (i in seq(from = 1,
              to = length(vsl_accuracy$ans),
              by = 1)) {
  corr <-
    append(corr, as.numeric(vsl_accuracy[i, ]$ans == vsl_accuracy[i, ]$key))
}
vsl_accuracy$corr <- corr

#Check stimuli and answer keys in the test phase against the entropy key---------------------------------
#Extract the testing phase--------------------------------------------------------------------------------

test_phase<- list()
loop_index = 0

for (id in vsl_bal_id) {
  loop_index = loop_index +1
  this_id_vsl <- vsl_bal[which(vsl_bal$part_id %in% id),]
  test_phase_start <- which(str_detect(this_id_vsl$stimulus, "vsl_instr14.wav$")) + 1
  test_phase_end <- which(str_detect(this_id_vsl$stimulus, "lsl_instr13.wav$")) - 1
  
  # blast_a_001 = blast_a_004 used old stimuli
  if (length(which(str_detect(this_id_vsl$stimulus, "lsl_instr13.wav$"))) == 0) {
    test_phase_end <- nrow(this_id_vsl) - 1
    print(id)
  }
  
  test_phase_this_id <- this_id_vsl[test_phase_start:test_phase_end,]
  # Extract exposure phase
  test_phase[[loop_index]] <- test_phase_this_id
}

test_phase <- do.call(rbind, test_phase)



#Check whether the answer keys match the answer keys from the entropy keys----------------------------------------------------------- 
#Answer keys in the Entropy keys are always correct
test_phase_stim <- list()
loop_index = 0 
test_phase_id <- unique(vsl_bal$part_id)
trial_index <- seq(from = 1, to = 192,  by = 1)

for (id in test_phase_id) {
  loop_index = loop_index + 1
  #Extract data for current id
  this_id_data <- test_phase[which(test_phase$part_id %in% id),]
  #Extract the rows that have the NA stimuli, vsl test phase starts and ends with NA
  row_white <- which(this_id_data$stimulus == "")
  #Extract the test phase trials for the current participant
  stim_test <- this_id_data[row_white[1]:row_white[length(row_white)], c("part_id", "stimulus")]
  #Remove the NA stimulus
  stim_test <- stim_test[which(stim_test$stimulus != ""),]
  #Add in trial number
  stim_test$trial_index <- trial_index
  #Extract only the stimuli column and split into triplets
  current_id_stim <- stim_test$stimulus
  current_id_stim <- gsub("alien", "", current_id_stim)
  current_id_triplet <- split(current_id_stim, ceiling(seq_along(current_id_stim)/3))
  #Combine the splitted triplets into a column
  current_id_triplet <- do.call(rbind, current_id_triplet)
  #Paste the three individual stimuli in a triplet into a column
  current_id_triplet <- data.frame(current_id_triplet)
  current_id_triplet$triplet <- with(current_id_triplet, paste(X1, X2, X3, sep = "_"))
  #format the triplet column into lower case to match with the entropy file
  current_id_triplet$triplet <- tolower(paste0("alien", current_id_triplet$triplet))
  #Extract triplets in the entropy file and insert an empty row every other row into the entropy key
  #Doing this will allow comparing 64 trials (targets + foils) with 32 trials (from entropy key)
  #First double all rows in vsl_entropy_keys
  doubled_entropy_key <- vsl_entropy_key_bal[rep(1:nrow(vsl_entropy_key_bal),1,each=2),]
  #Then make every other row's target triplet empty
  doubled_entropy_key[c(seq(2, dim(doubled_entropy_key)[1], by=2)), "alien_target"] <- NA
  #Check the triplets of the current id's data against entropy key
  #Every other rowsin doubled_entropy_key shows the target triplet, so if every other row yeilds TRUE, then answer will be 1
  check_every_other_row <- 
    as.numeric(current_id_triplet$triplet %in% doubled_entropy_key$alien_target)
  #Extract every other row and sub 0 with 2
  current_id_key <- check_every_other_row[seq(1, length(check_every_other_row), 2)]
  current_id_key <- gsub(0, 2, current_id_key)
  #Check current id's answer keys against the correct answer keys 
  current_id_correct_key <- sum(as.numeric(current_id_key == vsl_entropy_key_bal$answer_key))
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

# Entropy------------------------------------------------------------------------------------------------------------------

# Find the triplet type (each triplet gets coded with a value from A-D)
triplet_type <-
  rep(vsl_entropy_key_bal$target_type, times = length(unique(vsl_accuracy$subj)))
# Find the order for the triplet (the triplet either appeared first or second, with respect to the foil)
triplet_order <-
  rep(vsl_entropy_key_bal$answer_key, times = length(unique(vsl_accuracy$subj)))

# Find the image triplet (which three images make up the triplet)
image_triplet <-
  rep(vsl_entropy_key_bal$alien_target, times = length(unique(vsl_accuracy$subj)))

vsl_accuracy$triplet_type <- triplet_type
vsl_accuracy$triplet_order <- triplet_order
vsl_accuracy$image_triplet <- image_triplet


# Entropy
vsl_entropy_wide_bal <-
  cast(vsl_accuracy,
       subj ~ corr + triplet_type,
       value = "image_triplet",
       fun.aggregate = length)


#Caculate Entropy for each target type by group and by task
vsl_entropy_by_triplet_bal <- data.frame()

# vsl Entropy for each target type
for (i in 1:nrow(vsl_entropy_wide_bal)) {
  vsl_entropy_by_triplet_bal[i, "vsl_a_entropy"] <-
    Entropy(vsl_entropy_wide_bal[i, c("0_A", "1_A")])
  
  vsl_entropy_by_triplet_bal[i, "vsl_b_entropy"] <-
    Entropy(vsl_entropy_wide_bal[i, c("0_B", "1_B")])
  
  vsl_entropy_by_triplet_bal[i, "vsl_c_entropy"] <-
    Entropy(vsl_entropy_wide_bal[i, c("0_C", "1_C")])
  
  vsl_entropy_by_triplet_bal[i, "vsl_d_entropy"] <-
    Entropy(vsl_entropy_wide_bal[i, c("0_D", "1_D")])
  
  vsl_entropy_by_triplet_bal[i, "part_id"] <-
    vsl_entropy_wide_bal[i, c("subj")]
}



vsl_entropy_by_triplet_bal$mean_entropy <- 
  round(rowMeans(vsl_entropy_by_triplet_bal[,1:4], na.rm = FALSE, dims = 1), 3)


# Count how many answers were correct for each participant
subj_corr <- NULL
for (id in acc_id) {
  subj_corr <-
    append(subj_corr, round(sum(vsl_accuracy$corr[vsl_accuracy$subj == id]) /
                              32, digits = 3))
}

vsl_acc_table_bal <- data.frame(acc_id, subj_corr)


vsl_acc_table <- rbind(vsl_acc_table, vsl_acc_table_bal)
vsl_entropy_by_triplet <- rbind(vsl_entropy_by_triplet, vsl_entropy_by_triplet_bal)
vsl_entropy_wide <- rbind(vsl_entropy_wide, vsl_entropy_wide_bal)

#Save raw entropy by triplet counts
write.csv(vsl_entropy_wide,
          paste0(output_path, "entropy_by_triplet/blast_vsl_entropy_raw_sums.csv"))
#Save entropy by triplet type
write.csv(vsl_entropy_by_triplet,
          paste0(output_path, "entropy_by_triplet/blast_vsl_entropy_by_triplet.csv"))

#Save mean entropy 
write.csv(vsl_entropy_by_triplet[,5:6], 
          paste0(output_path, "blast_online_adult_vsl_entropy.csv"))
#Save accuracy
write.csv(vsl_acc_table, paste0(output_path, "blast_online_adult_vsl_accuracies.csv"))
#write.csv(vsl_acc_table, "/Volumes/data/projects/blast/data_summaries/blast_online_adult/breakdown/online_vsl_accuracies.csv")

