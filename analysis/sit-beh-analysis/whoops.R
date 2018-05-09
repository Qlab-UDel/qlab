#  SIT Reaction Time Analysis
#  Violet Kozloff
#  May 8, 2018
#  This script analyzes mean reaction time and reaction time slope for statistical learning tasks involving structured and random triplets of letters and images
#  NOTE: relevant columns have been pre-selected through sit_cleaning.R
#  NOTE: Excludes any trials where participant did not respond at all to the target or responded to a different target



# ******************** I. PREPARE FILES *************************


# Prepare workspace ------------------------------------------------------------------------------------------------------

# Install packages
install.packages("reshape")
install.packages("dplyr")
install.packages("corrplot")
library("reshape")
library("dplyr")
library("corrplot")

# Prepare workspace ------------------------------------------------------------------------------------------------------

# Remove objects in environment
rm(list=ls())


# Prepare paths for files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#For use on Mac 
ll_input <- ("../../../sit_data/clean/ll_clean/")
lv_input <- ("../../../sit_data/clean/lv_clean/")
vl_input <- ("../../../sit_data/clean/vl_clean/")
vv_input <- ("../../../sit_data/clean/vv_clean/")
vocab_input <- ("../../../sit_data/clean/vocab_clean/vocab_clean.csv")

# Read in NIH toolbox data
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

# Read "f_not_false" as "F"
levels(ll_data_frame$structured_targ)[levels(ll_data_frame$structured_targ)=="f_not_false"] <- "F"
levels(ll_data_frame$random_targ)[levels(ll_data_frame$random_targ)=="f_not_false"] <- "F"

# Convert reaction times from milliseconds to seconds
ll_data_frame$l_block_trial_key_resp.rt<-ll_data_frame$l_block_trial_key_resp.rt*1000

# Remove extensions from image names
ll_data_frame$image <- gsub (".png", "", ll_data_frame$image, ignore.case=TRUE)
ll_data_frame$image <- gsub (".bmp", "", ll_data_frame$image, ignore.case=TRUE)



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

# Read "f_not_false" as "F"
levels(lv_data_frame$structured_targ)[levels(lv_data_frame$structured_targ)=="f_not_false"] <- "F"
levels(lv_data_frame$random_targ)[levels(lv_data_frame$random_targ)=="f_not_false"] <- "F"

# Convert reaction times from milliseconds to seconds
lv_data_frame$l_block_trial_key_resp.rt <- lv_data_frame$l_block_trial_key_resp.rt*1000
lv_data_frame$v_block_trial_key_resp.rt <- lv_data_frame$v_block_trial_key_resp.rt*1000

# Remove extensions from image names
lv_data_frame$image <- gsub (".png", "", lv_data_frame$image, ignore.case=TRUE)
lv_data_frame$image <- gsub (".bmp", "", lv_data_frame$image, ignore.case=TRUE)


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

# Read "f_not_false" as "F"
levels(vl_data_frame$structured_targ)[levels(vl_data_frame$structured_targ)=="f_not_false"] <- "F"
levels(vl_data_frame$random_targ)[levels(vl_data_frame$random_targ)=="f_not_false"] <- "F"

# Convert reaction times from milliseconds to seconds
vl_data_frame$l_block_trial_key_resp.rt <- vl_data_frame$l_block_trial_key_resp.rt*1000
vl_data_frame$v_block_trial_key_resp.rt <- vl_data_frame$v_block_trial_key_resp.rt*1000

# Remove extensions from image names
vl_data_frame$image <- gsub (".png", "", vl_data_frame$image, ignore.case=TRUE)
vl_data_frame$image <- gsub (".bmp", "", vl_data_frame$image, ignore.case=TRUE)


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

# Convert response times to milliseconds
vv_data_frame$v_block_trial_key_resp.rt <- vv_data_frame$v_block_trial_key_resp.rt*1000

# Remove extensions from image names
vv_data_frame$image <- gsub (".png", "", vv_data_frame$image, ignore.case=TRUE)
vv_data_frame$image <- gsub (".bmp", "", vv_data_frame$image, ignore.case=TRUE)



# ******************** CONDITION 1: RANDOM LL*******************


# Separate random condition
random_ll <- ll_data_frame[ which(ll_data_frame$condition== "R"),]


## Index the targets -----------------------------------------------

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

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
# There should be 22 entries
length(rll_line_number$part_id)
# They should all contain 288 lines
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
  this_targ_rt <- random_ll_targets[i,]$l_block_trial_key_resp.rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- random_ll_targets[i,]$this_l_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_ll[which(random_ll$trial_num==this_trial_num-1 & random_ll$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_l_loop
  loop_before <- append(loop_before, preceding_loop) 
  preceding_rt <- this_trial_before$l_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_ll_targets[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_ll_targets[i,][,"l_block_trial_key_resp.rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_block_trial_key_resp.rt"])){
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
  else if (is.na(random_ll_targets[i,] [,"l_block_trial_key_resp.rt"])){
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

# TEST: This should be equal to 22
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
  mean_rt <- append(mean_rt, round(mean(random_ll_extracted$rt_col[random_ll_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_ll_extracted$rt_col[random_ll_extracted$id==id]~random_ll_extracted$targ_index[random_ll_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_ll_extracted[ which(random_ll_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rll <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)


# ******************** CONDITION 2: RANDOM LV *******************


# Separate random and structured conditions
random_lv <- lv_data_frame[ which(lv_data_frame$condition== "R"),]


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
# There should be 26 entries
length(rlv_line_number$part_id)
# They should all contain 288 lines
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
  this_targ_rt <- random_lv_targets[i,]$v_block_trial_key_resp.rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- random_lv_targets[i,]$v_block_trials.thistrialn
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_lv[which(random_lv$trialnum==this_trial_num-1 & random_lv$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trialnum
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$v_block_trials.thistrialn
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, folvowing_loop)
  preceding_rt <- this_trial_before$v_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_lv_targets[i,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_lv_targets[i,][,"v_block_trial_key_resp.rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["v_block_trial_key_resp.rt"])){
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
  else if (is.na(random_lv_targets[i,] [,"v_block_trial_key_resp.rt"])){
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

# TEST: This should be equal to 26
length (target_sum)
# TEST: This should contain a vector full of 24s
target_sum

# Add the targets' indices
random_lv_extracted$targ_index <- targ_index

# Remove any values of NA
random_lv_extracted <- random_lv_extracted[!is.na(random_lv_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

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

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "lv")
  type <- append (type, "random")
  same_or_diff <- append (same_or_diff, "different")
  test_phase <- append (test_phase, "lsl")
  mean_rt <- append(mean_rt, round(mean(random_lv_extracted$rt_col[random_lv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_lv_extracted$rt_col[random_lv_extracted$id==id]~random_lv_extracted$targ_index[random_lv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_lv_extracted[ which(random_lv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rlv <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)



# ******************** CONDITION 3: RANDOM VL*******************

# Separate random and structured conditions
random_vl <- vl_data_frame[ which(vl_data_frame$condition== "R"),]


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
# There should be 26 entries
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
  this_targ_rt <- random_vl_targets[i,]$l_block_trial_key_resp.rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- random_vl_targets[i,]$l_block_trial_loop.thistrialn
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_vl[which(random_vl$trial_num==this_trial_num-1 & random_vl$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$l_block_trial_loop.thistrialn
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, fovlowing_loop)
  preceding_rt <- this_trial_before$l_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_vl_targets[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_vl_targets[i,][,"l_block_trial_key_resp.rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_block_trial_key_resp.rt"])){
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
  else if (is.na(random_vl_targets[i,] [,"l_block_trial_key_resp.rt"])){
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

# TEST: This should be equal to 26
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
  rt_slope <- append (rt_slope, round(summary(lm(random_vl_extracted$rt_col[random_vl_extracted$id==id]~random_vl_extracted$targ_index[random_vl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vl_extracted[ which(random_vl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rvl <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rvl_rt_slope <- mean (rvl$rt_slope)



# ******************** CONDITION 4: RANDOM VV *******************

# Separate random and structured conditions
random_vv <- vv_data_frame[ which(vv_data_frame$condition== "R"),]


# Index the targets -----------------------------------------------

# Identify the rows when this condition's target was presented
random_vv_targets <- random_vv[which(random_vv$second_targ==random_vv$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(random_vv_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(random_vv_targets[which(random_vv$part_id==id),]))
}
rvv_line_number <- data.frame(part_id, total_lines)
# There should be 22 entries
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
random_vv_targets <- random_vv[which(random_vv$second_targ==random_vv$image),]

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
  this_targ_rt <- random_vv_targets[i,]$v_block_trial_key_resp.rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- random_vv_targets[i,]$v_block_trials.thistrialn
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_vv[which(random_vv$trial_num==this_trial_num-1 & random_vv$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$v_block_trials.thistrialn
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, fovvowing_loop)
  preceding_rt <- this_trial_before$v_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_vv_targets[i,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_vv_targets[i,][,"v_block_trial_key_resp.rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["v_block_trial_key_resp.rt"])){
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
  else if (is.na(random_vv_targets[i,] [,"v_block_trial_key_resp.rt"])){
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

# TEST: This should be equal to 22
length (target_sum)
# TEST: This should contain a vector full of 24s
target_sum

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
random_vv_extracted$targ_index <- targ_index

# Remove any values of NA. We do this a second time here to remove any participants who did not respond during the trial.
random_vv_extracted <- random_vv_extracted[!is.na(random_vv_extracted$rt_col),]

# List unique participant IDs for this condition
extracted_part_id <- unique(random_vv_extracted$id)

# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

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

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "vv")
  type <- append (type, "random")
  same_or_diff <- append (same_or_diff, "same")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(random_vv_extracted$rt_col[random_vv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_vv_extracted$rt_col[random_vv_extracted$id==id]~random_vv_extracted$targ_index[random_vv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vv_extracted[ which(random_vv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rvv <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)



# ******************** CONDITION 5: STRUCTURED LL*******************

# Separate random and structured conditions
structured_ll <- ll_data_frame[ which(ll_data_frame$condition== "S"),]

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
# There should be 22 entries
length(sll_line_number$part_id)
# They should all contain 288 lines
sll_line_number$total_lines


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------


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
  this_targ_rt <- structured_ll_targets[i,]$l_block_trial_key_resp.rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- structured_ll_targets[i,]$this_l_loop
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_ll[which(structured_ll$trial_num==this_trial_num-1 & structured_ll$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_l_loop
  loop_before <- append(loop_before, preceding_loop) 
  preceding_rt <- this_trial_before$l_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_ll_targets[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_ll_targets[i,][,"l_block_trial_key_resp.rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_block_trial_key_resp.rt"])){
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
  else if (is.na(structured_ll_targets[i,] [,"l_block_trial_key_resp.rt"])){
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

# TO TEST: This should be 22
length(target_sum)
# This should all contain values of 24
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
  rt_slope <- append (rt_slope, round(summary(lm(structured_ll_extracted$rt_col[structured_ll_extracted$id==id]~structured_ll_extracted$targ_index[structured_ll_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_ll_extracted[ which(structured_ll_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
sll <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# TEST: find mean rt_slope
mean_sll_rt_slope <- mean (sll$rt_slope)
# This should be negative
# ATTN AN: Can you tell why this is positive? An error in my code anywhere?
mean_sll_rt_slope


# ******************** CONDITION 6: lv structured*******************

# Separate structured and structured conditions
structured_lv <- lv_data_frame[ which(lv_data_frame$condition== "S"),]

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
# There should be 26 entries
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
  this_targ_rt <- structured_lv_targets[i,]$l_block_trial_key_resp.rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- structured_lv_targets[i,]$l_block_trial_loop.thistrialn
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_lv[which(structured_lv$trialnum==this_trial_num-1 & structured_lv$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trialnum
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$l_block_trial_loop.thistrialn
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, folvowing_loop)
  preceding_rt <- this_trial_before$l_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_lv_targets[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_lv_targets[i,][,"l_block_trial_key_resp.rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_block_trial_key_resp.rt"])){
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
  else if (is.na(structured_lv_targets[i,] [,"l_block_trial_key_resp.rt"])){
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

# TEST: This should be equal to 26
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
  rt_slope <- append (rt_slope, round(summary(lm(structured_lv_extracted$rt_col[structured_lv_extracted$id==id]~structured_lv_extracted$targ_index[structured_lv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_lv_extracted[ which(structured_lv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
slv <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# TEST: find mean rt_slope
mean_slv_rt_slope <- mean (slv$rt_slope)
# It should be negative
mean_slv_rt_slope


# ******************** CONDITION 7: vl structured*******************

# Separate structured and structured conditions
structured_vl <- vl_data_frame[ which(vl_data_frame$condition== "S"),]

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
# There should be 26 entries
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
  this_targ_rt <- structured_vl_targets[i,]$v_block_trial_key_resp.rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- structured_vl_targets[i,]$v_block_trials.thistrialn
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_vl[which(structured_vl$trial_num==this_trial_num-1 & structured_vl$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the preceding row's this_v_loop value.
  preceding_loop <- this_trial_before$v_block_trials.thistrialn
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, fovlowing_loop)
  preceding_rt <- this_trial_before$v_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_vl_targets[i,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_vl_targets[i,][,"v_block_trial_key_resp.rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["v_block_trial_key_resp.rt"])){
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
  else if (is.na(structured_vl_targets[i,] [,"v_block_trial_key_resp.rt"])){
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

# TEST: This should be equal to 26
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

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "vl")
  type <- append (type, "structured")
  same_or_diff <- append (same_or_diff, "different")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(structured_vl_extracted$rt_col[structured_vl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vl_extracted$rt_col[structured_vl_extracted$id==id]~structured_vl_extracted$targ_index[structured_vl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_vl_extracted[ which(structured_vl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
svl <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_svl_rt_slope <- mean (slv$rt_slope)

# TEST: find mean rt_slope
mean_svl_rt_slope <- mean (svl$rt_slope)
# It should be negative
mean_svl_rt_slope

# ******************** CONDITION 8: STRUCTURED VV *******************

# Separate structured and structured conditions
structured_vv <- vv_data_frame[ which(vv_data_frame$condition== "S"),]

# Identify the rows when this condition's target was presented
structured_vv_targets <- structured_vv[which(structured_vv$first_targ==structured_vv$image),]

# TEST: Create a data frame to check the number of lines per participant
list_part_id <- unique(structured_vv_targets$part_id)
part_id <- NULL
total_lines <- NULL
for(id in list_part_id){
  part_id <- append(part_id, id)
  total_lines <- append(total_lines, nrow(structured_vv_targets[which(structured_vv$part_id==id),]))
}
svv_line_number <- data.frame(part_id, total_lines)
# There should be 22 entries
length(svv_line_number$part_id)
# They should all contain 288 lines
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
  this_targ_rt <- structured_vv_targets[i,]$v_block_trial_key_resp.rt
  target_rt <- append(target_rt, paste(this_targ_rt))
  # Isolate the loop value
  this_loop <- structured_vv_targets[i,]$v_block_trials.thistrialn
  loop <- append (loop, this_loop)
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_vv[which(structured_vv$trial_num==this_trial_num-1 & structured_vv$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$v_block_trials.thistrialn
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, fovvowing_loop)
  preceding_rt <- this_trial_before$v_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_vv_targets[i,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_vv_targets[i,][,"v_block_trial_key_resp.rt"])
  }
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["v_block_trial_key_resp.rt"])){
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
  else if (is.na(structured_vv_targets[i,] [,"v_block_trial_key_resp.rt"])){
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

# TEST: This should be equal to 26
length (target_sum)
# TEST: This should contain a vector full of 24s
# ATTN AN: There are only 20 targets for each? Is this part of the design?
target_sum

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
structured_vv_extracted$targ_index <- targ_index

# Remove any values of NA
structured_vv_extracted <- structured_vv_extracted[!is.na(structured_vv_extracted$rt_col),]

#TO DO: Where are 10's response times? In any case, here we remove participants with no rts at all
# List unique participant IDs for this condition
extracted_part_id <- unique(structured_vv_extracted$id)

# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

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

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "vv")
  type <- append (type, "structured")
  same_or_diff <- append (same_or_diff, "same")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(structured_vv_extracted$rt_col[structured_vv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vv_extracted$rt_col[structured_vv_extracted$id==id]~structured_vv_extracted$targ_index[structured_vv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_vv_extracted[ which(structured_vv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
svv <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# TEST: find mean rt_slope
mean_svv_rt_slope <- mean (svv$rt_slope)
# It should be negative
mean_svv_rt_slope

# Bind conditions together--------------------------------------------------------------------------------------------------------------------------------------------------

# Bind conditions
indiv_rt_slope<- data.frame(rbind(rll, rlv, rvl, rvv, sll, slv, svl, svv))

# Summarize rt_slope
indiv_rt_slope_wide <- cast(indiv_rt, part_id ~ task, mean, value = 'rt_slope')
indiv_rt_slope_wide<- merge(indiv_rt_slope_wide, picture_vocab, by = "part_id", all=TRUE)
indiv_rt_slope_wide <- cbind(indiv_rt_slope_wide, "same_or_diff")
colnames(indiv_rt_slope_wide)[9] <- "same_or_diff"
all_same <- indiv_rt_slope_wide[ which(indiv_rt_slope_wide$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- indiv_rt_slope_wide[ which(indiv_rt_slope_wide$lv>0), ]
all_diff$same_or_diff <- ("different")
indiv_rt_slope_wide <- rbind(all_same, all_diff)
write.csv(indiv_rt_slope, "sit_rt_slope_indiv.csv")

# Summarize mean_rt
indiv_rt_wide <- cast(indiv_rt, part_id ~ task, mean, value = 'mean_rt')
indiv_rt_wide<- merge(indiv_rt_wide, picture_vocab, by = "part_id", all=TRUE)
indiv_rt_wide <- cbind(indiv_rt_wide, "same_or_diff")
colnames(indiv_rt_wide)[9] <- "same_or_diff"
all_same <- indiv_rt_wide[ which(indiv_rt_wide$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- indiv_rt_wide[ which(indiv_rt_wide$lv>0), ]
all_diff$same_or_diff <- ("different")
indiv_rt_wide <- rbind(all_same, all_diff)
write.csv(indiv_rt, "sit_mean_rt_indiv.csv")


# Find group-level mean accuracy accross tasks------------------------------------------------------------------------------------

group_rt_slope <- NULL
mean_struct_rt_slope <- NULL
mean_rand_rt_slope <- NULL
task <- NULL
mean_struct_rt <- NULL
mean_rand_rt <- NULL

# Find mean ll rt slope across participants
task <- append (task, paste ("ll"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "ll"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "ll"), ]$rt_slope), digits =3))
mean_struct_rt <- append(mean_struct_rt, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                    & indiv_rt$task== "ll"), ]$mean_rt), digits =3))
mean_rand_rt <- append(mean_rand_rt, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                & indiv_rt$task== "ll"), ]$mean_rt), digits =3))

# Find mean lv rt slope across participants
task <- append (task, paste ("lv"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "lv"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "lv"), ]$rt_slope), digits =3))
mean_struct_rt <- append(mean_struct_rt, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                    & indiv_rt$task== "lv"), ]$mean_rt), digits =3))
mean_rand_rt <- append(mean_rand_rt, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                & indiv_rt$task== "lv"), ]$mean_rt), digits =3))


# Find mean vl rt slope across participants
task <- append (task, paste ("vl"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "vl"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "vl"), ]$rt_slope), digits =3))
mean_struct_rt <- append(mean_struct_rt, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                    & indiv_rt$task== "vl"), ]$mean_rt), digits =3))
mean_rand_rt <- append(mean_rand_rt, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                & indiv_rt$task== "vl"), ]$mean_rt), digits =3))


# Find mean vv rt slope across participants
task <- append (task, paste ("vv"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "vv"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "vv"), ]$rt_slope), digits =3))
mean_struct_rt <- append(mean_struct_rt, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                    & indiv_rt$task== "vv"), ]$mean_rt), digits =3))
mean_rand_rt <- append(mean_rand_rt, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                & indiv_rt$task== "vv"), ]$mean_rt), digits =3))


# Combine group accuracies into one data frame
group_accuracy <- data.frame(cbind(task, mean_rand_rt_slope, mean_struct_rt_slope, mean_struct_rt, mean_rand_rt))


write.csv(group_accuracy, "sit_rt_slope_group.csv")





# ************************** ANALYSES ************************

# TO DO: Repeat after duplicates are removed!
# test whether in each condition rt slope was significantly different from zero.
t.test(sll$rt_slope,mu=0) # n.s.
t.test(slv$rt_slope,mu=0) # n.s.
t.test(svl$rt_slope,mu=0) # p-value: 0.04
t.test(svv$rt_slope,mu=0) # marginal t

# ATTN AN: Is this correct to see if there is a difference in score by same/ different conditions?
t.test(score~same_or_diff, data=indiv_rt_slope_wide)
t.test(score~same_or_diff, data=indiv_rt_wide)


# TO DO: Repeat for Mean RT
# TO DO: Remove any participants without both vsl/lsl test and both types
# TO DO : Makes sure that all cells show 1
cast(indiv_rt,part_id~test_phase+type,value="rt_slope",length)
m2 = aov(rt_slope~test_phase*same_or_diff*type+Error(part_id/(test_phase*type)), data = indiv_rt)
summary(m2)
# F(1,41) = 5.20, p = 0.028


# Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------

#TO DO : Remove participants with no vocab scores

# TO DO: Repeat for mean RT and accuracy
corr_data <- cast(indiv_rt, part_id ~ task, mean, value = 'rt_slope')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)

same_corr <- corr_data[ which(!is.na(corr_data$ll)), ]
same_corr <- same_corr[, c(2, 5, 6)]
diff_corr <- corr_data[ which(!is.na(corr_data$lv)), ]
diff_corr <- diff_corr[, c(3, 4, 6)]
same_corr$vv<-as.numeric(same_corr$vv)

# TO DO: Double check diff_corr

diff <- cor(diff_corr, method = c("pearson"),use="pairwise.complete.obs")
cor.test(diff_corr$lv,diff_corr$score)
# lv          vl       score
# lv     1.0000000 -0.19246082 -0.49248148
# vl    -0.1924608  1.00000000  0.02885029
# score -0.4924815  0.02885029  1.00000000

# Interpretation: for people who show sharpest rt_slope during online learning of ling sl info 
# Embedded in random nonling info show highest vocab score

# Pearson's product-moment correlation
# 
# data:  diff_corr$lv and diff_corr$score
# t = -2.1916, df = 15, p-value = 0.04461
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
# -0.78686783 -0.01550746
# sample estimates:
# cor 
# -0.4924815 

plot(diff_corr$lv,diff_corr$score)

same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")
# ll        vv      score
# ll     1.0000000 0.3660493 -0.1269438
# vv     0.3660493 1.0000000  0.2274042
# score -0.1269438 0.2274042  1.0000000
# n.s.

#For future: only include significant (some documentation of corrplot)
same_plot <- corrplot(same, method="circle")
diff_plot <- corrplot(diff, method="circle")






# ATTN. AN: Is this correct for these correlation matrices?

corr_data <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'mean_rt')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)

same_corr <- corr_data[ which(!is.na(corr_data$ll)), ]
same_corr <- same_corr[, c(2, 5, 6)]
diff_corr <- corr_data[ which(!is.na(corr_data$lv)), ]
diff_corr <- diff_corr[, c(3, 4, 6)]
same_corr$vv<-as.numeric(same_corr$vv)

diff <- cor(diff_corr, method = c("pearson"),use="pairwise.complete.obs")
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")


task <- NULL
condition <- NULL
mean_rt <- NULL

# Find mean ll rt across participants
task <- append (task, "ll")
condition <- append (condition, "structured")
mean_rt <- append(mean_rt, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                      & indiv_rt$task== "ll"), ]$mean_rt), digits =3))
task <- append (task, "ll")
condition <- append (condition, "random")
mean_rt <- append(mean_rt, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                      & indiv_rt$task== "ll"), ]$mean_rt), digits =3))

# Find mean lv rt across participants
task <- append (task, "lv")
condition <- append (condition, "structured")
mean_rt <- append(mean_rt, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                      & indiv_rt$task== "lv"), ]$mean_rt), digits =3))
task <- append (task, "lv")
condition <- append (condition, "random")
mean_rt <- append(mean_rt, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                      & indiv_rt$task== "lv"), ]$mean_rt), digits =3))

# Find mean vl rt across participants
task <- append (task, "vl")
condition <- append (condition, "structured")
mean_rt <- append(mean_rt, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                      & indiv_rt$task== "vl"), ]$mean_rt), digits =3))
task <- append (task, "vl")
condition <- append (condition, "random")
mean_rt <- append(mean_rt, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                      & indiv_rt$task== "vl"), ]$mean_rt), digits =3))

# Find mean vv rt across participants
task <- append (task, "vv")
condition <- append (condition, "structured")
mean_rt <- append(mean_rt, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                      & indiv_rt$task== "vv"), ]$mean_rt), digits =3))
task <- append (task, "vv")
condition <- append (condition, "random")
mean_rt <- append(mean_rt, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                      & indiv_rt$task== "vv"), ]$mean_rt), digits =3))


# Combine group accuracies into one data frame
mean_rt_df <- data.frame(cbind(task, condition, mean_rt))


write.csv(mean_rt_df, "sit_mean_rt_df.csv")


table_data <- read.csv(file='sit_mean_rt_df.csv',sep=',',header=T)
test_table <- table(table_data$task, table_data$condition, table_data$mean_rt)
means <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
        xlab="Number of Gears", col=c("darkblue","red"),
        legend = rownames(counts), beside=TRUE)





table_data <- read.csv(file='sit_rt_slope_indiv.csv',sep=',',header=T)
myvars <- c("task", "type", "mean_rt")
mini_data <- table_data[myvars]
#we could also aggregate on time and diet
testy<-head(aggregate(mini_data$mean_rt,
                      list(type_1 = mini_data$type, task_1 = mini_data$task),
                      mean
)
)
testy_bar<-barplot(t(as.matrix((data.frame(testy)))))



# Grouped Bar Plot
testy_2<-barplot(testy, main="Mean RT by Task and Type",
                 xlab="Task", col=c("darkblue","red"),
                 legend = rownames(testy), beside=TRUE)

# Grouped Bar Plot
counts <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
        xlab="Number of Gears", col=c("darkblue","red"),
        legend = rownames(counts), beside=TRUE)



# aggregate data frame mtcars by cyl and vs, returning means
# for numeric variables
attach(mtcars)
aggdata <-aggregate(mtcars, by=list(cyl,vs), 
                    FUN=mean, na.rm=TRUE)
print(aggdata)
detach(mtcars)


test_table <- aggregate(table_data$task, table_data$type, table_data$mean_rt)
means <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
        xlab="Number of Gears", col=c("darkblue","red"),
        legend = rownames(counts), beside=TRUE)








# Grouped Bar Plot
counts <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
        xlab="Number of Gears", col=c("darkblue","red"),
        legend = rownames(counts), beside=TRUE)




# combine rt columns for lv and vl df$x <- paste(df$n,df$s)









