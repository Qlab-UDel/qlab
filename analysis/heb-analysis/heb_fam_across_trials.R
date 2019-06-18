#R Script for HEB
#Loads individual files and matches familiarity rating scores with where that stimulus occurred in the file

#set directory 
setwd("/Users/julieschneider/Julie_Personal/Projects/HEB/data/")

# List input files
subject_files <- list.files(pattern="*asl.csv")

#initialize variable to hold data
df_asl_famtrial <- NULL

# Loop on list of all subjects
for (file in subject_files)
{
#Load in .csv file
df=read.csv(file)
#Create new column that extracts words only (not foils) from stimuli column
df$word <- NA
df$word <- ifelse(grepl("dukame", df$stimulus, ignore.case = T), "dukame",
                  ifelse(grepl("gedino", df$stimulus, ignore.case = T), "gedino",
                         ifelse(grepl("kimuga", df$stimulus, ignore.case = T), "kimuga",
                                ifelse(grepl("nalobi", df$stimulus, ignore.case = T), "nalobi",
                                       ifelse(grepl("tobelu", df$stimulus, ignore.case = T), "tobelu","foil")))))

#Create new column that extracts familiarity ratings
df$famrate <- NA
df$famrate <- ifelse(grepl("1", df$responses, ignore.case = T), "1",
                  ifelse(grepl("2", df$responses, ignore.case = T), "2",
                         ifelse(grepl("3", df$responses, ignore.case = T), "3",
                                ifelse(grepl("4", df$responses, ignore.case = T), "4",
                                       ifelse(grepl("5", df$responses, ignore.case = T), "5","0")))))

#Order the presentation of the familiarity ratings
famSubset <- df[grep("survey-likert", df$trial_type), ]
famorder <- 1:6
famSubset <-cbind(famSubset,famorder)

#Sort familiarity ratings based on word column
df[which(df$word == 'gedino'),]$famrate<-famSubset[which(famSubset$famorder == 1),]$famrate
df[which(df$word == 'dukame'),]$famrate<-famSubset[which(famSubset$famorder == 2),]$famrate
df[which(df$word == 'kimuga'),]$famrate<-famSubset[which(famSubset$famorder == 3),]$famrate
df[which(df$word == 'nalobi'),]$famrate<-famSubset[which(famSubset$famorder == 4),]$famrate
df[which(df$word == 'tobelu'),]$famrate<-famSubset[which(famSubset$famorder == 5),]$famrate

#Extract 25 familiarity ratings in order
extracted_data=df[which(df$word != 'foil'),]$famrate
  
# Combine data from current file
df_asl_famtrial<-rbind(df_asl_famtrial,extracted_data)

#transpose from double to single column
asl_fam_trial <- c(df_asl_famtrial)
}

#change directories and open master data
setwd("/Users/julieschneider/Julie_Personal/Projects/HEB/R_scripts/")
df_overall=read.csv('heb_df_final.csv')

#add new column and data to overall dataframe
df_overall$fam_ratings <- NA
df_overall[which(df_overall$task == 1),]$fam_ratings<-asl_fam_trial
write.csv(df_overall, "heb_withfam_Final.csv")
