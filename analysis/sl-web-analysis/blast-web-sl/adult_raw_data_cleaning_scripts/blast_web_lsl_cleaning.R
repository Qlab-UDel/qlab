#  Jojo Hu
#  Last updated Sep 25th, 2019
#  Adapted from An's script lsl_clean_file.Rmd
#  Can be used for cleaning both random and predictable 2afc lsl raw files
#  ****************************************************************************

#Added in checking for multiple keypresses in one trial, only the first keypress was kept for each trial
#Added in cleaning for 800ms-letter and 200ms-blank
#The number of people doing LSL randomized 2afc is the same as that experienced LSL 800-200ms exposure phase
#(seems the two changes happened at the same time, need to be double checked by JH)
#Added in checking for how many files have 800ms-long presentation for letter and 200ms-long for blanks
#To do: R markdown file needs to be compiled

install.packages("stringr")
install.packages("plyr")
library("stringr")
library("plyr")
# To do: setwd is redundant here.
setwd("/Volumes/data/projects/blast/data/online_sl/blast_adult")

input_path <- 
  "/Volumes/data/projects/blast/data/online_sl/blast_adult/"

#Change input path to run predictable lsl. 
#input_path <- 
#  "/Volumes/data/projects/blast/data/online_sl/blast_child/predictable_lsl/"

#Predictable and random lsl do not differ for the exposure phase. 
#Output path can be the same as long as blast_web_lsl_rt_analysis.R includes all lsl cleaned files.

output_path <-
  "/Volumes/data/projects/blast/data_summaries/blast_online_adult_lsl_clean/"

#Use two output paths if you are not sure what the comments above means
#output_path <-
#  "/Volumes/data/projects/blast/data_summaries/blast_online_child_lsl_clean/predictable_lsl"

#List all the files ending in lsl.csv
files <- list.files(path = input_path, pattern = "*lsl.csv")

#Write a long function to do this for every file in the list
# To Do: Dplyr should be used to increase performance
cleandata <- function(file) {
  #Read in each file one by one
  lsl <- read.csv(paste0(input_path, file))
  
  #Extract the stimuli and key press responses from the specific rows
  rep <-
    lsl$responses[which(str_detect(lsl$animation_sequence, "\\S") == TRUE)]
  #split the response to a neat format
  rep <-
    unlist(strsplit(paste(rep), split = ",", fixed = TRUE))

  ani_stim <-
    lsl$animation_sequence[which(str_detect(lsl$animation_sequence, "\\S") == TRUE)]
  
  ani_stim <-
    unlist(strsplit(paste(ani_stim), split = ",", fixed = TRUE))
  
  #Extract all the key press response time and stimuli presented during the key press
  key <- NULL
  rt  <- NULL
  stim_press <- NULL
  stim_disp <- NULL
  time <- NULL
  #Extract response time from the rows (2, 5, 8, 11, etc.) in rep
  for (j in seq(from = 2,
                to = length(rep),
                by = 3)) {
    rt <- append(rt,
                 as.numeric(str_extract(rep[j], "(?<=:)\\d+")))
  }
  #Extract the stimulus presented during the key press from the rows (3, 6, 9, etc.)
  for (k in seq(from = 3,
                to = length(rep),
                by = 3)) {
    stim_press <- append(stim_press,
                         str_extract(rep[k], "(?<=image/image/)\\S+(?=.png)"))
  }
  #Extract all the stimuli being presented from the rows (1, 3, 5, etc.)
  #To Do: Make the regular expression neater
  for (i in seq(from = 1,
                to = length(ani_stim),
                by = 2)) {
    stim_disp <- rbind(stim_disp,
                       str_extract(ani_stim[i], "(?<=(\\S)image/image/)\\S+(?=.png)"))
  }
  #Extract the time point at which each stimulus is presented from rows (2, 4, 6, etc.)
  #rbind here changes the type of table2$time
  for (n in seq(from = 2,
                to = length(ani_stim),
                by = 2)) {
    time <- rbind(time,
                  as.numeric(str_extract(ani_stim[n], "(?<=:)\\d+")))
  }
  
  #To Do: create data frame earlier to reduce these steps
  table1 <- data.frame(rt, stim_press)
  table2 <- data.frame(stim_disp, time)
  
  #This is only used for lsl files with 800 ms presentation time of letters and 200ms of blanks
  #Extract only the first presentation (the time of the first presentation is the onset of the letter)
  #Also extract every fifth presentation (that is the blank)
  
  subdata <- data.frame()
  #Initiate a number sequence following 1, 5, 6, 10 etc. pattern
  subdata_row <- 0 + cumsum(rep(c(1, 4), length(table2$stim_disp) / 5))
    subdata <- data.frame("row" = integer(length(subdata_row)))
  subdata$row <- subdata_row
  
  #Only run this if the letter trials in the exposure phase of LSL are 800ms long
  #Letters were displayed for 1000 ms (and blank for 1000ms) in some files. 
  #LSL was later corrected to have only 800ms for Letter and 200 ms for blank.
  wrong_trial_length = 0
  
  if(length(unique(table2[seq(
    from=0, to=length(table2$stim_disp), by=5),
    "stim_disp"])) == 1) {
  table2$row <- seq.int(nrow(table2))
  table2 <- match_df(table2, subdata, on = "row")
  table2 <- table2[, !names(table2) %in% c("row")]
  row.names(table2) <- 1:nrow(table2)
  wrong_trial_length <- wrong_trial_length + 1
  }
  
  #To Do: Print error for table2 if it has letters after row 576
  #Select only the exposure phase
  
  table2 <- table2[1:576, ]
  table2$col2 <- "NA"
  table2$col1 <- "NA"
  table1$stim_press <- paste(table1$stim_press)
  table2$stim_disp <- paste(table2$stim_disp)
  #see comment above about rbind
  table2$time <- as.numeric(paste(table2$time))

  #Check which sitmulus has two key presses--------------------------------------------------------------
  #Get rid of the second keypress for the same stimulus
  #Create a three-dimension array (numbers of total stimuli -1, number of keypresses by the participant,
  #number of columns needed for data entry)
  #The first dimension is total stimuli -1 because there will be 575 pairs of stimuli sequentially in a
  #576-long stimuli sequence
  i_dimension_length <- length(table1$stim_press != "NA")
  duplicate_keypress <- rep(0, 575*i_dimension_length*6)
  duplicate_keypress <- array(duplicate_keypress, c(575, i_dimension_length, 6));
  dimnames(duplicate_keypress)[[3]] <- c("index_stim",
                                         "current_stim_time",
                                         "next_stim_time",
                                         "index_keypress",
                                         "current_rt",
                                         "in_the_range")

  #Check whether a keypress falls into the time range of every two stimuli
  for (j in seq(from = 1,
                to = length(table2$stim_disp)-1,
                by = 1)){
    current_stim_time <- table2[j,"time"]
    next_stim_time <- table2[j+1,"time"]

    for (i in seq(from = 1,
                  to = length(table1$stim_press),
                  by = 1)) {
      current_rt <- table1[i, "rt"]

      duplicate_keypress[j, i, "index_stim"] <- j
      duplicate_keypress[j, i, "current_stim_time"] <- current_stim_time
      duplicate_keypress[j, i, "next_stim_time"] <- next_stim_time
      duplicate_keypress[j, i, "index_keypress"] <- i
      duplicate_keypress[j, i, "current_rt"] <- current_rt
      duplicate_keypress[j, i, "in_the_range"] <- as.numeric(
        current_rt %in% seq(current_stim_time, next_stim_time))
    }
  }

  #Squeeze the second dimension to get sum of how many keypresses are in every sequential pair of the displayed stimuli
  keypress_number <- apply(duplicate_keypress, MARGIN=c(1,3), sum)
  #Extract index in the squeezed table. The index represents the stimuli pair (the third dimension j) that contains more than 1 keypress
  dimension_j <- which(keypress_number[,"in_the_range"] > 1)

  #Put j back into the three-dimension array. Find the trials that have keypresses in the stimuli pair
  #Only keep the first trial of keypress for the stimuli. Remove all other keypresses for the same stimuli
  #Initiate a dataframe for storing RTs that are of duplicated keypresses
  #What's wrong with this?
  rt_with_duplicate_keypress <- list()
  loop_index = 0
  for (z in dimension_j) {
    loop_index = loop_index + 1
    #find the row number in the second dimension i
    trial_index_i <- which(duplicate_keypress[z, ,c("in_the_range")] == 1)
    #find the RTs that are of duplicated keypresses and exclude the first keypress
    rt_with_duplicate_keypress[[loop_index]] <-
      duplicate_keypress[z, trial_index_i[c(-1)], c("current_rt")]
  }

  rt_with_duplicate_keypress <- unlist(rt_with_duplicate_keypress, use.names=FALSE)

  #Remove the duplicate RTs from the data
  if(length(rt_with_duplicate_keypress) > 0){
  table1 <- table1[-which(table1[,"rt"] %in% rt_with_duplicate_keypress), ]
  row.names(table1) <- 1:nrow(table1)
  }

  #Count at which display of the target the participant pressed the key-------------------------------
  #For example, at the 3rd time of the target C, the participant pressed the key
  #Then index = 3
  #Two for loops, at each iteration of i,
  #loop through each key response's stimulus and all the displayed stimuli
  #This works well because the triplets are structured. The same letter will never appear consecutively in the stimuli being displayed.
  #Then at the target that's pressed, the response time and the stimulus being pressed are put back to
  #table2 which has all the stimuli diplayed.
  #To do: Dplyr should be able to realize the same thing with much faster speed,
  #use Dplyr to write the loop
  for (i in seq(from = 1,
                to = length(table1$stim_press),
                by = 1)) {
    temp1 <- table1[i,]
    index <- 0
    min <- .Machine$integer.max

    for (j in seq(from = 1,
                  to = length(table2$stim_disp),
                  by = 1)) {
      temp2 <- table2[j,]
      if (temp2[3] == "NA") {
        if (temp1[2] == temp2[1]) {
          if (abs(temp1[1] - temp2[2]) < min) {
            min <- abs(temp2[2] - temp1[1])
            index <- j
          }
        }
      }
    }#second for loop ends here
    table2$col1[index] <- temp1[1]
    table2$col2[index] <- as.character(unlist(temp1[2]))
  }

  #To Do: create data.frame earlier to skip these steps
  table2$target <- lsl$targ[1]
  table2$cond <- lsl$cond[1]
  #fixed the part_id, currently part_ids are all NAs
  table2$par_id <-
    rep(gsub('.{2}$', '', unlist(
      strsplit(paste(lsl$response[1]), split = ':"', fixed = TRUE)
    )[2]), length(lsl$responses[1]))
  #save this for troubleshooting when table1 has different rows than table2 in the command below
  table2_troubleshoot <- table2
  table2 <- as.matrix(table2)

  table1_troubleshoot <-table1
  #Remove the keypresses that are before any stimuli were displayed
  if (length(which(table1$stim_press=="NA")) > 0) {
  table1 <- table1[-which(table1$stim_press=="NA"),]
  }
  #To Do: Count how many responses are in col1 to make sure all the key pressed are in table2
  if (nrow(table1) !=
      sum(as.numeric(str_detect(table2[, "col1"], "\\d")))) {
    stop("Check if all the key presses are input correctly into table2.")
  }
  #blast_c_220_lsl has a key press at 273123ms showing stimuli H as key pressed stimulus
  #However, in animation sequence, 273123ms should be displaying G
  #Not sure how the key pressed stimuli is wrong
  #Commented out the stop command above to run the script anyways


  #Save table2 into data_summaries----------------------------------------------------------------
  write.csv(table2, paste0(output_path, as.character(file)))

  #Count how many lsl files have 800ms-long Letter presentation during the exposure phase---------
  return(wrong_trial_length)
}

#Initiate a data frame for saving which subject has 800ms-long trial------------------------------
count_800ms_files <- data.frame("subject_id" = character(0),
                                 "eight_hundred_ms_true_or_false" = integer(0))
count_800ms_files$subject_id <- as.character(count_800ms_files$subject_id) 
#Initiate the row number for the count_800ms_files data frame
count_index = 0 
#Run for each file/ subject
for (file in files)
{
  #Run the function which will save the cleaned lsl files
  total_800ms_trial_file <- cleandata(file)
  #Plus 1 for row number each time this for loop runs
  count_index <- count_index + 1
  #Save whether or not the current subject has 800ms-long trial
  count_800ms_files[count_index, 
                    "eight_hundred_ms_true_or_false"]<- total_800ms_trial_file
  #Save the current subject number
  count_800ms_files[count_index,
                    "subject_id"]<- as.character(file)
}

write.csv(count_800ms_files, paste0(output_path, "lsl_800ms_long_trial_indiv_count.csv"))

