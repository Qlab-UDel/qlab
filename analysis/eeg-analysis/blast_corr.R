##This script correlates behavioral blast data with ERP components. It also allows you to plot scatterplots and correct for multiple comparisons. 
library(Hmisc)
library(dplyr)

setwd("/Users/julieschneider/Julie_Personal/Projects/BLAST/R/")
df=read.csv('online_adult_overall_summary.csv')

#Remove low frequency outliers (blast 015, 020, 031)
df<- df[!grepl("blast_a_031", df$part_id),]
df<- df[!grepl("blast_a_020", df$part_id),]
df<- df[!grepl("blast_a_015", df$part_id),]
df <- df[,-(1)] 

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
df$domain_diff_late_whole_MMN = as.numeric(df$domain_diff_late_whole_MMN)
df$global_short_late_whole_MMN = as.numeric(df$global_short_late_whole_MMN)
df$local_high_late_whole_MMN = as.numeric(df$local_high_late_whole_MMN)
df$part_id = as.numeric(df$part_id)
df$SSL_entropy = as.numeric(df$SSL_entropy)

##Defining subsets of the larger dataframe
#behcorr_df <- df[c(1,3:15)]

##Correlation analysis
#Pearson
mycor <- rcorr(as.matrix(df), type="pearson")
r_pear<-mycor$r #Pearsons R
p_pear<-mycor$P #P values

#Spearman
mycor_s <- rcorr(as.matrix(df), type="spearman")
r_spear<-mycor_s$r #Spearmans R
p_spear<-mycor_s$P #P values

#Store the output
write.csv(r_spear,"R_spear_withentropy.csv")

#FDR Correction
ps_forcor=read.csv('P_spear_9values_onetail.csv')
ps_forcor<- ps_forcor[,-(1)] 
ps_forcor<-as.numeric(unlist(ps_forcor))
p_spear_fdr<-p.adjust(ps_forcor, method = "fdr", n = length(ps_forcor))

ps_forcor_erp=read.csv('P_spear_6comparisons.csv')
ps_forcor_erp <- ps_forcor_erp[,-(1)] 
ps_forcor_erp<-as.numeric(unlist(ps_forcor_erp))
p_spear_erp_fdr<-p.adjust(ps_forcor_erp, method = "fdr", n = length(ps_forcor_erp))

#Store FDR Correction output
write.csv(p_spear_fdr,"P_spear_fdrcorrection_3comparisons_onetail.csv")

##One-sample t-test to determine if online performance is above chance
t.test(df$ssl_acc, mu = 50, alternative = "two.sided") #significant p < .001
t.test(df$ssl_mean_rt, mu = 50, alternative = "two.sided") #significant p < .001
t.test(df$kbit_matrices_std, mu = 100, alternative = "two.sided") #significant p < .001


##Paired sample t-test
t.test(df$tsl_acc, df$ssl_acc, paired = TRUE, alternative = "two.sided") #not significant p = 0.2069
t.test(df$tsl_rt_slope, df$ssl_rt_slope, paired = TRUE, alternative = "two.sided") #not significant p = 0.786

##Check Outliers
outlier_values <- boxplot.stats(low_freq$MMN_late_whole)$out  # outlier values.
boxplot(low_freq$MMN_late_whole, main="MMN Amplitude", boxwex=0.1)
mtext(paste("Outliers: ", paste(outlier_values, collapse=", ")), cex=0.6)

##Remove Outliers
source("http://goo.gl/UUyEzD")
outlierKD(dat, variable)


####PLOTTING#####

library(ggplot2)
library(scales)
library(ggbeeswarm)
library(Hmisc)

# Basic scatter plot
ggplot(df, aes(x=ssl_acc, y=srs_std)) + geom_point(size=3, color="navy blue", shape=19) + labs(title="Speech Accuracy x SRS Standard",
       
# Basic scatter plot
ggplot(df, aes(x=tsl_rt_slope, y=ssl_rt_slope)) + geom_point(size=3, color="navy blue", shape=19) + labs(title="TSL Slope x SSL Slope",
                                                                                                                  x="TSL Slope", y = "SSL Slope") + theme(plot.title = element_text(hjust = 0.5)) + geom_smooth(method=lm)
