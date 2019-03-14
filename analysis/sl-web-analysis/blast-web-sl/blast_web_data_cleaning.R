#  BLAST Online Session Data Cleaning
#  Violet Kozloff
#  September 10th, 2018 
#  Adapted from lsl_rt_clean_file and mturk_combine_raw by An Nguyen
#  This script cleans LSL, SSL, TSL, and VSL files from the online session of the BLAST experiment
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------

# Set directory
setwd("/Volumes/data/projects/blast/data/online/blast_adult/original")

# Remove objects in environment
rm(list=ls())


# Prepare files ------------------------------------------------------------

# Set up output path
clean_data_path <- ("/../clean")

# List input files
lsl_files <- list.files(pattern="*lsl.csv")
ssl_files <- list.files(pattern="*ssl.csv")
tsl_files <- list.files(pattern="*tsl.csv")
vsl_files <- list.files(pattern="*vsl.csv")

# Clean TSL files ———————————————————————————————————

# Create a new file containing only the relevant columns in the output folder
tsl_clean <- function(file) {
  # Read files
  this_file <- read.csv(file)
  # Select relevant columns
  value <- c("rt", "trial_index", "targ","key_press","stimulus")
  newdata <- this_file[value]  
  # Create a column populated with the participant ID
  this_file["responses"] <- lapply(this_file["responses"], as.character)
  part_id <- substr(as.character(this_file["responses"[1]]), 14, 24)
  newdata$part_id <- part_id
  # Write file
  this_path<-file.path(tsl_output, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all tsl files
for (file in tsl_files)
{
  tsl_clean(paste0(tsl_input,file))
}

# Create one file with all tsl information
tsl <- list()
tsl_clean_files <- list.files(path=tsl_output, pattern="*.csv") 
for(file in tsl_clean_files)
{
  assign(
    gsub(" ","",file), 
    read.csv(paste(tsl_output,file,sep="")))
}

for(file in tsl_clean_files){tsl <- append(tsl,list(eval(parse(text=file))))}

}tsl <- do.call(rbind.data.frame, tsl)

# Standardize stimulus names
tsl$stimulus<- gsub(".wav","",tsl$stimulus)
tsl$stimulus<- gsub("../../tones/","",tsl$stimulus)


write.csv(tsl,"../../../../blast_adult_web_sl_data/clean/tsl_clean/tsl.csv")


# Clean ssl files ———————————————————————————————————

# Create a new file containing only the relevant columns in the output folder
ssl_clean <- function(file) {
  # Read files
  this_file <- read.csv(file)
  # Select relevant columns
  value <- c("rt", "trial_index","targ","key_press","stimulus")
  newdata <- this_file[value]  
  # Create a column populated with the participant ID
  this_file["responses"] <- lapply(this_file["responses"], as.character)
  part_id <- substr(as.character(this_file["responses"[1]]), 14, 24)
  newdata$part_id <- part_id
  # Write file
  this_path<-file.path(ssl_output, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all ssl files
for (file in ssl_original_files)
{
  ssl_clean(paste0(ssl_input,file))
}

# Apply function to all ssl files
for (file in ssl_original_files)
{
  ssl_clean(paste0(ssl_input,file))
}

# Create one file with all ssl information
ssl <- list()
ssl_clean_files <- list.files(path=ssl_output, pattern="*.csv") 
for(file in ssl_clean_files)
{
  assign(
    gsub(" ","",file), 
    read.csv(paste(ssl_output,file,sep="")))
}

for(file in ssl_clean_files){ssl <- append(ssl,list(eval(parse(text=file))))}

ssl <- do.call(rbind.data.frame, ssl)

# Standardize stimulus names
ssl$stimulus<- gsub(".wav","",ssl$stimulus)
# TO DO: Add this to other cases
ssl$stimulus<- gsub(" ","",ssl$stimulus)
ssl$stimulus<- gsub("sound/","",ssl$stimulus)

write.csv(ssl,"../../../../blast_adult_web_sl_data/clean/ssl_clean/ssl.csv")


# Clean vsl files ———————————————————————————————————

# Create a new file containing only the relevant columns in the output folder
vsl_clean <- function(file) {
  # Read files
  this_file <- read.csv(file)
  # Select relevant columns
  value <- c("rt", "trial_index","cond","targ","key_press","stimulus")
  newdata <- this_file[value]  
  # Create a column populated with the participant ID
  this_file["responses"] <- lapply(this_file["responses"], as.character)
  part_id <- substr(as.character(this_file["responses"[1]]), 14, 24)
  newdata$part_id <- part_id
  # Write file
  this_path<-file.path(vsl_output, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all vsl files
for (file in vsl_original_files)
{
  vsl_clean(paste0(vsl_input,file))
}

# Create one file with all vsl information
vsl <- list()
vsl_clean_files <- list.files(path=vsl_output, pattern="*.csv") 
for(file in vsl_clean_files)
{
  assign(
    gsub(" ","",file), 
    read.csv(paste(vsl_output,file,sep="")))
}

for(file in vsl_clean_files){vsl <- append(vsl,list(eval(parse(text=file))))}

vsl <- do.call(rbind.data.frame, vsl)

# Standardize stimulus names
vsl$stimulus<- gsub(".jpg","",vsl$stimulus)
vsl$stimulus<- gsub(".png","",vsl$stimulus)
vsl$stimulus<- gsub("../../images/","",vsl$stimulus)
# TO DO: Make sure this is the case for all
vsl$stimulus<- tolower(vsl$stimulus)

write.csv(vsl,"../../../../blast_adult_web_sl_data/clean/vsl_clean/vsl.csv")


# Clean lsl files for accuracy ———————————————————————————————————

test_lsl<- read.csv("../../../../blast_adult_web_sl_data/original/lsl_original/blast_c_006_lsl.csv")


# Create a new file containing only the relevant columns in the output folder
lsl_clean <- function(file) {
  # Read files
  this_file <- read.csv(file)
  this_file <- test_lsl
 
  # Select relevant columns
  value <- c("rt", "trial_index","targ","key_press","stimulus")
  newdata <- this_file[value]  
  # TO DO: Check that this is relevant for all files, but for 006 it looks like we only need to consider lines 16 on
  newdata<-newdata[which(newdata$trial_index>15),]
    # Create a column populated with the participant ID
  this_file["responses"] <- lapply(this_file["responses"], as.character)
  part_id <- substr(as.character(this_file["responses"[1]]), 14, 24)
  newdata$part_id <- part_id
  # Write file
  this_path<-file.path(lsl_acc_output, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all lsl files
for (file in lsl_original_files)
{
  lsl_clean(paste0(lsl_input,file))
}

# Create one file with all lsl information
lsl_acc <- list()
lsl_clean_files <- list.files(path=lsl_acc_output, pattern="*.csv") 
for(file in lsl_clean_files)
{
  assign(
    gsub(" ","",file), 
    read.csv(paste(lsl_acc_output,file,sep="")))
}

for(file in lsl_clean_files){lsl_acc <- append(lsl_acc,list(eval(parse(text=file))))}

lsl_acc <- do.call(rbind.data.frame, lsl_acc)

# Standardize stimulus names
lsl_acc$stimulus<- gsub(".png","",lsl_acc$stimulus)
lsl_acc$stimulus<- gsub("image/image/","",lsl_acc$stimulus)
lsl_acc$stimulus<- gsub("image/","",lsl_acc$stimulus)
# TO DO: Make sure this is the case for all
lsl_acc$stimulus<- tolower(lsl_acc$stimulus)
lsl_acc$targ<- tolower(lsl_acc$targ)

write.csv(lsl_acc,"../../../../blast_adult_web_sl_data/clean/lsl_acc_clean/lsl_acc.csv")


# Clean lsl files for reaction time———————————————————————————————————

# Create a new file containing only the relevant columns in the output folder
lsl_rt_clean <- function(file) {
  # Read current file
  this_file <- read.csv(file)
  this_file <- read.csv("/Users/vkozloff/Documents/blast_adult_web_sl_data/original/lsl_original/blast_a_006_lsl.csv")
  # If the responses column is column 11
  if(this_file[1,11]!=""){
    # Separates the responses into keypress, rt, and stimulus; puts this all into "rep"
    rep <- unlist(strsplit(paste(this_file[9,11]), split=',', fixed=TRUE))
  # Otherwise the reponses are in column 2
  } else {
    # Separates the responses into keypress, rt, and stimulus; puts this all into "rep"
    rep <- unlist(strsplit(paste(this_file[10,2]), split=',', fixed=TRUE))
  }
  
  #extract animation
  # If the responses column is column 11
  if(this_file[1,11]!=""){
    # ani_stim splits the stimulus from the time it was presented.
    # Is shows the whole animation sequence that the participant saw (as an array)
    ani_stim <- unlist(strsplit(paste(this_file[9,10]), split=',', fixed=TRUE))
  # Otherwise the animation_sequence is in column 11
  } else{
    ani_stim <- unlist(strsplit(paste(this_file[10,11]), split=',', fixed=TRUE))
  }
  
  key= NULL
  rt  <- NULL
  stim_press <- NULL
  stim_disp <- NULL
  time <- NULL
  
  # Takes the cell in "responses" and splits it based on colon
  # the cell in "responses" is separated into keypress, rt, and stimulus
  for (j in seq(from=2, to=length(rep), by=3)) {
    # Extracts the times of all the keypresses from "rep"
    rt<- append(rt,as.numeric(unlist(strsplit(paste(rep[j]), split=':'))[2]))
  }
  
  for (k in seq(from=3, to=length(rep), by=3)) {
    # stim_press contains all the stimuli where the participant responded
    stim_press<- append(stim_press, gsub('.{2}$','',unlist(strsplit(paste(rep[k]), split=':\"', fixed=TRUE))[2]))
  }
  
  for (i in seq(from=1, to=length(ani_stim), by=2)) {
    # Create a column for all of the stimuli that occurred during this_file exposure
    # Changes ani_stim from an array to a column.
    stim_disp<- rbind(stim_disp, gsub('.{1}$','',unlist(strsplit(paste(ani_stim[i]), split=':\"', fixed=TRUE))[2]))}
  
  # Extract the time from the ani_stim
  for (n in seq(from=2, to=length(ani_stim), by=2)) {
    time<- rbind(time, gsub('.{1}$','',unlist(strsplit(paste(ani_stim[n]), split=':', fixed=TRUE))[2]))}
  
  #These 2 tables are not the same length. 
  #Table 1 has all reaction times to all stimuli they responded to
  table1 <- data.frame(rt,stim_press)
  # Get rid of the extra " at the end of the final row
  table1$stim_press <- gsub('"',"",table1$stim_press)
  
  
  #Table 2 has info from the animation sequence, ie. when each stimulus was presented
  table2 <- data.frame(stim_disp,time)
  # Get rid of the extra } at the end of the final row
  table2$time <- gsub('}',"",table2$time)
  
  
  # Fits table 1 into table 2, depending on reaction time
  
  # Take out blank image
  # TO DO: Maybe test for one other example of case 1?    
  table2 <- table2[1:576,]
  
  table2$targ <- this_file$targ[1]
  
  # Col2 is stimpres from table 1
  table2$col2 <- "NA"
  #col1 signifies reaction time from table 1
  table2$col1 <- "NA"
  table1$stim_press <- paste(table1$stim_press)
  
  # stim_disp is the stimulus that was seen during the animation sequence
  table2$stim_disp <- paste(table2$stim_disp)
  table2$time <- as.numeric(paste(table2$time))
  
  for (i in seq(from=1,to =length(table1$stim_press),by=1)) {
    
    temp1 <- table1[i,]
    index <- 0
    min <- .Machine$integer.max
    
    # Difference between time and rt: time is when it appeared, rt is when they responded
    # Always compare to when the target was appeared. If they respond during H, subtract the H rt 
    # If they press during blank, subtract the blank RT from the time the previous stimulus appeared
    
    for  (j in seq(from=1,to =length(table2$stim_disp),by=1)) {
      
      temp2 <- table2[j,]
      if (temp2[3]=="NA") {
        if (temp1[2]==temp2[1]){
          if (abs(temp1[1]-temp2[2]) < min){
              min <- abs(temp2[2]-temp1[1])
            index <- j}
        }
      }
    }
    table2$col1[index] <- temp1[1]
    table2$col2[index] <- temp1[2]}
  
  
  table2$targ <- table2$targ[1]
  responses <- (this_file["responses"])
  full_id <- responses[1,1]
  id_char <-as.character(full_id)
  part_id <- substr(id_char, 8, 18)
  table2$part_id <- part_id
  table2$col1<-as.character(table2$col1)
  table2$col2<-as.character(table2$col2)
  # Write file
  
  write.csv(table2, "/Users/vkozloff/Desktop/presented_stimuli.csv")
  this_path<-file.path(lsl_rt_output, basename(file))
  write.csv(table2, file=(this_path))
}

# Apply function to all lsl files
for (file in lsl_original_files)
{
  lsl_rt_clean(paste0(lsl_input,file))
}

# Create one file with all lsl information
lsl <- list()
lsl_rt_clean_files <- list.files(path=lsl_rt_output, pattern="*.csv") 
for(file in lsl_rt_clean_files)
{
  assign(
    gsub(" ","",file), 
    read.csv(paste(lsl_rt_output,file,sep="")))
}

for(file in lsl_rt_clean_files){lsl <- append(lsl,list(eval(parse(text=file))))}

lsl <- do.call(rbind.data.frame, lsl)

# Standardize stimulus names
lsl$stimulus<-lsl$stim_disp
lsl$stimulus<- gsub(".png","",lsl$stimulus)
lsl$stimulus<- gsub("image/","",lsl$stimulus)
# TO DO: Make sure this is the case for all
lsl$stimulus<- tolower(lsl$stimulus)
lsl$targ<- tolower(lsl$targ)

write.csv(lsl,"../../../../blast_adult_web_sl_data/clean/lsl_rt_clean/lsl_rt.csv")
