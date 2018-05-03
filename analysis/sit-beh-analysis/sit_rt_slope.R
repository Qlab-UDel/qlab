# TO DO: Also, are we including reaction times for responses during the stimuli preceding/ following for l and v trials?
# TO DO: Remove points outside 2.5 Stdev of mean?
# TO DO: Image index in a way that accounts for different repetitions of S/R blocks. EG: participant A's two R blocks are merged.
# he doesn't respond during the last target of an S block, which is the last stimulus, so we take his reaction time from the
# following stimulus (which is actually the first stimulus of the next S block)
# TO DO: What are all the weird warnings in line 212?
# TO DO: What to do in line 247 if you're in the last line for that participant? Or the last line of that block?
# TO DO: What is 239?
# TO DO: Test 258 condition
# WHAT IS GOING ON IN THIS ROW? WHY IS IT TAKING RT 4 ROWS DOWN??? (id: sit_a_002, trial: 145)
# Why is random_ll taking two rows with this information?? id: sit_a_018 trial: 2
# TO DO: Somewhere this is reading in participant 18's ll data 4 times. Why?
# TO DO: Currently excludes sit_a_010_vv, which is missing the rt column?
# Read "f_not_false" as "F" for everything other than ll, which it already works for




# ******************** I. PREPARE FILES *************************

# Prepare workspace ------------------------------------------------------------------------------------------------------

# Remove objects in environment
rm(list=ls())

# Prepare paths for files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Prepare paths for files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#For use on Mac 
ll_input <- ("../../../sit_data/clean/ll_clean/")
lv_input <- ("../../../sit_data/clean/lv_clean/")
vl_input <- ("../../../sit_data/clean/vl_clean/")
vv_input <- ("../../../sit_data/clean/vv_clean/")

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

# Remove .png from image names
ll_data_frame$image <- gsub (".png", "", ll_data_frame$image, ignore.case=TRUE)


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
#levels(lv_data_frame$structured_targ)[levels(lv_data_frame$structured_targ)=="f_not_false"] <- "F"
#levels(lv_data_frame$random_targ)[levels(lv_data_frame$random_targ)=="f_not_false"] <- "F"

# Remove .png from image names
lv_data_frame$image <- gsub (".png", "", lv_data_frame$image, ignore.case=TRUE)


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
#levels(vl_data_frame$structured_targ)[levels(vl_data_frame$structured_targ)=="f_not_false"] <- "F"
#levels(vl_data_frame$random_targ)[levels(vl_data_frame$random_targ)=="f_not_false"] <- "F"

# Remove .png from image names
vl_data_frame$image <- gsub (".png", "", vl_data_frame$image, ignore.case=TRUE)


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

# Remove .png from image names
vv_data_frame$image <- gsub (".png", "", vv_data_frame$image, ignore.case=TRUE)


# ******************** CONDITION 1: LL*******************

# Separate random and structured conditions
random_ll <- ll_data_frame[ which(ll_data_frame$condition== "R"),]
structured_ll <- ll_data_frame[ which(ll_data_frame$condition== "S"),]

## Index the images by random/ structured-----------------------------------------------

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
#following_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
#following_loop <- NULL
preceding_loop <- NULL
#loop_after <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
#rt_after <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Identify the rows when this condition's target was presented
random_ll_targets <- random_ll[which(random_ll$random_targ==random_ll$image),]
structured_ll_targets <- structured_ll[which(structured_ll$structured_targ==structured_ll$image),]

# TO TEST
#part_2 <- random_ll[which(random_ll$part_id=="sit_a_002"),]
#random_ll_targets <- random_ll_targets[1:250,]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
  # Isolate the row with the following trial for that participant
  #following_trial <- random_ll[which(random_ll$trial_num==this_trial_num+1 & random_ll$part_id==this_id), ]
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- random_ll[which(random_ll$trial_num==this_trial_num-1 & random_ll$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the following row's this_l_loop value.
  #following_loop <- following_trial$this_l_loop
  #loop_after <- append(loop_after, following_loop) 
    # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_l_loop
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, following_loop)
  preceding_rt <- this_trial_before$l_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(random_ll_targets[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_ll_targets[i,][,"l_block_trial_key_resp.rt"])
  }
#  # If the participant responded during the stimulus following the target (implies that we are not in the last row, which would not have a following row)
 # else if (!is.na(following_trial["l_block_trial_key_resp.rt"])){
  #  # And the following line is from the same block
   # if (following_loop==this_loop+1){
    #  # Take the rt from the following line
     # following_rt <- following_trial$l_block_trial_key_resp.rt
      #rt_after <- append (rt_after, following_rt)
      ## And add the duration that the target stimulus was presented (1000 ms)
      ##rt_col <- append (rt_col, .1+following_rt)}}
      #rt_col <- append (rt_col, "test_2")
      #preceding_rt <- "case 2"
      #rt_before <- append (rt_before, preceding_rt)}}
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_block_trial_key_resp.rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "ll")
  type <- append (type, "random")
  mean_rt <- append(mean_rt, round(mean(random_ll_extracted$rt_col[random_ll_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_ll_extracted$rt_col[random_ll_extracted$id==id]~random_ll_extracted$targ_index[random_ll_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_ll_extracted[ which(random_ll_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rll <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rll_rt_slope <- mean (rll$rt_slope)


# ******************** CONDITION 2: lv Random*******************

# Separate random and structured conditions
random_lv <- lv_data_frame[ which(lv_data_frame$condition== "R"),]
structured_lv <- lv_data_frame[ which(lv_data_frame$condition== "S"),]

## Index the images by random/ structured-----------------------------------------------

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

# Identify the rows when this condition's target was presented
random_lv_targets <- random_lv[which(random_lv$random_targ==random_lv$image),]
structured_lv_targets <- structured_lv[which(structured_lv$structured_targ==structured_lv$image),]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "lv")
  type <- append (type, "random")
  mean_rt <- append(mean_rt, round(mean(random_lv_extracted$rt_col[random_lv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_lv_extracted$rt_col[random_lv_extracted$id==id]~random_lv_extracted$targ_index[random_lv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_lv_extracted[ which(random_lv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rlv <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rlv_rt_slope <- mean (rlv$rt_slope)



# ******************** CONDITION 3: vl Random*******************

# Separate random and structured conditions
random_vl <- vl_data_frame[ which(vl_data_frame$condition== "R"),]
structured_vl <- vl_data_frame[ which(vl_data_frame$condition== "S"),]

## Index the images by random/ structured-----------------------------------------------

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
structured_vl_targets <- structured_vl[which(structured_vl$structured_targ==structured_vl$image),]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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
  mean_rt <- append(mean_rt, round(mean(random_vl_extracted$rt_col[random_vl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_vl_extracted$rt_col[random_vl_extracted$id==id]~random_vl_extracted$targ_index[random_vl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vl_extracted[ which(random_vl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rvl <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rvl_rt_slope <- mean (rvl$rt_slope)

# ******************** CONDITION 3: vl Random*******************

# Separate random and structured conditions
random_vl <- vl_data_frame[ which(vl_data_frame$condition== "R"),]
structured_vl <- vl_data_frame[ which(vl_data_frame$condition== "S"),]

## Index the images by random/ structured-----------------------------------------------

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
structured_vl_targets <- structured_vl[which(structured_vl$structured_targ==structured_vl$image),]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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
  mean_rt <- append(mean_rt, round(mean(random_vl_extracted$rt_col[random_vl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_vl_extracted$rt_col[random_vl_extracted$id==id]~random_vl_extracted$targ_index[random_vl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vl_extracted[ which(random_vl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rvl <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rvl_rt_slope <- mean (rvl$rt_slope)

# ******************** CONDITION 4: vv Random*******************

# Separate random and structured conditions
random_vv <- vv_data_frame[ which(vv_data_frame$condition== "R"),]
structured_vv <- vv_data_frame[ which(vv_data_frame$condition== "S"),]

## Index the images by random/ structured-----------------------------------------------

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
structured_vv_targets <- structured_vv[which(structured_vv$first_targ==structured_vv$image),]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
random_vv_extracted$targ_index <- targ_index

# Remove any values of NA
random_vv_extracted <- random_vv_extracted[!is.na(random_vv_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
rvv<- NULL
domain <- NULL
range <- NULL
upper_bound <- NULL
lower_bound <- NULL
this_range <- NULL

#TO DO: Replace this
extracted_part_id <- extracted_part_id[-5]

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "vv")
  type <- append (type, "random")
  mean_rt <- append(mean_rt, round(mean(random_vv_extracted$rt_col[random_vv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_vv_extracted$rt_col[random_vv_extracted$id==id]~random_vv_extracted$targ_index[random_vv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vv_extracted[ which(random_vv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rvv <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rvv_rt_slope <- mean (rvv$rt_slope)


















# ******************** CONDITION 1: structured LL*******************

# Separate structured and structured conditions
structured_ll <- ll_data_frame[ which(ll_data_frame$condition== "S"),]

## Index the images by structured/ structured-----------------------------------------------

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
target_rt <- NULL
#following_rt <- NULL
preceding_rt <- NULL
id <- NULL
trial <-NULL
this_id <- NULL
this_trial_num <- NULL
this_loop <- NULL
loop <- NULL
#following_loop <- NULL
preceding_loop <- NULL
#loop_after <- NULL
loop_before <- NULL
this_targ_rt <- NULL
rt_before <- NULL
#rt_after <- NULL
case <- NULL
this_trial_before <- NULL
this_trial_num_before <- NULL
trial_before_df <- NULL
trial_num_before <- NULL

# Identify the rows when this condition's target was presented
structured_ll_targets <- structured_ll[which(structured_ll$structured_targ==structured_ll$image),]

# TO TEST
#part_2 <- structured_ll[which(structured_ll$part_id=="sit_a_002"),]
#structured_ll_targets <- structured_ll_targets[1:250,]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
  # Isolate the row with the following trial for that participant
  #following_trial <- structured_ll[which(structured_ll$trial_num==this_trial_num+1 & structured_ll$part_id==this_id), ]
  # Isolate the row with the preceding trial for that participant
  this_trial_before <- structured_ll[which(structured_ll$trial_num==this_trial_num-1 & structured_ll$part_id==this_id), ][1,]
  trial_before_df <- rbind (this_trial_before, this_trial_before)
  this_trial_num_before <- this_trial_before$trial_num
  trial_num_before <- append (trial_num_before, this_trial_num)
  # Isolate the following row's this_l_loop value.
  #following_loop <- following_trial$this_l_loop
  #loop_after <- append(loop_after, following_loop) 
  # Isolate the preceding row's this_l_loop value.
  preceding_loop <- this_trial_before$this_l_loop
  loop_before <- append(loop_before, preceding_loop) 
  #loop_after <- append (loop_after, following_loop)
  preceding_rt <- this_trial_before$l_block_trial_key_resp.rt
  rt_before <- append (rt_before, preceding_rt)
  # If the participant responded while the target was presented
  if (!is.na(structured_ll_targets[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, structured_ll_targets[i,][,"l_block_trial_key_resp.rt"])
  }
  #  # If the participant responded during the stimulus following the target (implies that we are not in the last row, which would not have a following row)
  # else if (!is.na(following_trial["l_block_trial_key_resp.rt"])){
  #  # And the following line is from the same block
  # if (following_loop==this_loop+1){
  #  # Take the rt from the following line
  # following_rt <- following_trial$l_block_trial_key_resp.rt
  #rt_after <- append (rt_after, following_rt)
  ## And add the duration that the target stimulus was presented (1000 ms)
  ##rt_col <- append (rt_col, .1+following_rt)}}
  #rt_col <- append (rt_col, "test_2")
  #preceding_rt <- "case 2"
  #rt_before <- append (rt_before, preceding_rt)}}
  # If the participant responded during the stimulus preceding the target (implies that we are not in the first row, which would not have a preceding row)
  else if (!is.na(this_trial_before["l_block_trial_key_resp.rt"])){
    # And the preceding line is from the same block
    if (preceding_loop==this_loop-1){
      # Take the rt from the preceding line and subtract it from 0, to determine how far in advance they responded
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
structured_ll_extracted$targ_index <- targ_index

# Remove any values of NA
structured_ll_extracted <- structured_ll_extracted[!is.na(structured_ll_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
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
  mean_rt <- append(mean_rt, round(mean(structured_ll_extracted$rt_col[structured_ll_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_ll_extracted$rt_col[structured_ll_extracted$id==id]~structured_ll_extracted$targ_index[structured_ll_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_ll_extracted[ which(structured_ll_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
sll <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_sll_rt_slope <- mean (sll$rt_slope)


# ******************** CONDITION 2: lv structured*******************

# Separate structured and structured conditions
structured_lv <- lv_data_frame[ which(lv_data_frame$condition== "S"),]

## Index the images by structured/ structured-----------------------------------------------

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

# Identify the rows when this condition's target was presented
structured_lv_targets <- structured_lv[which(structured_lv$structured_targ==structured_lv$image),]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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
  mean_rt <- append(mean_rt, round(mean(structured_lv_extracted$rt_col[structured_lv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_lv_extracted$rt_col[structured_lv_extracted$id==id]~structured_lv_extracted$targ_index[structured_lv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_lv_extracted[ which(structured_lv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
slv <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_slv_rt_slope <- mean (slv$rt_slope)



# ******************** CONDITION 3: vl structured*******************

# Separate structured and structured conditions
structured_vl <- vl_data_frame[ which(vl_data_frame$condition== "S"),]

## Index the images by structured/ structured-----------------------------------------------

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
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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
  mean_rt <- append(mean_rt, round(mean(structured_vl_extracted$rt_col[structured_vl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vl_extracted$rt_col[structured_vl_extracted$id==id]~structured_vl_extracted$targ_index[structured_vl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_vl_extracted[ which(structured_vl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
svl <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_svl_rt_slope <- mean (slv$rt_slope)


# ******************** CONDITION 4: vv structured*******************

# Separate structured and structured conditions
structured_vv <- vv_data_frame[ which(vv_data_frame$condition== "S"),]

## Index the images by structured/ structured-----------------------------------------------

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
structured_vv_targets <- structured_vv[which(structured_vv$second_targ==structured_vv$image),]
structured_vv_targets <- structured_vv[which(structured_vv$first_targ==structured_vv$image),]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
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
      rt_col <- append (rt_col, 0-(1-preceding_rt))
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

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {targ_index <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
structured_vv_extracted$targ_index <- targ_index

# Remove any values of NA
structured_vv_extracted <- structured_vv_extracted[!is.na(structured_vv_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
type <- NULL
task<- NULL
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
  mean_rt <- append(mean_rt, round(mean(structured_vv_extracted$rt_col[structured_vv_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vv_extracted$rt_col[structured_vv_extracted$id==id]~structured_vv_extracted$targ_index[structured_vv_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_vv_extracted[ which(structured_vv_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  range <- append (range, this_range)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

#TO DO: only 2 part ids?? why??

# Combine data for each participant
svv <- data.frame(part_id, task, domain,type,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_svv_rt_slope <- mean (rvv$rt_slope)












# Bind conditions together--------------------------------------------------------------------------------------------------------------------------------------------------

# Bind visual cconditions
indiv_rt<- rbind(rll, rlv, rvl, rvv, sll, slv, svl, svv)

write.csv(indiv_rt, "sit_rt_slope_indiv.csv")


# Find group-level mean accuracy accross tasks------------------------------------------------------------------------------------

group_rt_slope <- NULL
mean_struct_rt_slope <- NULL
mean_rand_rt_slope <- NULL
task <- NULL

# Find mean ll accuracy across participants
task <- append (task, paste ("ll"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "ll"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "ll"), ]$rt_slope), digits =3))

# Find mean lv accuracy across participants
task <- append (task, paste ("lv"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "lv"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "lv"), ]$rt_slope), digits =3))

# Find mean vl accuracy across participants
task <- append (task, paste ("vl"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "vl"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "vl"), ]$rt_slope), digits =3))

# Find mean vv accuracy across participants
task <- append (task, paste ("vv"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "vv"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "vv"), ]$rt_slope), digits =3))

# Combine group accuracies into one data frame
group_accuracy <- data.frame(cbind(task, mean_rand_rt_slope, mean_struct_rt_slope))


write.csv(group_accuracy, "sit_rt_slope_group.csv")






















# combine rt columns for lv and vl df$x <- paste(df$n,df$s)



