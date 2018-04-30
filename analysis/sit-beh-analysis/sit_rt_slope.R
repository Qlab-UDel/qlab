
# TO DO : Did participants see the first_targ during the structured condition and second_targ during the random condition?
# TO DO: Also, are we including reaction times for responses during the stimuli preceding/ following for l and v trials?
# TO DO: Remove points outside 2.5 Stdev of mean?
# TO DO: Image index in a way that accounts for different repetitions of S/R blocks. EG: participant A's two R blocks are merged.
# he doesn't respond during the last target of an S block, which is the last stimulus, so we take his reaction time from the
# following stimulus (which is actually the first stimulus of the next S block)
# TO DO: Successfully replace "f_not_false" with "F"
# TO DO: Why is id_test returning an odd, different list from the list of ids?
# TO DO: Why is list_part_id of type integer?? 
# TO DO: When, when I convert list_part_id to a string, are ids listed very oddly?
# TO DO: What are all the weird warnings in line 212?
# TO DO: What to do in line 247 if you're in the last line for that participant? Or the last line of that block?
# TO DO: What is 239?

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
#ll_data_frame$random_targ[ll_data_frame$random_targ == "f_not_false"] <- "F"
#ll_data_frame$structured_targ[ll_data_frame$structured_targ == "f_not_false"] <- "F"

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

#convert targets to string
lv_data_frame$random_targ<-toString(lv_data_frame$random_targ)
lv_data_frame$structured_targ<-toString(lv_data_frame$structured_targ)

# to test
#r_targs_before <- unique(lv_data_frame$random_targ)
#s_targs_before <- unique(lv_data_frame$structured_targ)

# Read "f_not_false" as "F"
#lv_data_frame$random_targ[lv_data_frame$random_targ == 'f_not_false'] <- 'F'
#lv_data_frame$structured_targ[lv_data_frame$structured_targ == 'f_not_false'] <- 'F'

# to test
#r_targs_after <- unique(lv_data_frame$random_targ)
#s_targs_after <- unique(lv_data_frame$structured_targ)


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

#convert targets to string
vl_data_frame$random_targ<-toString(vl_data_frame$random_targ)
vl_data_frame$structured_targ<-toString(vl_data_frame$structured_targ)

# to test
#r_targs_before <- unique(vl_data_frame$random_targ)
#s_targs_before <- unique(vl_data_frame$structured_targ)

# Read "f_not_false" as "F"
#vl_data_frame$random_targ[vl_data_frame$random_targ == 'f_not_false'] <- 'F'
#vl_data_frame$structured_targ[vl_data_frame$structured_targ == 'f_not_false'] <- 'F'

# to test
#r_targs_after <- unique(vl_data_frame$random_targ)
#s_targs_after <- unique(vl_data_frame$structured_targ)


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

#convert targets to string
vv_data_frame$random_targ<-toString(vv_data_frame$random_targ)
vv_data_frame$structured_targ<-toString(vv_data_frame$structured_targ)

# to test
#r_targs_before <- unique(vv_data_frame$random_targ)
#s_targs_before <- unique(vv_data_frame$structured_targ)

# Read "f_not_false" as "F"
#vv_data_frame$random_targ[vv_data_frame$random_targ == 'f_not_false'] <- 'F'
#vv_data_frame$structured_targ[vv_data_frame$structured_targ == 'f_not_false'] <- 'F'

# to test
#r_targs_after <- unique(vv_data_frame$random_targ)
#s_targs_after <- unique(vv_data_frame$structured_targ)

# Remove .png from image names
vv_data_frame$image <- gsub (".png", "", vv_data_frame$image, ignore.case=TRUE)


# ******************** CONDITION 1: LL*******************

# Separate random and structured conditions
random_ll <- ll_data_frame[ which(ll_data_frame$condition== "R"),]
structured_ll <- ll_data_frame[ which(ll_data_frame$condition== "S"),]

# Index the images by random/ structured-----------------------------------------------

# List unique participant IDs for this condition
list_part_id <- unique(ll_data_frame$part_id)

#test
View(typeof(list_part_id))

# Find the number of images shown to each participant
random_images_per_participant <- NULL
for(i in list_part_id){random_images_per_participant <- append(random_images_per_participant,sum(random_ll$part_id==i))}

#for testing purposes
id_test <- cbind(random_images_per_participant, list_part_id)

# For each participant, index the images
image_index <- NULL
for (i in random_images_per_participant) {image_index <- append (image_index, rep(1:random_images_per_participant, 1))}

# Add the targets' indices
random_ll$image_index <- image_index

# Identify response times to target stimuli. Include times when participant responded while target was displayed, or during preceding/ following stimulus ---------------------------------------------

# Set up variables to loop through participants by trials and track the target
rt_col <- NULL
id <- NULL
trial <-NULL
target <- NULL

# Identify the rows when this condition's target was presented
random_ll_targets <- random_ll[which(random_ll$random_targ==random_ll$image),]
structured_ll_targets <- structured_ll[which(structured_ll$structured_targ==structured_ll$image),]

# Isolate participants' response times.
# Include rows when the participant responded to stimuli adjacent to the target (i.e. any time that the participant pressed the button within one stimulus before or after the target)
for (i in random_ll_targets) {
  # Isolate the image index
  this_image_index <- random_ll_targets[i,]$image_index
  # Isolate the ID number
  this_id <- random_ll_targets[i]$part_id
  # Append the id number
  id <- append(id, paste(random_ll_targets[i,]$part_id))
  # If the participant responded while the target was presented
  if (!is.na(random_ll_targets[i,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time from the target stimulus
    rt_col <- append (rt_col, random_ll_targets[i,][,"l_block_trial_key_resp.rt"])}
  # If the participant responded during the stimulus following the target
  else if (!is.na(random_ll[i+1,] [,"l_block_trial_key_resp.rt"])){
    # Count their response time as the duration that the target was presented (1000 ms)
    # plus the response time to the following stimulus in random_ll
        # First, find the subset of lines related to this participant
        this_id_rts <- random_ll[which(random_ll$part_id == this_id)]
        # Second, identify the image indexed after this one
        following_stim <- this_id_rts [which( this_id_rts$image_index == this_image_index+1)]
        # Third, add this line's reaction time to the duration that the target was presented
        target_rt <- .1+ following_stim$l_block_trial_key_resp.rt
        rt_col <- append [rt_col, target_rt]
  # Check if you are looking at the first target, which is always the first stimulus. If so, it does not have a preceeding target
  else if (i>0){ 
    # Count their response time from the target stimulus (NA)
    rt_col <- append (rt_col, trials_1_3[i,][,"random_block_key_resp.rt"])}    
  # If the participant responded during the stimulus preceding the target
  else if (!is.na(trials_1_3[i-1,] [,"random_block_key_resp.rt"])){
    # Count their response time as how much sooner they responded than when the stimulus was presented
    # (0 minus their reaction time to the preceding stimulus)
        # First, find the subset of lines related to this participant
        this_id_rts <- random_ll[which(random_ll$part_id == this_id)]
        # Second, identify the image indexed before this one
        preceding_stim <- this_id_rts [which( this_id_rts$image_index == this_image_index-1)]
        # Third, subtract this line's reaction time from 0
        target_rt <- 0- preceding_stim$l_block_trial_key_resp.rt
        rt_col <- append [rt_col, target_rt]    
  # If the participant did not respond within 1 stimulus, 
  else if (is.na(trials_1_3[i,] [,"random_block_key_resp.rt"])){
    # Copy their response time of NA
    rt_col <- append (rt_col, trials_1_3[i,][,"random_block_key_resp.rt"])}
}

# Match id and response times
random_ll_extracted <- data.frame(id,rt_col)


# Reindex the trial numbers for only trials with response times -----------------------------------------------------------------------------------------------------

# List unique participant IDs for this condition
extracted_part_id <- unique(random_ll_extracted$id)

# Find the number of targets shown to each participant
target_sum <- NULL
for(i in extracted_part_id){target_sum <- append(target_sum,sum(random_ll_extracted$id==i))}

# For each participant, index the targets
targ_index <- NULL
for (i in target_sum) {reindex <- append (targ_index, rep(1:i, 1))}

# Add the targets' indices
random_ll_extracted$targ_index <- targ_index

# Remove any values of NA
random_ll_extracted <- random_tsl_extracted[!is.na(random_ll_extracted$rt_col),]


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

# For each participant, extract id
# Assign domain and type
# Calculate and record mean_rt, rt_slope, upper bound, and lower bound
for(id in extracted_part_id){
  part_id <- append(part_id, id)
  domain <- append(domain, "linguistic")
  task <- append(task, "ll")
  type <- append (type, "random")
  mean_rt <- append(mean_rt, round(mean(random_ll_extracted$rt_col[random_ll_extracted$id==id]),digits=3))
  rt_slope <- append (rt_slope, round(summary(lm(random_ll_extracted$rt_col[random_ll_extracted$id==id]~random_ll_extracted$reindex[random_ll_extracted$id==id]))$coefficient[2,1],digits = 4))
  data_this_id <- (random_ll_extracted[ which(random_ll_extracted$id==id),])
  range<- range(data_this_id$rt_col, na.rm = TRUE)
  upper_bound <- append (upper_bound,this_range[1])
  lower_bound <- append (lower_bound,this_range[2])
}

# Combine data for each participant
rll <- data.frame(part_id, task, domain,type,modality,mean_rt, range, upper_bound, lower_bound, rt_slope)

# for internal checking only: find mean rt_slope
mean_rll_rt_slope <- mean (rll$rt_slope)



# Note: This script excludes data from the file sit_a_010_vv, because the participant did not respond during the exposure phase

# combine rt columns for lv and vl df$x <- paste(df$n,df$s)


# TO DO: Add modality (ling/ non-ling)
# TO DO: Currently excludes sit_a_010_vv, which is missing the rt column?

