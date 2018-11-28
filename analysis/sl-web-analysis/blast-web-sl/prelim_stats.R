child_data<-read.csv("/Users/vkozloff/Desktop/child_prelim_stats.csv")

# Test whether ASD and SIB performance is significantly different for each task
lsl_by_group<-t.test(child_data$lsl_acc~child_data$group)
ssl_by_group<-t.test(child_data$ssl_acc~child_data$group)
tsl_by_group<-t.test(child_data$tsl_acc~child_data$group)
vsl_by_group<-t.test(child_data$vsl_acc~child_data$group)

# Test whether each group's performance on each task is significantly above chance
lsl_asd_chance <- t.test(child_data$asd_lsl_acc, mu=0.5, alternative="greater")
ssl_asd_chance <- t.test(child_data$asd_ssl_acc, mu=0.5, alternative="less")
tsl_asd_chance <- t.test(child_data$asd_tsl_acc, mu=0.5, alternative="greater")
vsl_asd_chance <- t.test(child_data$asd_vsl_acc, mu=0.5, alternative="greater")
lsl_sib_chance <- t.test(child_data$sib_lsl_acc, mu=0.5, alternative="greater")
ssl_sib_chance <- t.test(child_data$sib_ssl_acc, mu=0.5, alternative="greater")
tsl_sib_chance <- t.test(child_data$sib_tsl_acc, mu=0.5, alternative="less")
vsl_sib_chance <- t.test(child_data$sib_vsl_acc, mu=0.5, alternative="greater")

adult_data<-read.csv("/Users/vkozloff/Desktop/adult_prelim_stats.csv")
adult_data[1]<-NULL

# Correlation matrix for adult tasks
install.packages("Hmisc")
library("Hmisc")
correlation_matrix <- cor(adult_data, method = c("pearson"),use="pairwise.complete.obs")
results<-rcorr(as.matrix(adult_data), type="pearson")
write.csv(results,file="corr_mat")


