#  SIT Reaction Time Analysis
#  Violet Kozloff
#  Adapted from extraction files produced by An Nguyen
#  Last modified July 3rd, 2019
#  This script extracts mean reaction time and reaction time slope for statistical learning tasks involving structured and random triplets of letters and images
#  NOTE: relevant columns have been pre-selected through sit_cleaning.R
#  NOTE: Excludes any trials where participant responded to less than 50% of the targets (or responded to a different image than the target)

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
setwd("/Volumes/data/projects/completed_projects/sit/analysis/")

# Remove objects in environment
rm(list=ls())

# Read in picture vocabulary scores --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
picture_vocab <- read.csv("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vocab_clean/vocab_clean.csv")


# Read in ll files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/ll_clean")
ll_files <- list.files(pattern=("*.csv"))
ll_data <- NULL

for (file in ll_files)
{
  current_file <- read.csv(file)
  ll_data <- rbind.fill (ll_data, current_file)
}

# Read "f_not_false" as "F"
levels(ll_data$structured_targ)[levels(ll_data$structured_targ)=="f_not_false"] <- "F"
levels(ll_data$random_targ)[levels(ll_data$random_targ)=="f_not_false"] <- "F"

# Convert reaction times from milliseconds to seconds
ll_data$l_rt<-ll_data$l_rt*1000

# Remove extensions from image names
ll_data$image <- gsub (".png", "", ll_data$image, ignore.case=TRUE)
ll_data$image <- gsub (".bmp", "", ll_data$image, ignore.case=TRUE)
ll_data$random_targ <- gsub (".png", "", ll_data$random_targ, ignore.case=TRUE)
ll_data$structured_targ <- gsub (".png", "", ll_data$structured_targ, ignore.case=TRUE)
ll_data$random_targ <- gsub (".bmp", "", ll_data$random_targ, ignore.case=TRUE)
ll_data$structured_targ <- gsub (".bmp", "", ll_data$structured_targ, ignore.case=TRUE)


# Read in lv files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/lv_clean")
lv_files <- list.files(pattern=("*.csv"))
lv_data <- NULL

for (file in lv_files)
{
  current_file <- read.csv(file)
  lv_data <- rbind.fill (lv_data, current_file)
}

# Read "f_not_false" as "F"
levels(lv_data$structured_targ)[levels(lv_data$structured_targ)=="f_not_false"] <- "F"
levels(lv_data$random_targ)[levels(lv_data$random_targ)=="f_not_false"] <- "F"

# Convert reaction times from milliseconds to seconds
lv_data$l_rt <- lv_data$l_rt*1000
lv_data$v_rt <- lv_data$v_rt*1000

# Remove extensions from image names
lv_data$image <- gsub (".png", "", lv_data$image, ignore.case=TRUE)
lv_data$image <- gsub (".bmp", "", lv_data$image, ignore.case=TRUE)
lv_data$random_targ <- gsub (".png", "", lv_data$random_targ, ignore.case=TRUE)
lv_data$structured_targ <- gsub (".png", "", lv_data$structured_targ, ignore.case=TRUE)
lv_data$random_targ <- gsub (".bmp", "", lv_data$random_targ, ignore.case=TRUE)
lv_data$structured_targ <- gsub (".bmp", "", lv_data$structured_targ, ignore.case=TRUE)


# Read in vl files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vl_clean")
vl_files <- list.files(pattern=("*.csv"))
vl_data <- NULL

for (file in vl_files)
{
  current_file <- read.csv(file)
  vl_data <- rbind.fill (vl_data, current_file)
}

# Read "f_not_false" as "F"
levels(vl_data$structured_targ)[levels(vl_data$structured_targ)=="f_not_false"] <- "F"
levels(vl_data$random_targ)[levels(vl_data$random_targ)=="f_not_false"] <- "F"

# Convert reaction times from milliseconds to seconds
vl_data$l_rt <- vl_data$l_rt*1000
vl_data$v_rt <- vl_data$v_rt*1000

# Remove extensions from image names
vl_data$image <- gsub (".png", "", vl_data$image, ignore.case=TRUE)
vl_data$image <- gsub (".bmp", "", vl_data$image, ignore.case=TRUE)
vl_data$random_targ <- gsub (".png", "", vl_data$random_targ, ignore.case=TRUE)
vl_data$structured_targ <- gsub (".png", "", vl_data$structured_targ, ignore.case=TRUE)
vl_data$random_targ <- gsub (".bmp", "", vl_data$random_targ, ignore.case=TRUE)
vl_data$structured_targ <- gsub (".bmp", "", vl_data$structured_targ, ignore.case=TRUE)


# Read in vv files and combine them into one data frame -----------------------------------------------------------------------------------------------------------------------------------

setwd("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vv_clean")
vv_files <- list.files(pattern=("*.csv"))
vv_data <- NULL

for (file in vv_files)
{
  current_file <- read.csv(file)
  vv_data <- rbind.fill (vv_data, current_file)
}

# Convert response times to milliseconds
vv_data$v_rt <- vv_data$v_rt*1000

# Remove extensions from image names
vv_data$image <- gsub (".png", "", vv_data$image, ignore.case=TRUE)
vv_data$image <- gsub (".bmp", "", vv_data$image, ignore.case=TRUE)
vv_data$random_targ <- gsub (".png", "", vv_data$random_targ, ignore.case=TRUE)
vv_data$structured_targ <- gsub (".png", "", vv_data$structured_targ, ignore.case=TRUE)
vv_data$random_targ <- gsub (".bmp", "", vv_data$random_targ, ignore.case=TRUE)
vv_data$structured_targ <- gsub (".bmp", "", vv_data$structured_targ, ignore.case=TRUE)


# ******************** CONDITION 1: RANDOM LL*******************


# Separate random condition
random_ll <- ll_data[ which(ll_data$condition== "R"),]


## Index the targets -----------------------------------------------

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding stimulus ---------------------------------------------

# Identify the rows when this condition's target was presented
random_ll_targets <- random_ll[which(random_ll$random_targ==random_ll$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(random_ll_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(random_ll_targets[which(random_ll$part_id==id),]))
}
rll_line_number <- data.frame(part_id, total_lines)
# TEST: There should be 32 entries
length(rll_line_number$part_id)
# TEST: They should all contain 288 lines
rll_line_number$total_lines

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
preceding_loop <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Isolate participants' response times.
# Include rows when the participant responded to the stimulus preceding the target (i.e. any time that the participant pressed the button within one stimulus before the target)
for(i in 1:nrow(random_ll_targets)) 
{
  # Isolate the ID number
  this_id <- random_ll_targets[i,]$part_id
  id <- append(id, paste(this_id))
  # Isolate the trial number
  this_trial_num <- random_ll_targets[i,]$trial_num
  trial <- append(trial, paste(this_trial_num))
  # Isolate the target's rt
  this_targ_rt <- random_ll_targets[i,]$l_rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- random_ll_targets[i,]$this_l_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_ll[which(random_ll$trial_num==(this_trial_num-1) & random_ll$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num_before)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_l_loop
  loop_before <- append(loop_before, preceding_loop) 
  preceding_rt <- this_trial_before$l_rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_ll_targets[i,] [,"l_rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_ll_targets[i,][,"l_rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1000-preceding_rt))
      case <- append (case, "case 2")}
    else {
      # Copy the target response time of NA
      rt_col <- append (rt_col, this_targ_rt)
      case <- append (case, "case 3")}
  }
  # If the participant did not respond within 1 stimulus preceding the target, 
  else if (is.na(random_ll_targets[i,] [,"l_rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, this_targ_rt)
    case <- append (case, "case 4")}
  else{
    rt_col <- append (rt_col, "anomaly, this shouldn't happen")
    case <- append (case, "case 5")}
}

# Match id and response times
random_ll_extracted <- data.frame(id, trial, trial_num_before, loop, loop_before, target_rt, rt_before, rt_col)

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(random_ll_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(random_ll_extracted$id==i))}

# TEST: This should be equal to 32
length (target_sum)
# TEST: This should contain a vector full of 24s
target_sum

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
random_ll_extracted$targ_index <- targ_index

# Remove any values of NA
random_ll_extracted <- random_ll_extracted[!is.na(random_ll_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

#There are 24 targets for each participant. Some may have a low hit rate (responded to 12 targets or less)
low_hits<-NULL
hits<-NULL
# Find people with a low hit rate
for (id in extracted_part_id){
  if (length(random_ll_extracted[which(random_ll_extracted$id==id & !is.na(random_ll_extracted$rt_col)),]$rt_col)<13)
  {low_hits<-append(low_hits, id)
  hits<-append(hits, length(random_ll_extracted[which(random_ll_extracted$id==id),]$loop))
  }
}

# Remove people with low hit rate
random_ll_extracted <- random_ll_extracted[! random_ll_extracted$id %in% low_hits, ]
# Find only participants with over 50% hit rate
extracted_part_id <- unique(random_ll_extracted$id)

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
rll<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL
same_or_diff <- NULL
test_phase <- NULL
number_rts <- NULL

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "ll")
  type <- append (type, "random")
  same_or_diff <- append (same_or_diff, "same")
  test_phase <- append (test_phase, "lsl")
  number_rts <- append(number_rts, length(!is.na(random_ll_extracted$rt_col[random_ll_extracted$id==id])))
  mean_rt <- append(mean_rt, round(mean(random_ll_extracted$rt_col[random_ll_extracted$id==id], na.rm = TRUE),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_ll_extracted$rt_col[random_ll_extracted$id==id]~random_ll_extracted$targ_index[random_ll_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_ll_extracted[ which(random_ll_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  range <- append (range, (this_range[2]-this_range[1]))
}

number_rts
mean(number_rts)
sd(number_rts)

# Combine data for each participant
rll <- data.frame(part_id, task, same_or_diff, test_phase, domain, type, mean_rt, range, upper_bound, lower_bound, rt_slope) 

#Remove any points outside 2.5 stdev of the mean
# lowerbound <- mean(rll$rt_slope) - 2.5*sd(rll$rt_slope)
# upperbound <- mean(rll$rt_slope) + 2.5*sd(rll$rt_slope)
# rll <- rll[rll$rt_slope>=lowerbound,]
# rll <- rll[rll$rt_slope<=upperbound,]


# ******************** CONDITION 2: RANDOM LV *******************


# Separate random and structured conditions
random_lv <- lv_data[ which(lv_data$condition== "R"),]


# Index the targets -----------------------------------------------

# Identify the rows when this condition's target was presented
random_lv_targets <- random_lv[which(random_lv$random_targ==random_lv$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(random_lv_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(random_lv_targets[which(random_lv$part_id==id),]))
}
rlv_line_number <- data.frame(part_id, total_lines)
# TEST: There should be 32 entries
length(rlv_line_number$part_id)
# TEST: They should all contain 288 lines
rlv_line_number$total_lines


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ folvowing stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
preceding_loop <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Isolate participants' response times.
# Include rows when the participant responded to the stimulus preceding the target (i.e. any time that the participant pressed the button within one stimulus before the target)
for(i in 1:nrow(random_lv_targets)) 
{
  # Isolate the ID number
  this_id <- random_lv_targets[i,]$part_id
  id <- append(id, paste(this_id))
  # Isolate the trial number
  this_trial_num <- random_lv_targets[i,]$trialnum
  trial <- append(trial, paste(this_trial_num))
  # Isolate the target's rt
  this_targ_rt <- random_lv_targets[i,]$v_rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- random_lv_targets[i,]$this_v_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_lv[which(random_lv$trialnum==this_trial_num-1 & random_lv$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trialnum
  trial_num_before <- append (trial_num_before, this_trial_num_before)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_v_loop
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, folvowing_loop)
  preceding_rt <- this_trial_before$v_rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_lv_targets[i,] [,"v_rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_lv_targets[i,][,"v_rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["v_rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1000-preceding_rt))
      case <- append (case, "case 2")}
    else {
      # Copy the target response time of NA
      rt_col <- append (rt_col, this_targ_rt)
      case <- append (case, "case 3")}
  }
  # If the participant did not respond within 1 stimulus preceding the target, 
  else if (is.na(random_lv_targets[i,] [,"v_rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, this_targ_rt)
    case <- append (case, "case 4")}
  else{
    rt_col <- append (rt_col, "anomaly, this shouldn't happen")
    case <- append (case, "case 5")}
}

# Match id and response times
random_lv_extracted <- data.frame(id, trial, trial_num_before, loop, loop_before, target_rt, rt_before, rt_col)

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(random_lv_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(random_lv_extracted$id==i))}

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# TEST: This should be equal to 32
length (target_sum)
# TEST: This should contain a vector full of 24s
target_sum

# Add the targets' indices
random_lv_extracted$targ_index <- targ_index

# Remove any values of NA
random_lv_extracted <- random_lv_extracted[!is.na(random_lv_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

#There are 24 targets for each participant. Some may have a low hit rate (responded to 12 targets or less)
low_hits<-NULL
# Find people with a low hit rate
for (id in extracted_part_id){
  if (length(random_lv_extracted[which(random_lv_extracted$id==id),]$loop)<13)
  {low_hits<-append(low_hits, id)}
}
# Remove people with low hit rate
random_lv_extracted <- random_lv_extracted[! random_lv_extracted$id %in% low_hits, ]
# Find only participants with over 50% hit rate
extracted_part_id <- unique(random_lv_extracted$id)

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
rlv<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL
same_or_diff <- NULL
test_phase <- NULL
number_rts <- NULL

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "non-linguistic")
  task <- append(task, "lv")
  type <- append (type, "random")
  same_or_diff <- append (same_or_diff, "different")
  test_phase <- append (test_phase, "lsl")
  mean_rt <- append(mean_rt, round(mean(random_lv_extracted$rt_col[random_lv_extracted$id==id]),digits=3))
  number_rts <- append(number_rts, length(!is.na(random_lv_extracted$rt_col[random_lv_extracted$id==id])))
  rt_slope <- append (rt_slope, round(summary(lm(random_lv_extracted$rt_col[random_lv_extracted$id==id]~random_lv_extracted$targ_index[random_lv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_lv_extracted[ which(random_lv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rlv <- data.frame(part_id, task, same_or_diff, test_phase, domain,type, mean_rt, range, upper_bound, lower_bound, rt_slope)

number_rts
mean(number_rts)
sd(number_rts)

#Remove any points outside 2.5 stdev of the mean
# lowerbound <- mean(rlv$rt_slope) - 2.5*sd(rlv$rt_slope)
# upperbound <- mean(rlv$rt_slope) + 2.5*sd(rlv$rt_slope)
# rlv <- rlv[rlv$rt_slope>=lowerbound,]
# rlv <- rlv[rlv$rt_slope<=upperbound,]



# ******************** CONDITION 3: RANDOM VL*******************

# Separate random and structured conditions
random_vl <- vl_data[ which(vl_data$condition== "R"),]


# Index the targets -----------------------------------------------

# Identify the rows when this condition's target was presented

random_vl_targets <- random_vl[which(random_vl$random_targ==random_vl$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(random_vl_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(random_vl_targets[which(random_vl$part_id==id),]))
}
rvl_line_number <- data.frame(part_id, total_lines)
# There should be 32 entries
length(rvl_line_number$part_id)
# They should all contain 288 lines
rvl_line_number$total_lines


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ fovlowing stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
preceding_loop <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Identify the rows when this condition's target was presented
random_vl_targets <- random_vl[which(random_vl$random_targ==random_vl$image),]

# Isolate participants' response times.
# Include rows when the participant responded to the stimulus preceding the target (i.e. any time that the participant pressed the button within one stimulus before the target)
for(i in 1:nrow(random_vl_targets)) 
{
  # Isolate the ID number
  this_id <- random_vl_targets[i,]$part_id
  id <- append(id, paste(this_id))
  # Isolate the trial number
  this_trial_num <- random_vl_targets[i,]$trial_num
  trial <- append(trial, paste(this_trial_num))
  # Isolate the target's rt
  this_targ_rt <- random_vl_targets[i,]$l_rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- random_vl_targets[i,]$this_l_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_vl[which(random_vl$trial_num==this_trial_num-1 & random_vl$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num_before)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_l_loop
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, fovlowing_loop)
  preceding_rt <- this_trial_before$l_rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_vl_targets[i,] [,"l_rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_vl_targets[i,][,"l_rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1000-preceding_rt))
      case <- append (case, "case 2")}
    else {
      # Copy the target response time of NA
      rt_col <- append (rt_col, this_targ_rt)
      case <- append (case, "case 3")}
  }
  # If the participant did not respond within 1 stimulus preceding the target, 
  else if (is.na(random_vl_targets[i,] [,"l_rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, this_targ_rt)
    case <- append (case, "case 4")}
  else{
    rt_col <- append (rt_col, "anomaly, this shouldn't happen")
    case <- append (case, "case 5")}
}

# Match id and response times
random_vl_extracted <- data.frame(id, trial, trial_num_before, loop, loop_before, target_rt, rt_before, rt_col)

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(random_vl_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(random_vl_extracted$id==i))}

# TEST: This should be equal to 32
length (target_sum)
# TEST: This should contain a vector full of 24s
target_sum

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
random_vl_extracted$targ_index <- targ_index

# Remove any values of NA
random_vl_extracted <- random_vl_extracted[!is.na(random_vl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

#There are 24 targets for each participant. Some may have a low hit rate (responded to 12 targets or less)
low_hits<-NULL
# Find people with a low hit rate
for (id in extracted_part_id){
  if (length(random_vl_extracted[which(random_vl_extracted$id==id),]$loop)<13)
  {low_hits<-append(low_hits, id)}
}
# Remove people with low hit rate
random_vl_extracted <- random_vl_extracted[! random_vl_extracted$id %in% low_hits, ]
# Find only participants with over 50% hit rate
extracted_part_id <- unique(random_vl_extracted$id)


# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
same_or_diff <- NULL
test_phase <- NULL
rvl<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL
number_rts <- NULL

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "vl")
  type <- append (type, "random")
  same_or_diff <- append (same_or_diff, "different")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(random_vl_extracted$rt_col[random_vl_extracted$id==id]),digits=3))
  number_rts <- append(number_rts, length(!is.na(random_vl_extracted$rt_col[random_vl_extracted$id==id])))
  rt_slope <- append (rt_slope, round(summary(lm(random_vl_extracted$rt_col[random_vl_extracted$id==id]~random_vl_extracted$targ_index[random_vl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vl_extracted[ which(random_vl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rvl <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

number_rts
mean(number_rts)
sd(number_rts)

#Remove any points outside 2.5 stdev of the mean
# lowerbound <- mean(rvl$rt_slope) - 2.5*sd(rvl$rt_slope)
# upperbound <- mean(rvl$rt_slope) + 2.5*sd(rvl$rt_slope)
# rvl <- rvl[rvl$rt_slope>=lowerbound,]
# rvl <- rvl[rvl$rt_slope<=upperbound,]


# for internal checking only: find mean rt_slope
mean_rvl_rt_slope <- mean (rvl$rt_slope)


# ******************** CONDITION 4: RANDOM VV *******************

# Separate random and structured conditions
random_vv <- vv_data[ which(vv_data$condition== "R"),]

# Index the targets -----------------------------------------------

# Identify the rows when this condition's target was presented
random_vv_targets <- random_vv[which(random_vv$random_targ==random_vv$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(random_vv_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(random_vv_targets[which(random_vv$part_id==id),]))
}
rvv_line_number <- data.frame(part_id, total_lines)
# There should be 32 entries
length(rvv_line_number$part_id)
# They should all contain 288 lines
rvv_line_number$total_lines

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ fovvowing stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
preceding_loop <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Identify the rows when this condition's target was presented
random_vv_targets <- random_vv[which(random_vv$random_targ==random_vv$image),]

# Isolate participants' response times.
# Include rows when the participant responded to the stimulus preceding the target (i.e. any time that the participant pressed the button within one stimulus before the target)
for(i in 1:nrow(random_vv_targets)) 
{
  # Isolate the ID number
  this_id <- random_vv_targets[i,]$part_id
  id <- append(id, paste(this_id))
  # Isolate the trial number
  this_trial_num <- random_vv_targets[i,]$trial_num
  trial <- append(trial, paste(this_trial_num))
  # Isolate the target's rt
  this_targ_rt <- random_vv_targets[i,]$v_rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- random_vv_targets[i,]$this_v_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_vv[which(random_vv$trial_num==this_trial_num-1 & random_vv$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num_before)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_v_loop
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, fovvowing_loop)
  preceding_rt <- this_trial_before$v_rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_vv_targets[i,] [,"v_rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_vv_targets[i,][,"v_rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["v_rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1000-preceding_rt))
      case <- append (case, "case 2")}
    else {
      # Copy the target response time of NA
      rt_col <- append (rt_col, this_targ_rt)
      case <- append (case, "case 3")}
  }
  # If the participant did not respond within 1 stimulus preceding the target, 
  else if (is.na(random_vv_targets[i,] [,"v_rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, this_targ_rt)
    case <- append (case, "case 4")}
  else{
    rt_col <- append (rt_col, "anomaly, this shouldn't happen")
    case <- append (case, "case 5")}
}

# Match id and response times
random_vv_extracted <- data.frame(id, trial, trial_num_before, loop, loop_before, target_rt, rt_before, rt_col)

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(random_vv_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(random_vv_extracted$id==i))}

# TEST: This should be equal to 32 (for each of the 32 participants)
length (target_sum)
# TEST: This should contain a vector full of 24s (for the 24 targets each participant saw)
target_sum

# TO DO: sit_a_054 only saw 16 before psychopy quit, so consider removing them

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
random_vv_extracted$targ_index <- targ_index

# Remove any values of NA. 
# We do this a second time here to remove any participants who did not respond during the trial.
random_vv_extracted <- random_vv_extracted[!is.na(random_vv_extracted$rt_col),]

# List unique participant IDs for this condition
extracted_part_id <- unique(random_vv_extracted$id)

# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

#There are 24 targets for each participant. Some may have a low hit rate (responded to 12 targets or less)
low_hits<-NULL
# Find people with a low hit rate
for (id in extracted_part_id){
  if (length(random_vv_extracted[which(random_vv_extracted$id==id),]$loop)<13)
  {low_hits<-append(low_hits, id)}
}
# Remove people with low hit rate
random_vv_extracted <- random_vv_extracted[! random_vv_extracted$id %in% low_hits, ]
# Find only participants with over 50% hit rate
extracted_part_id <- unique(random_vv_extracted$id)


# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
same_or_diff <- NULL
test_phase <- NULL
task<- NULL
rvv<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL
number_rts <- NULL

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "non-linguistic")
  task <- append(task, "vv")
  type <- append (type, "random")
  same_or_diff <- append (same_or_diff, "same")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(random_vv_extracted$rt_col[random_vv_extracted$id==id]),digits=3))
  number_rts <- append(number_rts, length(!is.na(random_vv_extracted$rt_col[random_vv_extracted$id==id])))
  rt_slope <- append (rt_slope, round(summary(lm(random_vv_extracted$rt_col[random_vv_extracted$id==id]~random_vv_extracted$targ_index[random_vv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vv_extracted[ which(random_vv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rvv <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

number_rts
length(number_rts)
mean(number_rts)
sd(number_rts)

# Remove any points outside 2.5 stdev of the mean
# lowerbound <- mean(rvv$rt_slope) - 2.5*sd(rvv$rt_slope)
# upperbound <- mean(rvv$rt_slope) + 2.5*sd(rvv$rt_slope)
# rvv <- rvv[rvv$rt_slope>=lowerbound,]
# rvv <- rvv[rvv$rt_slope<=upperbound,]



# ******************** CONDITION 5: STRUCTURED LL*******************

# Separate random and structured conditions
structured_ll <- ll_data[ which(ll_data$condition== "S"),]

# Identify the rows when this condition's target was presented
structured_ll_targets <- structured_ll[which(structured_ll$structured_targ==structured_ll$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(structured_ll_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(structured_ll_targets[which(structured_ll$part_id==id),]))
}
sll_line_number <- data.frame(part_id, total_lines)
# TEST: There should be 32 entries (for the 32 participants)
length(sll_line_number$part_id)
# TEST: They should all contain 288 lines (for the 288 lines each participant saw)
sll_line_number$total_lines


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding stimulus ---------------------------------------------


# Index the targets -----------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
preceding_loop <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL


# Isolate participants' response times.
# Include rows when the participant responded to the stimulus preceding the target (i.e. any time that the participant pressed the button within one stimulus before the target)
for(i in 1:nrow(structured_ll_targets)) 
{
  # Isolate the ID number
  this_id <- structured_ll_targets[i,]$part_id
  id <- append(id, paste(this_id))
  # Isolate the trial number
  this_trial_num <- structured_ll_targets[i,]$trial_num
  trial <- append(trial, paste(this_trial_num))
  # Isolate the target's rt
  this_targ_rt <- structured_ll_targets[i,]$l_rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- structured_ll_targets[i,]$this_l_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_ll[which(structured_ll$trial_num==this_trial_num-1 & structured_ll$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num_before)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_l_loop
  loop_before <- append(loop_before, preceding_loop) 
  preceding_rt <- this_trial_before$l_rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_ll_targets[i,] [,"l_rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_ll_targets[i,][,"l_rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1000-preceding_rt))
      case <- append (case, "case 2")}
    else {
      # Copy the target response time of NA
      rt_col <- append (rt_col, this_targ_rt)
      case <- append (case, "case 3")}
  }
  # If the participant did not respond within 1 stimulus preceding the target, 
  else if (is.na(structured_ll_targets[i,] [,"l_rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, this_targ_rt)
    case <- append (case, "case 4")}
  else{
    rt_col <- append (rt_col, "anomaly, this shouldn't happen")
    case <- append (case, "case 5")}
}

# Match id and response times
structured_ll_extracted <- data.frame(id, trial, trial_num_before, loop, loop_before, target_rt, rt_before, rt_col)


# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(structured_ll_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(structured_ll_extracted$id==i))}

# TO TEST: This should be 32 (for the 32 participants)
length(target_sum)
# This should all contain values of 24 (for the 24 targets per participant)
target_sum

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
structured_ll_extracted$targ_index <- targ_index

# Remove any values of NA
structured_ll_extracted <- structured_ll_extracted[!is.na(structured_ll_extracted$rt_col),]

# List unique participant IDs for this condition
extracted_part_id <- unique(structured_ll_extracted$id)

# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

#There are 24 targets for each participant. Some may have a low hit rate (responded to 12 targets or less)
low_hits<-NULL
# Find people with a low hit rate
for (id in extracted_part_id){
  if (length(structured_ll_extracted[which(structured_ll_extracted$id==id),]$loop)<13)
  {low_hits<-append(low_hits, id)}
}
# Remove people with low hit rate
structured_ll_extracted <- structured_ll_extracted[! structured_ll_extracted$id %in% low_hits, ]
# Find only participants with over 50% hit rate
extracted_part_id <- unique(structured_ll_extracted$id)


# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
same_or_diff <- NULL
test_phase <- NULL
sll<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL
number_rts <- NULL

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "ll")
  type <- append (type, "structured")
  same_or_diff <- append (same_or_diff, "same")
  test_phase <- append (test_phase, "lsl")
  mean_rt <- append(mean_rt, round(mean(structured_ll_extracted$rt_col[structured_ll_extracted$id==id]),digits=3))
  number_rts <- append(number_rts, length(!is.na(structured_ll_extracted$rt_col[structured_ll_extracted$id==id])))
  rt_slope <- append (rt_slope, round(summary(lm(structured_ll_extracted$rt_col[structured_ll_extracted$id==id]~structured_ll_extracted$targ_index[structured_ll_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_ll_extracted[ which(structured_ll_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
sll <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

length(number_rts)
number_rts
mean(number_rts)
sd(number_rts)

#Remove any points outside 2.5 stdev of the mean
# lowerbound <- mean(sll$rt_slope) - 2.5*sd(sll$rt_slope)
# upperbound <- mean(sll$rt_slope) + 2.5*sd(sll$rt_slope)
# sll <- sll[sll$rt_slope>=lowerbound,]
# sll <- sll[sll$rt_slope<=upperbound,]

# TEST: find mean rt_slope
mean_sll_rt_slope <- mean (sll$rt_slope)
# This should be negative
mean_sll_rt_slope



# ******************** CONDITION 6: lv structured*******************

# Separate structured and structured conditions
structured_lv <- lv_data[ which(lv_data$condition== "S"),]

# Identify the rows when this condition's target was presented
structured_lv_targets <- structured_lv[which(structured_lv$structured_targ==structured_lv$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(structured_lv_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(structured_lv_targets[which(structured_lv$part_id==id),]))
}

slv_line_number <- data.frame(part_id, total_lines)
# There should be 31 entries
length(slv_line_number$part_id)
# They should all contain 288 lines
slv_line_number$total_lines

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ folvowing stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
preceding_loop <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Isolate participants' response times.
# Include rows when the participant responded to the stimulus preceding the target (i.e. any time that the participant pressed the button within one stimulus before the target)
for(i in 1:nrow(structured_lv_targets)) 
{
  # Isolate the ID number
  this_id <- structured_lv_targets[i,]$part_id
  id <- append(id, paste(this_id))
  # Isolate the trial number
  this_trial_num <- structured_lv_targets[i,]$trialnum
  trial <- append(trial, paste(this_trial_num))
  # Isolate the target's rt
  this_targ_rt <- structured_lv_targets[i,]$l_rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- structured_lv_targets[i,]$this_l_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_lv[which(structured_lv$trialnum==this_trial_num-1 & structured_lv$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trialnum
  trial_num_before <- append (trial_num_before, this_trial_num_before)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_l_loop
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, folvowing_loop)
  preceding_rt <- this_trial_before$l_rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_lv_targets[i,] [,"l_rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_lv_targets[i,][,"l_rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1000-preceding_rt))
      case <- append (case, "case 2")}
    else {
      # Copy the target response time of NA
      rt_col <- append (rt_col, this_targ_rt)
      case <- append (case, "case 3")}
  }
  # If the participant did not respond within 1 stimulus preceding the target, 
  else if (is.na(structured_lv_targets[i,] [,"l_rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, this_targ_rt)
    case <- append (case, "case 4")}
  else{
    rt_col <- append (rt_col, "anomaly, this shouldn't happen")
    case <- append (case, "case 5")}
}

# Match id and response times
structured_lv_extracted <- data.frame(id, trial, trial_num_before, loop, loop_before, target_rt, rt_before, rt_col)


# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(structured_lv_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(structured_lv_extracted$id==i))}

# TEST: This should be equal to 32
length (target_sum)
# TEST: This should contain a vector full of 24s
target_sum


# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
structured_lv_extracted$targ_index <- targ_index

# Remove any values of NA
structured_lv_extracted <- structured_lv_extracted[!is.na(structured_lv_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

#There are 24 targets for each participant. Some may have a low hit rate (responded to 12 targets or less)
low_hits<-NULL
# Find people with a low hit rate
for (id in extracted_part_id){
  if (length(structured_lv_extracted[which(structured_lv_extracted$id==id),]$loop)<13)
  {low_hits<-append(low_hits, id)}
}
# Remove people with low hit rate
structured_lv_extracted <- structured_lv_extracted[! structured_lv_extracted$id %in% low_hits, ]
# Find only participants with over 50% hit rate
extracted_part_id <- unique(structured_lv_extracted$id)

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
same_or_diff <- NULL
test_phase <- NULL
slv<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL
number_rts <- NULL

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "lv")
  type <- append (type, "structured")
  same_or_diff <- append (same_or_diff, "different")
  test_phase <- append (test_phase, "lsl")
  mean_rt <- append(mean_rt, round(mean(structured_lv_extracted$rt_col[structured_lv_extracted$id==id]),digits=3))
  number_rts <- append(number_rts, length(!is.na(structured_lv_extracted$rt_col[structured_lv_extracted$id==id])))
  rt_slope <- append (rt_slope, round(summary(lm(structured_lv_extracted$rt_col[structured_lv_extracted$id==id]~structured_lv_extracted$targ_index[structured_lv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_lv_extracted[ which(structured_lv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
slv <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

number_rts
length(number_rts)
mean(number_rts)
sd(number_rts)

#Remove any points outside 2.5 stdev of the mean
# lowerbound <- mean(slv$rt_slope) - 2.5*sd(slv$rt_slope)
# upperbound <- mean(slv$rt_slope) + 2.5*sd(slv$rt_slope)
# slv <- slv[slv$rt_slope>=lowerbound,]
# slv <- slv[slv$rt_slope<=upperbound,]


# TEST: find mean rt_slope
mean_slv_rt_slope <- mean (slv$rt_slope)
# It should be negative
mean_slv_rt_slope


# ******************** CONDITION 7: vl structured*******************

# Separate structured and structured conditions
structured_vl <- vl_data[ which(vl_data$condition== "S"),]

# Identify the rows when this condition's target was presented
structured_vl_targets <- structured_vl[which(structured_vl$structured_targ==structured_vl$image),]


## Index the images by structured/ structured-----------------------------------------------

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(structured_vl_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(structured_vl_targets[which(structured_vl$part_id==id),]))
}
svl_line_number <- data.frame(part_id, total_lines)
# There should be 32 entries
length(svl_line_number$part_id)
# They should all contain 288 lines
svl_line_number$total_lines

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ fovlowing stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
preceding_loop <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Identify the rows when this condition's target was presented
structured_vl_targets <- structured_vl[which(structured_vl$structured_targ==structured_vl$image),]

# Isolate participants' response times.
# Include rows when the participant responded to the stimulus preceding the target (i.e. any time that the participant pressed the button within one stimulus before the target)
for(i in 1:nrow(structured_vl_targets)) 
{
  # Isolate the ID number
  this_id <- structured_vl_targets[i,]$part_id
  id <- append(id, paste(this_id))
  # Isolate the trial number
  this_trial_num <- structured_vl_targets[i,]$trial_num
  trial <- append(trial, paste(this_trial_num))
  # Isolate the target's rt
  this_targ_rt <- structured_vl_targets[i,]$v_rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- structured_vl_targets[i,]$this_v_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_vl[which(structured_vl$trial_num==this_trial_num-1 & structured_vl$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num_before)
  # Isolate the preceding row's this_v_loop value.
  preceding_loop <- this_trial_before$this_v_loop
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, fovlowing_loop)
  preceding_rt <- this_trial_before$v_rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_vl_targets[i,] [,"v_rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_vl_targets[i,][,"v_rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["v_rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1000-preceding_rt))
      case <- append (case, "case 2")}
    else {
      # Copy the target response time of NA
      rt_col <- append (rt_col, this_targ_rt)
      case <- append (case, "case 3")}
  }
  # If the participant did not respond within 1 stimulus preceding the target, 
  else if (is.na(structured_vl_targets[i,] [,"v_rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, this_targ_rt)
    case <- append (case, "case 4")}
  else{
    rt_col <- append (rt_col, "anomaly, this shouldn't happen")
    case <- append (case, "case 5")}
}

# Match id and response times
structured_vl_extracted <- data.frame(id, trial, trial_num_before, loop, loop_before, target_rt, rt_before, rt_col)


# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(structured_vl_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(structured_vl_extracted$id==i))}

# TEST: This should be equal to 32
length (target_sum)
# TEST: This should contain a vector full of 24s
target_sum


# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
structured_vl_extracted$targ_index <- targ_index

# Remove any values of NA
structured_vl_extracted <- structured_vl_extracted[!is.na(structured_vl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

#There are 24 targets for each participant. Some may have a low hit rate (responded to 12 targets or less)
low_hits<-NULL
# Find people with a low hit rate
for (id in extracted_part_id){
  if (length(structured_vl_extracted[which(structured_vl_extracted$id==id),]$rt_col)<13)
  {low_hits<-append(low_hits, id)}
}
# Remove people with low hit rate
structured_vl_extracted <- structured_vl_extracted[! structured_vl_extracted$id %in% low_hits, ]
# Find only participants with over 50% hit rate
extracted_part_id <- unique(structured_vl_extracted$id)


# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
same_or_diff <- NULL
test_phase <- NULL
svl<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL
number_rts <- NULL

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "non-linguistic")
  task <- append(task, "vl")
  type <- append (type, "structured")
  same_or_diff <- append (same_or_diff, "different")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(structured_vl_extracted$rt_col[structured_vl_extracted$id==id]),digits=3))
  number_rts <- append(number_rts, length(!is.na(structured_vl_extracted$rt_col[structured_vl_extracted$id==id])))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vl_extracted$rt_col[structured_vl_extracted$id==id]~structured_vl_extracted$targ_index[structured_vl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_vl_extracted[ which(structured_vl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
svl <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

number_rts
mean(number_rts)
sd(number_rts)
length(number_rts)

#Remove any points outside 2.5 stdev of the mean
# lowerbound <- mean(svl$rt_slope) - 2.5*sd(svl$rt_slope)
#upperbound <- mean(svl$rt_slope) + 2.5*sd(svl$rt_slope)
#svl <- svl[svl$rt_slope>=lowerbound,]
#svl <- svl[svl$rt_slope<=upperbound,]


# for internal checking only: find mean rt_slope
mean_svl_rt_slope <- mean (slv$rt_slope)

# TEST: find mean rt_slope
mean_svl_rt_slope <- mean (svl$rt_slope)
# It should be negative
mean_svl_rt_slope



# ******************** CONDITION 8: STRUCTURED VV *******************

# Separate structured and structured conditions
structured_vv <- vv_data[ which(vv_data$condition== "S"),]

# Identify the rows when this condition's target was presented
structured_vv_targets <- structured_vv[which(structured_vv$structured_targ==structured_vv$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(structured_vv_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(structured_vv_targets[which(structured_vv$part_id==id),]))
}
svv_line_number <- data.frame(part_id, total_lines)
# There should be 32 entries (for the 32 participants)
length(svv_line_number$part_id)
# They should all contain 288 lines (for the lines per participant)
svv_line_number$total_lines
# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ fovvowing stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
preceding_loop <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Isolate participants' response times.
# Include rows when the participant responded to the stimulus preceding the target (i.e. any time that the participant pressed the button within one stimulus before the target)
for(i in 1:nrow(structured_vv_targets)) 
{
  # Isolate the ID number
  this_id <- structured_vv_targets[i,]$part_id
  id <- append(id, paste(this_id))
  # Isolate the trial number
  this_trial_num <- structured_vv_targets[i,]$trial_num
  trial <- append(trial, paste(this_trial_num))
  # Isolate the target's rt
  this_targ_rt <- structured_vv_targets[i,]$v_rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- structured_vv_targets[i,]$this_v_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_vv[which(structured_vv$trial_num==this_trial_num-1 & structured_vv$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num_before)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_v_loop
  loop_before <- append(loop_before, preceding_loop) 
  preceding_rt <- this_trial_before$v_rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_vv_targets[i,] [,"v_rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_vv_targets[i,][,"v_rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["v_rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1000-preceding_rt))
      case <- append (case, "case 2")}
    else {
      # Copy the target response time of NA
      rt_col <- append (rt_col, this_targ_rt)
      case <- append (case, "case 3")}
  }
  # If the participant did not respond within 1 stimulus preceding the target, 
  else if (is.na(structured_vv_targets[i,] [,"v_rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, this_targ_rt)
    case <- append (case, "case 4")}
  else{
    rt_col <- append (rt_col, "anomaly, this shouldn't happen")
    case <- append (case, "case 5")}
}

# Match id and response times
structured_vv_extracted <- data.frame(id, trial, trial_num_before, loop, loop_before, target_rt, rt_before, rt_col)

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(structured_vv_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(structured_vv_extracted$id==i))}

# TEST: This should be equal to 32 (for the 32 participants)
length (target_sum)
# TEST: This should contain a vector full of 24s (for the 24 targets per participant)
target_sum

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
structured_vv_extracted$targ_index <- targ_index

# Remove any values of NA
# NOTE: This removes sit_a_010 who has no keypresses for the target
structured_vv_extracted <- structured_vv_extracted[!is.na(structured_vv_extracted$rt_col),]

# List unique participant IDs for this condition
extracted_part_id <- unique(structured_vv_extracted$id)

# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

#There are 24 targets for each participant. Some may have a low hit rate (responded to 12 targets or less)
low_hits<-NULL
# Find people with a low hit rate
for (id in extracted_part_id){
  if (length(!is.na(structured_vv_extracted[which(structured_vv_extracted$id==id),]$rt_col))<13)
  {low_hits<-append(low_hits, id)}
}
# Remove people with low hit rate
structured_vv_extracted <- structured_vv_extracted[! structured_vv_extracted$id %in% low_hits, ]
# Find only participants with over 50% hit rate
extracted_part_id <- unique(structured_vv_extracted$id)

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
same_or_diff <- NULL
test_phase <- NULL
svv<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL
number_rts <- NULL

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "non-linguistic")
  task <- append(task, "vv")
  type <- append (type, "structured")
  same_or_diff <- append (same_or_diff, "same")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(structured_vv_extracted$rt_col[structured_vv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vv_extracted$rt_col[structured_vv_extracted$id==id]~structured_vv_extracted$targ_index[structured_vv_extracted$id==id]))$coefficient[2,1],digits = 4))
  number_rts <- append(number_rts, length(!is.na(structured_vv_extracted$rt_col[structured_vv_extracted$id==id])))
  data_this_id <- (structured_vv_extracted[ which(structured_vv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

number_rts
mean(number_rts)
sd(number_rts)
length(number_rts)

# Combine data for each participant
svv <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

#Remove any points outside 2.5 stdev of the mean
#lowerbound <- mean(svv$rt_slope) - 2.5*sd(svv$rt_slope)
#upperbound <- mean(svv$rt_slope) + 2.5*sd(svv$rt_slope)
#svv <- svv[svv$rt_slope>=lowerbound,]
#svv <- svv[svv$rt_slope<=upperbound,]

# TEST: find mean rt_slope
mean_svv_rt_slope <- mean (svv$rt_slope)
# It should be negative
mean_svv_rt_slope


# Bind conditions together--------------------------------------------------------------------------------------------------------------------------------------------------

# Bind conditions
indiv_rt_slope<- data.frame(rbind(rll, rlv, rvl, rvv, sll, slv, svl, svv))

sd_rll_rt_slope <- sd(rll$rt_slope)
sd_rlv_rt_slope <- sd(rlv$rt_slope)
sd_rvl_rt_slope <- sd(rvl$rt_slope)
sd_rvv_rt_slope <- sd(rvv$rt_slope)
sd_sll_rt_slope <- sd(sll$rt_slope)
sd_slv_rt_slope <- sd(slv$rt_slope)
sd_svl_rt_slope <- sd(svl$rt_slope)
sd_svv_rt_slope <- sd(svv$rt_slope)



# Summarize rt_slope
indiv_rt_slope_wide <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'rt_slope')
indiv_rt_slope_wide<- merge(indiv_rt_slope_wide, picture_vocab, by = "part_id", all=TRUE)
indiv_rt_slope_wide <- cbind(indiv_rt_slope_wide, "same_or_diff")
colnames(indiv_rt_slope_wide)[9] <- "same_or_diff"
all_same <- indiv_rt_slope_wide[ which(indiv_rt_slope_wide$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- indiv_rt_slope_wide[ which(indiv_rt_slope_wide$lv>0), ]
all_diff$same_or_diff <- ("different")
indiv_rt_slope_wide <- rbind(all_same, all_diff)

# Write rt_slope summary into a file
write.csv(indiv_rt_slope_wide, "/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_rts_vocab_wide.csv")

# Summarize mean_rt
indiv_rt_wide <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'mean_rt')
indiv_rt_wide<- merge(indiv_rt_wide, picture_vocab, by = "part_id", all=TRUE)
indiv_rt_wide <- cbind(indiv_rt_wide, "same_or_diff")
colnames(indiv_rt_wide)[9] <- "same_or_diff"
all_same <- indiv_rt_wide[ which(indiv_rt_wide$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- indiv_rt_wide[ which(indiv_rt_wide$lv>0), ]
all_diff$same_or_diff <- ("different")
indiv_rt_wide <- rbind(all_same, all_diff)

# Write mean_rt summary into a file
write.csv(indiv_rt_wide, "/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_mean_rt_vocab.csv")


# Find group-level mean rt_slope accross tasks------------------------------------------------------------------------------------

group_rt_slope <- NULL
mean_struct_rt_slope <- NULL
mean_rand_rt_slope <- NULL
task <- NULL
mean_struct_rt <- NULL
mean_rand_rt <- NULL

# Find mean ll rt slope across participants
task <- append (task, paste ("ll"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="structured" 
                                                                                      & indiv_rt_slope$task== "ll"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="random" 
                                                                                  & indiv_rt_slope$task== "ll"), ]$rt_slope), digits =3))
mean_struct_rt <- append(mean_struct_rt, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="structured" 
                                                                          & indiv_rt_slope$task== "ll"), ]$mean_rt), digits =3))
mean_rand_rt <- append(mean_rand_rt, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="random" 
                                                                      & indiv_rt_slope$task== "ll"), ]$mean_rt), digits =3))

# Find mean lv rt slope across participants
task <- append (task, paste ("lv"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="structured" 
                                                                                      & indiv_rt_slope$task== "lv"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="random" 
                                                                                  & indiv_rt_slope$task== "lv"), ]$rt_slope), digits =3))
mean_struct_rt <- append(mean_struct_rt, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="structured" 
                                                                          & indiv_rt_slope$task== "lv"), ]$mean_rt), digits =3))
mean_rand_rt <- append(mean_rand_rt, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="random" 
                                                                      & indiv_rt_slope$task== "lv"), ]$mean_rt), digits =3))


# Find mean vl rt slope across participants
task <- append (task, paste ("vl"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="structured" 
                                                                                      & indiv_rt_slope$task== "vl"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="random" 
                                                                                  & indiv_rt_slope$task== "vl"), ]$rt_slope), digits =3))
mean_struct_rt <- append(mean_struct_rt, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="structured" 
                                                                          & indiv_rt_slope$task== "vl"), ]$mean_rt), digits =3))
mean_rand_rt <- append(mean_rand_rt, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="random" 
                                                                      & indiv_rt_slope$task== "vl"), ]$mean_rt), digits =3))


# Find mean vv rt slope across participants
task <- append (task, paste ("vv"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="structured" 
                                                                                      & indiv_rt_slope$task== "vv"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="random" 
                                                                                  & indiv_rt_slope$task== "vv"), ]$rt_slope), digits =3))
mean_struct_rt <- append(mean_struct_rt, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="structured" 
                                                                          & indiv_rt_slope$task== "vv"), ]$mean_rt), digits =3))
mean_rand_rt <- append(mean_rand_rt, round(mean(indiv_rt_slope[ which(indiv_rt_slope$type=="random" 
                                                                      & indiv_rt_slope$task== "vv"), ]$mean_rt), digits =3))


# Combine group accuracies into one data frame
group_rt_slope <- data.frame(cbind(task, mean_rand_rt_slope, mean_struct_rt_slope, mean_struct_rt, mean_rand_rt))

# Write rt slope data into a file
write.csv(group_rt_slope, "/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_rt_slope_group.csv")

