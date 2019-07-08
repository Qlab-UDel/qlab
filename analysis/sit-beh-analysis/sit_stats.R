#  SIT STATISTICAL ANALYSIS
#  Violet Kozloff
#  Created with support from Zhenghan Qi
#  Last modified July 3rd, 2019
#  This script finds and analyzes measures of statistical learning tasks involving structured and random triplets of letters and images
#  NOTE: Accuracies have been previously calculated in sit_accuracy.R
#  NOTE: Reaction time means and slopes have been previously calculated in sit_rt_slope.R 
#  ****************************************************************************


# ************************ ANALYSIS 1: SEE IF GROUPS ARE MATCHED WITH CHI-SQUARE TEST AND T-TESTS ************************

chi_square_data <- read.csv("/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_accuracy_vocab_wide.csv")

# Subset only relevant data about the population
chi_square_vars <- c("part_id", "age", "sex", "score", "same_or_diff")
chi_square_data <- chi_square_data[chi_square_vars]
matched_data <- chi_square_data

# Chi-square test for gender
# p>0.05 tells us that they are matched for gender
gender_table <- cast(matched_data,sex~same_or_diff,value = "score",length)
chisq.test(gender_table)

# T-test for vocab score by group
# p>0.05 tells us that vocab scores are not significantly different by group
t.test(score~same_or_diff, data=matched_data) 

# T-test for age by group 
# p>0.05 tells us that ages are not significantly different by group
t.test(age~same_or_diff, data=matched_data)



# *************************** 2. TEST EFFECTS OF GROUP AND TEST PHASE ON ACCURACY *******************

indiv_accuracies <- read.csv("/Volumes/data/projects/completed_projects/sit/analysis/summaries/sit_accuracy_long.csv")


# ANOVA to test effects
# Remove accuracies for participants with no accuracy score for one task
indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_054"),]

# Remove accuracies for participants who had at least one phase with very low hit rates (<50%)
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_013"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_019"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_035"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_051"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_053"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_056"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_059"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_062"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_063"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_064"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_065"),]
# indiv_accuracies<-indiv_accuracies[which(indiv_accuracies$part_id!="sit_a_066"),]

m1=aov(accuracy~test_phase*same_or_diff+Error(part_id/test_phase), data=indiv_accuracies)
summary(m1)

#  ************* ANALYSIS 4: SEE WHETHER PERFORMANCE WAS ABOVE CHANCE WITH T-TESTS *************

# Remove accuracies for participants with no accuracy score for one task
indiv_ll_accuracies<-indiv_ll_accuracies[which(indiv_ll_accuracies$part_id!="sit_a_054"),]
indiv_vv_accuracies<-indiv_vv_accuracies[which(indiv_vv_accuracies$part_id!="sit_a_054"),]


# Test whether group performed significantly above chance 
t.test(indiv_ll_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_vv_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_vl_accuracies$accuracy, alternative= "greater", mu=0.5)
t.test(indiv_lv_accuracies$accuracy, alternative= "greater", mu=0.5)

#2-sample t-test within letter and image types to see whether group diff is significant (accuracy)
# t.test(indiv_accuracies$accuracy)






# *************************** CORRELATIONS **********************************


# Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------

# Extract relevant data from indiv_accuracies and picture_vocab
corr_data <- cast(indiv_accuracies, part_id ~ task, mean, value = 'accuracy')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)

# Add corr_data's groups of same/ different
corr_data <- cbind(corr_data, "same_or_diff")
colnames(corr_data)[9] <- "same_or_diff"
all_same <- corr_data[ which(corr_data$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- corr_data[ which(corr_data$lv>0), ]
all_diff$same_or_diff <- ("different")
corr_data <- rbind(all_same, all_diff)
corr_data <- corr_data[ which(corr_data$score>0), ]

# Separate corr_data into groups by same/ different
same_corr <- corr_data[ which(!is.na(corr_data$ll)), ]
same_corr <- same_corr[, c(2, 5, 6)]
diff_corr <- corr_data[ which(!is.na(corr_data$lv)), ]
diff_corr <- diff_corr[, c(3, 4, 6)]
same_corr$vv<-as.numeric(same_corr$vv)

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




# *************************** ANALYSIS 1: TEST EFFECTS OF GROUP, TYPE, AND TEST PHASE *******************

indiv_rt_slope <- read.csv("indiv_rt_slope.csv")

# ANOVA to test effects of type (random/ structured), test phase and group (same/ different) on RT Slope----------------------

# Find all of the ids
all_ids <- unique(indiv_rt_slope$part_id)

# Remove participants with incomplete rt slope data
incomplete_ids <- NULL

# Find the number of RT slopes for each person
for (id in all_ids){
  # Each participant should have 4 rt slopes: lingustic random, linguistic structured, non-linguistic structured, and non-linguistic random
  if (sum(indiv_rt_slope$part_id==id)!=4){
    incomplete_ids <- append (incomplete_ids, id)
  }
}

# Remove data from any participants who have an incomplete number of RT slopes
for (id in incomplete_ids){
  indiv_rt_slope <- indiv_rt_slope[which(indiv_rt_slope$part_id!=id),]
}

# RT Slope ANOVA ----------------------

# Test effects of type (random/ structured), test phase and group (same/ different) on rt slope
m2 = aov(rt_slope~domain*type*same_or_diff+Error(part_id/(domain*type)),data =indiv_rt_slope)
summary(m2)

# Error: part_id
# Df Sum Sq Mean Sq F value Pr(>F)  
# same_or_diff  1  145.7  145.72   4.406  0.041 *
#   Residuals    49 1620.8   33.08                 
# ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Error: part_id:domain
# Df Sum Sq Mean Sq F value Pr(>F)
# domain               1   53.9   53.91   2.503  0.120
# domain:same_or_diff  1    6.1    6.06   0.281  0.598
# Residuals           49 1055.4   21.54               
# 
# Error: part_id:type
# Df Sum Sq Mean Sq F value  Pr(>F)   
# type               1  329.8   329.8   9.266 0.00375 **
#   type:same_or_diff  1   46.1    46.1   1.297 0.26038   
# Residuals         49 1743.8    35.6                   
# ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Error: part_id:domain:type
# Df Sum Sq Mean Sq F value Pr(>F)
# domain:type               1   37.7   37.74   1.040  0.313
# domain:type:same_or_diff  1   11.0   10.98   0.303  0.585
# Residuals                49 1777.4   36.27 


# Mean RT ANOVA ----------------------

# Test effects of type (random/ structured), test phase and group (same/ different) on rt slope
m3 = aov(mean_rt~domain*type*same_or_diff+Error(part_id/(domain*type)),data =indiv_rt_slope)
summary(m3)


# Error: part_id
# Df  Sum Sq Mean Sq F value Pr(>F)
# same_or_diff  1       5       5       0   0.99
# Residuals    49 1493032   30470               
# 
# Error: part_id:domain
# Df Sum Sq Mean Sq F value Pr(>F)
# domain               1   2486    2486   0.758  0.388
# domain:same_or_diff  1    877     877   0.267  0.607
# Residuals           49 160717    3280               
# 
# Error: part_id:type
# Df Sum Sq Mean Sq F value   Pr(>F)    
# type               1  68160   68160  23.163 1.47e-05 ***
#   type:same_or_diff  1   6166    6166   2.095    0.154    
# Residuals         49 144188    2943                     
# ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Error: part_id:domain:type
# Df Sum Sq Mean Sq F value Pr(>F)
# domain:type               1    677   677.0   0.349  0.558
# domain:type:same_or_diff  1    194   194.4   0.100  0.753
# Residuals                49  95159  1942.0    


# *************************** ANALYSIS 2: CORRELATION MATRICES **********************************


# RT Slope Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------

# Extract relevant data from indiv_rt_slope and picture_vocab
corr_data <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'rt_slope')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)

# Add corr_data's groups of same/ different
corr_data <- cbind(corr_data, "same_or_diff")
colnames(corr_data)[9] <- "same_or_diff"
all_same <- corr_data[ which(corr_data$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- corr_data[ which(corr_data$lv>0), ]
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
diff

# lv         vl      score
# lv     1.0000000  0.3459391 -0.1547292
# vl     0.3459391  1.0000000 -0.1648938
# score -0.1547292 -0.1648938  1.0000000

# Test p-values of correlation matrices for different condition
lv_corr<-cor.test(diff_corr$lv,diff_corr$score)
lv_corr

# Pearson's product-moment correlation
# 
# data:  diff_corr$lv and diff_corr$score
# t = -0.56468, df = 13, p-value = 0.5819
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  -0.6180075  0.3883120
# sample estimates:
#        cor 
# -0.1547292 

vl_corr<-cor.test(diff_corr$vl,diff_corr$score)
vl_corr

# Pearson's product-moment correlation
# 
# data:  diff_corr$vl and diff_corr$score
# t = -0.60278, df = 13, p-value = 0.557
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  -0.6244131  0.3794181
# sample estimates:
#        cor 
# -0.1648938 

# Create correlation matrices for same condition
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")
same

# ll         vv      score
# ll     1.0000000  0.3496793 -0.4487120
# vv     0.3496793  1.0000000 -0.3239596
# score -0.4487120 -0.3239596  1.0000000

# Test p-values of correlation matrices for different condition
ll_corr<-cor.test(same_corr$ll, same_corr$score)
ll_corr

# Pearson's product-moment correlation
# 
# data:  same_corr$ll and same_corr$score
# t = -1.9446, df = 15, p-value = 0.07082
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
# -0.76448043  0.04071353
# sample estimates:
# cor 
# -0.448712 

vv_corr<-cor.test(same_corr$vv, same_corr$score)
vv_corr


# Pearson's product-moment correlation
# 
# data:  same_corr$vv and same_corr$score
# t = -1.3262, df = 15, p-value = 0.2046
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  -0.6961995  0.1855821
# sample estimates:
#        cor 
# -0.3239596 

# calculate the difference scores between structured condition and random condition within linguistic and non-linguistic domains.
rt_slope_diff = cast(indiv_rt_slope,part_id+same_or_diff+domain~type,value = "rt_slope")
rt_slope_diff$slope_diff = rt_slope_diff$structured-rt_slope_diff$random
rt_slope_diff = merge(rt_slope_diff,picture_vocab,id=1)
rt_slope_diff = cast(rt_slope_diff,part_id+score+same_or_diff~domain,value="slope_diff")
colnames(rt_slope_diff)[5]="non_linguistic"

# Plot rt slope difference

rt_slope_diff_diff = subset(rt_slope_diff,same_or_diff=="diff")
rt_slope_diff_diff_complete = rt_slope_diff_diff[complete.cases(rt_slope_diff_diff),]

# Test the correlation between the same condition's difference scores and vocabulary 
rt_slope_diff_same = subset(rt_slope_diff,same_or_diff=="same")
rt_slope_diff_same_complete = rt_slope_diff_same[complete.cases(rt_slope_diff_same),]
cor.test(rt_slope_diff_same_complete$linguistic,rt_slope_diff_same_complete$score,altermative ="less",method="pearson")
# Pearson's product-moment correlation
# 
# data:  rt_slope_diff_same_complete$linguistic and rt_slope_diff_same_complete$score
# t = 1.0223, df = 20, p-value = 0.3188
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  -0.2193692  0.5891086
# sample estimates:
#       cor 
# 0.2228502 

cor.test(rt_slope_diff_same_complete$non_linguistic,rt_slope_diff_same_complete$score,altermative ="less",method="pearson") 

# Pearson's product-moment correlation
# 
# data:  rt_slope_diff_same_complete$non_linguistic and rt_slope_diff_same_complete$score
# t = -0.4596, df = 20, p-value = 0.6508
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
# -0.5021939  0.3337634
# sample estimates:
# cor 
# -0.1022307 


# Test the correlation between the different condition's difference scores and vocabulary 
rt_slope_diff_diff = subset(rt_slope_diff,same_or_diff=="different")
rt_slope_diff_diff_complete = rt_slope_diff_diff[complete.cases(rt_slope_diff_diff),]
cor.test(rt_slope_diff_diff_complete$linguistic,rt_slope_diff_diff_complete$score,alternative = "less", method="pearson")

# Pearson's product-moment correlation

# data:  rt_slope_diff_diff_complete$linguistic and rt_slope_diff_diff_complete$score
# t = -1.8693, df = 23, p-value = 0.03718
# alternative hypothesis: true correlation is less than 0
# 95 percent confidence interval:
#  -1.00000000 -0.02983264
# sample estimates:
#        cor 
# -0.3631637 

cor.test(rt_slope_diff_diff_complete$non_linguistic,rt_slope_diff_diff_complete$score,alternative = "less", method="pearson")

# 	Pearson's product-moment correlation
# 
# data:  rt_slope_diff_diff_complete$non_linguistic and rt_slope_diff_diff_complete$score
# t = -0.20274, df = 23, p-value = 0.4206
# alternative hypothesis: true correlation is less than 0
# 95 percent confidence interval:
#   -1.0000000  0.2990003
# sample estimates:
#   cor 
# -0.04223738 

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
corrplot(rt_slope_correlations, method = "circle", insig = "p-value")

# Mean RT Correlation matrices-------------------------------------------------------------------------------------------------------------------------------------

# Extract relevant data from indiv_rt_slope and picture_vocab
corr_data <- cast(indiv_rt_slope, part_id ~ task, mean, value = 'mean_rt')
corr_data <- merge(corr_data, picture_vocab, by = "part_id", all=TRUE)

# Add corr_data's groups of same/ different
corr_data <- cbind(corr_data, "same_or_diff")
colnames(corr_data)[9] <- "same_or_diff"
all_same <- corr_data[ which(corr_data$ll>0), ]
all_same$same_or_diff <- ("same")
all_diff <- corr_data[ which(corr_data$lv>0), ]
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
# Pearson's product-moment correlation
# 
# data:  diff_corr$lv and diff_corr$score
# t = -0.19232, df = 23, p-value = 0.8492
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  -0.4284177  0.3607731
# sample estimates:
#         cor 
# -0.04006983 

vl_corr<-cor.test(diff_corr$vl,diff_corr$score)
vl_corr

# Pearson's product-moment correlation
# 
# data:  diff_corr$vl and diff_corr$score
# t = -0.63044, df = 23, p-value = 0.5346
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
# -0.4997298  0.2791735
# sample estimates:
# cor 
# -0.1303346 

# Create correlation matrices for same condition
same <- cor(same_corr, method = c("pearson"),use="pairwise.complete.obs")

# Test p-values of correlation matrices for different condition
ll_corr<-cor.test(same_corr$ll, same_corr$score)
ll_corr

# Pearson's product-moment correlation
# 
# data:  same_corr$ll and same_corr$score
# t = -1.2305, df = 20, p-value = 0.2328
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
# -0.6177986  0.1760042
# sample estimates:
# cor 
# -0.26529 

vv_corr<-cor.test(same_corr$vv, same_corr$score)
vv_corr


# Pearson's product-moment correlation
# 
# data:  same_corr$vv and same_corr$score
# t = -0.99696, df = 20, p-value = 0.3307
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
# -0.5854849  0.2246283
# sample estimates:
# cor 
# -0.2175868 

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
# Pearson's product-moment correlation
# 
# data:  rt_diff_same_complete$linguistic and rt_diff_same_complete$score
# t = 0.0070777, df = 20, p-value = 0.4972
# alternative hypothesis: true correlation is greater than 0
# 95 percent confidence interval:
# -0.3590307  1.0000000
# sample estimates:
# cor 
# 0.001582609 
cor.test(rt_diff_same_complete$non_linguistic,rt_diff_same_complete$score,alternative = "greater", method="pearson")
# Pearson's product-moment correlation
# 
# data:  rt_diff_same_complete$non_linguistic and rt_diff_same_complete$score
# t = -0.048734, df = 20, p-value = 0.5192
# alternative hypothesis: true correlation is greater than 0
# 95 percent confidence interval:
# -0.3698525  1.0000000
# sample estimates:
# cor 
# -0.01089653 
rt_diff_diff = subset(rt_diff,same_or_diff=="different")
cor.test(rt_diff_diff$linguistic,rt_diff_diff$score, alternative = "greater", method="pearson")
# Pearson's product-moment correlation
# 
# data:  rt_diff_diff$linguistic and rt_diff_diff$score
# t = -0.2116, df = 23, p-value = 0.5829
# alternative hypothesis: true correlation is greater than 0
# 95 percent confidence interval:
# -0.3754843  1.0000000
# sample estimates:
# cor 
# -0.0440798 

cor.test(rt_diff_diff$non_linguistic,rt_diff_diff$score, alternative = "less", method="pearson")
# Pearson's product-moment correlation
# 
# data:  rt_diff_diff$non_linguistic and rt_diff_diff$score
# t = -1.4688, df = 23, p-value = 0.07771
# alternative hypothesis: true correlation is less than 0
# 95 percent confidence interval:
# -1.00000000  0.04896847
# sample estimates:
# cor 
# -0.2928459 

plot(rt_diff_diff$non_linguistic,rt_diff_diff$score)




#  ************* SEE WHETHER RT slope is below zero: T-TESTS *************

# test whether in each condition rt slope was different from zero.
t.test(sll$rt_slope, mu=0)
# One Sample t-test
# 
# data:  sll$rt_slope
# t = 1.3134, df = 26, p-value = 0.2005
# alternative hypothesis: true mean is not equal to 0
# 95 percent confidence interval:
#   -0.8045023  3.6518356
# sample estimates:
#   mean of x 
# 1.423667 
t.test(slv$rt_slope, mu=0)
# One Sample t-test
# 
# data:  slv$rt_slope
# t = -1.3345, df = 28, p-value = 0.1928
# alternative hypothesis: true mean is not equal to 0
# 95 percent confidence interval:
#   -3.8256434  0.8073538
# sample estimates:
#   mean of x 
# -1.509145 
t.test(svl$rt_slope, mu=0) 
# One Sample t-test
# 
# data:  svl$rt_slope
# t = -1.7802, df = 28, p-value = 0.0859
# alternative hypothesis: true mean is not equal to 0
# 95 percent confidence interval:
#   -5.9930192  0.4198882
# sample estimates:
#   mean of x 
# -2.786566 
t.test(svv$rt_slope, mu=0)
# One Sample t-test
# 
# data:  svv$rt_slope
# t = -1.0701, df = 28, p-value = 0.2937
# alternative hypothesis: true mean is not equal to 0
# 95 percent confidence interval:
#   -3.978967  1.248181
# sample estimates:
#   mean of x 
# -1.365393 




# test whether in each condition rt slope was significantly less than zero.
t.test(sll$rt_slope, alternative="less", mu=0)

# One Sample t-test
# 
# data:  sll$rt_slope
# t = 1.3134, df = 26, p-value = 0.8997
# alternative hypothesis: true mean is less than 0
# 95 percent confidence interval:
#   -Inf 3.272536
# sample estimates:
#   mean of x 
# 1.423667 
t.test(slv$rt_slope, alternative="less", mu=0)
# One Sample t-test
# 
# data:  slv$rt_slope
# t = -1.3345, df = 28, p-value = 0.0964
# alternative hypothesis: true mean is less than 0
# 95 percent confidence interval:
#   -Inf 0.4146267
# sample estimates:
#   mean of x 
# -1.509145 
t.test(svl$rt_slope, alternative="less", mu=0)
# One Sample t-test
# 
# data:  svl$rt_slope
# t = -1.7802, df = 28, p-value = 0.04295
# alternative hypothesis: true mean is less than 0
# 95 percent confidence interval:
#   -Inf -0.1237172
# sample estimates:
#   mean of x 
# -2.786566 
t.test(svv$rt_slope, alternative="less", mu=0) 
# One Sample t-test
# 
# data:  svv$rt_slope
# t = -1.0701, df = 28, p-value = 0.1468
# alternative hypothesis: true mean is less than 0
# 95 percent confidence interval:
#   -Inf 0.805089
# sample estimates:
#   mean of x 
# -1.365393 
