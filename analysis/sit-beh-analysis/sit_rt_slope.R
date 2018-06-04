#  SIT Reaction Time Analysis
#  Violet Kozloff
#  May 8, 2018
#  This script analyzes mean reaction time and reaction time slope for statistical learning tasks involving structured and random triplets of letters and images
#  NOTE: relevant columns have been pre-selected through sit_cleaning.R
#  NOTE: Excludes any trials where participant did not respond at all to the target or responded to a different target
#  NOTE: Currently excludes sit_a_010 from analysis from line 1679 on, because they do not have any rt data for one of the files

# ******************** I. PREPARE FILES *************************


# Prepare workspace ------------------------------------------------------------------------------------------------------

# Install packages
install.packages("reshape")
install.packages("dplyr")
install.packages("corrplot")
library("reshape")
library("dplyr")
library("corrplot")

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
ll_data_frame$l_rt<-ll_data_frame$l_rt*1000

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
lv_data_frame$l_rt <- lv_data_frame$l_rt*1000
lv_data_frame$v_rt <- lv_data_frame$v_rt*1000

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
vl_data_frame$l_rt <- vl_data_frame$l_rt*1000
vl_data_frame$v_rt <- vl_data_frame$v_rt*1000

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
vv_data_frame$v_rt <- vv_data_frame$v_rt*1000

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
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  range <- append (range, (this_range[2]-this_range[1]))
}

# Combine data for each participant
rll <- data.frame(part_id, task, same_or_diff, test_phase, domain, type, mean_rt, range, upper_bound, lower_bound, rt_slope) 

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
  domain <- append(domain, "non-linguistic")
  task <- append(task, "lv")
  type <- append (type, "random")
  same_or_diff <- append (same_or_diff, "different")
  test_phase <- append (test_phase, "lsl")
  mean_rt <- append(mean_rt, round(mean(random_lv_extracted$rt_col[random_lv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_lv_extracted$rt_col[random_lv_extracted$id==id]~random_lv_extracted$targ_index[random_lv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_lv_extracted[ which(random_lv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
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
  range <- append (range, (this_range[2]-this_range[1]))
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
  domain <- append(domain, "non-linguistic")
  task <- append(task, "vv")
  type <- append (type, "random")
  same_or_diff <- append (same_or_diff, "same")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(random_vv_extracted$rt_col[random_vv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_vv_extracted$rt_col[random_vv_extracted$id==id]~random_vv_extracted$targ_index[random_vv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vv_extracted[ which(random_vv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
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
  range <- append (range, (this_range[2]-this_range[1]))
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
sll <- data.frame(part_id, task, same_or_diff, test_phase, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# TEST: find mean rt_slope
mean_sll_rt_slope <- mean (sll$rt_slope)
# This should be negative
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
  range <- append (range, (this_range[2]-this_range[1]))
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
  domain <- append(domain, "non-linguistic")
  task <- append(task, "vl")
  type <- append (type, "structured")
  same_or_diff <- append (same_or_diff, "different")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(structured_vl_extracted$rt_col[structured_vl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vl_extracted$rt_col[structured_vl_extracted$id==id]~structured_vl_extracted$targ_index[structured_vl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_vl_extracted[ which(structured_vl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
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

# TEST: This should be equal to 22
length (target_sum)
# TEST: This should contain a vector full of 24s
target_sum

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
structured_vv_extracted$targ_index <- targ_index

# Remove any values of NA
structured_vv_extracted <- structured_vv_extracted[!is.na(structured_vv_extracted$rt_col),]

# Where are 10's response times are missing; here we remove participants with no rts at all
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
  domain <- append(domain, "non-linguistic")
  task <- append(task, "vv")
  type <- append (type, "structured")
  same_or_diff <- append (same_or_diff, "same")
  test_phase <- append (test_phase, "vsl")
  mean_rt <- append(mean_rt, round(mean(structured_vv_extracted$rt_col[structured_vv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vv_extracted$rt_col[structured_vv_extracted$id==id]~structured_vv_extracted$targ_index[structured_vv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_vv_extracted[ which(structured_vv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, (this_range[2]-this_range[1]))
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
write.csv(indiv_rt_slope_wide, "sit_rt_slope_indiv.csv")

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
write.csv(indiv_rt_wide, "sit_mean_rt_indiv.csv")


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
write.csv(group_rt_slope, "sit_rt_slope_group.csv")



# *************************** ANALYSIS 1: TEST EFFECTS OF GROUP, TYPE, AND TEST PHASE *******************


# ANOVA to test effects of type (random/ structured), test phase and group (same/ different) on RT Slope----------------------

# TEST: Make sure that all cells show 1
test_cast <- cast(indiv_rt_slope,part_id~test_phase+type,value="rt_slope",length)

# TO DO: Make this more automatic

# They don't, because sit_a_010 is missing vv data. Remove this participant.
indiv_rt_slope <- indiv_rt_slope[which(indiv_rt_slope$part_id!="sit_a_010"),]
# TEST: Make sure that all cells show 1 now that we have removed this participant
cast(indiv_rt_slope,part_id~test_phase+type,value="rt_slope",length)
# Now they do

# Test the effects of domain
m2 = aov(rt_slope~domain*type*same_or_diff+Error(part_id/domain*type),data =indiv_rt_slope)
summary(m2)
## interpretation: people show sharper decrease of response time in linguistic than in non-linguistic conditions. (or the other way around)
# 
# Error: part_id
# Df Sum Sq Mean Sq F value Pr(>F)
# domain        1    0.4    0.43   0.011  0.916
# same_or_diff  1  105.3  105.33   2.788  0.102
# Residuals    45 1700.3   37.78               
# 
# Error: type
# Df Sum Sq Mean Sq
# type  1  403.7   403.7
# 
# Error: part_id:domain
# Df Sum Sq Mean Sq F value Pr(>F)  
# domain               1  131.1  131.05   6.754 0.0126 *
# domain:same_or_diff  1   36.7   36.67   1.890 0.1760  
# Residuals           45  873.2   19.40                 
# ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Error: part_id:type
# Df Sum Sq Mean Sq F value Pr(>F)
# domain:type        1    5.2    5.24   0.134  0.716
# type:same_or_diff  1   21.5   21.48   0.551  0.462
# Residuals         45 1755.6   39.01               
# 
# Error: part_id:domain:type
# Df Sum Sq Mean Sq F value Pr(>F)
# domain:type               1   33.9   33.94   0.858  0.359
# domain:type:same_or_diff  1    1.2    1.24   0.031  0.860
# Residuals                45 1781.0   39.58 

# ANOVA to test effects of type (random/ structured), test phase and group (same/ different) on mean RT----------------------

# TEST: Make sure that all cells show 1
cast(indiv_rt_slope,part_id~test_phase+type,value="mean_rt",length)

# Test the effects of domain
m4 = aov(mean_rt~domain*type*same_or_diff+Error(part_id/domain*type),data =indiv_rt_slope)
summary(m4)
# Interpretation: marginally larger difference between linguistic and non-linguistic in the different than the same condition (or the other way around).
# Error: part_id
# Df  Sum Sq Mean Sq F value Pr(>F)
# domain        1     649     649   0.016  0.899
# same_or_diff  1     975     975   0.025  0.876
# Residuals    45 1781591   39591               
# 
# Error: type
# Df Sum Sq Mean Sq
# type  1  40639   40639
# 
# Error: part_id:domain
# Df Sum Sq Mean Sq F value Pr(>F)  
# domain               1  26455   26455   2.849 0.0983 .
# domain:same_or_diff  1  26287   26287   2.831 0.0994 .
# Residuals           45 417808    9285                 
# ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Error: part_id:type
# Df Sum Sq Mean Sq F value Pr(>F)
# domain:type        1    580     580   0.063  0.802
# type:same_or_diff  1  18152   18152   1.981  0.166
# Residuals         45 412391    9164               
# 
# Error: part_id:domain:type
# Df Sum Sq Mean Sq F value Pr(>F)
# domain:type               1  11969   11969   1.751  0.192
# domain:type:same_or_diff  1   8617    8617   1.261  0.267
# Residuals                45 307551    6834  

# No longer testing the effects of test_phase
# m5 = aov(mean_rt~test_phase*same_or_diff*type+Error(part_id/(test_phase*type)), data = indiv_rt_slope)


# *************************** ANALYSIS 2: CORRELATION MATRICES **********************************


# RT Slope Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------

# Extract relevant data from indiv_rt_slope and picture_vocab
corr_data <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'rt_slope')
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
# same_corr$vv<-as.numeric(same_corr$vv)

# Create correlation matrices for different condition
diff <- cor(diff_corr, method = c("pearson"),use="pairwise.complete.obs")
diff
#            lv         vl      score
# lv     1.0000000  0.4688697 -0.1291501
# vl     0.4688697  1.0000000 -0.2289698
# score -0.1291501 -0.2289698  1.0000000

# Test p-values of correlation matrices for different condition
lv_corr<-cor.test(diff_corr$lv,diff_corr$score) # n.s.: p-value = 0.6891
vl_corr<-cor.test(diff_corr$vl,diff_corr$score) # n.s.: p-value = 0.4741 

# Create correlation matrices for same condition
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")
same
#            ll          vv       score
# ll     1.0000000  0.39270625 -0.58501755
# vv     0.3927063  1.00000000 -0.01956922
# score -0.5850176 -0.01956922  1.00000000

# Test p-values of correlation matrices for different condition
ll_corr<-cor.test(same_corr$ll, same_corr$score) # n.s.: p-value = 0.05868
ll_corr
vv_corr<-cor.test(same_corr$vv, same_corr$score) # n.s.: p-value = 0.9545
vv_corr

# calculate the difference scores between structured condition and random condition within linguistic and non-linguistic domains.
rt_slope_diff = cast(indiv_rt_slope,part_id+same_or_diff+domain~type,value = "rt_slope")
rt_slope_diff$slope_diff = rt_slope_diff$structured-rt_slope_diff$random
rt_slope_diff = merge(rt_slope_diff,vocab_clean,id=1)
rt_slope_diff = cast(rt_slope_diff,part_id+score+same_or_diff~domain,value="slope_diff")
colnames(rt_slope_diff)[5]="non_linguistic"
rt_slope_diff_same = subset(rt_slope_diff,same_or_diff=="same")
rt_slope_diff_same_complete = rt_slope_diff_same[complete.cases(rt_slope_diff_same),]
cor.test(rt_slope_diff_same_complete$linguistic,rt_slope_diff_same_complete$score,method="pearson") # r = 0.50, one-tailed p = 0.48
cor.test(rt_slope_diff_same_complete$non_linguistic,rt_slope_diff_same_complete$score,method="pearson") # r = 0.08, p = 0.78
#lsl same slope_diff is significantly associated with vocabulary but in the wrong direction.
rt_slope_diff_diff = subset(rt_slope_diff,same_or_diff=="different")
cor.test(rt_slope_diff_diff$linguistic,rt_slope_diff_diff$score,method="pearson") # r = -0.54, one-tailed p = 0.007
cor.test(rt_slope_diff_diff$non_linguistic,rt_slope_diff_diff$score,method="pearson") # r = -0.02, p = 0.46
# lsl diff slope_diff is significantly associated with vocabulary

plot(rt_slope_diff_diff$linguistic,rt_slope_diff_diff$score)

# Mean RT Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------

# Extract relevant data from indiv_rt_slope and picture_vocab
corr_data <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'mean_rt')
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

# Create correlation matrices for different condition
diff <- cor(diff_corr, method = c("pearson"),use="pairwise.complete.obs")
#           lv         vl      score
# lv     1.0000000  0.9127378 -0.1289455
# vl     0.9127378  1.0000000 -0.2700405
# score -0.1289455 -0.2700405  1.0000000

# Test p-values of correlation matrices for different condition
lv_corr<-cor.test(diff_corr$lv,diff_corr$score) # n.s.: p-value = 0.59
vl_corr<-cor.test(diff_corr$vl,diff_corr$score) # n.s.: p-value = 0.2495

# Create correlation matrices for same condition
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")
#          ll         vv      score
# ll     1.0000000  0.8029570 -0.1796982
# vv     0.8029570  1.0000000 -0.2091292
# score -0.1796982 -0.2091292  1.0000000

# Test p-values of correlation matrices for different condition
ll_corr<-cor.test(same_corr$ll, same_corr$score) # n.s.: p-value = 0.052
ll_corr
vv_corr<-cor.test(same_corr$vv, same_corr$score) # n.s.: p-value = 0.45
vv_corr


# calculate the difference scores between structured condition and random condition within linguistic and non-linguistic domains.
# for individual difference analyses
rt_diff = cast(indiv_rt_slope,part_id+same_or_diff+domain~type,value = "mean_rt")
rt_diff$meanrt_diff = rt_diff$structured-rt_diff$random
rt_diff = merge(rt_diff,vocab_clean,id=1)
rt_diff = cast(rt_diff,part_id+score+same_or_diff~domain,value="meanrt_diff")
colnames(rt_diff)[5]="non_linguistic"
rt_diff_same = subset(rt_diff,same_or_diff=="same")
rt_diff_same_complete = rt_diff_same[complete.cases(rt_diff_same),]
cor.test(rt_diff_same_complete$linguistic,rt_diff_same_complete$score,method="pearson")# r = -0.35, one-tailed p = 0.10)
cor.test(rt_diff_same_complete$non_linguistic,rt_diff_same_complete$score,method="pearson")# r = 0.07, one-tailed p = 0.40)

rt_diff_diff = subset(rt_diff,same_or_diff=="different")
cor.test(rt_diff_diff$linguistic,rt_diff_diff$score,method="pearson") # r = 0.03, one-tailed p = 0.45)
cor.test(rt_diff_diff$non_linguistic,rt_diff_diff$score,method="pearson") # r = -0.40, one-tailed p = 0.04
# vsl diff rt_diff is significantly associated with vocabulary 
plot(rt_diff_diff$non_linguistic,rt_diff_diff$score)


#  ************* SEE WHETHER PERFORMANCE WAS ABOVE CHANCE: T-TESTS *************

# Here we remove participant 10 from SVV, because they did not respond in that condition
svv <- indiv_rt_slope[which(svv$part_id!="sit_a_010"),]


# test whether in each condition rt slope was different from zero.
t.test(sll$rt_slope, mu=0) # n.s. p-value = 0.24
t.test(slv$rt_slope, mu=0) # n.s. p-value = 0.23
t.test(svl$rt_slope, mu=0) # n.s. p-value = 0.091
t.test(svv$rt_slope, mu=0) # RESULT: p-value = 0.012

# test whether in each condition rt slope was significantly less than zero.
# ATTN ZQ: Is it useful to include these one-tailed, since we want to see if they are significantly negative?
t.test(sll$rt_slope, alternative="less", mu=0) # n.s. p-value = 0.88
t.test(slv$rt_slope, alternative="less", mu=0) # n.s. p-value = 0.1149
t.test(svl$rt_slope, alternative="less", mu=0) # RESULT: p-value = 0.045
t.test(svv$rt_slope, alternative="less", mu=0) # n.s. p-value = 0.099

