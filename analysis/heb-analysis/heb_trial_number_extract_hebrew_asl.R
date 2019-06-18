#R Script for HEB
#Loads individual files and identifies which trial occurs at test. It numbers these trials consistently across all participants and merges it with the larger df.
library(tidyr)
rm(list=ls())

# Max print output.
options(max.print=1e9)
options(dplyr.print_max = 1e10)

#set directory 
setwd("/Users/julieschneider/Julie_Personal/Projects/HEB/data/")
df_arnon=read.csv('ASL-both-sessions-adults-formatted-clean.csv')
df_overall=read.csv('heb_final_asltrial.csv')

#Merge two columns into one (need to do this as presentation of files could be counterbalanced)
df_sort<-unite(df_arnon, comb_col, c('nonword','word'), remove=FALSE)

#Create new column that extracts words only (not foils) from stimuli column
df_sort$trial_number <- NA

df_sort$trial_number <-ifelse(grepl("dukame.*tomubi|tomubi.*dukame", df_sort$comb_col, ignore.case = T, fixed = FALSE), 1,  #DUKAME
                              ifelse(grepl("dukame.*nadime|nadime.*dukame", df_sort$comb_col, ignore.case = T, fixed = FALSE), 2,
                                     ifelse(grepl("dukame.*duloga|duloga.*dukame", df_sort$comb_col, ignore.case = T, fixed = FALSE), 3,
                                            ifelse(grepl("dukame.*gekalu|gekalu.*dukame", df_sort$comb_col, ignore.case = T, fixed = FALSE), 4,
                                                   ifelse(grepl("dukame.*kibeno|kibeno.*dukame", df_sort$comb_col, ignore.case = T, fixed = FALSE), 5,
                                                          ifelse(grepl("gedino.*tomubi|tomubi.*gedino", df_sort$comb_col, ignore.case = T, fixed = FALSE), 6,  #GEDINO
                                                                 ifelse(grepl("gedino.*nadime|nadime.*gedino", df_sort$comb_col, ignore.case = T, fixed = FALSE), 7,
                                                                        ifelse(grepl("gedino.*duloga|duloga.*gedino", df_sort$comb_col, ignore.case = T, fixed = FALSE), 8,
                                                                               ifelse(grepl("gedino.*gekalu|gekalu.*gedino", df_sort$comb_col, ignore.case = T, fixed = FALSE), 9,
                                                                                      ifelse(grepl("gedino.*kibeno|kibeno.*gedino", df_sort$comb_col, ignore.case = T, fixed = FALSE), 10,
                                                                                             ifelse(grepl("kimuga.*tomubi|tomubi.*kimuga", df_sort$comb_col, ignore.case = T, fixed = FALSE), 11, #KIMUGA
                                                                                                    ifelse(grepl("kimuga.*nadime|nadime.*kimuga", df_sort$comb_col, ignore.case = T, fixed = FALSE), 12,
                                                                                                           ifelse(grepl("kimuga.*duloga|duloga.*kimuga", df_sort$comb_col, ignore.case = T, fixed = FALSE), 13,
                                                                                                                  ifelse(grepl("kimuga.*gekalu|gekalu.*kimuga", df_sort$comb_col, ignore.case = T, fixed = FALSE), 14,
                                                                                                                         ifelse(grepl("kimuga.*kibeno|kibeno.*kimuga", df_sort$comb_col, ignore.case = T, fixed = FALSE), 15,
                                                                                                                                ifelse(grepl("nalobi.*tomubi|tomubi.*nalobi", df_sort$comb_col, ignore.case = T, fixed = FALSE), 16,  #NALOBI
                                                                                                                                       ifelse(grepl("nalobi.*nadime|nadime.*nalobi", df_sort$comb_col, ignore.case = T, fixed = FALSE), 17,
                                                                                                                                              ifelse(grepl("nalobi.*duloga|duloga.*nalobi", df_sort$comb_col, ignore.case = T, fixed = FALSE), 18,
                                                                                                                                                     ifelse(grepl("nalobi.*gekalu|gekalu.*nalobi", df_sort$comb_col, ignore.case = T, fixed = FALSE), 19,
                                                                                                                                                            ifelse(grepl("nalobi.*kibeno|kibeno.*nalobi", df_sort$comb_col, ignore.case = T, fixed = FALSE), 20,
                                                                                                                                                                   ifelse(grepl("tobelu.*tomubi|tomubi.*tobelu", df_sort$comb_col, ignore.case = T, fixed = FALSE), 21,   #TOBELU 
                                                                                                                                                                          ifelse(grepl("tobelu.*nadime|nadime.*tobelu", df_sort$comb_col, ignore.case = T, fixed = FALSE), 22,
                                                                                                                                                                                 ifelse(grepl("tobelu.*duloga|duloga.*tobelu", df_sort$comb_col, ignore.case = T, fixed = FALSE), 23,
                                                                                                                                                                                        ifelse(grepl("tobelu.*gekalu|gekalu.*tobelu", df_sort$comb_col, ignore.case = T, fixed = FALSE), 24,
                                                                                                                                                                                               ifelse(grepl("tobelu.*kibeno|kibeno.*tobelu", df_sort$comb_col, ignore.case = T, fixed = FALSE), 25, 0)))))))))))))))))))))))))
#delete unnecessary rows
df_sort<-df_sort[!(df_sort$Procedure.Block.=="exposureProc"),]

#add new column and data to overall dataframe
df_overall[(df_overall$language == "hebrew") & (df_overall$task == 1),]$trial_number<-df_sort$trial_number
write.csv(df_overall, "heb_trial_clean_031719.csv")

