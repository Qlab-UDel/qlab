#R Script for HEB
#Organizes data on a trial by trial basis to compute accuracy, RT, and order of foils/words

#set directory 
setwd("/Users/julieschneider/Julie_Personal/Projects/HEB/data/")

# List input files
subject_files <- list.files(pattern="*asl.csv")

#initialize variables to hold data
df_asl_trial<- NULL
df_asl_accuracy<- NULL

# Loop on list of all subjects
for (file in subject_files)
{
  #Load in .csv file
  df=read.csv(file)

  #load subject data and create column that evaluates whether foil or word came first on each trial
  df <- df[!grepl("null",df$rt),]
  df$trial_response <- NA
  df$trial_response <- ifelse(df$key_press == 50 & df$correct == 'true', 'foil', 
                                                   ifelse(df$key_press == 49 & df$correct == 'true', 'word', 
                                                          ifelse(df$key_press == 50 & df$correct == 'false', 'word', 
                                                                 ifelse(df$key_press == 49 & df$correct == 'false', 'foil','null'))))
  df$trial_accuracy <- ifelse(df$correct == 'true', '1', '0')

#combine just the word and foil items for the individual into the larger building group list
asl_trial<-df[c(3:27),(11)]
asl_accuracy<-df[c(3:27),(12)]

df_asl_trial <-cbind(df_asl_trial,asl_trial)
df_asl_accuracy <-cbind(df_asl_accuracy,asl_accuracy)

}

asl_trial <- c(df_asl_trial) #concatenate data from rows to columns
asl_accuracy <- c(df_asl_accuracy) #concatenate data from rows to columns

#combine newly extracted data into overall dataframe
setwd("/Users/julieschneider/Julie_Personal/Projects/HEB/R_scripts/")
heb_trial=read.csv('heb_corrected_data.csv')
asl_df<- heb_trial[which(heb_trial$task == 1),]
asl_df$trial_order<-asl_trial
asl_df$trial_accuracy<-asl_accuracy
save(asl_df,file = "temporary_asldf.Rda")

#write.csv(export,"heb_msl_delete.csv")
