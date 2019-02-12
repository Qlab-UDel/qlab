#R Script for HEB
#Organizes data on a trial by trial basis to compute accuracy, RT, and order of foils/words

#set directory 
setwd("/Users/julieschneider/Julie_Personal/Projects/HEB/data/")

# List input files
subject_files <- list.files(pattern="*msl.csv")

#initialize variables to hold data
df_msl_trial<- NULL
df_msl_accuracy<- NULL

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
msl_trial<-df[c(3:27),(10)]
msl_accuracy<-df[c(3:27),(11)]

df_msl_trial <-cbind(df_msl_trial,msl_trial)
df_msl_accuracy <-cbind(df_msl_accuracy,msl_accuracy)

}

msl_trial <- c(df_msl_trial) #concatenate data from rows to columns
msl_accuracy <- c(df_msl_accuracy) #concatenate data from rows to columns

#combine newly extracted data into overall dataframe
setwd("/Users/julieschneider/Julie_Personal/Projects/HEB/R_scripts/")
heb_trial=read.csv('heb_corrected_data.csv')
msl_df<- heb_trial[which(heb_trial$task == 0),]
msl_df$trial_order<-msl_trial
msl_df$trial_accuracy<-msl_accuracy
save(msl_df,file = "temporary_msldf.Rda")


#after completing both asl and msl, combine the two
df=rbind(asl_df,msl_df)
write.csv(df,"heb_df_final.csv")
