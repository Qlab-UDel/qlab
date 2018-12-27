#R Script for HEB
#Organizes data on a trial by trial basis to compute accuracy, RT, and order of foils/words
#Only run during initial setup
setwd("/Users/julieschneider/Julie_Personal/Projects/HEB")
overall_df=read.csv('heb_msl_trial.csv')
overall_df$trial_order<-NA
#subject=read.csv('subject.csv')

#load subject data and create column that evaluates whether foil or word came first on each trial
df=read.csv('data/a_008_heb_msl.csv')
df <- df[!grepl("null",df$rt),]
df$trial_response <- NA
df$trial_response <- ifelse(df$key_press == 50 & df$correct == 'true', 'foil', ifelse(df$key_press == 49 & df$correct == 'true', 'foil', ifelse(df$key_press == 50 & df$correct == 'false', 'word', ifelse(df$key_press == 49 & df$correct == 'false', 'word','null'))))
df$trial_accuracy <- ifelse(df$correct == 'true', '1', '0')

#combine just the word and foil items for the individual into the larger building group list
export<-df[c(3:27),(10:11)]
#temporary<-export #just for subject 1
temporary<-rbind(temporary,export)
#export<-df[c(3:27),"trial_accuracy"]
#test<-c(temporary,export)

#combine merged group list with large overall dataframe
overall_df$trial_accuracy<-temporary
save(overall_df,file="overall_trial_data.Rda")
save(temporary,file = "temporary_accuracy_info.Rda")
write.csv(export,"heb_msl_delete_2.csv")
