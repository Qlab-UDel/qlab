#  SIT STATISTICAL ANALYSIS
#  Violet Kozloff
#  Created with support from Zhenghan Qi
#  Last modified February 27th, 2020
#  This script finds and analyzes measures of statistical learning tasks involving structured and random triplets of letters and images
#  NOTE: Accuracies have been previously calculated in sit_accuracy.R
#  NOTE: Reaction time means and slopes have been previously calculated in sit_rt_slope.R 
#  ****************************************************************************

# install.packages("tidyverse", "car", "ez", "reshape2", "lme4")
require("tidyverse")
require("car")
require ("ez")
require ("reshape2")
require ("lme4")

library(lmerTest)
library(reshape)
library(reshape2)

rm(list=ls())


# ************************ SEE IF GROUPS ARE MATCHED FOR DEMOGRAPHICS WITH CHI-SQUARE TEST AND T-TESTS ************************

chi_square_data <- read.csv("/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_accuracy_vocab_wide.csv")
picture_vocab <- read.csv("/Volumes/data/projects/completed_projects/sit/analysis/data/clean/vocab_clean/vocab_clean.csv")


# Subset only relevant data about the population
chi_square_vars <- c("part_id", "age", "sex", "score", "same_or_diff")
matched_data <- chi_square_data[chi_square_vars]

# Chi-square test for gender
gender_table <- cast(matched_data,sex~same_or_diff,value = "score",length)
chisq.test(gender_table)

# T-test for vocab score by group
t.test(score~same_or_diff, data=matched_data) 

# Find means for each group
same_vocab<- mean((filter(chi_square_data, same_or_diff=="same"))$score, na.rm=TRUE)
diff_vocab<- mean((filter(chi_square_data, same_or_diff=="different"))$score, na.rm=TRUE)


# T-test for age by group 
t.test(age~same_or_diff, data=matched_data)



# *************************** TEST EFFECTS OF GROUP AND TEST PHASE ON ACCURACY *******************

indiv_accuracies <- read.csv("/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_accuracy_long.csv")

task_acc_lmer <- lmer(accuracy ~ test_phase * same_or_diff + (1 | part_id), data = indiv_accuracies, REML = FALSE)
summary(task_acc_lmer)

#  ************* SEE WHETHER ACCURACY PERFORMANCE WAS ABOVE CHANCE WITH T-TESTS *************

indiv_ll_accuracies <- dplyr::filter(indiv_accuracies, task =="ll")
indiv_vv_accuracies <- dplyr::filter(indiv_accuracies, task =="vv")
indiv_lv_accuracies <- dplyr::filter(indiv_accuracies, task =="lv")
indiv_vl_accuracies <- dplyr::filter(indiv_accuracies, task =="vl")


# Remove accuracies for participants with no accuracy score for one task
indiv_ll_accuracies<-indiv_ll_accuracies[which(indiv_ll_accuracies$part_id!="sit_a_054"),]
indiv_vv_accuracies<-indiv_vv_accuracies[which(indiv_vv_accuracies$part_id!="sit_a_054"),]


# Test whether group performed significantly above chance 
t.test(indiv_ll_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_vv_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_vl_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_lv_accuracies$accuracy, alternative= "greater", mu=0.5)



# *************************** CORRELATIONS **********************************


# Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------

# Extract relevant data from indiv_accuracies and picture_vocab
corr_data <- cast(indiv_accuracies, part_id ~ task, mean, value = 'accuracy')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)

# Add corr_data's groups of same/ different
corr_data <- dplyr::rename(corr_data, same_or_diff = group)
same_corr <- dplyr::filter(corr_data, same_or_diff == "same")
diff_corr <- dplyr::filter(corr_data, same_or_diff == "different")

diff_corr <- dplyr::select(corr_data, lv, vl, score)
same_corr <- dplyr::select(corr_data, ll, vv, score)

# Create correlation matrices for different condition
diff <- cor(diff_corr, method = c("pearson"),use="pairwise.complete.obs")

# Test p-values of correlation matrices for different condition
lv_corr<-cor.test(diff_corr$lv,diff_corr$score)
lv_corr
vl_corr<-cor.test(diff_corr$vl,diff_corr$score)
vl_corr

# Create correlation matrices for same condition
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")

# Test p-values of correlation matrices for different condition
ll_corr<-cor.test(same_corr$ll, same_corr$score) 
ll_corr
vv_corr<-cor.test(same_corr$vv, same_corr$score) 
vv_corr




# *************************** RT SLOPE MODEL *******************

indiv_rt_slope <- read.csv("/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_indiv_rt_slope.csv")

# Model to test effects of type (random/ structured), test phase and group (same/ different) on RT Slope----------------------
 
# Find all of the ids
all_ids <- unique(indiv_rt_slope$part_id)

# Find the number of RT slopes for each person
incomplete_ids <- NULL

for (id in all_ids){
  # Each participant should have 4 rt slopes: lingustic random, linguistic structured, non-linguistic structured, and non-linguistic random
   if (nrow(dplyr::filter(indiv_rt_slope, part_id==id))!=4){
     incomplete_ids <- append (incomplete_ids, id)
   }
 }


rt_slope_lmer <- lmer(rt_slope ~ domain * type * same_or_diff + (1 | part_id), data = indiv_rt_slope, REML = FALSE)
summary(rt_slope_lmer)



mean(filter(indiv_rt_slope, same_or_diff=="different")$rt_slope)
mean(filter(indiv_rt_slope, same_or_diff=="same")$rt_slope)

mean(filter(indiv_rt_slope, type=="random")$rt_slope)
mean(filter(indiv_rt_slope, type=="structured")$rt_slope)


indiv_rts <- dplyr::select(read.csv("/Volumes/data/projects/completed_projects/sit/analysis/summaries/indiv_rts.csv"), -X)

indiv_rt_lmer <- lmer(rt ~ domain * type * same_or_diff + (1 | part_id) + (1|target_item), data = indiv_rts, REML = FALSE)



# *************************** CORRELATION MATRICES **********************************
 

# RT Slope Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------
 
# Extract relevant data from indiv_rt_slope and picture_vocab
corr_data <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'rt_slope')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)
 
# Add corr_data's groups of same/ different
colnames(corr_data)[9] <- "same_or_diff"
all_same <- filter(corr_data, !is.na(ll))
all_diff <- filter(corr_data, !is.na(lv))
corr_data <- rbind(all_same, all_diff)

# Separate corr_data into groups by same/ different
same_corr <- corr_data[ which(!is.na(corr_data$ll)), ]
same_corr <- same_corr[, c(2, 5, 6)]
diff_corr <- corr_data[ which(!is.na(corr_data$lv)), ]
diff_corr <- diff_corr[, c(3, 4, 6)]
 
# Create correlation matrices for different condition
diff <- cor(diff_corr, method = c("pearson"),use="pairwise.complete.obs")
diff

 
# Test p-values of correlation matrices for different condition: these are the individual rt slopes against vocab
lv_corr<-cor.test(diff_corr$lv,diff_corr$score)
lv_corr


vl_corr<-cor.test(diff_corr$vl,diff_corr$score)
vl_corr

# Create correlation matrices for same condition
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")
same

same_corr2<-cor.test(same_corr$vv,same_corr$score)
same_corr2


# Test p-values of correlation matrices for different condition
ll_corr<-cor.test(same_corr$ll, same_corr$score)
ll_corr

vv_corr<-cor.test(same_corr$vv, same_corr$score)
vv_corr
 
# calculate the difference scores between structured condition and random condition within linguistic and non-linguistic domains.
rt_slope_diff = cast(indiv_rt_slope,part_id+same_or_diff+domain~type,value = "rt_slope")
rt_slope_diff$slope_diff = rt_slope_diff$structured-rt_slope_diff$random
rt_slope_diff = merge(rt_slope_diff,picture_vocab,id=1)
rt_slope_diff = cast(rt_slope_diff,part_id+score+same_or_diff~domain,value="slope_diff")
 
# Plot rt slope difference
 
rt_slope_diff_diff = subset(rt_slope_diff,same_or_diff=="diff")
rt_slope_diff_diff_complete = rt_slope_diff_diff[complete.cases(rt_slope_diff_diff),]
 
# Test the correlation between the same condition's difference scores and vocabulary 
rt_slope_diff_same = subset(rt_slope_diff,same_or_diff=="same")
rt_slope_diff_same_complete = rt_slope_diff_same[complete.cases(rt_slope_diff_same),]
cor.test(rt_slope_diff_same_complete$linguistic,rt_slope_diff_same_complete$score,alternative ="less",method="pearson")

colnames(rt_slope_diff_same_complete)[5] <- "non_linguistic"
cor.test(rt_slope_diff_same_complete$non_linguistic,rt_slope_diff_same_complete$score,alternative ="less",method="pearson") 

# Test the correlation between the different condition's difference scores and vocabulary 
rt_slope_diff_diff = subset(rt_slope_diff,same_or_diff=="different")
rt_slope_diff_diff_complete = rt_slope_diff_diff[complete.cases(rt_slope_diff_diff),]
cor.test(rt_slope_diff_diff_complete$linguistic,rt_slope_diff_diff_complete$score,alternative = "less", method="pearson")


vocab_corr<- rt_slope_diff_diff_complete
vocab_corr <- dplyr::rename(vocab_corr, image = `non-linguistic`)
vocab_corr <- dplyr::rename(vocab_corr, letter = linguistic)
vocab_corr <- dplyr::rename(vocab_corr, group = same_or_diff)
vocab_corr <- melt(data = data.frame(vocab_corr), id.vars = c("part_id", "group", "score"), measure.vars = c("image", "letter"))
vocab_corr <- dplyr::rename(vocab_corr, rt_slope_diff = value)
vocab_corr <- dplyr::rename(vocab_corr, Stimulus = variable)

# Plot vocabulary correlation
ggplot(data=vocab_corr, aes(x=rt_slope_diff,y=score,color=Stimulus, shape=Stimulus)) + 
   geom_point(size=10) + 
   geom_smooth(method=lm, se=FALSE, aes(linetype = Stimulus)) + 
   ylab(label="Vocabulary Score") +
   theme(panel.border = element_rect(colour='black', fill=NA),  panel.background = element_blank()) + 
   xlab(label="Difference in RT Slope Between \nStructured and Random Condition") +
   scale_colour_hue(l = 50) +
   theme_classic() +
   theme(plot.title = element_text(size = 30),
         axis.text.x = element_text(size = 30),
         axis.text.y = element_text(size = 30),
         axis.title.x = element_text(size = 30),
         axis.title.y = element_text(size = 30),
         legend.title = element_text(size = 30),
         legend.text = element_text(size = 30))


colnames(rt_slope_diff_diff_complete)[5]<- "non_linguistic"
cor.test(rt_slope_diff_diff_complete$non_linguistic,rt_slope_diff_diff_complete$score,alternative = "less", method="pearson")

heading_names <- c("score", "linguistic", "non_linguistic")
test_same <- data.frame(rt_slope_diff_same_complete[heading_names])
test_diff <- data.frame(rt_slope_diff_diff_complete[heading_names])
names(test_same) <- gsub ("linguistic", "linguistic_same", names(test_same))
names(test_diff) <- gsub ("linguistic", "linguistic_diff", names(test_diff))
test_same[,"linguistic_diff"] <- NA
test_same[,"non_linguistic_diff"] <- NA
test_diff[,"linguistic_same"] <- NA
test_diff[,"non_linguistic_same"] <- NA
test<-(rbind(test_same,test_diff))
test[is.na(test)] <- 0
names(test)<-gsub("_", " ", names(test))
 
test$part_id <- NULL
rt_slope_correlations <- cor(test, use="pairwise.complete.obs")

# Mean RT Correlations-------------------------------------------------------------------------------------------------------------------------------------
# 
# Extract relevant data from indiv_rt_slope and picture_vocab
corr_data <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'mean_rt')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)

# Add corr_data's groups of same/ different
corr_data <- cbind(corr_data, "same_or_diff")
colnames(corr_data)[9] <- "same_or_diff"
all_same <- corr_data[ which(!is.na(corr_data$ll)), ]
all_same$same_or_diff <- ("same")
all_diff <- corr_data[ which(!is.na(corr_data$lv>0)), ]
all_diff$same_or_diff <- ("different")
corr_data <- rbind(all_same, all_diff)
corr_data <- corr_data[ which(corr_data$score>0), ]
 
# Separate corr_data into groups by same/ different
same_corr <- corr_data[ which(!is.na(corr_data$ll)), ]
same_corr <- same_corr[, c(2, 5, 6)]
diff_corr <- corr_data[ which(!is.na(corr_data$lv)), ]
diff_corr <- diff_corr[, c(3, 4, 6)]
 
# Create correlation matrices for different condition
diff <- cor(diff_corr, method = c("pearson"),use="pairwise.complete.obs")
 
# Test p-values of correlation matrices for different condition
lv_corr<-cor.test(diff_corr$lv,diff_corr$score)
lv_corr

vl_corr<-cor.test(diff_corr$vl,diff_corr$score)
vl_corr

# Create correlation matrices for same condition
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")
 
# Test p-values of correlation matrices for different condition
ll_corr<-cor.test(same_corr$ll, same_corr$score)
ll_corr
 
vv_corr<-cor.test(same_corr$vv, same_corr$score)
vv_corr

# calculate the mean rt difference scores between structured condition and random condition 
# within linguistic and non-linguistic domainsfor individual difference analyses
rt_diff = cast(indiv_rt_slope,part_id+same_or_diff+domain~type,value = "mean_rt")
rt_diff$meanrt_diff = rt_diff$structured-rt_diff$random
rt_diff = merge(rt_diff,picture_vocab,id=1)
rt_diff = cast(rt_diff,part_id+score+same_or_diff~domain,value="meanrt_diff")
colnames(rt_diff)[5]="non_linguistic"
rt_diff_same = subset(rt_diff,same_or_diff=="same")
rt_diff_same_complete = rt_diff_same[complete.cases(rt_diff_same),]
cor.test(rt_diff_same_complete$linguistic,rt_diff_same_complete$score,alternative = "greater", method="pearson")
cor.test(rt_diff_same_complete$non_linguistic,rt_diff_same_complete$score,alternative = "greater", method="pearson")
rt_diff_diff = subset(rt_diff,same_or_diff=="different")
cor.test(rt_diff_diff$linguistic,rt_diff_diff$score, alternative = "greater", method="pearson")
cor.test(rt_diff_diff$non_linguistic,rt_diff_diff$score, alternative = "less", method="pearson")

 
# #  ************* SEE WHETHER RT slope is below zero: T-TESTS *************

sll <- filter (indiv_rt_slope, type =="structured" &  task == "ll")
slv <- filter (indiv_rt_slope, type =="structured" &  task == "lv")
svl <- filter (indiv_rt_slope, type =="structured" &  task == "vl")
svv <- filter (indiv_rt_slope, type =="structured" &  task == "vv")
rll <- filter (indiv_rt_slope, type =="random" &  task == "ll")
rlv <- filter (indiv_rt_slope, type =="random" &  task == "lv")
rvl <- filter (indiv_rt_slope, type =="random" &  task == "vl")
rvv <- filter (indiv_rt_slope, type =="random" &  task == "vv")


# test whether in each condition rt slope was significantly less than zero.
t.test(sll$rt_slope, alternative="less", mu=0)

t.test(svv$rt_slope, alternative="less", mu=0) 

t.test(slv$rt_slope, alternative="less", mu=0)

t.test(svl$rt_slope, alternative="less", mu=0)


