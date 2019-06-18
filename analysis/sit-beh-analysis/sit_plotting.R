# Plotting Script for SIT data results
# Written by An Nguyen, adapted and annotated by Violet Kozloff

install.packages("ggplot2")
install.packages("ggbeeswarm")
library("ggplot2")
library("ggbeeswarm")

rts<-indiv_rt_slope
acc<-indiv_accuracies

#Plot RT slope with beeswarm
ggplot(data=rts,aes(x=factor(task, level=c("ll","lv","vv","vl")), y=rt_slope, fill=factor(type))) + geom_bar(stat="summary", position = position_dodge()) + theme_classic() + annotate("text", label = "Same", x = 0.9, y = 25, color = "black")  + annotate("text", label = "Different", x = 1.97, y = 25, color = "black") + annotate("text", label = "Same", x = 2.9, y = 25, color = "black")  + annotate("text", label = "Different", x = 4, y = 25, color = "black") + geom_vline(xintercept = 2.5, linetype=3) + scale_x_discrete(labels=c("Letter","Image")) + xlab(label="Task") + ylab(label="Reaction Time Slope (ms/trial)") + scale_fill_manual(name = "Type",labels = c("Random","Structured"),values = c("darkorange2", "lightskyblue2")) +  geom_beeswarm(aes(x=factor(task, level=c("ll","lv","vv","vl")), y=rt_slope, fill=factor(type)),dodge.width=1)

#Plot RT slope differece with beeswarm
#ggplot(data=rt_slope_diff,aes(x=factor(task, level=c("linguistic","non_linguistic")), y=rt_slope_diff, fill=factor(same_or_diff))) + geom_bar(stat="summary", position = position_dodge()) + theme_classic() + ylab(label="Reaction Time Difference")  +  geom_beeswarm(aes(x=factor(task, level=c("linguistic", "non_linguistic")), y=),dodge.width=1, show.legend=FALSE) + annotate("text", label = "Same", x = 0.9, y = 1.1, color = "black")  + annotate("text", label = "Different", x = 1.97, y = 1.1, color = "black") + annotate("text", label = "Same", x = 2.9, y = 1.1, color = "black")  + annotate("text", label = "Different", x = 4, y = 1.1, color = "black") + geom_hline(yintercept = 0.5, linetype=3) + scale_x_discrete(labels=c("Letter","Image")) + xlab(label="Task") + ylab(label="Accuracy") + scale_fill_manual(name="Task",labels=c("Letter","Image"),values = c("tomato1", "#2166ac"))

#Plot mean RT slope with beeswarm
ggplot(data=rts,aes(x=factor(task, level=c("ll","lv","vv","vl")), y=mean_rt, fill=factor(type))) + geom_bar(stat="summary", position = position_dodge()) + theme_classic() + annotate("text", label = "Same", x = 0.9, y = 800, color = "black")  + annotate("text", label = "Different", x = 1.97, y = 800, color = "black") + annotate("text", label = "Same", x = 2.9, y = 800, color = "black")  + annotate("text", label = "Different", x = 4, y = 800, color = "black") + geom_vline(xintercept = 2.5, linetype=3) + scale_x_discrete(labels=c("Letter","Image")) + xlab(label="Task") + ylab(label="Mean Reaction Time") + scale_fill_manual(name = "Type",labels = c("Random","Structured"),values = c("darkorange2", "lightskyblue2")) +  geom_beeswarm(aes(x=factor(task, level=c("ll","lv","vv","vl")), y=mean_rt, fill=factor(type)),dodge.width=1)

#RT with beeswarm
# ggplot(data=rt,aes(x=factor(task, level=c("ll","lv","vv","vl")), y=mean_rt, fill=factor(type))) + geom_bar(stat="summary", position = position_dodge()) + theme_classic() + annotate("text", label = "Same", x = 0.9, y = 800, color = "black")  + annotate("text", label = "Different", x = 1.97, y = 800, color = "black") + annotate("text", label = "Same", x = 2.9, y = 800, color = "black")  + annotate("text", label = "Different", x = 4, y = 800, color = "black") + geom_vline(xintercept = 2.5, linetype=3) + scale_x_discrete(labels=c("Letter","Image")) + xlab(label="Task") + ylab(label="Reaction Time (ms)") + scale_fill_manual(name = "Type",labels = c("Random","Structured"),values = c("darkorange2", "lightskyblue2")) + geom_beeswarm(aes(x=factor(task, level=c("ll","lv","vv","vl")), y=mean_rt, fill=factor(type)),dodge.width=1)

#ACCURACY
ggplot(data=acc,aes(x=factor(task, level=c("ll","lv","vv","vl")), y=accuracy, fill=factor(test_phase))) + geom_bar(stat="summary", position = position_dodge()) + theme_classic() + ylab(label="Accuracy")  +  geom_beeswarm(aes(x=factor(task, level=c("ll","lv","vv","vl")), y=accuracy),dodge.width=1, show.legend=FALSE) + annotate("text", label = "Same", x = 0.9, y = 1.1, color = "black")  + annotate("text", label = "Different", x = 1.97, y = 1.1, color = "black") + annotate("text", label = "Same", x = 2.9, y = 1.1, color = "black")  + annotate("text", label = "Different", x = 4, y = 1.1, color = "black") + geom_hline(yintercept = 0.5, linetype=3) + xlab(label="Task") + ylab(label="Accuracy") + scale_fill_manual(name="Task",values = c("#F27645", "#51C19B"))

#Correlation
ggplot(data=test, aes(x=rt,y=score,color=Task, shape=Task)) + geom_point(size=2) + facet_grid(~same_or_diff) + geom_smooth(method=lm, se=FALSE) + scale_shape_manual(values=c(0,16)) + scale_color_manual(values= c("#2166ac","tomato1")) + ylab(label="Vocabulary Score") + theme(panel.border = element_rect(colour='black', fill=NA),  panel.background = element_blank()) + xlab(label="Mean Reaction Time (ms)")
