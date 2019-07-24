#  BLAST assessment analysis
#  Violet Kozloff and Anqi Hu
#  Last updated April 22nd, 2019
#  This script analyzes assessment scores from at-home activities, statistical learning tasks, and in-lab assessments
#  ****************************************************************************

# Prepare workspace ------------------------------------------------------------

# Install libraries
library(reshape)

# Remove objects in environment
rm(list=ls())

# Read in online scores
online_scores <- read.csv("/Volumes/data-1/projects/blast/data_summaries/blast_online_child/online_child_overall_summary.csv")  
# Read in home RSR scores
home_rsr_scores <- read.csv("/Volumes/data-1/projects/blast/data_summaries/blast_online_child/breakdown/blast_spoli_rsr_home_scores.csv")
# Read in lab assessment scores
lab_scores <- read.csv("/Volumes/data-1/projects/blast/data_summaries/blast_in_lab_child/blast_child_in_lab_score_summary.csv")
# Read in demographic data
demographic_data <- read.csv("/Volumes/data-1/projects/blast/demographic_data/blast_bucld_demographic_data.csv")

# Merge files
all_scores <- merge(lab_scores, home_rsr_scores, by = "part_id", all = TRUE)
all_scores <- merge(all_scores,online_scores,by="part_id", all= TRUE)
all_data <- merge(demographic_data,all_scores,by="part_id", all.x= TRUE)

# Check for duplicated IDs
test_duplicates <- duplicated(all_data$part_id)


# Set output path
output_path <- ("/Volumes/data-1/projects/blast/data_summaries/blast_online_child/")


# I. ALL ASD V. TD: SL TASKS ------------------------------------------------------------


### A. Check whether groups are matched for age and gender


###### 1. Check whether groups are matched for gender

# TO DO: Clean up these extra columns
#Find the number of Male ASD, Female ASD, Male TD, Female TD
gender<- all_data[all_data$gender != "", c("part_id","group","gender","in_lab")]
gender_long <- melt(gender, id.vars = c("part_id", "group","gender"))
gender_wide <- cast(gender_long, gender~group, length)

# Chi-square on gender
# p<0.05 tells us that they are not matched for gender between group
chisq.test(gender_wide)
# TO DO: Waiting on SPARK to tell us remaining genders for a few last participants

# Pearson's Chi-squared test with Yates' continuity correction
# 
# data:  gender_wide
# X-squared = 12.944, df = 1, p-value = 0.0003209
# 
# Warning message:
#   In chisq.test(gender_wide) : Chi-squared approximation may be incorrect


###### 2. Check whether groups are matched for age

# Combine ages
all_data$age_at_lab_visit <- gsub("NA", NA, all_data$age_at_lab_visit)
all_data$age_at_lab_visit <- gsub("Null", NA, all_data$age_at_lab_visit)
all_data$age_at_gjt <- gsub("NA", NA, all_data$age_at_gjt)
all_data$age_at_gjt <- gsub("Null", "", all_data$age_at_gjt)
ages_all <- all_data[c("part_id","group","age_at_lab_visit", "age_at_gjt", "in_lab")]
# Convert factors to numeric
ages_all$age_at_gjt <- as.numeric(ages_all$age_at_gjt)

# T-test for age by group 
t.test(age_at_gjt~group, data=ages_all)

# Welch Two Sample t-test
# 
# data:  age_at_gjt by group
# t = -2.0488, df = 11.753, p-value = 0.06349
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -42.083929   1.343188
# sample estimates:
#   mean in group ASD  mean in group TD 
# 100.4074          120.7778 


### B. SL accuracy by group

# Separate the ASD and TD groups
asd_accuracy <- all_data[which(all_data$group=="ASD"),]
td_accuracy <- all_data[which(all_data$group=="TD"),]

###### Test whether each group's performance is above chance for each task

t.test(td_accuracy$lsl_accuracy, mu=0.5, alternative= "greater")
# One Sample t-test
# 
# data:  td_accuracy$lsl_accuracy
# t = 1.7437, df = 5, p-value = 0.07083
# alternative hypothesis: true mean is greater than 0.5
# 95 percent confidence interval:
#   0.4813793       Inf
# sample estimates:
#   mean of x 
# 0.6196667

t.test(td_accuracy$ssl_accuracy, mu=0.5, alternative= "greater")
# One Sample t-test
# 
# data:  td_accuracy$ssl_accuracy
# t = 0.8237, df = 5, p-value = 0.2238
# alternative hypothesis: true mean is greater than 0.5
# 95 percent confidence interval:
#   0.4623955       Inf
# sample estimates:
#   mean of x 
# 0.526 

t.test(td_accuracy$tsl_accuracy, mu=0.5, alternative= "greater")
# One Sample t-test
# 
# data:  td_accuracy$tsl_accuracy
# t = 2.7059, df = 6, p-value = 0.01765
# alternative hypothesis: true mean is greater than 0.5
# 95 percent confidence interval:
#   0.5503357       Inf
# sample estimates:
#   mean of x 
# 0.6785714 

t.test(td_accuracy$vsl_accuracy, mu=0.5, alternative= "greater")
# One Sample t-test
# 
# data:  td_accuracy$vsl_accuracy
# t = 1.2918, df = 6, p-value = 0.122
# alternative hypothesis: true mean is greater than 0.5
# 95 percent confidence interval:
#   0.4436744       Inf
# sample estimates:
#   mean of x 
# 0.6117143 

t.test(asd_accuracy$lsl_accuracy, mu=0.5, alternative= "greater")
# One Sample t-test
# 
# data:  asd_accuracy$lsl_accuracy
# t = 2.5558, df = 33, p-value = 0.007692
# alternative hypothesis: true mean is greater than 0.5
# 95 percent confidence interval:
#   0.5217614       Inf
# sample estimates:
#   mean of x 
# 0.5644118 


t.test(asd_accuracy$ssl_accuracy, mu=0.5, alternative= "greater")
# One Sample t-test
# 
# data:  asd_accuracy$ssl_accuracy
# t = 0.70306, df = 34, p-value = 0.2434
# alternative hypothesis: true mean is greater than 0.5
# 95 percent confidence interval:
#   0.4849855       Inf
# sample estimates:
#   mean of x 
# 0.5106857 

t.test(asd_accuracy$tsl_accuracy, mu=0.5, alternative= "greater")
# One Sample t-test
# 
# data:  asd_accuracy$tsl_accuracy
# t = 2.05, df = 33, p-value = 0.02419
# alternative hypothesis: true mean is greater than 0.5
# 95 percent confidence interval:
#   0.5080051       Inf
# sample estimates:
#   mean of x 
# 0.5458824 

t.test(asd_accuracy$vsl_accuracy, mu=0.5, alternative= "greater")
# One Sample t-test
# 
# data:  asd_accuracy$vsl_accuracy
# t = 2.7483, df = 35, p-value = 0.004704
# alternative hypothesis: true mean is greater than 0.5
# 95 percent confidence interval:
#   0.5274048       Inf
# sample estimates:
#   mean of x 
# 0.5711389 


###### Two-sample t-tests: compare groups' performance on each task


t.test(lsl_accuracy~group, data=all_data)
# Welch Two Sample t-test
# 
# data:  lsl_accuracy by group
# t = -0.75579, df = 6.4218, p-value = 0.4766
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -0.2313348  0.1208250
# sample estimates:
#   mean in group ASD  mean in group TD 
# 0.5644118         0.6196667 
t.test(ssl_accuracy~group, data=all_data)
# Welch Two Sample t-test
# 
# data:  ssl_accuracy by group
# t = -0.43713, df = 7.5278, p-value = 0.6743
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -0.09699203  0.06636346
# sample estimates:
#   mean in group ASD  mean in group TD 
# 0.5106857         0.5260000 
t.test(tsl_accuracy~group, data=all_data)
# Welch Two Sample t-test
# 
# data:  tsl_accuracy by group
# t = -1.9041, df = 7.4417, p-value = 0.09612
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -0.29550509  0.03012694
# sample estimates:
#   mean in group ASD  mean in group TD 
# 0.5458824         0.6785714 
# t.test(ssl_accuracy~group, data=all_data)
t.test(vsl_accuracy~group, data=all_data)
# Welch Two Sample t-test
# 
# data:  vsl_accuracy by group
# t = -0.4495, df = 7.1135, p-value = 0.6664
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -0.2533358  0.1721850
# sample estimates:
#   mean in group ASD  mean in group TD 
# 0.5711389         0.6117143 



# Anova test: (did not remove people who have one score)
sl_accuracy <- all_data[c("vsl_accuracy", "lsl_accuracy", "tsl_accuracy","ssl_accuracy","part_id","gender","group")]
sl_accuracy_long <- melt(sl_accuracy, by.vars = c("part_id", "group","gender"), measure.vars = c("vsl_accuracy","lsl_accuracy","tsl_accuracy","ssl_accuracy"))

#variable is category of sl task; value is accuracy
m1 = aov(value~variable*group+Error(part_id/variable), data = sl_accuracy_long)
summary(m1)


# II. IN-LAB ASD V. TD: SL TASKS + IN-LAB ASSESSMENTS ------------------------------------------------------------

### A. Check whether groups are matched for age and gender
###### 1. Check whether groups are matched for gender

# Subset the participants who came to the lab
# Summarize numbers of participants in each group
gender_in_lab <- all_data[which(all_data$gender != "" & all_data$in_lab == "TRUE"), c("part_id","group","gender","in_lab")]
gender_in_lab_long <- melt(gender_in_lab, id.vars = c("part_id", "group","gender"))
gender_in_lab_wide <- cast(gender_in_lab_long, gender~group,length)

# p<0.05 tells us that they are not matched for gender between group
chisq.test(gender_in_lab.wide)
# 
# Pearson's Chi-squared test with Yates' continuity correction
# 
# data:  gender_in_lab.wide
# X-squared = 8.4632, df = 1, p-value = 0.003624
# 
# Warning message:
#   In chisq.test(gender_in_lab.wide) :
#   Chi-squared approximation may be incorrect


###### 2. Check whether groups are matched for age

# Subset the participants who came to the lab
ages_in_lab <- all_data[c("part_id","group","age_at_lab_visit", "age_at_gjt", "in_lab")]
ages_in_lab <- ages_in_lab[which(ages_in_lab$in_lab==TRUE),]
# Convert factors to numeric
ages_in_lab$age_at_lab_visit <- as.numeric(ages_in_lab$age_at_lab_visit)
ages_in_lab$age_at_gjt <- as.numeric(ages_in_lab$age_at_gjt)

# Run t-test
# T-test for age by group 
# p<0.05 tells us that ages are significantly different by group
t.test(age_at_lab_visit~group, data=ages_in_lab) 
# Welch Two Sample t-test
# 
# data:  age_at_lab_visit by group
# t = -2.7698, df = 11.063, p-value = 0.01815
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -48.869655  -5.608978
# sample estimates:
#   mean in group ASD  mean in group TD 
# 93.53846         120.77778 


# p<0.05 tells us that ages are significantly different by group
t.test(age_at_gjt~group, data=ages_in_lab)
# 
# Welch Two Sample t-test
# 
# data:  age_at_gjt by group
# t = -2.9543, df = 9.6849, p-value = 0.01491
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -49.421111  -6.818205
# sample estimates:
#   mean in group ASD  mean in group TD 
# 92.76923         120.88889 

#paired t-test
#p>0.05 tells us that age_at_lab_visit and age_at_gjt are not significantly different across groups
t.test(ages_in_lab$age_at_lab_visit, ages_in_lab$age_at_gjt, paired = TRUE)
# 
# Paired t-test
# 
# data:  ages_in_lab$age_at_lab_visit and ages_in_lab$age_at_gjt
# t = 0.21919, df = 21, p-value = 0.8286
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -3.472258  4.290440
# sample estimates:
#   mean of the differences 
# 0.4090909 




### B. SL accuracy versus assessment scores
# TO DO: Correlation matrix




# III. SPOLI + BLAST ASD: SL TASKS + GJT/RSR ------------------------------------------------------------

### A. SL V. GJT/RSR (HOME)
# TO DO: Correlation matrix

### B. ARE SSL AND LSL MORE RELATED TO GJT/RSR THAN TSL AND VSL?
# TO DO: Check p-values of t-tests











# missing_ids <- setdiff(all_scores$part_id, demographic_data$part_id)
# missing_ids2 <- setdiff(demographic_data$part_id, all_scores$part_id)
#TO DO: check for missing ids if(length(all_scores[which(all_scores$part_id%in%missing_ids),])$ids!=0){print"one or more missing ids"}


