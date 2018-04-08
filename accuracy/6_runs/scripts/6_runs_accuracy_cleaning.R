#  6_RUNS ACCURACY FILE CLEANING
#  Violet Kozloff
#  March 11, 2018
#  This script cleans the auditory and visual files from the 6-run pilot for accuracy analysis
#  ****************************************************************************


# Prepare files ------------------------------------------------------------

# Move to folder from GitHub (Mac when folder is on desktop)
setwd("/Users/jasinskagroup/Desktop/QLAB/psychopy_sl_beh-master/accuracy/6_runs/scripts")

# Remove objects in environment
rm(list=ls())

# Set up auditory input file path
auditory_input_path <- ("../original_data/auditory/")
auditory_files<- list.files(path=auditory_input_path, pattern="*.csv")

# Separate tsl and ssl file paths
tsl_files <- list.files(path=auditory_input_path, pattern="*6.csv")
ssl_files <- list.files(path=auditory_input_path, pattern="*3.csv")

# Set up audiotry ouput file path
auditory_output_path <- "../cleaned_data/auditory/"

# Set up visual file path
visual_input_path <- ("../original_data/visual/")
visual_files<- list.files(path=visual_input_path, pattern="*.csv")

# Separate vsl and lsl file paths
vsl_files <- list.files(path=visual_input_path, pattern="*6.csv")
lsl_files <- list.files(path=visual_input_path, pattern="*3.csv")

# Set up visual output file path
visual_output_path <- "../cleaned_data/visual/"


# Clean auditory files----------------------------------------------

# tsl: create a new file containing only the relevant columns in the output folder
tsl_cleaning <- function(file) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("key_resp_6.corr", "Run","PartID","expName")
  newdata <- current_file[value]
  # Standardize "key_resp.corr" column across runs
  names(newdata)[names(newdata) == 'key_resp_6.corr'] <- 'key_resp.corr'
  # Remove any lines prior to test phase
  newdata <- newdata[ which(!is.na(newdata$key_resp.corr)), ]
  # Add domain
  newdata$modality <- rep("non-linguistic",nrow(newdata))
  # Add task
  newdata$task <- rep("TSL",nrow(newdata))
  #Write file
  this_path<-file.path(auditory_output_path, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all tsl files
for (file in tsl_files)
{
  tsl_cleaning(paste0(auditory_input_path,file))
}

# ssl: create a new file containing only the relevant columns in the output folder
ssl_cleaning <- function(file) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("question_key_resp.corr","Run","PartID","expName")
  newdata <- current_file[value]
  # Standardize "key_resp.corr" column across runs
  names(newdata)[names(newdata) == 'question_key_resp.corr'] <- 'key_resp.corr'
  # Remove any lines prior to test phase
  newdata <- newdata[ which(!is.na(newdata$key_resp.corr)), ]
  # Add domain
  newdata$modality <- rep("linguistic",nrow(newdata))
  # Add task
  newdata$task <- rep("SSL",nrow(newdata))
  # Write file
  this_path<-file.path(auditory_output_path, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all ssl files
for (file in ssl_files)
{
  ssl_cleaning(paste0(auditory_input_path,file))
}


# Clean visual files ----------------------------------------------------------

# lsl: create a new file containing only the relevant columns in the output folder
lsl_cleaning <- function(file) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("question_key_resp.corr","Run","PartID","expName")
  newdata <- current_file[value]
  # Standardize "key_resp.corr" column across runs
  names(newdata)[names(newdata) == 'question_key_resp.corr'] <- 'key_resp.corr'
  # Remove any lines prior to test phase
  newdata <- newdata[ which(!is.na(newdata$key_resp.corr)), ]
  # Add domain
  newdata$modality <- rep("linguistic",nrow(newdata))
  # Add task
  newdata$task <- rep("LSL",nrow(newdata))
  # Write file
  this_path<-file.path(visual_output_path, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all lsl files
for (file in lsl_files)
{
  lsl_cleaning(paste0(visual_input_path,file))
}

# vsl: create a new file containing only the relevant columns in the output folder
vsl_cleaning <- function(file) {
  current_file <- read.csv(file)
  # Select relevant columns
  value <- c("question_key_resp.corr","Run","PartID","expName")
  newdata <- current_file[value]
  # Standardize "key_resp.corr" column across runs
  names(newdata)[names(newdata) == 'question_key_resp.corr'] <- 'key_resp.corr'
  # Remove any lines prior to test phase
  newdata <- newdata[ which(!is.na(newdata$key_resp.corr)), ]
  # Add domain
  newdata$modality <- rep("non-linguistic",nrow(newdata))
  # Add task
  newdata$task <- rep("VSL",nrow(newdata))
  # Write file
  this_path<-file.path(visual_output_path, basename(file))
  write.csv(newdata, file=(this_path))
}

# Apply function to all vsl files
for (file in vsl_files)
{
  vsl_cleaning(paste0(visual_input_path,file))
}

