install.packages("lme4")
install.packages("lmerTest")
install.packages("optimx")
library(lmerTest)
library(lme4)
library(optimx)

setwd("/Users/julieschneider/Julie_Personal/Projects/HEB/R_scripts/")
df=read.csv('heb_trial_task_overall_numeric.csv')

glmer(trial_accuracy~ task*order + task*trial_order + trial + (1|subject) + (1+order|trial), family = binomial, control=glmerControl(optimizer="Nelder_Mead", optCtrl=list(maxfun=2e5)),data = df)
glmer(trial_accuracy~ task*order + task*trial_order + trial + (1|subject) + (1+order|trial), family = binomial, control = glmerControl(optimizer ='optimx', optCtrl=list(method='L-BFGS-B')),data = df)

#linearMod <- lm(accuracy ~ englishexperience, data=df)
#summary(linearMod)
#scatter.smooth(x=accuracy, y=englishexperience, main="Accuracy & English Experience")  # scatterplot
