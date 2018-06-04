#  SIT ACCURACY ANALYSIS
#  Violet Kozloff
#  April 17, 2018
#  This script analyzes mean reaction time and reaction time slope for statistical learning tasks involving structured and random triplets of letters and images
#  NOTE: relevant columns have been pre-selected through sit_cleaning.R
#  ****************************************************************************



# ******************** I. PREPARE FILES *************************


# Prepare workspace ------------------------------------------------------------------------------------------------------

# Install packages
install.packages("reshape")
install.packages("dplyr")
install.packages("corrplot")
library("reshape")
library("dplyr")
library("corrplot")

# Set working directory
setwd("Documents/qlab/analysis/sit-beh-analysis")

# Remove objects in environment
rm(list=ls())

# Prepare paths for files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#For use on Mac 
ll_input <- ("../../../sit_data/clean/ll_clean/")
lv_input <- ("../../../sit_data/clean/lv_clean/")
vl_input <- ("../../../sit_data/clean/vl_clean/")
vv_input <- ("../../../sit_data/clean/vv_clean/")
vocab_input <- ("../../../sit_data/clean/vocab_clean/vocab_clean.csv")

#Read in picture vocabulary scores
picture_vocab <- read.csv(vocab_input)

# Read in ll files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

ll_underscore_files <- list.files(path=ll_input, pattern = ".csv")

#Remove the underscores in file names
ll_files <- gsub("_", "", ll_underscore_files)

# Prepare data_frame to hold the files you're reading in
ll_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in ll_underscore_files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(ll_input, file, sep="")))
}

# Combine each file with the previous files into ll_data_frame
for (file in ll_files){ll_data_frame <- append(ll_data_frame, list(eval(parse(text=file))))}
ll_data_frame <- do.call(rbind.data.frame, ll_data_frame)


# Read in lv files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

lv_underscore_files <- list.files(path=lv_input, pattern = ".csv")

#Remove the underscores in file names
lv_files <- gsub("_", "", lv_underscore_files)

# Prepare data_frame to hold the files you're reading in
lv_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in lv_underscore_files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(lv_input, file, sep="")))
}

# Combine each file with the previous files into lv_data_frame
for (file in lv_files){lv_data_frame <- append(lv_data_frame, list(eval(parse(text=file))))}
lv_data_frame <- do.call(rbind.data.frame, lv_data_frame)


# Read in vl files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

vl_underscore_files <- list.files(path=vl_input, pattern = ".csv")

#Remove the underscores in file names
vl_files <- gsub("_", "", vl_underscore_files)

# Prepare data_frame to hold the files you're reading in
vl_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in vl_underscore_files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(vl_input, file, sep="")))
}

# Combine each file with the previous files into vl_data_frame
for (file in vl_files){vl_data_frame <- append(vl_data_frame, list(eval(parse(text=file))))}
vl_data_frame <- do.call(rbind.data.frame, vl_data_frame)


# Read in vv files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

vv_underscore_files <- list.files(path=vv_input, pattern = ".csv")

#Remove the underscores in file names
vv_files <- gsub("_", "", vv_underscore_files)

# Prepare data_frame to hold the files you're reading in
vv_data_frame<-list()

# Remove the dashes in each file name read it in
for(file in vv_underscore_files)
{
  assign(
    gsub("_", "", file),
    read_file <- read.csv(paste(vv_input, file, sep="")))
}

# Combine each file with the previous files into vv_data_frame
for (file in vv_files){vv_data_frame <- append(vv_data_frame, list(eval(parse(text=file))))}
vv_data_frame <- do.call(rbind.data.frame, vv_data_frame)



# ******************** FIND ACCURACY FOR LL FILES *************************

# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(lv_data_frame$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task <- NULL
same_or_diff <-NULL
test_phase <- NULL

# For each participant, extract id
# Assign domain, same_or_diff, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "lv")
  same_or_diff <- append(same_or_diff, "different")
  test_phase <- append (test_phase, "lsl")
  accuracy <- append(accuracy, round(mean(lv_data_frame[which(lv_data_frame$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_lv_accuracies <- data.frame(part_id, task, same_or_diff, test_phase, accuracy)

# TEST: There should be 26 entries
length(indiv_lv_accuracies$part_id)

# TEST: All entries should all have an accuracy value
# View(indiv_lv_accuracies)



# ******************** III. FIND ll ACCURACY *************************


# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(ll_data_frame$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task <- NULL
same_or_diff <-NULL
test_phase <- NULL

# For each participant, extract id
# Assign domain, same_or_diff, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "ll")
  same_or_diff <- append(same_or_diff, "same")
  test_phase <- append (test_phase, "lsl")
  accuracy <- append(accuracy, round(mean(ll_data_frame[which(ll_data_frame$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_ll_accuracies <- data.frame(part_id, task, same_or_diff, test_phase, accuracy)

# TEST: There should be 22 entries
length(indiv_ll_accuracies$part_id)

# TEST: All entries should all have an accuracy value
# View(indiv_ll_accuracies)



# ******************** V. FIND VL ACCURACY *************************


# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(vl_data_frame$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task<- NULL
same_or_diff <-NULL
test_phase <- NULL

# For each participant, extract id
# Assign domain, same_or_diff, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "vl")
  same_or_diff <- append(same_or_diff, "different")
  test_phase <- append (test_phase, "vsl")
  accuracy <- append(accuracy, round(mean(vl_data_frame[which(vl_data_frame$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_vl_accuracies <- data.frame(part_id, task, same_or_diff, test_phase, accuracy)

# TEST: There should be 26 entries
length(indiv_vl_accuracies$part_id)

# TEST: All entries should all have an accuracy value
# View(indiv_vl_accuracies)



# ******************** IV. FIND vv ACCURACY *************************


# Create a single data frame with each participant's accuracy for each condition-----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(vv_data_frame$part_id)

# Set up data frame to hold accuracies
accuracy <- NULL
part_id <- NULL
task<- NULL
same_or_diff <- NULL
test_phase <- NULL

# For each participant, extract id
# Assign domain, same_or_diff, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  task <- append(task, "vv")
  same_or_diff <- append(same_or_diff, "same")
  test_phase <- append(test_phase, "vsl")
  #accuracy <- append(accuracy, round(mean(vv_data_frame[ which(vv_data_frame$PartID==id), ]$corr_resp, na.rm=TRUE), digits =3),)
  accuracy <- append(accuracy, round(mean(vv_data_frame[which(vv_data_frame$part_id==id),]$corr_resp, na.rm=TRUE), digits = 3))
}

# Combine data for each participant
indiv_vv_accuracies <- data.frame(part_id, task, same_or_diff, test_phase, accuracy)

# TEST: There should be 22 entries
length(indiv_vv_accuracies$part_id)

# TEST: All entries should all have an accuracy value
# View(indiv_vv_accuracies)


#Summarize individual accuracies--------

# Bind different accuracy data frames
indiv_accuracies <- rbind(indiv_ll_accuracies, indiv_lv_accuracies, indiv_vl_accuracies, indiv_vv_accuracies)

# Create a wide form version of the data
indiv_accuracies_wide <- cast(indiv_accuracies, part_id ~ task, mean, value = 'accuracy')
indiv_accuracies_wide<- merge(indiv_accuracies_wide, picture_vocab, by = "part_id", all=TRUE)

# Mark by same or different group
indiv_accuracies_wide <- cbind(indiv_accuracies_wide, "same_or_diff")
colnames(indiv_accuracies_wide)[9] <- "same_or_diff"
all_same <- indiv_accuracies_wide[ which(indiv_accuracies_wide$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- indiv_accuracies_wide[ which(indiv_accuracies_wide$lv>0), ]
all_diff$same_or_diff <- ("different")
indiv_accuracies_wide <- rbind(all_same, all_diff)

#Write individual accuracies to output file
write.csv(indiv_accuracies_wide, "sit_accuracy_indiv.csv")


# Find group-level mean accuracy accross tasks------------------------------------------------------------------------------------

# Set up variables
group_accuracy <- NULL
mean_accuracy <- NULL
task <- NULL

# Find mean ll accuracy across participants
all_ll<-subset(indiv_accuracies, task=="ll")
task <- append (task, paste ("ll"))
mean_accuracy <- append (mean_accuracy, round(mean(all_ll$accuracy), digits = 3))

# Find mean ssl accuracy across participants
all_lv<-subset(indiv_accuracies, task=="lv")
task <- append (task, paste ("lv"))
mean_accuracy <- append (mean_accuracy, round(mean(all_lv$accuracy), digits = 3))

# Find mean tsl accuracy across participants
all_vl<-subset(indiv_accuracies, task=="vl")
task <- append (task, paste ("vl"))
mean_accuracy <- append (mean_accuracy, round(mean(all_vl$accuracy), digits = 3))

# Find mean vsl accuracy across participants
all_vv<-subset(indiv_accuracies, task=="vv")
task <- append (task, paste ("vv"))
mean_accuracy <- append (mean_accuracy, round(mean(all_vv$accuracy), digits = 3))

# Find mean accuracy across all lsl tests
all_lsl<-rbind(all_ll, all_lv)
task <- append (task, paste ("lsl_test"))
mean_accuracy <- append (mean_accuracy, round(mean(all_lsl$accuracy), digits = 3))

# Find mean accuracy across all vsl tests
all_vsl<-rbind(all_vl, all_vv)
task <- append (task, paste ("vsl_test"))
mean_accuracy <- append (mean_accuracy, round(mean(all_vsl$accuracy), digits = 3))

# Find mean accuracy across all "same condition"
all_same<-rbind(all_ll, all_vv)
task <- append (task, paste ("same_condition"))
mean_accuracy <- append (mean_accuracy, round(mean(all_same$accuracy), digits = 3))

# Find mean accuracy across all "different condition"
all_different<-rbind(all_lv, all_vl)
task <- append (task, paste ("different_condition"))
mean_accuracy <- append (mean_accuracy, round(mean(all_different$accuracy), digits = 3))

# Combine group accuracies into one data frame
group_accuracy <- data.frame(cbind(task, mean_accuracy))

write.csv(group_accuracy, "sit_accuracy_group.csv")



# ************************ ANALYSIS 1: SEE IF GROUPS ARE MATCHED: CHI-SQUARE TEST AND T-TESTS ************************

# Join individual accuracy and vocab score data
chi_square_data <- cast(indiv_accuracies, part_id ~ task, mean, value = 'accuracy')
chi_square_data <- merge(chi_square_data, picture_vocab, by = "part_id", all=TRUE)

# Add group (same or different)
chi_square_data <- cbind(chi_square_data, "same_or_diff")
colnames(chi_square_data)[9] <- "same_or_diff"
all_same <- chi_square_data[ which(chi_square_data$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- chi_square_data[ which(chi_square_data$lv>0), ]
all_diff$same_or_diff <- ("different")
chi_square_data <- rbind(all_same, all_diff)

# Subset only relevant data about the population
chi_square_vars <- c("part_id", "age", "sex", "score", "same_or_diff")
chi_square_data <- chi_square_data[chi_square_vars]
matched_data <- chi_square_data

# Chi-square test for gender
gender_table <- cast(matched_data,sex~same_or_diff,value = "score",length)
chisq.test(gender_table)

# T-test for vocab score by group
t.test(score~same_or_diff, data=matched_data) 

# T-test for age by group 
t.test(age~same_or_diff, data=matched_data)



# *************************** TEST EFFECTS OF GROUP AND TEST PHASE ON ACCURACY *******************

# ANOVA to test effects
m1=aov(accuracy~test_phase*same_or_diff+Error(part_id/test_phase), data=indiv_accuracies)
summary(m1)



# *************************** CORRELATIONS **********************************


# Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------

# Extract relevant data from indiv_accuracies and picture_vocab
corr_data <- cast(indiv_accuracies, part_id ~ task, mean, value = 'accuracy')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)

# Add corr_data's groups of same/ different
corr_data <- cbind(corr_data, "same_or_diff")
colnames(corr_data)[9] <- "same_or_diff"
all_same <- corr_data[ which(corr_data$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- corr_data[ which(corr_data$lv>0), ]
all_diff$same_or_diff <- ("different")
corr_data <- rbind(all_same, all_diff)
corr_data <- corr_data[ which(corr_data$score>0), ]

# Separate corr_data into groups by same/ different
same_corr <- corr_data[ which(!is.na(corr_data$ll)), ]
same_corr <- same_corr[, c(2, 5, 6)]
diff_corr <- corr_data[ which(!is.na(corr_data$lv)), ]
diff_corr <- diff_corr[, c(3, 4, 6)]
same_corr$vv<-as.numeric(same_corr$vv)

# Create correlation matrices for different condition
diff <- cor(diff_corr, method = c("pearson"),use="pairwise.complete.obs")

# Test p-values of correlation matrices for different condition
lv_corr<-cor.test(diff_corr$lv,diff_corr$score)
vl_corr<-cor.test(diff_corr$vl,diff_corr$score)

# Create correlation matrices for same condition
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")

# Test p-values of correlation matrices for different condition
ll_corr<-cor.test(same_corr$ll, same_corr$score) 
vv_corr<-cor.test(same_corr$vv, same_corr$score) 



#  ************* ANALYSIS 4: SEE WHETHER PERFORMANCE WAS ABOVE CHANCE WITH T-TESTS *************

# Test whether group performed significantly above chance 
t.test(indiv_ll_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_vv_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_vl_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_lv_accuracies$accuracy, alternative= "greater", mu=0.5)
