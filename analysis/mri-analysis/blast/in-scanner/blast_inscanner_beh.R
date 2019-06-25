library(Hmisc)
library(dplyr)
library(reshape2)


setwd("/Users/julieschneider/Julie_Personal/Projects/BLAST/R/")
df=read.csv('blast_in_scanner_beh.csv')

##Transforming variables into numeric
df$age = as.numeric(df$age)
df$ctopp_bw_std = as.numeric(df$ctopp_bw_std)
df$ctopp_nwr_std = as.numeric(df$ctopp_nwr_std)
df$ctopp_el_std = as.numeric(df$ctopp_el_std)
df$kbit_matrices_std = as.numeric(df$kbit_matrices_std)
df$nih_pvt_std = as.numeric(df$nih_pvt_std)
df$nih_flanker_std = as.numeric(df$nih_flanker_std)
df$srs_std = as.numeric(df$srs_std)
df$tsl_acc = as.numeric(df$tsl_acc)
df$tsl_mean_rt = as.numeric(df$tsl_mean_rt)
df$tsl_rt_slope = as.numeric(df$tsl_rt_slope)
df$ssl_acc = as.numeric(df$ssl_acc)
df$ssl_mean_rt = as.numeric(df$ssl_mean_rt)
df$ssl_rt_slope = as.numeric(df$ssl_rt_slope)
df$random_syllable_mean = as.numeric(df$random_syllable_mean)
df$random_tone_mean = as.numeric(df$random_tone_mean)
df$structured_syllable_mean = as.numeric(df$structured_syllable_mean)
df$structured_tone_mean = as.numeric(df$structured_tone_mean)
df$structured_image_mean = as.numeric(df$structured_image_mean)
df$structured_letter_mean = as.numeric(df$structured_letter_mean)
df$random_tsl_rt_slope = as.numeric(df$random_tsl_rt_slope)
df$random_ssl_rt_slope = as.numeric(df$random_ssl_rt_slope)
df$structured_tsl_rt_slope = as.numeric(df$structured_tsl_rt_slope)
df$structured_ssl_rt_slope = as.numeric(df$structured_ssl_rt_slope)
df$part_id = as.numeric(df$part_id)

#Get summary 
summary(df)

##Correlation analysis
#Pearson
mycor <- rcorr(as.matrix(df), type="pearson")
r_pear<-mycor$r #Pearsons R
p_pear<-mycor$P #P values

#Store the correlation output
write.csv(p_pear,"P_pear_inscanner_beh.csv")

#Run a ttest to compare conditional differences
tone_df <- data.frame(a = c(df[,"tsl_mean_rt"], df[,"structured_tone_mean"]))
tone_df$group<-(tone_df[c(1:26),2] = "online")
tone_df$group<-(tone_df[c(27:52),2] = "inscanner")

TSL_ttest<- t.test(tone_df$a~tone_df$V2)
print(TSL_ttest)

# Welch Two Sample t-test
# 
# data:  tone_df$a by tone_df$V2
# t = 2.0685, df = 41.402, p-value = 0.04488
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   2.46068 203.03549
# sample estimates:
#   mean in group inscanner    mean in group online 
# 437.6975                334.9494 

speech_df <- data.frame(a = c(df[,"ssl_mean_rt"], df[,"structured_syllable_mean"]))
speech_df$group<-(speech_df[c(1:26),2] = "online")
speech_df$group<-(speech_df[c(27:52),2] = "inscanner")

SSL_ttest<- t.test(speech_df$a~speech_df$V2)
print(SSL_ttest)

# Welch Two Sample t-test
# 
# data:  speech_df$a by speech_df$V2
# t = 1.7552, df = 33.218, p-value = 0.08845
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -11.56827 157.20648
# sample estimates:
#   mean in group inscanner    mean in group online 
# 593.8585                521.0394 

