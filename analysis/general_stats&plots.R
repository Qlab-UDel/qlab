##This script can be used to run general statistics and plot those analyses.
##Load all libraries
library(Hmisc)
library(dplyr)
library(QuantPsyc)
library(ggplot2)
library(scales)
library(ggbeeswarm)

#Establish where your data is located (this is the path to your data)
setwd("/Volumes/data/projects/blast/summer_2019/")

#State the name of your spreadsheet
df=read.csv('summerblast_324-400anova.csv')

#Establish your variables of interest
colnames(df)[colnames(df)=="amplitude"] <- "DV" #change the name of your DV
colnames(df)[colnames(df)=="bin"] <- "IV_1" #change the name of your IV_1
colnames(df)[colnames(df)=="bin"] <- "IV_2" #change the name of your IV_2 (if more than 1)

##One-Way ANOVA 
##Your data must be organized as one column with your IV (group) and one column with your DV data
is.factor(df$IV_1) #the output from this must be TRUE
model1<- aov(df$DV~df$IV_1)
summary(model1)

boxplot(df$DV~df$IV_1, main="Mean ERP Amplitude by Condition", col= (c("palevioletred4", "royalblue3", "palegreen4"))) #can modify the colors and the title (green text)

##T-tests
#Must make your variables of interest numeric
df$DV = as.numeric(df$DV)
df$IV_1 = as.numeric(df$IV_1)
df$IV_2 = as.numeric(df$IV_2)

#IF you have more groups than 2 to compare (i.e. you had a threeway anova and want to just compare 2) remove one group:
df<-df[!(df$IV_1=="syllable"),]

#Paired samples
t.test(df$DV, df$IV_1, paired = TRUE, alternative = "two.sided")
boxplot(df$DV~df$IV_1, main="Mean ERP Amplitude by Condition", col= (c("palevioletred4", "royalblue3"))) #can modify the colors and the title (green text)

#Independent samples
t.test(df$DV~df$IV_1)
boxplot(df$DV~df$IV_1, main="Mean ERP Amplitude by Condition", col= (c("palevioletred4", "royalblue3"))) #can modify the colors and the title (green text)

##Correlation analysis between behavioral measures and ERP
#Read in different data (my data needs to be organized differently than for a one-way ANOVA)
df_corr=read.csv('summerblast_324-400_corr.csv')

# #identify if there are any outliers in the data, do this once 
df$var <- df_corr$srs_std #this is the only thing you need to change. Try each variable.
summary(df$var)
low <- quantile(df$var,0.25,na.rm=TRUE)
high <- quantile(df$var,0.75,na.rm=TRUE)
IQR <- high-low
inner <- (1.5*IQR)
outer <- (3*IQR)
low_out <- (low-outer)
high_out <- (high+outer)
low_in <- (low-inner)
high_in <- (high+inner)

#Run correlation matrix
#Pearson
mycor <- rcorr(as.matrix(df_corr), type="pearson")
r_pear<-mycor$r #Pearsons R
p_pear<-mycor$P #P values

#Spearman
mycor_s <- rcorr(as.matrix(df_corr), type="spearman")
r_spear<-mycor_s$r #Spearmans R
p_spear<-mycor_s$P #P values

#Store the output
#Pearson's output
write.csv(p_pear,"P_pear.csv")
write.csv(r_pear,"R_pear.csv")

#Spearman's output
write.csv(p_spear,"P_spear.csv")
write.csv(r_spear,"R_spear.csv")

####PLOTTING#####
# Basic scatter plot
df_corr$var1 <- df_corr$nih_flanker_std #Change variable of interest
df_corr$var2 <- df_corr$voice #Change variable of interest

#Change titles
ggplot(df_corr, aes(x=var1, y=var2)) + geom_point(size=3, color="navy blue", shape=19) + labs(title="Voice & Inhibition/Attention",
                                                                                                          x="NIH Flanker", y = "Voice ERP") + theme_classic() +theme(plot.title = element_text(hjust = 0.5)) + theme(text = element_text(family="Times", size=20, color="black")) + geom_smooth(method=lm)

