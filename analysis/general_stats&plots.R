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

#Line Plots for group means and standard error

#You will need a data frame with 4 columns: group, condition, mean, standard error.
#Change your_data_frame, your_condition_column (experiment conditions), 
#your_mean (means in each condition/group combination), your_std_error (standard error)

pd <- position_dodge(width = 0.2)

your_data_frame %>%
  ggplot(aes(x = your_condition_column, y = your_mean, group = your_group_column)) +
  geom_line(aes(linetype = your_group_column, color = your_group_column), position = pd, size = 1.8) +
  geom_errorbar(aes(ymin = your_mean - your_std_error, ymax = your_mean + your_std_error), width = .1, position = pd) +
  geom_point(aes(color = your_group_column), size = 4, position = pd,show.legend = FALSE) + 
  geom_point(size = 3, color = "white", position = pd) +
  labs(title = "Your Plot Title", # Change Title
       x = "Your X-axis label",  # Change axes labels
       y = "Your Y-axis label") + 
  theme(plot.title = element_text(hjust = 0.5)) + # Center or left align title
  theme(
    plot.title = element_text(size=16, face="bold"), 
    axis.title.x = element_text(size=14, face="bold"),
    axis.title.y = element_text(size=14, face="bold"),
    axis.text=element_text(size=12, face = "bold")
  ) +
  theme(legend.text=element_text(size=14, face="bold"),
        legend.title=element_text(size=15, face="bold")) +
  theme(
    panel.background = element_rect(fill = "white"),         # Set plot background to white
    legend.key  = element_rect(fill = "white"),              # Set legend item backgrounds to white
    axis.line.x = element_line(colour = "black", size = 1),  # Add line to x axis
    axis.line.y = element_line(colour = "black", size = 1)   # Add line to y axis
  ) 


# Correlation Plot with multiple groups and tasks

#Use scale_shape_manual and scale_color_manual with caution. 
#This is used for complex plots that need customized dot shape and colors.

your_data_frame %>%
  ggplot(
    aes(x= your_value_for_correlation, 
        y = your_other_value_for_correlation,
        color = your_group,
        shape = your_group
    )) +
  theme(legend.title = element_blank()) + #Remove legend title
  geom_point(size = 4) +
  scale_shape_manual(values=c(16, 16, 17, 17))+ #Manually change the dot shape for each group
  scale_color_manual(values = c("#756bb1", "#fec44f", "#756bb1", "#fec44f")) + #Manually change the colors of dots for each group
  labs(title = "Your Title",
       y = bquote(bold("Your X-axis Label"~(mm^3))),  # Change x-axis label with mm^3 as unit
       x = "Your Y-axis label") +
  theme(plot.title = element_text(hjust = 0.23)) + # Center or left align title
  theme(
    plot.title = element_text(size=16, face="bold"), # Format legend text
    axis.title.x = element_text(size=14, face="bold"),
    axis.title.y = element_text(size=14, face="bold"),
    axis.text=element_text(size=12, face = "bold")
  ) +
  theme(legend.text=element_text(size=14, face="bold")) +
  theme(
    panel.background = element_rect(fill = "white"),         # Set plot background to white
    legend.key  = element_rect(fill = "white"),              # Set legend item backgrounds to white
    axis.line.x = element_line(colour = "black", size = 1),  # Add line to x axis
    axis.line.y = element_line(colour = "black", size = 1)   # Add line to y axis
  ) 

#Uncomment below if you would like to add linear lines and R and p-values to your correlation plots
#This allows you to subset your data event further, so that the line does not have to have the same grouping
#as the dot plot above

# +
#   geom_smooth(data = subset(your_data_frame, your_column == "your_variable_to_subset"),
#               aes(x=your_x_axis_value, y=your_y_axis_value),
#               method=lm, se=FALSE, show.legend = F, inherit.aes = F, color = "#756bb1") + #inherit.aes is necessary to override the grouping above
#   stat_cor(data = subset(your_data_frame, your_column == "your_variable_to_subset"), #add the R and p value to the plot
#            aes(x=your_x_axis_value, y=your_x_axis_value), method = "pearson", label.x = your_customized_x_position, label.y = your_customized_y_position,
#            inherit.aes = F, color = "#756bb1", size = 5) 



