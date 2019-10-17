install.packages("ggplot2")
install.packages("Hmisc")
install.packages("reshape")
install.packages("ggbeeswarm")
install.packages("ggsignif")
install.packages("psych")

#Set up current working directory
setwd ("/Users/jojohu/Documents/in_scanner_beh_analysis")

# Read in in-scanner behavioral data
visual_data <- read.csv("adult_in_scanner_visual_behavioral.csv")
auditory_data <-
  read.csv("adult_in_scanner_auditory_behavioral.csv")

#Visual data--------------------------------------------------------------------------------------
#Plot the basic data------------------------------------------------------------------------------
#Remove the participants who do not have data
visual_data <-
  visual_data[-which(visual_data$visual_part_id == "blast_a_044"),]
visual_data$structured_vsl_rt_slope <-
  as.numeric(as.character(visual_data$structured_vsl_rt_slope))
visual_data$random_vsl_rt_slope <-
  as.numeric(as.character(visual_data$random_vsl_rt_slope))
visual_data$structured_lsl_rt_slope <-
  as.numeric(as.character(visual_data$structured_lsl_rt_slope))
visual_data$random_lsl_rt_slope <-
  as.numeric(as.character(visual_data$random_lsl_rt_slope))
visual_data$structured_image_mean_rt <-
  as.numeric(as.character(visual_data$structured_image_mean_rt))
visual_data$random_image_mean_rt <-
  as.numeric(as.character(visual_data$random_image_mean_rt))
visual_data$structured_letter_mean_rt <-
  as.numeric(as.character(visual_data$structured_letter_mean_rt))
visual_data$random_letter_mean_rt <-
  as.numeric(as.character(visual_data$random_letter_mean_rt))

#Plot histograms and dot plots to look at the distribution of the data first (Normal Distribution? Outliners?)
#Save the plots into a pdf file
pdf("visual_data_distribution_sanity_check.pdf")

hist(visual_data$structured_letter_mean_rt)
hist(visual_data$random_letter_mean_rt)

hist(visual_data$structured_lsl_rt_slope)
hist(visual_data$random_lsl_rt_slope)

hist(visual_data$structured_image_mean_rt)
hist(visual_data$random_image_mean_rt)

hist(visual_data$structured_vsl_rt_slope)
hist(visual_data$random_vsl_rt_slope)

library("ggplot2")
ggplot(visual_data,
       aes(x = visual_part_id, y = structured_letter_mean_rt)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(visual_data, aes(x = visual_part_id, y = random_letter_mean_rt)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

ggplot(visual_data,
       aes(x = visual_part_id, y = structured_lsl_rt_slope)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(visual_data, aes(x = visual_part_id, y = random_lsl_rt_slope)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

ggplot(visual_data,
       aes(x = visual_part_id, y = structured_image_mean_rt)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(visual_data, aes(x = visual_part_id, y = random_image_mean_rt)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

ggplot(visual_data,
       aes(x = visual_part_id, y = structured_vsl_rt_slope)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(visual_data, aes(x = visual_part_id, y = random_vsl_rt_slope)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

dev.off()
#----------------------------------------------------------------------------------------------

#Learning Effect Analysis-------------------------------------------------------------------------------
# Run Welch's paired t-test on mean RT
# p<0.05 tells us that random has significantly longer mean RT than structured, and there is learning effect
t.test(
  visual_data$random_letter_mean_rt,
  visual_data$structured_letter_mean_rt,
  paired = TRUE,
  alternative = "greater"
)
# Paired t-test
# 
# data:  visual_data$random_letter_mean_rt and visual_data$structured_letter_mean_rt
# t = 4.6579, df = 26, p-value = 4.146e-05
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   78.12416      Inf
# sample estimates:
#   mean of the differences 
# 123.2586

t.test(
  visual_data$random_image_mean_rt,
  visual_data$structured_image_mean_rt,
  paired = TRUE,
  alternative = "greater"
)
# Paired t-test
# 
# data:  visual_data$random_image_mean_rt and visual_data$structured_image_mean_rt
# t = 2.0863, df = 26, p-value = 0.02345
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   4.959587      Inf
# sample estimates:
#   mean of the differences 
# 27.17859 


t.test(
  visual_data$random_lsl_rt_slope,
  visual_data$structured_lsl_rt_slope,
  paired = TRUE,
  alternative = "greater"
)
# Paired t-test
# 
# data:  visual_data$random_lsl_rt_slope and visual_data$structured_lsl_rt_slope
# t = 1.0047, df = 26, p-value = 0.1621
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   -1.30384      Inf
# sample estimates:
#   mean of the differences 
# 1.869148 

t.test(
  visual_data$random_vsl_rt_slope,
  visual_data$structured_vsl_rt_slope,
  paired = TRUE,
  alternative = "greater"
)
# Paired t-test
# 
# data:  visual_data$random_vsl_rt_slope and visual_data$structured_vsl_rt_slope
# t = 2.8486, df = 26, p-value = 0.004236
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   1.709207      Inf
# sample estimates:
#   mean of the differences 
# 4.259852 
#---------------------------------------------------------------------------------------------

#RT Difference Analysis-----------------------------------------------------------------------
#Calculate the normalized mean RT difference between structured and random: (structured - random)/ random
visual_data$letter_mean_rt_difference <-
  (visual_data$structured_letter_mean_rt - visual_data$random_letter_mean_rt) /
  visual_data$random_letter_mean_rt

visual_data$image_mean_rt_difference <-
  (visual_data$structured_image_mean_rt - visual_data$random_image_mean_rt) / visual_data$random_image_mean_rt

#Calculate the normalized RT Slope difference between structured and random: (structured - random)/ random
visual_data$lsl_rt_slope_difference <-
  (visual_data$structured_lsl_rt_slope - visual_data$random_lsl_rt_slope) /
  visual_data$random_lsl_rt_slope

visual_data$vsl_rt_slope_difference <-
  (visual_data$structured_vsl_rt_slope - visual_data$random_vsl_rt_slope) / visual_data$random_vsl_rt_slope


#Plot the normalized Mean RT difference and RT Slope difference
#Save the plots into a pdf

pdf("visual_normed_rt_diff_histogram.pdf")

hist(visual_data$letter_mean_rt_difference)
hist(visual_data$lsl_rt_slope_difference)

hist(visual_data$image_mean_rt_difference)
hist(visual_data$vsl_rt_slope_difference)

ggplot(visual_data,
       aes(x = visual_part_id, y = letter_mean_rt_difference)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(visual_data,
       aes(x = visual_part_id, y = lsl_rt_slope_difference)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

ggplot(visual_data,
       aes(x = visual_part_id, y = image_mean_rt_difference)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(visual_data,
       aes(x = visual_part_id, y = vsl_rt_slope_difference)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

dev.off()
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

#Auditory data--------------------------------------------------------------------------------
#Remove the participants who do not have data
auditory_data <-
  auditory_data[-which(auditory_data$auditory_part_id == "blast_a_028"),]
auditory_data$structured_ssl_rt_slope <-
  as.numeric(as.character(auditory_data$structured_ssl_rt_slope))
auditory_data$random_tsl_rt_slope <-
  as.numeric(as.character(auditory_data$random_tsl_rt_slope))

pdf("auditory_data_distribution_sanity_check.pdf")

hist(auditory_data$structured_syllable_mean_rt)
hist(auditory_data$random_syllable_mean_rt)

hist(auditory_data$structured_ssl_rt_slope)
hist(auditory_data$random_ssl_rt_slope)

hist(auditory_data$structured_tone_mean_rt)
hist(auditory_data$random_tone_mean_rt)

hist(auditory_data$structured_tsl_rt_slope)
hist(auditory_data$random_tsl_rt_slope)

library("ggplot2")
ggplot(auditory_data,
       aes(x = auditory_part_id, y = structured_syllable_mean_rt)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(auditory_data,
       aes(x = auditory_part_id, y = random_syllable_mean_rt)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

ggplot(auditory_data,
       aes(x = auditory_part_id, y = structured_ssl_rt_slope)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(auditory_data,
       aes(x = auditory_part_id, y = random_ssl_rt_slope)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

ggplot(auditory_data,
       aes(x = auditory_part_id, y = structured_tone_mean_rt)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(auditory_data,
       aes(x = auditory_part_id, y = random_tone_mean_rt)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

ggplot(auditory_data,
       aes(x = auditory_part_id, y = structured_tsl_rt_slope)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(auditory_data,
       aes(x = auditory_part_id, y = random_tsl_rt_slope)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

dev.off()
#----------------------------------------------------------------------------------------------

#Learning Effect Analysis-------------------------------------------------------------------------------
# Run Welch's paired t-test on mean RT
# p<0.05 tells us that random has significantly longer mean RT than structured, and there is learning effect
t.test(
  auditory_data$random_syllable_mean_rt,
  auditory_data$structured_syllable_mean_rt,
  paired = TRUE,
  alternative = "greater"
)
# Paired t-test
# 
# data:  auditory_data$random_syllable_mean_rt and auditory_data$structured_syllable_mean_rt
# t = 2.7209, df = 28, p-value = 0.005533
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   34.63968      Inf
# sample estimates:
#   mean of the differences 
# 92.42443 

t.test(
  auditory_data$random_tone_mean_rt,
  auditory_data$structured_tone_mean_rt,
  paired = TRUE,
  alternative = "greater"
)
# Paired t-test
# 
# data:  auditory_data$random_tone_mean_rt and auditory_data$structured_tone_mean_rt
# t = -0.21758, df = 28, p-value = 0.5853
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   -57.34127       Inf
# sample estimates:
#   mean of the differences 
# -6.502429 

t.test(
  auditory_data$random_ssl_rt_slope,
  auditory_data$structured_ssl_rt_slope,
  paired = TRUE,
  alternative = "greater"
)
# Paired t-test
# 
# data:  auditory_data$random_ssl_rt_slope and auditory_data$structured_ssl_rt_slope
# t = -0.97283, df = 28, p-value = 0.8305
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   -2.380328       Inf
# sample estimates:
#   mean of the differences 
# -0.866 

t.test(
  auditory_data$random_tsl_rt_slope,
  auditory_data$structured_tsl_rt_slope,
  paired = TRUE,
  alternative = "greater"
)
# Paired t-test
# 
# data:  auditory_data$random_tsl_rt_slope and auditory_data$structured_tsl_rt_slope
# t = 1.2116, df = 28, p-value = 0.1179
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   -0.9055286        Inf
# sample estimates:
#   mean of the differences 
# 2.241
#--------------------------------------------------------------------------------------------------------------------------
#RT Difference Analysis-----------------------------------------------------------------------
#Calculate the normalized mean RT difference between structured and random: (structured - random)/ random
auditory_data$syllable_mean_rt_difference <-
  (
    auditory_data$structured_syllable_mean_rt - auditory_data$random_syllable_mean_rt
  ) / auditory_data$random_syllable_mean_rt

auditory_data$tone_mean_rt_difference <-
  (auditory_data$structured_tone_mean_rt - auditory_data$random_tone_mean_rt) / auditory_data$random_tone_mean_rt

#Calculate the normalized RT Slope difference between structured and random: (structured - random)/ random
auditory_data$ssl_rt_slope_difference <-
  (auditory_data$structured_ssl_rt_slope - auditory_data$random_ssl_rt_slope) /
  auditory_data$random_ssl_rt_slope

auditory_data$tsl_rt_slope_difference <-
  (auditory_data$structured_tsl_rt_slope - auditory_data$random_tsl_rt_slope) / auditory_data$random_tsl_rt_slope


#Plot the normalized Mean RT difference and RT Slope difference
#Save the plots into a pdf

pdf("auditory_normed_rt_diff_histogram.pdf")

hist(auditory_data$syllable_mean_rt_difference)
hist(auditory_data$ssl_rt_slope_difference)

hist(auditory_data$tone_mean_rt_difference)
hist(auditory_data$tsl_rt_slope_difference)

ggplot(auditory_data,
       aes(x = auditory_part_id, y = syllable_mean_rt_difference)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(auditory_data,
       aes(x = auditory_part_id, y = ssl_rt_slope_difference)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

ggplot(auditory_data,
       aes(x = auditory_part_id, y = tone_mean_rt_difference)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')
ggplot(auditory_data,
       aes(x = auditory_part_id, y = tsl_rt_slope_difference)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center')

dev.off()
#------------------------------------------------------------------------------------------
#Correlation Analysis-----------------------------------------------------------------------
#Check if visual and auditory data have the same sample size
delete_visual <-
  setdiff(visual_data$visual_part_id, auditory_data$auditory_part_id)
#"blast_a_028"
delete_auditory <-
  setdiff(auditory_data$auditory_part_id, visual_data$visual_part_id)
# "blast_a_029" "blast_a_032"

matched_auditory_data <-
  auditory_data[-which(auditory_data$auditory_part_id %in% delete_auditory), ]
matched_visual_data <-
  visual_data[-which(visual_data$visual_part_id %in% delete_visual), ]

corr_data_visual <-
  matched_visual_data[, c(
    "image_mean_rt_difference",
    "letter_mean_rt_difference",
    "vsl_rt_slope_difference",
    "lsl_rt_slope_difference"
  )]

corr_data_auditory <-
  matched_auditory_data[, c(
    "syllable_mean_rt_difference",
    "tone_mean_rt_difference",
    "ssl_rt_slope_difference",
    "tsl_rt_slope_difference"
  )]

corr_data <- cbind(corr_data_auditory, corr_data_visual)

library("Hmisc")
#alternative hypothesis: rho is truly above 0: positive correlation
#(calculate both above and below 0)
#Mean RT and RT slope correlation may be positive or negative
corr_results <- rcorr(as.matrix(corr_data), type = c("spearman"))
corr_results_r <- corr_results$r
corr_results_n <- corr_results$n
corr_results_p <- corr_results$P

corr_results_p_alter_positive_corr <- ifelse (corr_results_r > 0, corr_results$P /
                                                2, 1 - corr_results$P / 2)

corr_results_p_alter_negative_corr  <- ifelse (corr_results_r < 0, corr_results$P /
                                                 2, 1 - corr_results$P / 2)

write.table(
  corr_results_r,
  "in_scanner_behavioral_sl_corr_all.csv",
  col.names = TRUE,
  sep = ","
)

write.table(
  corr_results_n,
  "in_scanner_behavioral_sl_corr_all.csv",
  col.names = TRUE,
  sep = ",",
  append = TRUE
)

write.table(
  corr_results_p,
  "in_scanner_behavioral_sl_corr_all.csv",
  col.names = TRUE,
  sep = ",",
  append = TRUE
)

write.table(
  corr_results_p_alter_positive_corr,
  "in_scanner_behavioral_sl_corr_all.csv",
  col.names = TRUE,
  sep = ",",
  append = TRUE
)

write.table(
  corr_results_p_alter_negative_corr,
  "in_scanner_behavioral_sl_corr_all.csv",
  col.names = TRUE,
  sep = ",",
  append = TRUE
)

#-------------------------------------------------------------------------------------------

#Plot visual Mean RT bar graph-----------------------------------------------------------------
#Prepare data for bar graph-----------------------------------------------------------------
library("reshape")

bar_visual_data <-
  melt(
    visual_data,
    by.vars = c("visual_part_id"),
    measure.vars = c(
      "structured_image_mean_rt",
      "random_image_mean_rt",
      "structured_letter_mean_rt",
      "random_letter_mean_rt"
    )
  )

colnames(bar_visual_data)[colnames(bar_visual_data) == "value"] <-
  "Mean_Reaction_Time"

bar_visual_data[which(bar_visual_data$variable == "structured_image_mean_rt"), c("Condition")]  <-
  "Structured"
bar_visual_data[which(bar_visual_data$variable == "random_image_mean_rt"), c("Condition")]  <-
  "Random"
bar_visual_data[which(bar_visual_data$variable == "structured_letter_mean_rt"), c("Condition")]  <-
  "Structured"
bar_visual_data[which(bar_visual_data$variable == "random_letter_mean_rt"), c("Condition")]  <-
  "Random"

bar_visual_data[which(bar_visual_data$variable == "structured_image_mean_rt"), c("Type")]  <-
  "Image"
bar_visual_data[which(bar_visual_data$variable == "random_image_mean_rt"), c("Type")]  <-
  "Image"
bar_visual_data[which(bar_visual_data$variable == "structured_letter_mean_rt"), c("Type")]  <-
  "Letter"
bar_visual_data[which(bar_visual_data$variable == "random_letter_mean_rt"), c("Type")]  <-
  "Letter"

#ggplot bar grapgh--------------------------------------------------------------------------------------
library("ggbeeswarm")
library("ggsignif")

visual_bar_graph <-
  ggplot(bar_visual_data, aes(x = Type, y = Mean_Reaction_Time)) +
  geom_bar(
    aes(fill = Condition),
    stat = "summary",
    fun.y = "mean",
    position = position_dodge(width = 0.9),
    width = 0.9
  ) +
  geom_beeswarm(
    aes(fill = Condition),
    dodge.width = 0.9,
    cex = 2.5,
    size = 0.8,
    show.legend = FALSE
  ) +
  ylab("Mean Reaction Time (ms)") +
  xlab("Task") +
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=14,face="bold"),
        legend.title = element_text(size = 12),
        legend.text = element_text(size = 12)) +
  geom_signif(
    annotations = "*",
    y_position = 650,
    xmin = 0.75,
    xmax = 1.25,
    tip_length = 0.01,
    vjust = 0.4
  ) +
  geom_signif(
    annotations = "***",
    y_position = 650,
    xmin = 1.75,
    xmax = 2.25,
    tip_length = 0.01,
    vjust = 0.4
  )

ggsave(
  "visual_mean_rt_graph.png",
  dpi = 150
)
#----------------------------------------------------------------------------------------------

#Plot auditory Mean RT bar graph-----------------------------------------------------------------
#Prepare data for bar graph-----------------------------------------------------------------
bar_auditory_data <-
  melt(
    auditory_data,
    by.vars = c("auditory_part_id"),
    measure.vars = c(
      "structured_tone_mean_rt",
      "random_tone_mean_rt",
      "structured_syllable_mean_rt",
      "random_syllable_mean_rt"
    )
  )

colnames(bar_auditory_data)[colnames(bar_auditory_data) == "value"] <-
  "Mean_Reaction_Time"

bar_auditory_data[which(bar_auditory_data$variable == "structured_syllable_mean_rt"), c("Condition")]  <-
  "Structured"
bar_auditory_data[which(bar_auditory_data$variable == "random_syllable_mean_rt"), c("Condition")]  <-
  "Random"
bar_auditory_data[which(bar_auditory_data$variable == "structured_tone_mean_rt"), c("Condition")]  <-
  "Structured"
bar_auditory_data[which(bar_auditory_data$variable == "random_tone_mean_rt"), c("Condition")]  <-
  "Random"

bar_auditory_data[which(bar_auditory_data$variable == "structured_tone_mean_rt"), c("Type")]  <-
  "Tone"
bar_auditory_data[which(bar_auditory_data$variable == "random_tone_mean_rt"), c("Type")]  <-
  "Tone"
bar_auditory_data[which(bar_auditory_data$variable == "structured_syllable_mean_rt"), c("Type")]  <-
  "Syllable"
bar_auditory_data[which(bar_auditory_data$variable == "random_syllable_mean_rt"), c("Type")]  <-
  "Syllable"

bar_auditory_data$Type <- as.character(bar_auditory_data$Type)
bar_auditory_data$Type <- factor(bar_auditory_data$Type, levels =
                                   c("Tone", "Syllable"))

bar_auditory_data <-
  bar_auditory_data[order(bar_auditory_data$Type), ]
#ggplot bar grapgh--------------------------------------------------------------------------------------
library("ggbeeswarm")
library("ggsignif")

auditory_bar_graph <-
  ggplot(bar_auditory_data, aes(x = Type, y = Mean_Reaction_Time)) +
  geom_bar(
    aes(fill = Condition),
    stat = "summary",
    fun.y = "mean",
    position = position_dodge(width = 0.9),
    width = 0.9
  ) +
  geom_beeswarm(
    aes(fill = Condition),
    dodge.width = 0.9,
    cex = 2.5,
    size = 0.8,
    show.legend = FALSE
  ) +
  ylab("Mean Reaction Time (ms)") +
  xlab("Task") +
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=14,face="bold"),
        legend.title = element_text(size = 12),
        legend.text = element_text(size = 12)) +
  geom_signif(
    annotations = "**",
    y_position = 800,
    xmin = 1.75,
    xmax = 2.25,
    tip_length = 0.01,
    vjust = 0.4
  ) +
  scale_fill_brewer(palette = "Set2")

ggsave(
  "auditory_mean_rt_graph.png",
  dpi = 150
)
#----------------------------------------------------------------------------------------------

#RT Slope Plot----------------------------------------------------------------------------------
#Prepare the visual RT Slope data---------------------------------------------------------------
slope_bar_visual_data <-
  melt(
    visual_data,
    by.vars = c("auditory_part_id"),
    measure.vars = c(
      "structured_lsl_rt_slope",
      "random_lsl_rt_slope",
      "structured_vsl_rt_slope",
      "random_vsl_rt_slope"
    )
  )

colnames(slope_bar_visual_data)[colnames(slope_bar_visual_data) == "value"] <-
  "RT_Slope"

slope_bar_visual_data[which(slope_bar_visual_data$variable == "structured_vsl_rt_slope"), c("Condition")]  <-
  "Structured"
slope_bar_visual_data[which(slope_bar_visual_data$variable == "random_vsl_rt_slope"), c("Condition")]  <-
  "Random"
slope_bar_visual_data[which(slope_bar_visual_data$variable == "structured_lsl_rt_slope"), c("Condition")]  <-
  "Structured"
slope_bar_visual_data[which(slope_bar_visual_data$variable == "random_lsl_rt_slope"), c("Condition")]  <-
  "Random"

slope_bar_visual_data[which(slope_bar_visual_data$variable == "structured_vsl_rt_slope"), c("Type")]  <-
  "Image"
slope_bar_visual_data[which(slope_bar_visual_data$variable == "random_vsl_rt_slope"), c("Type")]  <-
  "Image"
slope_bar_visual_data[which(slope_bar_visual_data$variable == "structured_lsl_rt_slope"), c("Type")]  <-
  "Letter"
slope_bar_visual_data[which(slope_bar_visual_data$variable == "random_lsl_rt_slope"), c("Type")]  <-
  "Letter"

#ggplot visual RT Slope bar grapgh --------------------------------------------------------------------------------------
visual_slope_bar_graph <-
  ggplot(slope_bar_visual_data, aes(x = Type, y = RT_Slope)) +
  geom_bar(
    aes(fill = Condition),
    stat = "summary",
    fun.y = "mean",
    position = position_dodge(width = 0.9),
    width = 0.9
  ) +
  geom_beeswarm(
    aes(fill = Condition),
    dodge.width = 0.9,
    cex = 2.5,
    size = 0.8,
    show.legend = FALSE
  ) +
  ylab("Reaction Time Slope (ms/ trial)") +
  xlab("Task") +
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=14,face="bold"),
        legend.title = element_text(size = 12),
        legend.text = element_text(size = 12)) +
  geom_signif(
    annotations = "**",
    y_position = 15,
    xmin = 0.75,
    xmax = 1.25,
    tip_length = 0.01,
    vjust = 0.4
  )


ggsave(
  "visual_rt_slope_graph.png",
  dpi = 150
)
#----------------------------------------------------------------------------------------------

#ggplot auditory RT Slope bar grapgh --------------------------------------------------------------------------------------
slope_bar_auditory_data <-
  melt(
    auditory_data,
    by.vars = c("auditory_part_id"),
    measure.vars = c(
      "structured_tsl_rt_slope",
      "random_tsl_rt_slope",
      "structured_ssl_rt_slope",
      "random_ssl_rt_slope"
    )
  )

colnames(slope_bar_auditory_data)[colnames(slope_bar_auditory_data) == "value"] <-
  "RT_Slope"

slope_bar_auditory_data[which(slope_bar_auditory_data$variable == "structured_ssl_rt_slope"), c("Condition")]  <-
  "Structured"
slope_bar_auditory_data[which(slope_bar_auditory_data$variable == "random_ssl_rt_slope"), c("Condition")]  <-
  "Random"
slope_bar_auditory_data[which(slope_bar_auditory_data$variable == "structured_tsl_rt_slope"), c("Condition")]  <-
  "Structured"
slope_bar_auditory_data[which(slope_bar_auditory_data$variable == "random_tsl_rt_slope"), c("Condition")]  <-
  "Random"

slope_bar_auditory_data[which(slope_bar_auditory_data$variable == "structured_ssl_rt_slope"), c("Type")]  <-
  "Syllable"
slope_bar_auditory_data[which(slope_bar_auditory_data$variable == "random_ssl_rt_slope"), c("Type")]  <-
  "Syllable"
slope_bar_auditory_data[which(slope_bar_auditory_data$variable == "structured_tsl_rt_slope"), c("Type")]  <-
  "Tone"
slope_bar_auditory_data[which(slope_bar_auditory_data$variable == "random_tsl_rt_slope"), c("Type")]  <-
  "Tone"

slope_bar_auditory_data$Type <-
  as.character(slope_bar_auditory_data$Type)
slope_bar_auditory_data$Type <-
  factor(slope_bar_auditory_data$Type, levels =
           c("Tone", "Syllable"))

slope_bar_auditory_data <-
  slope_bar_auditory_data[order(slope_bar_auditory_data$Type), ]
#ggplot auditory RT Slope bar grapgh --------------------------------------------------------------------------------------
auditory_slope_bar_graph <-
  ggplot(slope_bar_auditory_data, aes(x = Type, y = RT_Slope)) +
  geom_bar(
    aes(fill = Condition),
    stat = "summary",
    fun.y = "mean",
    position = position_dodge(width = 0.9),
    width = 0.9
  ) +
  geom_beeswarm(
    aes(fill = Condition),
    dodge.width = 0.9,
    cex = 2.5,
    size = 0.8,
    show.legend = FALSE
  ) +
  ylab("Reaction Time Slope (ms/ trial)") +
  xlab("Task") +
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=14,face="bold"),
        legend.title = element_text(size = 12),
        legend.text = element_text(size = 12)) +
  scale_fill_brewer(palette = "Set2")

ggsave(
  "auditory_rt_slope_graph.png",
  dpi = 150
)
#----------------------------------------------------------------------------------------------

#Heat map--------------------------------------------------------------------------------------
#Prepare data for heat map---------------------------------------------------------------------
#Manual: copy and save the relevant correlation data you want to plot
#from the table saved from the corr analysis above, create a csv file
#named "corr_data.csv
corr_data_manual <- read.csv("corr_data_manual.csv")

#Get the lower half of the correlation table so there is no duplicates of r values
#Copyright: http://www.sthda.com/english/wiki/ggplot2-quick-correlation-matrix-heatmap-r-software-and-data-visualization#compute-the-correlation-matrix

# lower_half <-function(corr_data){
#   corr_data[upper.tri(corr_data)] <- NA
#   return(corr_data)
# }
#
# heat_map_corr_data <- lower_half(corr_data)
#
heat_map_corr_data <- melt(corr_data_manual)

#Rename the data
#------------------------------------------------------------------------------------------------------------------------
heat_map_corr_data[which(heat_map_corr_data$variable == "image_mean_rt_difference"), c("Type")]  <-
  "Image Mean RT"
heat_map_corr_data[which(heat_map_corr_data$variable == "letter_mean_rt_difference"), c("Type")]  <-
  "Letter Mean RT"
heat_map_corr_data[which(heat_map_corr_data$variable == "syllable_mean_rt_difference"), c("Type")]  <-
  "Syllable Mean RT"
heat_map_corr_data[which(heat_map_corr_data$variable == "tone_mean_rt_difference"), c("Type")]  <-
  "Tone Mean RT"

heat_map_corr_data[which(heat_map_corr_data$variable == "vsl_rt_slope_difference"), c("Type")]  <-
  "Image RT Slope"
heat_map_corr_data[which(heat_map_corr_data$variable == "lsl_rt_slope_difference"), c("Type")]  <-
  "Letter RT Slope"
heat_map_corr_data[which(heat_map_corr_data$variable == "ssl_rt_slope_difference"), c("Type")]  <-
  "Syllable RT Slope"
heat_map_corr_data[which(heat_map_corr_data$variable == "tsl_rt_slope_difference"), c("Type")]  <-
  "Tone RT Slope"

heat_map_corr_data[which(heat_map_corr_data$X == "image_mean_rt_difference"), c("Condition")]  <-
  "Image Mean RT"
heat_map_corr_data[which(heat_map_corr_data$X == "letter_mean_rt_difference"), c("Condition")]  <-
  "Letter Mean RT"
heat_map_corr_data[which(heat_map_corr_data$X == "syllable_mean_rt_difference"), c("Condition")]  <-
  "Syllable Mean RT"
heat_map_corr_data[which(heat_map_corr_data$X == "tone_mean_rt_difference"), c("Condition")]  <-
  "Tone Mean RT"

heat_map_corr_data[which(heat_map_corr_data$X == "vsl_rt_slope_difference"), c("Condition")]  <-
  "Image RT Slope"
heat_map_corr_data[which(heat_map_corr_data$X == "lsl_rt_slope_difference"), c("Condition")]  <-
  "Letter RT Slope"
heat_map_corr_data[which(heat_map_corr_data$X == "ssl_rt_slope_difference"), c("Condition")]  <-
  "Syllable RT Slope"
heat_map_corr_data[which(heat_map_corr_data$X == "tsl_rt_slope_difference"), c("Condition")]  <-
  "Tone RT Slope"
#------------------------------------------------------------------------------------------------------------------------

#reorder the data for the heat map

heat_map_corr_data$Type <- as.character(heat_map_corr_data$Type)
heat_map_corr_data$Type <- factor(
  heat_map_corr_data$Type,
  levels =
    c(
      "Image Mean RT",
      "Letter Mean RT",
      "Syllable Mean RT",
      "Tone Mean RT",
      "Image RT Slope",
      "Letter RT Slope",
      "Syllable RT Slope",
      "Tone RT Slope"
    )
)


heat_map_corr_data$Condition <-
  as.character(heat_map_corr_data$Condition)
heat_map_corr_data$Condition <-
  factor(
    heat_map_corr_data$Condition,
    levels =
      c(
        "Image Mean RT",
        "Letter Mean RT",
        "Syllable Mean RT",
        "Tone Mean RT",
        "Image RT Slope",
        "Letter RT Slope",
        "Syllable RT Slope",
        "Tone RT Slope"
      )
  )

heat_map_corr_data <-
  heat_map_corr_data[order(heat_map_corr_data$Type,
                           heat_map_corr_data$Condition), ]

heat_map_corr_data$value <- round(heat_map_corr_data$value, 2)

#GGplot the heat map----------------------------------------------------------------------------------------------
in_scanner_beh_corr_heat_map <-
  ggplot(data = heat_map_corr_data, aes(x = Condition, y = Type, fill = value)) +
  geom_tile(color = "white") +
  scale_fill_gradient2(
    low = "blue",
    high = "red",
    mid = "white",
    midpoint = 0,
    limit = c(-1, 1),
    space = "Lab",
    name = "Spearman\nCorrelation"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(
    angle = 45,
    vjust = 1,
    size = 12,
    hjust = 1
  )) +
  theme(axis.title.x = element_blank(),
        axis.text.y = element_text (size = 12),
        axis.title.y = element_blank()) +
  coord_fixed() +
  geom_text(aes(label = value), color = "black", size = 3.5)

ggsave(
  "in_scanner_beh_corr_heat_map.png",
  dpi = 150
)
#Descriptive Statistics------------------------------------------------------------------------
library("psych")
descriptive_visual_data <- describe(visual_data)
write.csv(descriptive_visual_data, file = "descriptive_stat_visual_in_scanner_beh_data.csv")

descriptive_auditory_data <- describe(auditory_data)
write.csv(descriptive_auditory_data, file = "descriptive_stat_auditory_in_scanner_beh_data.csv")

#Plot mean RT bar graphs with all tasks in one plot----------------------------------------------------

visual_rbind <- bar_visual_data
auditory_rbind <- bar_auditory_data

colnames(visual_rbind)[colnames(visual_rbind) == "visual_part_id"] <-
  "part_id"
colnames(auditory_rbind)[colnames(auditory_rbind) == "auditory_part_id"] <-
  "part_id"

common_cols <- intersect(colnames(visual_rbind), colnames(auditory_rbind))

bar_mean_rt_all <- rbind(
  subset(visual_rbind, select = common_cols), 
  subset(auditory_rbind, select = common_cols)
)

bar_mean_rt_all$Type <-
  factor(bar_mean_rt_all$Type, levels =
           c("Image", "Letter", "Tone", "Syllable"))

bar_mean_rt_all <-
  bar_mean_rt_all[order(bar_mean_rt_all$Type), ]

View(bar_mean_rt_all)
mean_rt_bar_plot <-
  ggplot(bar_mean_rt_all, aes(x = Type, y = Mean_Reaction_Time)) +
  geom_bar(
    aes(fill = Condition),
    stat = "summary",
    fun.y = "mean",
    position = position_dodge(width = 0.9),
    width = 0.9
  ) +
  geom_beeswarm(
    aes(fill = Condition),
    dodge.width = 0.9,
    cex = 1.8,
    size = 0.5,
    show.legend = FALSE
  ) +
  ylab("Mean Reaction Time (ms)") +
  xlab("Task") +
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=14,face="bold"),
        legend.title = element_text(size = 12),
        legend.text = element_text(size = 12)) + 
  geom_signif(
          annotations = "**",
          y_position = 800,
          xmin = 3.75,
          xmax = 4.25,
          tip_length = 0.01,
          vjust = 0.4
        ) +
  geom_signif(
    annotations = "***",
    y_position = 800,
    xmin = 1.75,
    xmax = 2.25,
    tip_length = 0.01,
    vjust = 0.4
  ) +
  geom_signif(
    annotations = "*",
    y_position = 800,
    xmin = 0.75,
    xmax = 1.25,
    tip_length = 0.01,
    vjust = 0.4
  )


ggsave(
  "mean_rt_graph_all.png",
  dpi = 300
)

#Plot RT slope bar graphs with all tasks------------------------------------------------------------
visual_slope_rbind <- slope_bar_visual_data
auditory_slope_rbind <- slope_bar_auditory_data

colnames(visual_slope_rbind)[colnames(visual_slope_rbind) == "visual_part_id"] <-
  "part_id"
colnames(auditory_slope_rbind)[colnames(auditory_slope_rbind) == "auditory_part_id"] <-
  "part_id"

common_cols_slope <- intersect(colnames(visual_slope_rbind), colnames(auditory_slope_rbind))

bar_rt_slope_all <- rbind(
  subset(visual_slope_rbind, select = common_cols_slope), 
  subset(auditory_slope_rbind, select = common_cols_slope)
)

View(bar_rt_slope_all)

bar_rt_slope_all$Type <-
  factor(bar_rt_slope_all$Type, levels =
           c("Image", "Letter", "Tone", "Syllable"))

bar_rt_slope_all <-
  bar_rt_slope_all[order(bar_rt_slope_all$Type), ]

rt_slope_bar_all <-
  ggplot(bar_rt_slope_all, aes(x = Type, y = RT_Slope)) +
  geom_bar(
    aes(fill = Condition),
    stat = "summary",
    fun.y = "mean",
    position = position_dodge(width = 0.9),
    width = 0.9
  ) +
  geom_beeswarm(
    aes(fill = Condition),
    dodge.width = 0.9,
    cex = 1.8,
    size = 0.5,
    show.legend = FALSE
  ) +
  ylab("Reaction Time Slope (ms/ trial)") +
  xlab("Task") +
  theme(axis.text=element_text(size=12),
        axis.title=element_text(size=14,face="bold"),
        legend.title = element_text(size = 12),
        legend.text = element_text(size = 12)) + 
  scale_fill_brewer(palette = "Set2") +
  geom_signif(
    annotations = "**",
    y_position = 20,
    xmin = 0.75,
    xmax = 1.25,
    tip_length = 0.01,
    vjust = 0.4
  )


ggsave(
  "rt_slope_bar_all.png",
  dpi = 300
)

#The descriptive stats on Diana's poster is only for the 26 participants in the correlation matrix.

#-------------------------------------------------------------------------------------------
#Just for personal interests----------------------------------------------------------------
#removing one outliner, the normalized vsl_rt_slope_difference is no longer significant
remove_outliner <-
  visual_data[-which(visual_data$visual_part_id == "blast_a_035"),]
t.test(remove_outliner$vsl_rt_slope_difference,
       mu = 0,
       alternative = "less")
#------------------------------------------------------------------------------------------
