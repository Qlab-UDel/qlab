#  BLAST LSL Analysis
#  Jojo Hu
#  Last updated Sep 25th, 2019
#  Adapted from blast_web_lsl_random_2afc by Violet Kozloff and mturk_lsl by An Nguyen
#  This script analyses accuracy and entropy for lsl files from the online session of the BLAST experiment
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------
# TO DO: Add this to SSL, LSL pred, VSL
install.packages("reshape")
library("reshape")
install.packages("DescTools")
library("DescTools")
install.packages("stringr")
library("stringr")

# Remove objects in environment
rm(list=ls())

# Set directory
#setwd("/Volumes/data/projects/blast/data/online_sl/blast_adult")
# NOTE: Comment out the above line and use this one for children
setwd("/Volumes/data/projects/blast/data/online_sl/blast_child")

input_path <- ("/Volumes/data/projects/blast/data/online_sl/blast_child/")
#Since June 11th 2019, the test phase of all SL tasks have been changed to a balanced design
#New answer keys should be used
input_path2 <- ("/Volumes/data/projects/blast/data/online_sl/blast_child/counterbalance_2afc_sl_data/")

# NOTE: This is the one for SPOLI
# setwd("/Volumes/data-1/projects/spoli/raw_sl_data")


# Output path
#output_path <- ("/Volumes/data/projects/blast/data_summaries/blast_online_adult/breakdown/")
output_path <- ("/Volumes/data/projects/blast/data_summaries/blast_online_child/breakdown/")


#importing files

#List all lsl files with randomized 2afc
lsl_files <- list.files(path=input_path, pattern="*lsl.csv")
#List the lsl files after June 11th, 2019 with counterbalanced target-foils in the test phase
#Extract the ids for balanced lsl
lsl_files_balanced <- list.files(path=input_path2, pattern="*lsl.csv")
lsl_bal_id <- str_extract(lsl_files_balanced, "\\S+(?=_lsl.csv)")
#List the files that are not counterbalanced which are collected before June 11th, 2019
lsl_files_unbal <- lsl_files[!(lsl_files %in% lsl_files_balanced)]
lsl_unb_id <- str_extract(lsl_files_unbal, "\\S+(?=_lsl.csv)")


# TO DO: This should change for corrected LSL files
answer_key = list(1,2,2,1,2,2,1,2,1,1,2,1,2,2,1,1,2,1,1,2,1,2,1,2,1,2,2,1,1,2,2,1)
#Store the answer keys into a dataframe for checking against entropy below
acc_key <- data.frame(unlist(answer_key))

# Initialize variable to hold data
lsl <- NULL

# Extract relevant data and combine it
for (file in lsl_files){
  # Select only relevant columns
  extracted_data <- read.csv(file)[c("rt", "trial_index", "targ","key_press", "stimulus", "animation_sequence")]  
  # Create a column populated with the participant ID based on the file name
  extracted_data["part_id"] <- substr(basename(file), 1, 11)
  # Change target and stimulus to string
  extracted_data["targ"] <- as.character(extracted_data$targ)
  extracted_data["stimulus"] <- as.character(extracted_data$stimulus)
  # The keypress value recorded as "rt" in the raw files is not the true reaction time. Rename the column. See below for details on how to use this value.
  colnames(extracted_data)[colnames(extracted_data)=="rt"] <- "press_time"
  # Standardize stimulus names and types
  extracted_data$stimulus<- gsub(".png","", extracted_data$stimulus)
  extracted_data$stimulus<- gsub("image/image/","",extracted_data$stimulus)
  extracted_data$stimulus<- gsub("image/","",extracted_data$stimulus)
  extracted_data$press_time<-as.numeric(extracted_data$press_time)
  # Identify blank keypresses
  extracted_data[which(extracted_data$press_time==-1),]$press_time<-NA
  # Identify preceding and following stimuli
  extracted_data$prev_stim <- append(NA, (head(extracted_data$stimulus, -1)))
  extracted_data$next_stim <- append(extracted_data$stimulus[-1], NA)
  # Combine data from current file
  lsl<-rbind(lsl,extracted_data)
}


# Calculate and summarize individual accuracies ------------------------------------------------------------

#Extract the data for participants who did unbalanced design
test_phase_unb <- lsl[which(lsl$part_id %in% unlist(lsl_unb_id)),]

#Extract the data for participants who did balanced design
test_phase <- lsl[which(lsl$part_id %in% unlist(lsl_bal_id)),]

#Internal check: this should be exactly 32 (32 forced choices per participant)
# TO DO: Make this automatic so it just warns user if participant doesn't have exactly 32

ans <- NULL
keyv <- NULL
subj <- NULL
stim <- NULL
#Extract rows in which the participant gives a response in the test phase
row_numberv <- which(test_phase$key_press != -1 & test_phase$stimulus == "white")

for (i in row_numberv){
  ans<-append(ans, test_phase[i,]$key_press)
  subj <- append(subj, paste(test_phase[i,]$part_id))
}

# Create a data frame that contains the participants' responses
lsl_accuracy <- data.frame(ans, subj)
lsl_accuracy <- lsl_accuracy[!(lsl_accuracy$ans==32),]

#Check the number of trials for each participant
if ((length(lsl_accuracy$ans)/
     length(unique(lsl_accuracy$subj))) != 32) {
  print("Check the number of trials for each participant.")
  stop()
}

keyv<- NULL

i=0

# Repeat the answer keys for each participant
keyv <- rep(answer_key, times = length(unique(lsl_accuracy$subj)))

lsl_accuracy$key <- keyv

#Substitute the key press (49,50) with the answer (1,2)
lsl_accuracy$ans <- gsub(50,2,lsl_accuracy$ans)
lsl_accuracy$ans <- gsub(49,1,lsl_accuracy$ans)

#Loop through and mark answers as correct or incorrect
corr <- NULL
for (i in seq(from = 1,
              to = length(lsl_accuracy$ans),
              by = 1)) {
  corr <-
    append(corr, as.numeric(lsl_accuracy[i, ]$ans == lsl_accuracy[i, ]$key))
}
lsl_accuracy$corr <- corr


# Entropy

# Read in the entropy key
#lsl_entropy_key <- read.csv("/Volumes/data/projects/blast/data/online_sl/entropy_keys/lsl_entropy_key_randomized.csv")
lsl_entropy_key <-
  read.csv("/Volumes/data/projects/blast/data/online_sl/balanced2afc_entropy_keys/lsl_bal_entropy.csv")
lsl_entropy_key <-
  (lsl_entropy_key[c("target_type",
                     "answer_key",
                     "lsl_target_triplet")])

#Check answer keys used in analysis
check_acc_key <- cbind(lsl_entropy_key, acc_key)

if (all(check_acc_key$answer_key == 
        check_acc_key$unlist.answer_key.) == FALSE) {
  print("Check the accuracy keys: answer_key above")
  stop()
}

# Entropy

# Find the target triplet type (each triplet gets coded with a value from A-D)
triplet_type <-
  rep(lsl_entropy_key$target_type, times = length(unique(lsl_accuracy$subj)))
# Find the order for the triplet (the triplet either appeared first or second, with respect to the foil)
#This is also the correct answer keys for the task
triplet_order <-
  rep(lsl_entropy_key$answer_key, times = length(unique(lsl_accuracy$subj)))

# Find the letter triplet (which three syllables make up the target triplet)
letter_triplet <-
  rep(lsl_entropy_key$lsl_target_triplet, times = length(unique(lsl_accuracy$subj)))

lsl_accuracy$triplet_type <- triplet_type
lsl_accuracy$triplet_order <- triplet_order
lsl_accuracy$letter_triplet <- letter_triplet

#Check whether the answer keys match the answer keys from the entropy keys. 
#Answer keys in the Entropy keys are always correct
test_phase_stim <- list()
loop_index = 0 
test_phase_id <- unique(test_phase$part_id)
trial_index <- seq(from = 1, to = 192,  by = 1)

for (id in test_phase_id) {
  loop_index = loop_index + 1
  #Extract data for current id
  this_id_data <- test_phase[which(test_phase$part_id %in% id),]
  #Extract the rows that have the white stimuli, lsl test phase starts and ends with white
  row_white <- which(this_id_data$stimulus == "white")
  #Extract the test phase trials for the current participant
  stim_test <- this_id_data[row_white[1]:row_white[length(row_white)], c("part_id", "stimulus")]
  #Remove the white stimulus
  stim_test <- stim_test[which(stim_test$stimulus != "white"),]
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
  current_id_triplet$triplet <- tolower(paste0("letter", current_id_triplet$triplet))
  #Extract triplets in the entropy file and insert an empty row every other row into the entropy key
  #Doing this will allow comparing 64 trials (targets + foils) with 32 trials (from entropy key)
  #First double all rows in lsl_entropy_keys
  doubled_entropy_key <- lsl_entropy_key[rep(1:nrow(lsl_entropy_key),1,each=2),]
  #Then make every other row's target triplet empty
  doubled_entropy_key[c(seq(2, dim(doubled_entropy_key)[1], by=2)), "lsl_target_triplet"] <- NA
  #Check the triplets of the current id's data against entropy key
  #Every other rowsin doubled_entropy_key shows the target triplet, so if every other row yeilds TRUE, then answer will be 1
  check_every_other_row <- 
    as.numeric(current_id_triplet$triplet %in% doubled_entropy_key$lsl_target_triplet)
  #Extract every other row and sub 0 with 2
  current_id_key <- check_every_other_row[seq(1, length(check_every_other_row), 2)]
  current_id_key <- gsub(0, 2, current_id_key)
  #Check current id's answer keys against the correct answer keys 
  current_id_correct_key <- sum(as.numeric(current_id_key == lsl_entropy_key$answer_key))
  #Save the result into a list
  test_phase_stim[[loop_index]] <- data.frame(id, current_id_correct_key)
}

test_phase_stim <- do.call(rbind, test_phase_stim)

if (mean(test_phase_stim$current_id_correct_key) != 32) {
  print(test_phase_stim)
  print("Check subject IDs that do not have 32. They are not supposed to be in the counterbalanced group.")
  stop()
}

#-------------------------------------------------------------------------------------------------------------


# Entropy-----------------------------------------------------------------------------------------------------
lsl_entropy_wide <-
  cast(lsl_accuracy,
       subj ~ corr + triplet_type,
       value = "letter_triplet",
       fun.aggregate = length)


#Caculate Entropy for each target type by group and by task
lsl_entropy_by_triplet <- data.frame()

# LSL Entropy for each target type
for (i in 1:nrow(lsl_entropy_wide)) {
  lsl_entropy_by_triplet[i,"lsl_a_entropy"] <- Entropy(lsl_entropy_wide[i,c("0_A","1_A")])
  lsl_entropy_by_triplet[i,"lsl_b_entropy"] <- Entropy(lsl_entropy_wide[i,c("0_B","1_B")])
  lsl_entropy_by_triplet[i,"lsl_c_entropy"] <- Entropy(lsl_entropy_wide[i,c("0_C","1_C")])
  lsl_entropy_by_triplet[i,"lsl_d_entropy"] <- Entropy(lsl_entropy_wide[i,c("0_D","1_D")])
  lsl_entropy_by_triplet[i,"part_id"] <- lsl_entropy_wide[i,c("subj")]
}

lsl_entropy_by_triplet$mean_entropy <-
  round(rowMeans(lsl_entropy_by_triplet[, 1:4], na.rm = FALSE, dims = 1), 3)



# Find the number of correct answers for each participant
subj_corr <- NULL

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(lsl_accuracy$subj)

for (id in acc_id) {
  subj_corr <-
    append(subj_corr, round(sum(lsl_accuracy$corr[lsl_accuracy$subj == id]) /
                              32, digits = 3))
}

#Save lsl accuracy for participants who did the balanced design
lsl_acc_table <- data.frame(acc_id, subj_corr)

#--------------------------------------------------------------------------------------------------------------------------------






#Accuracy for subjects collected before June 11th, 2019 (NOT counterbalanced triplet/ foil in the test phase)-----------------------------

#Answer keys for unbalanced test phase
language = list(1,1,2,1,1,1,2,2,2,2,1,1,1,2,2,1,2,2,1,1,2,1,2,1,2,1,2,1,1,2,2,2)
#Internal check: this should be exactly 32 (32 forced choices per participant)
# TO DO: Make this automatic so it just warns user if participant doesn't have exactly 32

ans <- NULL
subj <- NULL

#Extract rows in which the participant gives a response
row_numberv <- which(test_phase_unb$key_press != -1 & test_phase_unb$stimulus == "white")

for (i in row_numberv){
  ans<-append(ans, test_phase_unb[i,]$key_press)
  subj <- append(subj, paste(test_phase_unb[i,]$part_id))
}

# Create a data frame that contains the participants' responses
lsl_accuracy_unb <- data.frame(ans, subj)
lsl_accuracy_unb <- lsl_accuracy_unb[!(lsl_accuracy_unb$ans==32),]

#Check the number of trials for each participant
if ((length(lsl_accuracy_unb$ans)/
     length(unique(lsl_accuracy_unb$subj))) != 32) {
  print("Check the number of trials for each participant.")
  stop()
}

keyv_unb<- NULL

i=0

# Combine the answer keys for the two language conditions that the participant saw
keyv_unb <- rep(language, times = length(unique(lsl_accuracy_unb$subj)))


lsl_accuracy_unb$key <- keyv_unb

#Substitute the key press (49,50) with the answer (1,2)
lsl_accuracy_unb$ans <- gsub(50,2,lsl_accuracy_unb$ans)
lsl_accuracy_unb$ans <- gsub(49,1,lsl_accuracy_unb$ans)

#Loop through and mark answers as correct or incorrect
corr <- NULL
for (i in seq(from = 1,
              to = length(lsl_accuracy_unb$ans),
              by = 1)) {
  corr <-
    append(corr, as.numeric(lsl_accuracy_unb[i, ]$ans == lsl_accuracy_unb[i, ]$key))
}

lsl_accuracy_unb$corr <- corr


# Entropy

# Read in the entropy key
lsl_entropy_key_unb <- read.csv("/Volumes/data/projects/blast/data/online_sl/entropy_keys/lsl_entropy_key_randomized.csv")

lsl_entropy_key_unb <-
  (lsl_entropy_key_unb[c("target_type",
                         "target_order",
                         "target_occurance_order",
                         "letter_target")])

#Check answer keys used in analysis
check_acc_key <- cbind(lsl_entropy_key_unb, acc_key)

if (all(check_acc_key$target_order == 
        check_acc_key$unlist.language.) == FALSE) {
  print("Check the accuracy keys: language above")
  stop()
}

#Check whether the answer keys match the answer keys from the entropy keys----------------------------------------------------------- 
#Answer keys in the Entropy keys are always correct
test_phase_stim <- list()
loop_index = 0 
test_phase_id_unb <- unique(test_phase_unb$part_id)
trial_index <- seq(from = 1, to = 192,  by = 1)

for (id in test_phase_id_unb) {
  loop_index = loop_index + 1
  #Extract data for current id
  this_id_data <- test_phase_unb[which(test_phase_unb$part_id %in% id),]
  #Extract the rows that have the white stimuli, lsl test phase starts and ends with white
  row_white <- which(this_id_data$stimulus == "white")
  #Extract the test phase trials for the current participant
  stim_test <- this_id_data[row_white[1]:row_white[length(row_white)], c("part_id", "stimulus")]
  #Remove the white stimulus
  stim_test <- stim_test[which(stim_test$stimulus != "white"),]
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
  current_id_triplet$triplet <- tolower(paste0("letter", current_id_triplet$triplet))
  #Extract triplets in the entropy file and insert an empty row every other row into the entropy key
  #Doing this will allow comparing 64 trials (targets + foils) with 32 trials (from entropy key)
  #First double all rows in lsl_entropy_keys
  doubled_entropy_key <- lsl_entropy_key_unb[rep(1:nrow(lsl_entropy_key_unb),1,each=2),]
  #Then make every other row's target triplet empty
  doubled_entropy_key[c(seq(2, dim(doubled_entropy_key)[1], by=2)), "letter_target"] <- NA
  #Check the triplets of the current id's data against entropy key
  #Every other rowsin doubled_entropy_key shows the target triplet, so if every other row yeilds TRUE, then answer will be 1
  check_every_other_row <- 
    as.numeric(current_id_triplet$triplet %in% doubled_entropy_key$letter_target)
  #Extract every other row and sub 0 with 2
  current_id_key <- check_every_other_row[seq(1, length(check_every_other_row), 2)]
  current_id_key <- gsub(0, 2, current_id_key)
  #Check current id's answer keys against the correct answer keys 
  current_id_correct_key <- sum(as.numeric(current_id_key == lsl_entropy_key_unb$target_order))
  #Save the result into a list
  test_phase_stim[[loop_index]] <- data.frame(id, current_id_correct_key)
}

test_phase_stim <- do.call(rbind, test_phase_stim)

if (mean(test_phase_stim$current_id_correct_key) != 32) {
  print(test_phase_stim)
  print("Check subject IDs that do not have 32. They are not supposed to be in the counterbalanced group.")
  stop()
}


# Entropy------------------------------------------------------------------------------------------------------------------------

# Find the triplet type (each triplet gets coded with a value from A-D)
triplet_type <-
  rep(lsl_entropy_key_unb$target_type, times = length(unique(lsl_accuracy_unb$subj)))
# Find the order for the triplet (the triplet either appeared first or second, with respect to the foil)
#This is also the correct answer keys for the task
triplet_order <-
  rep(lsl_entropy_key_unb$target_order, times = length(unique(lsl_accuracy_unb$subj)))
# Find the occurance for the triplet (each triplet occurs between 7 and 9 times. Number each occurance.)
triplet_occurance <-
  rep(lsl_entropy_key_unb$target_occurance_order, times = length(unique(lsl_accuracy_unb$subj)))
# Find the letter triplet (which three syllables make up the triplet)
letter_triplet <-
  rep(lsl_entropy_key_unb$letter_target, times = length(unique(lsl_accuracy_unb$subj)))

lsl_accuracy_unb$triplet_type <- triplet_type
lsl_accuracy_unb$triplet_order <- triplet_order
lsl_accuracy_unb$triplet_occurance <- triplet_occurance
lsl_accuracy_unb$letter_triplet <- letter_triplet

#Check whether the answer keys match the answer keys from the entropy keys. 
#Answer keys in the Entropy keys are always correct
if (unique(lsl_accuracy_unb$triplet_order == lsl_accuracy_unb$key) != TRUE) {
  print("Check the answer keys for each participant.")
  stop()
}



# Entropy
lsl_entropy_wide_unb <-
  cast(lsl_accuracy_unb,
       subj ~ corr + triplet_type,
       value = "letter_triplet",
       fun.aggregate = length)


#Caculate Entropy for each target type by group and by task
lsl_entropy_by_triplet_unb <- data.frame()

# LSL Entropy for each target type
for (i in 1:nrow(lsl_entropy_wide_unb)) {
  lsl_entropy_by_triplet_unb[i,"lsl_a_entropy"] <- Entropy(lsl_entropy_wide_unb[i,c("0_A","1_A")])
  lsl_entropy_by_triplet_unb[i,"lsl_b_entropy"] <- Entropy(lsl_entropy_wide_unb[i,c("0_B","1_B")])
  lsl_entropy_by_triplet_unb[i,"lsl_c_entropy"] <- Entropy(lsl_entropy_wide_unb[i,c("0_C","1_C")])
  lsl_entropy_by_triplet_unb[i,"lsl_d_entropy"] <- Entropy(lsl_entropy_wide_unb[i,c("0_D","1_D")])
  lsl_entropy_by_triplet_unb[i,"part_id"] <- lsl_entropy_wide_unb[i,c("subj")]
}

lsl_entropy_by_triplet_unb$mean_entropy <-
  round(rowMeans(lsl_entropy_by_triplet_unb[, 1:4], na.rm = FALSE, dims = 1), 3)

lsl_entropy_wide <- rbind(lsl_entropy_wide, lsl_entropy_wide_unb)

lsl_entropy_by_triplet <- rbind(lsl_entropy_by_triplet, lsl_entropy_by_triplet_unb)

#Save raw sums for entropy
write.csv(lsl_entropy_wide,
          paste0(output_path, "entropy_by_triplet/blast_lsl_randomized_entropy_raw_sums.csv"))
#Save entropy by triplet type
write.csv(lsl_entropy_by_triplet,
          paste0(output_path, "entropy_by_triplet/blast_lsl_randomized_entropy_by_triplet.csv"))
#Save mean entropy 
write.csv(lsl_entropy_by_triplet[,5:6], 
          paste0(output_path, "blast_online_children_lsl_randomized_entropy.csv"))



# Find the number of correct answers for each participant
subj_corr <- NULL

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(lsl_accuracy_unb$subj)

for (id in acc_id) {
  subj_corr <-
    append(subj_corr, round(sum(lsl_accuracy_unb$corr[lsl_accuracy_unb$subj == id]) /
                              32, digits = 3))
}

lsl_acc_table_unb <- data.frame(acc_id, subj_corr)

lsl_acc_table <- rbind(lsl_acc_table, lsl_acc_table_unb)
  
write.csv(lsl_acc_table, paste0(output_path, "blast_online_children_lsl_random_2afc_accuracies.csv"))



