#  NOVEMBER PILOT RT SLOPE ANALYSIS
#  Violet Kozloff
#  April 7, 2017
#  This script analyzes structured and random blocks across four tasks: auditory (speech and tones) and visual (letters and images).
#  It measures the mean reaction time and the slope of the reaction time for each participant for each condition.
#  It also runs an ANOVA to compare reaction time slope between tasks, modalities, and domains.
# NOTE: Does not remove points outside 2.5 stdev of mean
# NOTE: does not include participant 9, who did not respond in several conditions
# It also excludes 12_visual_4, due to an error in targets
# NOTE: file names have been changed to begin with a non-numerical character
# NOTE: relevant columns pre-selected through fmri_data_cleaning.Rmd
#  ****************************************************************************



# ******************** I. PREPARE FILES *************************



# Prepare workspace ------------------------------------------------------------------------------------------------------

#Set correct working directory
setwd("Documents/qlab/analysis/sl-psychopy-analysis/rt_slope/nov_pilot/scripts/")

# Remove objects in environment
rm(list=ls())


# Prepare paths for files --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NOTE: For use on Mac 
auditory_path <- "../cleaned_data/auditory/"
visual_path <- "../cleaned_data/visual/"



# List auditory and visual files---------------------------------------------------------------------------------------------------------------------------------------------------------------------

afiles <- list.files(path=auditory_path, pattern="*.csv")
vfiles <- list.files(path=visual_path, pattern = ".csv")

#Remove the underscores in file names
auditory_files <- gsub("_", "", afiles)
visual_files <- gsub("_", "", vfiles)


# Read in auditory files and combine them into one data frame--------------------------------------------------------------------------------------------------------------------------------------------

# Prepare auditory_data_frame to hold the files you're reading in
auditory_data_frame<-list()

# Remove the dashes in each file name read it in
for(auditory_file in afiles)
{
  assign(
    gsub("_", "", auditory_file),
    read.csv(paste(auditory_path, auditory_file, sep="")))
}

# Combine each file with the previous files into auditory_data_frame
for (afile in auditory_files){auditory_data_frame <- append(auditory_data_frame, list(eval(parse(text=afile))))}
auditory_data_frame <- do.call(rbind.data.frame, auditory_data_frame)


# Prepare auditory files for use----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Match name of image with name of target in auditory files by removing extension from end of sound_file
auditory_data_frame$soundFile <- gsub (".wav", "", auditory_data_frame$soundFile, ignore.case=TRUE)

# Convert targets and soundFile from factors to atomic variables 
auditory_data_frame$ttarget<-as.character(auditory_data_frame$ttarget)
auditory_data_frame$soundFile<-as.character(auditory_data_frame$soundFile)
auditory_data_frame$starget<-as.character(auditory_data_frame$starget)

# Rename expName column as "modality"
names(auditory_data_frame)[names(auditory_data_frame) == 'expName'] <- 'modality'


# Read in visual files and combine them into one data frame------------------------------------------------------------------------------------------------------

# Prepare visual_data_frame to hold the files you're reading in
visual_data_frame <- data.frame()
visual_data_frame<-list()

# Remove the dashes from each file name and read it in
for(visual_file in vfiles)
{
  assign(
    gsub("_", "", visual_file),
    read.csv(paste(visual_path, visual_file, sep="")))
  }

#Combine the visual files into visual_data_frame
for (vfile in visual_files){visual_data_frame <- append(visual_data_frame, list(eval(parse(text=vfile))))}
visual_data_frame <- do.call(rbind.data.frame, visual_data_frame)


# match name of image with name of target in visual files by removing extension from end of image and "Alien" from beginning of image ----------------------------------------------------------------------------------------

visual_data_frame$image <- gsub ("Alien", "", visual_data_frame$image, ignore.case=TRUE)
visual_data_frame$image <- gsub (".bmp", "", visual_data_frame$image, ignore.case=TRUE)
visual_data_frame$image <- gsub (".png", "", visual_data_frame$image, ignore.case=TRUE)
  
# Rename expName column as 'modality'
names(visual_data_frame)[names(visual_data_frame) == 'expName'] <- 'modality'




# ******************** II. EXTRACT RELEVANT AUDITORY DATA (ID, MODALITY, DOMAIN, TYPE, RT_SLOPE, MEAN_RT) BY CONDITION, THEN COMBINE 4 CONDITIONS TOGETHER**************************

# Separate trials 1-3 from trials 4-6----------------------------------------------------------------------------------------------------------------------------------------------------------

trials_1_3 <- auditory_data_frame[ which(auditory_data_frame$Run < 4), ]
trials_4_6 <- auditory_data_frame[ which(auditory_data_frame$Run > 3), ]


# ******************** CONDITION 1: RANDOM_TSL*******************


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
random_tsl_targets <- which(tolower(trials_1_3$ttarget)==tolower(trials_1_3$soundFile))

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in random_tsl_targets) {
  # Isolate the ID number
  id <- append(id, paste(trials_1_3[i,]$PartID))
  # If the participant responded while the target was presented
  if (!is.na(trials_1_3[i,] [,"random_block_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, trials_1_3[i,][,"random_block_key_resp.rt"])}
  # If the participant responded during the stimulus following the target
  else if (!is.na(trials_1_3[i+1,] [,"random_block_key_resp.rt"])){
    # Count their response time as the duration that the target was presented (480 ms) plus the response time to the following stimulus 
    rt_col[(match(i, random_tsl_targets))] <- .48+trials_1_3[i+1, ][,"random_block_key_resp.rt"]}
  # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_1_3[i,][,"random_block_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_1_3[i-1,] [,"random_block_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    rt_col[match(i, random_tsl_targets)] <- 0-trials_1_3[i-1,][,"random_block_key_resp.rt"]}
  # If the participant did not respond within 1 stimulus, 
  else if (is.na(trials_1_3[i,] [,"random_block_key_resp.rt"])){
      # Copy their response time of NA
      rt_col <- append (rt_col, trials_1_3[i,][,"random_block_key_resp.rt"])}
  }

# Match id and response times
random_tsl_extracted <- data.frame(id,rt_col)


# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(random_tsl_extracted$id)

# Find the number of targets shown to each participant
a <- NULL
for(i in list_part_id){a <- append(a,sum(random_tsl_extracted$id==i))}

# For each participant, index the targets
reindex <- NULL
for (i in a) {reindex <- append (reindex, rep(1:i, 1))}

# Add the targets' indices
random_tsl_extracted$reindex <- reindex

# Remove any values lower than -.48, higher than .96, or of NA
random_tsl_extracted <- random_tsl_extracted[random_tsl_extracted$rt_col<=0.96 & random_tsl_extracted$rt_col>= -.48 & !is.na(random_tsl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
domain <- NULL
modality <- NULL
type <- NULL
task<- NULL
RTSL<- NULL
rtsl_range <- NULL
upper_bound <- NULL
lower_bound <- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in list_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "auditory")
  task <- append(task, "TSL")
  type <- append (type, "random")
  modality <- append (modality, "non-linguistic")
  mean_rt <- append(mean_rt, round(mean(random_tsl_extracted$rt_col[random_tsl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_tsl_extracted$rt_col[random_tsl_extracted$id==id]~random_tsl_extracted$reindex[random_tsl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_tsl_extracted[ which(random_tsl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  }

# Combine data for each participant
RTSL <- data.frame(part_id, task, domain,type,modality,mean_rt, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rtsl_rt_slope <- mean (RTSL$rt_slope)


# ******************** CONDITION 2: STRUCTURED_SSL*******************


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
structured_ssl_targets <- which(tolower(trials_1_3$starget)==tolower(trials_1_3$soundFile))

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in structured_ssl_targets) {
  # Isolate the ID number
  id <- append(id, paste(trials_1_3[i,]$PartID))
  # If the participant responded while the target was presented
  if (!is.na(trials_1_3[i,] [,"structured_block_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, trials_1_3[i,][,"structured_block_key_resp.rt"])}
  # If the participant responded during the stimulus following the target
  else if (!is.na(trials_1_3[i+1,] [,"structured_block_key_resp.rt"])){
    # Count their response time as the duration that the target was presented (480 ms) plus the response time to the following stimulus 
    rt_col[(match(i, structured_ssl_targets))] <- .48+trials_1_3[i+1, ][,"structured_block_key_resp.rt"]}
  # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_1_3[i,][,"structured_block_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_1_3[i-1,] [,"structured_block_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    rt_col[match(i, structured_ssl_targets)] <- 0-trials_1_3[i-1,][,"structured_block_key_resp.rt"]}
  # If the participant did not respond
  else if (is.na(trials_1_3[i,] [,"structured_block_key_resp.rt"])){
    # Count their response time as NA
    rt_col <- append (rt_col, trials_1_3[i,][,"structured_block_key_resp.rt"])}
  
}

# Match id and response times
structured_ssl_extracted <- data.frame(id,rt_col)

# For internal checking only: Make sure that there are 48 per participant

#sssl_test<-count(structured_ssl_extracted, "id")
#sssl_test$task<- "structured ssl"

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(structured_ssl_extracted$id)

# Find the number of targets shown to each participant
a <- NULL
for(i in list_part_id){a <- append(a,sum(structured_ssl_extracted$id==i))}

# For each participant, index the targets
reindex <- NULL
for (i in a) {reindex <- append (reindex, rep(1:i, 1))}

# Add the targets' indices
structured_ssl_extracted$reindex <- reindex

# Remove any values lower than -.48, higher than .96, or of NA
structured_ssl_extracted <- structured_ssl_extracted[structured_ssl_extracted$rt_col<=0.96 & structured_ssl_extracted$rt_col>= -.48 & !is.na(structured_ssl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
domain <- NULL
task <- NULL
modality <- NULL
type <- NULL
SSSL<- NULL
sssl_range <- NULL
upper_bound <- NULL
lower_bound <- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt and rt_slope
for(id in list_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "auditory")
  type <- append (type, "structured")
  task<- append(task, "SSL")
  modality <- append (modality, "linguistic")
  mean_rt <- append(mean_rt, round(mean(structured_ssl_extracted$rt_col[structured_ssl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_ssl_extracted$rt_col[structured_ssl_extracted$id==id]~structured_ssl_extracted$reindex[structured_ssl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_ssl_extracted[ which(structured_ssl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  }

# Combine data for each participant
SSSL <- data.frame(part_id, task, domain,type,modality,mean_rt, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_sssl_rt_slope <- mean (SSSL$rt_slope)


# ******************** CONDITION 3: STRUCTURED_TSL*******************


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
structured_tsl_targets <- which(tolower(trials_4_6$ttarget)==tolower(trials_4_6$soundFile))

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in structured_tsl_targets) {
  # Isolate the ID number
  id <- append(id, paste(trials_4_6[i,]$PartID))
  # If the participant responded while the target was presented
  if (!is.na(trials_4_6[i,] [,"structured_block_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, trials_4_6[i,][,"structured_block_key_resp.rt"])}
  # If the participant responded during the stimulus following the target
  else if (!is.na(trials_4_6[i+1,] [,"structured_block_key_resp.rt"])){
    # Count their response time as the duration that the target was presented (480 ms) plus the response time to the following stimulus 
    rt_col[(match(i, structured_tsl_targets))] <- .48+trials_4_6[i+1, ][,"structured_block_key_resp.rt"]}
  # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_4_6[i,][,"structured_block_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_4_6[i-1,] [,"structured_block_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    rt_col[match(i, structured_tsl_targets)] <- 0-trials_4_6[i-1,][,"structured_block_key_resp.rt"]}
  # If the participant did not respond at all
  else if (is.na(trials_4_6[i,] [,"structured_block_key_resp.rt"])){
    # Count their response time from the target stimulus (NA)
    rt_col<- append (rt_col, trials_4_6[i,][,"structured_block_key_resp.rt"])  }
}

# Match id and response times
structured_tsl_extracted <- data.frame(id,rt_col)

# Remove any values lower than -.48, higher than .96, or of NA
structured_tsl_extracted <- structured_tsl_extracted[structured_tsl_extracted$rt_col<=0.96 & structured_tsl_extracted$rt_col>= -.48 & !is.na(structured_tsl_extracted$rt_col),]

# For internal checking only: Make sure that there are 48 per participant

#stsl_test<-count(structured_tsl_extracted, "id")
#stsl_test$task<- "structured tsl"

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(structured_tsl_extracted$id)

# Find the number of targets shown to each participant
a <- NULL
for(i in list_part_id){a <- append(a,sum(structured_tsl_extracted$id==i))}

# For each participant, index the targets
reindex <- NULL
for (i in a) {reindex <- append (reindex, rep(1:i, 1))}

# Add the targets' indices
structured_tsl_extracted$reindex <- reindex

# Remove targets with no response time
structured_tsl_extracted <- structured_tsl_extracted[!is.na(structured_tsl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
domain <- NULL
modality <- NULL
type <- NULL
task <- NULL
STSL<- NULL
stsl_range <- NULL
upper_bound <- NULL
lower_bound <- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt and rt_slope
for(id in list_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "auditory")
  type <- append (type, "structured")
  task<- append(task, "TSL")
  modality <- append (modality, "non-linguistic")
  mean_rt <- append(mean_rt, round(mean(structured_tsl_extracted$rt_col[structured_tsl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_tsl_extracted$rt_col[structured_tsl_extracted$id==id]~structured_tsl_extracted$reindex[structured_tsl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_tsl_extracted[ which(structured_tsl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  }

# Combine data for each participant
STSL <- data.frame(part_id, task, domain,type,modality,mean_rt, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_stsl_rt_slope <- mean (STSL$rt_slope)


# ******************** CONDITION 4: RANDOM_SSL*******************


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
random_ssl_targets <- which(tolower(trials_4_6$starget)==tolower(trials_4_6$soundFile))

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in random_ssl_targets) {
  # Isolate the ID number
  id <- append(id, paste(trials_4_6[i,]$PartID))
  # If the participant responded while the target was presented
  if (!is.na(trials_4_6[i,] [,"random_block_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, trials_4_6[i,][,"random_block_key_resp.rt"])}
  # If the participant responded during the stimulus following the target
  else if (!is.na(trials_4_6[i+1,] [,"random_block_key_resp.rt"])){
    # Count their response time as the duration that the target was presented (480 ms) plus the response time to the following stimulus 
    rt_col[(match(i, random_ssl_targets))] <- .48+trials_4_6[i+1, ][,"random_block_key_resp.rt"]}
  # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_4_6[i,][,"random_block_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_4_6[i-1,] [,"random_block_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    rt_col[match(i, random_ssl_targets)] <- 0-trials_4_6[i-1,][,"random_block_key_resp.rt"]}
  # If they did not respond within the correct time frame
  else if (is.na(trials_4_6[i,] [,"random_block_key_resp.rt"])){
      # Count their response time as NA
      rt_col <- append (rt_col, NA)}
}

# Match id and response times
random_ssl_extracted <- data.frame(id,rt_col)


# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(random_ssl_extracted$id)

# Find the number of targets shown to each participant
a <- NULL
for(i in list_part_id){a <- append(a,sum(random_ssl_extracted$id==i))}

# For each participant, index the targets
reindex <- NULL
for (i in a) {reindex <- append (reindex, rep(1:i, 1))}

# Add the targets' indices
random_ssl_extracted$reindex <- reindex

# Remove targets with no response time
random_ssl_extracted <- random_ssl_extracted[!is.na(random_ssl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
domain <- NULL
modality <- NULL
task <- NULL
type <- NULL
RSSL<- NULL
rssl_range <- NULL
upper_bound <- NULL
lower_bound <- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt and rt_slope
for(id in list_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "auditory")
  task <- append (task, "SSL")
  type <- append (type, "random")
  modality <- append (modality, "linguistic")
  mean_rt <- append(mean_rt, round(mean(random_ssl_extracted$rt_col[random_ssl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_ssl_extracted$rt_col[random_ssl_extracted$id==id]~random_ssl_extracted$reindex[random_ssl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_ssl_extracted[ which(random_ssl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  
  }

# Combine data for each participant
RSSL <- data.frame(part_id, task, domain,type,modality,mean_rt, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rssl_rt_slope <- mean (RSSL$rt_slope)


# ******************** III. EXTRACT RELEVANT VISUAL DATA (ID, MODALITY, DOMAIN, TYPE, RT_SLOPE, MEAN_RT) BY CONDITION, THEN COMBINE 4 CONDITIONS TOGETHER**************************




# Separate trials 1-3 from trials 4-6----------------------------------------------------------------------------------------------------------------------------------------------------------

trials_1_3 <- visual_data_frame[ which(visual_data_frame$Run < 4), ]
trials_4_6 <- visual_data_frame[ which(visual_data_frame$Run > 3), ]


# ******************** CONDITION 1: STRUCTURED_LSL*******************


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
structure_lsl_targets <- which(tolower(trials_1_3$ltarget)==tolower(trials_1_3$image))

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in structure_lsl_targets) {
  # Isolate the ID number
  id <- append(id, paste(trials_1_3[i,]$PartID))
  # If the participant responded while the target was presented
  if (!is.na(trials_1_3[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, trials_1_3[i,][,"l_block_trial_key_resp.rt"])}
    # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_1_3[i,][,"l_block_trial_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_1_3[i-1,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    rt_col[match(i, structure_lsl_targets)] <- 0-trials_1_3[i-1,][,"l_block_trial_key_resp.rt"]}
  # If the participant did not respond to the target within the correct time frame
  else if (is.na(trials_1_3[i,] [,"l_block_trial_key_resp.rt"])){
      # Count their response time from the target stimulus (NA)
      rt_col <- append (rt_col, trials_1_3[i,][,"l_block_trial_key_resp.rt"])}
}

# Match id and response times
structure_lsl_extracted <- data.frame(id,rt_col)


# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(structure_lsl_extracted$id)

# Find the number of targets shown to each participant
a <- NULL
for(i in list_part_id){a <- append(a,sum(structure_lsl_extracted$id==i))}

# For each participant, index the targets
reindex <- NULL
for (i in a) {reindex <- append (reindex, rep(1:i, 1))}

# Add the targets' indices
structure_lsl_extracted$reindex <- reindex

# Remove targets with no response time
structure_lsl_extracted <- structure_lsl_extracted[!is.na(structure_lsl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
domain <- NULL
modality <- NULL
type <- NULL
task <- NULL
RLSL<- NULL
slsl_range <- NULL
upper_bound <- NULL
lower_bound <- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt and rt_slope
for(id in list_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "visual")
  type <- append (type, "structured")
  modality <- append (modality, "linguistic")
  task <- append (task, "LSL")
  mean_rt <- append(mean_rt, round(mean(structure_lsl_extracted$rt_col[structure_lsl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structure_lsl_extracted$rt_col[structure_lsl_extracted$id==id]~structure_lsl_extracted$reindex[structure_lsl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structure_lsl_extracted[ which(structure_lsl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  }

# Combine data for each participant
SLSL <- data.frame(part_id, task, domain,type,modality,mean_rt, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
#mean_slsl_rt_slope <- mean (SLSL$rt_slope)

#slsl_test<-count(structure_lsl_extracted, "id")
#slsl_test$task<- "structured lsl"

# ******************** CONDITION 2: STRUCTURED_VSL*******************


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
structured_vsl_targets <- which(tolower(trials_4_6$vtarget)==tolower(trials_4_6$image))

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in structured_vsl_targets) {
  # Isolate the ID number
  id <- append(id, paste(trials_4_6[i,]$PartID))
  # If the participant responded while the target was presented
  if (!is.na(trials_4_6[i,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, trials_4_6[i,][,"v_block_trial_key_resp.rt"])}
  # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_4_6[i,][,"v_block_trial_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_4_6[i-1,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    rt_col[match(i, structured_vsl_targets)] <- 0-trials_4_6[i-1,][,"v_block_trial_key_resp.rt"]}
  # If the participant did not respond to the target within the correct time frame
  else if (is.na(trials_4_6[i,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_4_6[i,][,"v_block_trial_key_resp.rt"])}
}

# Match id and response times
structured_vsl_extracted <- data.frame(id,rt_col)

# For internal checking only: Make sure that there are 24 per participant

#svsl_test<-count(structured_vsl_extracted, "id")
#svsl_test$task<- "structured vsl"

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(structured_vsl_extracted$id)

# Find the number of targets shown to each participant
a <- NULL
for(i in list_part_id){a <- append(a,sum(structured_vsl_extracted$id==i))}

# For each participant, index the targets
reindex <- NULL
for (i in a) {reindex <- append (reindex, rep(1:i, 1))}

# Add the targets' indices
structured_vsl_extracted$reindex <- reindex

# Remove targets with no response time
structured_vsl_extracted <- structured_vsl_extracted[!is.na(structured_vsl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
domain <- NULL
task<- NULL
modality <- NULL
type <- NULL
SVSL<- NULL
svsl_range <- NULL
upper_bound <- NULL
lower_bound <- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt and rt_slope
for(id in list_part_id){
  task <- append (task, "VSL")
  part_id <- append(part_id, id)
  domain <- append(domain, "visual")
  type <- append (type, "structured")
  modality <- append (modality, "non-linguistic")
  mean_rt <- append(mean_rt, round(mean(structured_vsl_extracted$rt_col[structured_vsl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(structured_vsl_extracted$rt_col[structured_vsl_extracted$id==id]~structured_vsl_extracted$reindex[structured_vsl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (structured_vsl_extracted[ which(structured_vsl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  }

# Combine data for each participant
SVSL <- data.frame(part_id,task, domain,type,modality,mean_rt,upper_bound, lower_bound,rt_slope)

# for internal checking only: find mean rt_slope
#mean_svsl_rt_slope <- mean (SVSL$rt_slope)
#svsl_test<-count(structured_vsl_extracted, "id")
#svsl_test$task<-"structured vsl"


# ******************** CONDITION 3: RANDOM_LSL*******************


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
random_lsl_targets <- which(tolower(trials_4_6$ltarget)==tolower(trials_4_6$image))

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in random_lsl_targets) {
  # Isolate the ID number
  id <- append(id, paste(trials_4_6[i,]$PartID))
  # If the participant responded while the target was presented
  if (!is.na(trials_4_6[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, trials_4_6[i,][,"l_block_trial_key_resp.rt"])}
  # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_4_6[i,][,"l_block_trial_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_4_6[i-1,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    rt_col[match(i, random_lsl_targets)] <- 0-trials_4_6[i-1,][,"l_block_trial_key_resp.rt"]}
  # If the participant did not respond to the target within the correct time frame
  else if (is.na(trials_4_6[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_4_6[i,][,"l_block_trial_key_resp.rt"])}
}

# Match id and response times
random_lsl_extracted <- data.frame(id,rt_col)

# For internal checking only: Make sure that there are 24 per participant

#rlsl_test<-count(random_lsl_extracted, "id")
#rlsl_test$task<- "random lsl"

# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(random_lsl_extracted$id)

# Find the number of targets shown to each participant
a <- NULL
for(i in list_part_id){a <- append(a,sum(random_lsl_extracted$id==i))}

# For each participant, index the targets
reindex <- NULL
for (i in a) {reindex <- append (reindex, rep(1:i, 1))}

# Add the targets' indices
random_lsl_extracted$reindex <- reindex

# Remove targets with no response time
random_lsl_extracted <- random_lsl_extracted[!is.na(random_lsl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
domain <- NULL
modality <- NULL
type <- NULL
task <- NULL
RLSL<- NULL
rlsl_range <- NULL
upper_bound <- NULL
lower_bound <- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt and rt_slope
for(id in list_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "visual")
  type <- append (type, "random")
  modality <- append (modality, "linguistic")
  mean_rt <- append(mean_rt, round(mean(random_lsl_extracted$rt_col[random_lsl_extracted$id==id]),digits=3))
  task <- append (task, "LSL")
  rt_slope <- append (rt_slope, round(summary(lm(random_lsl_extracted$rt_col[random_lsl_extracted$id==id]~random_lsl_extracted$reindex[random_lsl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_lsl_extracted[ which(random_lsl_extracted$id==id),])
  rlsl_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  
  }

# Combine data for each participant
RLSL <- data.frame(part_id,task, domain,type,modality,mean_rt, upper_bound, lower_bound, rt_slope)


# for internal checking only: find mean rt_slope
mean_rlsl_rt_slope <- mean (RLSL$rt_slope)


# ******************** CONDITION 4: RANDOM_VSL*******************


# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
random_vsl_targets <- which(tolower(trials_1_3$vtarget)==tolower(trials_1_3$image))

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in random_vsl_targets) {
  # Isolate the ID number
  id <- append(id, paste(trials_1_3[i,]$PartID))
  # If the participant responded while the target was presented
  if (!is.na(trials_1_3[i,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, trials_1_3[i,][,"v_block_trial_key_resp.rt"])}
  # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_1_3[i,][,"v_block_trial_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_1_3[i-1,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    rt_col[match(i, random_vsl_targets)] <- 0-trials_1_3[i-1,][,"v_block_trial_key_resp.rt"]}
  # If the participant did not respond to the target within the correct time frame
  else if (is.na(trials_1_3[i,] [,"v_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_1_3[i,][,"v_block_trial_key_resp.rt"])}
}

# Match id and response times
random_vsl_extracted <- data.frame(id,rt_col)


# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(random_vsl_extracted$id)

# Find the number of targets shown to each participant
a <- NULL
for(i in list_part_id){a <- append(a,sum(random_vsl_extracted$id==i))}

# For each participant, index the targets
reindex <- NULL
for (i in a) {reindex <- append (reindex, rep(1:i, 1))}

# Add the targets' indices
random_vsl_extracted$reindex <- reindex

# Remove targets with no response time
random_vsl_extracted <- random_vsl_extracted[!is.na(random_vsl_extracted$rt_col),]


# Calculate mean rt and rt_slope  -----------------------------------------------------------------------------------------------------

# Define variables
mean_rt <- NULL
rt_slope <- NULL
part_id <- NULL
domain <- NULL
modality <- NULL
type <- NULL
task <-NULL
RVSL <- NULL
rvsl_range <- NULL
upper_bound <- NULL
lower_bound <- NULL

# For each participant, extract id
# Assign domain, type, and modality
# Calculate and record mean_rt and rt_slope
for(id in list_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "visual")
  type <- append (type, "random")
  task <- append (task, "VSL")
  modality <- append (modality, "non-linguistic")
  mean_rt <- append(mean_rt, round(mean(random_vsl_extracted$rt_col[random_vsl_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_vsl_extracted$rt_col[random_vsl_extracted$id==id]~random_vsl_extracted$reindex[random_vsl_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_vsl_extracted[ which(random_vsl_extracted$id==id),])
  this_range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
  }

# Combine data for each participant
RVSL <- data.frame(part_id, task, domain, type,modality,mean_rt,upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rvsl_rt_slope <- mean (RVSL$rt_slope)


# Bind conditions together--------------------------------------------------------------------------------------------------------------------------------------------------

# Bind visual cconditions
visual_rt<- rbind(RLSL, RVSL, SLSL, SVSL)
# Bind auditory conditions
auditory_rt<- rbind(RTSL, RSSL, STSL, SSSL)
# Bind all conditions
indiv_rt <- rbind(RLSL, RSSL, RTSL, RVSL, SLSL, SSSL, STSL, SVSL)

setwd("../output_files/")

write.csv(indiv_rt, "nov_pilot_rt_slope_indiv.csv")

# Find group-level mean accuracy accross tasks------------------------------------------------------------------------------------

group_rt_slope <- NULL
mean_struct_rt_slope <- NULL
mean_rand_rt_slope <- NULL
task <- NULL

# Find mean LSL accuracy across participants
task <- append (task, paste ("lsl"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "LSL"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "LSL"), ]$rt_slope), digits =3))

# Find mean SSL accuracy across participants
task <- append (task, paste ("ssl"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "SSL"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "SSL"), ]$rt_slope), digits =3))

# Find mean TSL accuracy across participants
task <- append (task, paste ("tsl"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "TSL"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "TSL"), ]$rt_slope), digits =3))

# Find mean VSL accuracy across participants
task <- append (task, paste ("vsl"))
mean_struct_rt_slope <- append(mean_struct_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="structured" 
                                                                                & indiv_rt$task== "VSL"), ]$rt_slope), digits =3))
mean_rand_rt_slope <- append(mean_rand_rt_slope, round(mean(indiv_rt[ which(indiv_rt$type=="random" 
                                                                            & indiv_rt$task== "VSL"), ]$rt_slope), digits =3))

# Combine group accuracies into one data frame
group_accuracy <- data.frame(cbind(task, mean_rand_rt_slope, mean_struct_rt_slope))

setwd("../output_files/")
write.csv(group_accuracy, "nov_pilot_rt_slope_group.csv")



# For internal checking only:
#targets_per_task<-rbind(slsl_test,sssl_test, stsl_test, svsl_test)
#write.csv(targets_per_task, "nov_pilot_targets.csv")


# # ******************** III. STATISTICAL ANALYSIS **************************
# Load libraries ------------------------------------------------------------------------------------------------------
# install.packages("gtools")
# install.packages("plyr")
# library(gtools)
# library(plyr)
# library(reshape2)
# library(reshape)
# 
# # use cast to summarize mean, sd, range of each task.
# rt_sum <- cast(indiv_rt,domain~modality+type,value="rt_slope",range)
# rt_sum
# 
# indiv_rt <- data.frame(matrix(ncol = 2, nrow = 0))
# indiv_rt_names <- c("category", "rt_p_value")
# colnames(indiv_rt) <- indiv_rt_names
# 
# # Run t-tests for random/structured combined------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# rt_slope_t_test<-indiv_rt
# 
# # t-test on all lsl
# all_lsl<-subset(rt_slope_t_test, task=="LSL")
# indiv_rt$category <- append(indiv_rt$category, paste("LSL"))
# indiv_rt$rt_p_value <- append(indiv_rt$rt_p_value, paste((t.test (all_lsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on all ssl
# all_ssl<-subset(rt_slope_t_test, task=="SSL")
# category <- append(category, paste("SSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (all_ssl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on all tsl
# all_tsl<-subset(rt_slope_t_test, task=="TSL")
# category <- append(category, paste("TSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (all_tsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on all vsl
# all_vsl<-subset(rt_slope_t_test, task=="VSL")
# category <- append(category, paste("vsl"))
# rt_p_value <- append(rt_p_value, paste((t.test (all_vsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on all non-linguistic
# all_non_ling<-subset(rt_slope_t_test, modality=="non-linguistic")
# category <- append(category, paste("non-linguistic"))
# rt_p_value <- append(rt_p_value, paste((t.test (all_non_ling$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on all linguistic
# all_ling<-subset(rt_slope_t_test, modality=="linguistic")
# category <- append(category, paste("linguistic"))
# rt_p_value <- append(rt_p_value, paste((t.test (all_ling$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on all auditory
# all_auditory<-subset(rt_slope_t_test, domain=="auditory")
# category <- append(category, paste("auditory"))
# rt_p_value <- append(rt_p_value, paste((t.test (all_auditory$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on all visual
# all_visual<-subset(rt_slope_t_test, domain=="visual")
# category <- append(category, paste("visual"))
# rt_p_value <- append(rt_p_value, paste((t.test (all_visual$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# 
# # Run t-tests for structured values------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# # Subset structured condition and convert rt_slope to numeric
# all_structured <- subset(rt_slope_t_test, type="structured")
# all_structured$rt_slope <- as.numeric(all_structured$rt_slope)
# 
# # t-test on structured ssl
# slsl<-subset(all_structured, task=="LSL")
# category <- append(category, paste("structured LSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (slsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on structured ssl
# sssl<-subset(all_structured, task=="SSL")
# category <- append(category, paste("structured SSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (sssl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on random tsl
# stsl<-subset(all_structured, task=="tsl")
# category <- append(category, paste("structured TSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (stsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on structured vsl
# svsl<-subset(all_structured, task=="vsl")
# category <- append(category, paste("structured VSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (svsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on structured non-linguistic
# s_non_ling<-subset(all_structured, modality=="non-linguistic")
# category <- append(category, paste("structured non-linguistic"))
# rt_p_value <- append(rt_p_value, paste((t.test (s_non_ling$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on structured linguistic
# s_ling<-subset(all_structured, modality=="linguistic")
# category <- append(category, paste("structured linguistic"))
# rt_p_value <- append(rt_p_value, paste((t.test (s_ling$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on structured auditory
# s_auditory<-subset(all_structured, domain=="auditory")
# category <- append(category, paste("structured auditory"))
# rt_p_value <- append(rt_p_value, paste((t.test (s_auditory$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on structured visual
# s_visual<-subset(all_structured, domain=="visual")
# category <- append(category, paste("structured visual"))
# rt_p_value <- append(rt_p_value, paste((t.test (s_visual$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # Run t-tests for random values------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
# # Subset random condition and convert rt_slope to numeric
# all_random <- subset(rt_slope_t_test, type=="random")
# all_random$rt_slope <- as.numeric(all_random$rt_slope)
# 
# # t-test on random ssl
# rlsl<-subset(all_random, task=="LSL")
# category <- append(category, paste("random LSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (rlsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on random ssl
# rssl<-subset(all_random, task=="SSL")
# category <- append(category, paste("random SSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (rssl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on random tsl
# rtsl<-subset(all_random, task=="TSL")
# category <- append(category, paste("random TSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (rtsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on random vsl
# rvsl<-subset(all_random, task=="VSL")
# category <- append(category, paste("random VSL"))
# rt_p_value <- append(rt_p_value, paste((t.test (rvsl$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on random non-linguistic
# r_non_ling<-subset(all_random, modality=="non-linguistic")
# category <- append(category, paste("random non-linguistic"))
# rt_p_value <- append(rt_p_value, paste((t.test (r_non_ling$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on random linguistic
# r_ling<-subset(all_random, modality=="linguistic")
# category <- append(category, paste("random linguistic"))
# rt_p_value <- append(rt_p_value, paste((t.test (r_ling$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on random auditory
# r_auditory<-subset(all_random, domain=="auditory")
# category <- append(category, paste("random auditory"))
# rt_p_value <- append(rt_p_value, paste((t.test (r_auditory$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # t-test on random visual
# r_visual<-subset(all_random, domain=="visual")
# category <- append(category, paste("random visual"))
# rt_p_value <- append(rt_p_value, paste((t.test (r_visual$rt_slope, mu =0, alternative= "less"))$p.value))
# 
# # Combine into one data frame
# indiv_rt_p_values<- data.frame(category, rt_p_value)
