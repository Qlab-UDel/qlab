#  BLAST TSL Analysis
#  Jojo Hu
#  Last updated Sep 25th, 2019 
#  Adapted from mturk_lsl by An Nguyen and blast_web_lsl_predictable_2afc by Violet Kozloff
#  This script analyses accuracy and entropy for LSL files with predictable 2afc from the online session of the BLAST experiment
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------
install.packages("reshape")
library("reshape")
install.packages("DescTools")
library("DescTools")
library("stringr")


# Remove objects in environment
rm(list = ls())

# Set directory

setwd("/Volumes/data/projects/blast/data/online_sl/blast_adult/predictable_lsl")



# Output path
output_path <- ("/Volumes/data/projects/blast/data_summaries/blast_online_adult/breakdown/")

#importing files

# List input files
lsl_files <- list.files(pattern = "*lsl.csv")

# TO DO: This should change for corrected LSL files
language = list(1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2)

# Initialize variable to hold data
lsl <- NULL

# Extract relevant data and combine it
for (file in lsl_files) {
  # Select only relevant columns
  extracted_data <-
    read.csv(file)[c("rt",
                     "trial_index",
                     "targ",
                     "key_press",
                     "stimulus",
                     "animation_sequence")]
  # Create a column populated with the participant ID based on the file name
  extracted_data["part_id"] <- substr(basename(file), 1, 11)
  # Change target and stimulus to string
  extracted_data["targ"] <- 
    as.character(extracted_data$targ)
  extracted_data["stimulus"] <-
    as.character(extracted_data$stimulus)
  # The keypress value recorded as "rt" in the raw files is not the true reaction time. Rename the column. See below for details on how to use this value.
  colnames(extracted_data)[colnames(extracted_data) == "rt"] <-
    "press_time"
  # Standardize stimulus names and types
  # gsub is used as blast_a_001-blast_a_004 saw old letter stimuli that are not from blast
  extracted_data$stimulus <-
    gsub(".png", "", extracted_data$stimulus)
  extracted_data$stimulus <-
    gsub("image/", "", extracted_data$stimulus)
  
  extracted_data$press_time <- as.numeric(extracted_data$press_time)
  # Identify blank keypresses
  extracted_data[which(extracted_data$press_time == -1), ]$press_time <-
    NA
  # Identify preceding and following stimuli
  extracted_data$prev_stim <-
    append(NA, (head(extracted_data$stimulus,-1)))
  extracted_data$next_stim <-
    append(extracted_data$stimulus[-1], NA)
  # Combine data from current file
  lsl <- rbind(lsl, extracted_data)
}


# Calculate and summarize individual accuracies ------------------------------------------------------------

#Extract the test phase
test_phase <- lsl[(lsl$stimulus == "white" & !lsl$key_press == -1),]
#Remove all the rows that only contain NA
test_phase <- test_phase[rowSums(is.na(test_phase)) != ncol(test_phase),]

#Internal check: this should be exactly 32 (32 forced choices per participant)
#All test phase added together divided by the number of people should be 32 if everyone has 32 trials
#for test phase
number_of_trials <- length(test_phase$targ) / length(unique(test_phase$part_id))

if (number_of_trials!=32){
  stop("Check the number of trials. Participants do not have equal number of trials.")
}


#Extract rows in which the participant gives a response
row_numberv <-
  which(test_phase$key_press != -1 & test_phase$stimulus == "white")

# Create a data frame that contains the participants' responses
lsl_accuracy <- data.frame("ans" = NULL, 
                           "subj" = NULL,
                           "corr" = NULL)

for (i in 1:length(row_numberv)) {
  lsl_accuracy[i, "ans"] <- test_phase[row_numberv[i], ]$key_press
  lsl_accuracy[i, "subj"] <- test_phase[row_numberv[i], ]$part_id
}

lsl_accuracy <- lsl_accuracy[!(lsl_accuracy$ans == 32), ]

keyv <- NULL


# Combine the answer keys for the two language conditions that the participant saw
#This works, but maybe consider changing to cbind with repetition (filling in blank rows with the same language list)
keyv <- rep(language, times = length(unique(lsl_accuracy$subj)))

# Find all of the IDs for the participants whose accuracy you're calculating
acc_id <- unique(lsl_accuracy$subj)

lsl_accuracy$key <- keyv

#Substitute the key press (49,50) with the answer (1,2)
lsl_accuracy$ans <- gsub(50, 2, lsl_accuracy$ans)
lsl_accuracy$ans <- gsub(49, 1, lsl_accuracy$ans)

# Code answers as correct or incorrect

for (i in seq(from = 1,
              to = length(lsl_accuracy$ans),
              by = 1)) {
  lsl_accuracy[i, "corr"] <-
    as.numeric(lsl_accuracy[i, ]$ans == lsl_accuracy[i, ]$key)
}



# Entropy--------------------------------------------------------------------------------------

# Read in the entropy key
lsl_entropy_key <-
  read.csv(
    "/Volumes/data/projects/blast/data/online_sl/entropy_keys/lsl_entropy_key_predictable.csv"
  )
lsl_entropy_key <-
  (lsl_entropy_key[c("target_type",
                     "target_order",
                     "target_occurance_order",
                     "letter_target")])

#Check whether the answer keys match the answer keys from the entropy keys----------------------------------------------------------- 
#Answer keys in the Entropy keys are always correct
test_phase_stim <- list()
loop_index = 0 
test_phase_id <- unique(lsl$part_id)
trial_index <- seq(from = 1, to = 192,  by = 1)

for (id in test_phase_id) {
  loop_index = loop_index + 1
  #Extract data for current id
  this_id_data <- lsl[which(lsl$part_id %in% id),]
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
  doubled_entropy_key[c(seq(2, dim(doubled_entropy_key)[1], by=2)), "letter_target"] <- NA
  #Check the triplets of the current id's data against entropy key
  #Every other rowsin doubled_entropy_key shows the target triplet, so if every other row yeilds TRUE, then answer will be 1
  check_every_other_row <- 
    as.numeric(current_id_triplet$triplet %in% doubled_entropy_key$letter_target)
  #Extract every other row and sub 0 with 2
  current_id_key <- check_every_other_row[seq(1, length(check_every_other_row), 2)]
  current_id_key <- gsub(0, 2, current_id_key)
  #Check current id's answer keys against the correct answer keys 
  current_id_correct_key <- sum(as.numeric(current_id_key == lsl_entropy_key$target_order))
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

# Find the triplet type (each triplet gets coded with a value from A-D)
triplet_type <-
  rep(lsl_entropy_key$target_type, times = length(unique(lsl_accuracy$subj)))
# Find the order for the triplet (the triplet either appeared first or second, with respect to the foil)
triplet_order <-
  rep(lsl_entropy_key$target_order, times = length(unique(lsl_accuracy$subj)))
# Find the occurance for the triplet (each triplet occurs between 7 and 9 times. Number each occurance.)
triplet_occurance <-
  rep(lsl_entropy_key$target_occurance_order, times = length(unique(lsl_accuracy$subj)))
# Find the letter triplet (which three syllables make up the triplet)
letter_triplet <-
  rep(lsl_entropy_key$letter_target, times = length(unique(lsl_accuracy$subj)))

lsl_accuracy$triplet_type <- triplet_type
lsl_accuracy$triplet_order <- triplet_order
lsl_accuracy$triplet_occurance <- triplet_occurance
lsl_accuracy$letter_triplet <- letter_triplet



# Entropy
lsl_entropy_wide <-
  cast(lsl_accuracy,
       subj ~ corr + triplet_type,
       value = "letter_triplet",
       fun.aggregate = length)


#Caculate Entropy for each target type by group and by task
lsl_entropy_by_triplet <- data.frame()

# LSL Entropy for each target type
for (i in 1:nrow(lsl_entropy_wide)) {
  lsl_entropy_by_triplet[i, "lsl_a_entropy"] <-
    Entropy(lsl_entropy_wide[i, c("0_A", "1_A")])
  
  lsl_entropy_by_triplet[i, "lsl_b_entropy"] <-
    Entropy(lsl_entropy_wide[i, c("0_B", "1_B")])
  
  lsl_entropy_by_triplet[i, "lsl_c_entropy"] <-
    Entropy(lsl_entropy_wide[i, c("0_C", "1_C")])
  
  lsl_entropy_by_triplet[i, "lsl_d_entropy"] <-
    Entropy(lsl_entropy_wide[i, c("0_D", "1_D")])
  
  lsl_entropy_by_triplet[i, "part_id"] <-
    lsl_entropy_wide[i, c("subj")]
}


lsl_entropy_by_triplet$mean_entropy <-
  round(rowMeans(lsl_entropy_by_triplet[, 1:4], na.rm = FALSE, dims = 1), 3)




# Count correct answers-----------------------------------------------------------------

subj_corr <- NULL

for (id in acc_id) {
  subj_corr <-
    append(subj_corr, round(sum(lsl_accuracy$corr[lsl_accuracy$subj == id]) /
                              32, digits = 3))
}

lsl_acc_table <- data.frame(acc_id, subj_corr)

#Save raw sums for entropy
write.csv(lsl_entropy_wide,
          paste0(output_path, "entropy_by_triplet/blast_lsl_predictable_entropy_raw_sums.csv"))
#Save entropy by triplet type
write.csv(lsl_entropy_by_triplet,
          paste0(output_path, "entropy_by_triplet/blast_lsl_predictable_entropy_by_triplet.csv"))
#Save mean entropy 
write.csv(lsl_entropy_by_triplet[,5:6], 
          paste0(output_path, "blast_online_adult_lsl_predictable_entropy.csv"))

write.csv(lsl_acc_table,
          paste0(output_path, "blast_online_adult_lsl_predictable_2afc_accuracies.csv"))







# TO DO: Deal with all the warnings that come here? Idk why?
# Something is funky with the rts, which seem to be the presentation times and not response times?