---
  title: "ABCD Analysis"
author: "An Nguyen"
date: "October 9, 2017"
output:
  pdf_document: default
html_document: default
---
  ```{r,echo=FALSE,warning=FALSE}
#Loading library
library(ggplot2)
library(knitr)
library(kableExtra)
library(readr)
```

```{r,echo=FALSE}
#importing files

tsl <- list()
vsl <- list()
vsl_par_id <- NULL
tsl_par_id <- NULL
path <- "C:/Users/Qlab/Downloads/sl-analysis/tsl/data/"
files <- list.files(path=path, pattern="*.csv")
for(file in files)
{
  
  assign(
    gsub(" ","",file), 
    read.csv(paste(path,file,sep="")))
}
for(file in files){tsl <- append(tsl,list(eval(parse(text=file))))}

vsl_path <- "C:/Users/Qlab/Downloads/sl-analysis/vsl/"
vsl_files <- list.files(path=vsl_path, pattern="*.csv")
for(vslfile in vsl_files)
{
  assign(
    gsub(" ","",vslfile), 
    read.csv(paste(vsl_path,vslfile,sep="")))
}
for(text in vsl_files){vsl <- append(vsl,list(eval(parse(text=text))))}

vsl <- do.call(rbind.data.frame, vsl)
tsl <- do.call(rbind.data.frame, tsl)

#add an ID column for each row
for (i in seq(from=1,to=length(vsl$responses),by=533)){vsl_par_id<-append(vsl_par_id,rep(substr(vsl$responses[i],8,16),533))}
for (i in seq(from=1,to=length(tsl$responses),by=832)){tsl_par_id<-append(tsl_par_id,rep(substr(tsl$responses[i],8,16),832))}
vsl$par_id <- vsl_par_id
tsl$par_id <- tsl_par_id

list_vsl_id <- unique(vsl$par_id)
list_tsl_id <- unique(tsl$par_id)

#Group set up
DD <- list("ABCD_1711", "ABCD_1714", "ABCD_1727", "ABCD_1735", "ABCD_1751", "ABCD_1756", "ABCD_1764", "ABCD_1767")

TYP <- list("ABCD_1702", "ABCD_1703", "ABCD_1705", "ABCD_1708", "ABCD_1709", "ABCD_1710", "ABCD_1716", "ABCD_1720", "ABCD_1721", "ABCD_1724", "ABCD_1725", "ABCD_1728", "ABCD_1729", "ABCD_1730", "ABCD_1732", "ABCD_1734", "ABCD_1736", "ABCD_1739", "ABCD_1742", "ABCD_1747", "ABCD_1749", "ABCD_1754" )
group <- NULL
for (i in seq(from=1,to=length(tsl$par_id),by=1))
{if (tsl[i,]$par_id %in% TYP)
{group[i]<-"TYP"}
  else if (tsl[i,]$par_id %in% DD)
  {group[i] <- "DD"}}
tsl$group <- group
groupv <- NULL
for (i in seq(from=1,to=length(vsl$par_id),by=1))
{if (vsl[i,]$par_id %in% TYP)
{groupv[i]<-"TYP"}
  else if (vsl[i,]$par_id %in% DD)
  {groupv[i] <- "DD"}}
vsl$group <- groupv


language_1 = list(1,2,2,2,1,1,2,1,1,2,1,2,1,1,2,2,1,1,2,1,2,2,1,2,2,2,1,2,1,2,1,1)
language_2 = list(1,1,2,1,1,1,2,2,2,2,1,1,1,2,2,1,2,2,1,1,2,1,2,1,2,1,2,1,1,2,2,2)
```

```{r,echo=FALSE}
#Clean data

vsl$stimulus<- gsub(".jpg","",vsl$stimulus)
vsl$stimulus<- gsub("../../images/","",vsl$stimulus)

tsl$stimulus<- gsub(".wav","",tsl$stimulus)
tsl$stimulus<- gsub("../../tones/","",tsl$stimulus)
```

#Compute RT for VSL
```{r,echo=FALSE}
compute_visual <- function(data)
{
  rt_col <- NULL
  id <- NULL
  trial <- NULL
  target <- NULL
  group_cond <- NULL
  row_number <- which(vsl$targ==vsl$stimulus)
  for (i in row_number){
    rt_col <- append(rt_col,vsl[i,][,"rt"])
    trial <- append(trial,vsl[i,][,"trial_index"])
    id <- append(id,vsl[i,]$par_id)
    group_cond <- append(group_cond,vsl[i,]$group)
    if (vsl[i-1,][,"rt"]!=-1){
      rt_col[(match(i,row_number))] <- vsl[i-1,][,"rt"]
      
    }}
  rt_df1 <- data.frame(trial,rt_col,id,group_cond)
  fam_block <- vsl[which(vsl$trial_index<303 & vsl$trial_index>14),]
  fam_trial <- rt_df1[which(rt_df1$trial<303 & rt_df1$trial>14), ]
  reindex <- rep(1:24,29)
  fam_trial$reindex <- reindex
  hit_rate <- NULL
  miss_rate <- NULL
  correct_rejection <- NULL
  false_alarm <- NULL
  mean_rt <- NULL
  rt_slope <- NULL
  mean_table <- fam_trial[which(fam_trial$rt_col!=-1 & fam_trial$rt_col<1000 & fam_trial$rt_col>-1000), ]
  for(id in list_vsl_id){
    mean_rt<-append(mean_rt,round(mean(mean_table$rt_col[mean_table$id==id]),digits=3))
    rt_slope <-append(rt_slope,round(summary(lm(mean_table$rt_col[mean_table$id==id]~mean_table$trial[mean_table$id==id]))$coefficient[2,1],digits=3))
    hit_rate<-append(hit_rate,round(sum(!is.na(mean_table$rt_col[mean_table$id==id]))/24,digits =2))
    miss_rate<-append(miss_rate,round(sum(fam_trial$rt_col[fam_trial$id==id]==-1)/24,digits=2))
    correct_rejection <- append(correct_rejection, round(sum(fam_block$rt[fam_block$par_id==id]==-1 & fam_block$targ[fam_block$par_id==id]!=fam_block$stimulus[fam_block$par_id==id])/264,digits=2))
    false_alarm <- append(false_alarm, round(sum(fam_block$rt[fam_block$par_id==id]!=-1 & fam_block$targ[fam_block$par_id==id]!=fam_block$stimulus[fam_block$par_id==id])/264,digits=2))
  }
  
  subj_table <- data.frame(list_vsl_id,mean_rt, rt_slope,hit_rate, miss_rate,correct_rejection,false_alarm)
  colnames(subj_table) <- c("VSL_ID","mean_rt", "rt_slope","hit_rate", "miss_rate","correct_rejection","false_alarm")
  print(kable(subj_table,format = "pandoc"))
  return(mean_table)
}
```

##Summary Table
```{r}
fam_trial_vsl <- compute_visual()
```

##Plot of VSL
```{r,echo=FALSE}
ggplot(fam_trial_vsl,aes(y=rt_col,x=reindex))+geom_point(color='deepskyblue3') + geom_smooth(method='lm') + labs(x="Trial Index", y="Response time (ms)",title="Resposne time by trial index in VSL")
```

##Boxplot of the first half of the trials is significantly greater than the latter half of the trial
```{r,echo=FALSE}
par(mfrow=c(1,2))
boxplot(fam_trial_vsl$rt_col[fam_trial_vsl$reindex<12], main="RT - first half of the trials",col="deepskyblue4",pars=list(ylim=c(100,800)))
boxplot(fam_trial_vsl$rt_col[fam_trial_vsl$reindex>12], main="RT - latter half of the trials",col="deepskyblue4")

```

#Compute RT for TSL
```{r,echo=FALSE}
compute_aud <- function(data)
{
  rt_col <- NULL
  id <- NULL
  trial <- NULL
  target <- NULL
  group_cond <- NULL
  row_number <- which(tsl$targ==tsl$stimulus)
  for (i in row_number){
    if (tsl[i,]$rt > 0){rt_col <- append(rt_col,tsl[i,][,"rt"]-100)}
    if (tsl[i,]$rt < 0){rt_col <- append(rt_col,100-tsl[i,][,"rt"]-100)}
    trial <- append(trial,tsl[i,][,"trial_index"])
    id <- append(id,tsl[i,]$par_id)
    group_cond <- append(group_cond,tsl[i,]$group)
    if (tsl[i+1,][,"rt"]!=-1000 & tsl[i+1,][,"rt"]<0){
      rt_col[(match(i,row_number))] <- 480-tsl[i+1,][,"rt"]}
    
    if (tsl[i-1,][,"rt"]>0){
      rt_col[(match(i,row_number))] <- 480-tsl[i-1,][,"rt"]
      
    }}
  rt_df1 <- data.frame(trial,rt_col,id,group_cond)
  fam_block <- tsl[which(tsl$trial_index<603 & tsl$trial_index>26),]
  fam_trial <- rt_df1[which(rt_df1$trial<603 & rt_df1$trial>26), ]
  reindex <- rep(1:48,29)
  fam_trial$reindex <- reindex
  mean_table <- fam_trial[which(fam_trial$rt_col!=-1000),]
  mean_table <- fam_trial[which(fam_trial$rt_col<580 & fam_trial$rt_col>-380), ]
  hit_rate <- NULL
  miss_rate <- NULL
  correct_rejection <- NULL
  false_alarm <- NULL
  mean_rt <- NULL
  rt_slope <- NULL
  for(id in list_tsl_id){
    mean_rt<-append(mean_rt,round(mean(mean_table$rt_col[mean_table$id==id]),digits=3))
    rt_slope <-append(rt_slope,round(summary(lm(mean_table$rt_col[mean_table$id==id]~mean_table$trial[mean_table$id==id]))$coefficient[2,1],digits=3))
    hit_rate<-append(hit_rate,round(sum(mean_table$rt_col[mean_table$id==id]!=-1000)/48,digits =2))
    miss_rate<-append(miss_rate,round(sum(fam_trial$rt_col[fam_trial$id==id]==-1000 | fam_trial$rt_col[fam_trial$id==id]<=-480 | fam_trial$rt_col[fam_trial$id==id]>960)/48,digits=2))
    correct_rejection <- append(correct_rejection, round(sum(fam_block$rt[fam_block$par_id==id]==-1000 & fam_block$targ[fam_block$par_id==id]!=fam_block$stimulus[fam_block$par_id==id])/528,digits=2))
    false_alarm <- append(false_alarm, round(sum(fam_block$rt[fam_block$par_id==id]!=-1000 & fam_block$targ[fam_block$par_id==id]!=fam_block$stimulus[fam_block$par_id==id])/528,digits=2))
  }
  
  
  subj_table <- data.frame(list_tsl_id,mean_rt, rt_slope,hit_rate, miss_rate,correct_rejection,false_alarm)
  colnames(subj_table) <- c("TSL ID","mean_rt", "rt_slope","hit_rate", "miss_rate","correct_rejection","false_alarm")
  print(kable(subj_table))
  return(mean_table)
}
```

##Summary Table
```{r}
fam_trial_tsl <- compute_aud()
```

##Plot of TSL
```{r,echo=FALSE}
ggplot(fam_trial_tsl,aes(y=rt_col,x=reindex))+geom_point(color='deepskyblue3') + geom_smooth(method='lm') + labs(x="Trial Index", y="Response time (ms)",title="Resposne time by trial index in TSL")
```

##Boxplot of the first half of the trials is significantly greater than the latter half of the trial
```{r,echo=FALSE}
par(mfrow=c(1,2))
boxplot(fam_trial_tsl$rt_col[fam_trial_tsl$reindex<24], main="RT - first half of the trials",col="deepskyblue4")
boxplot(fam_trial_tsl$rt_col[fam_trial_tsl$reindex<24], main="RT - latter half of the trials",col="deepskyblue4")

```

```{r,fig.width=10, fig.height=6, echo=FALSE}
DD_mean_vsl <- NULL
DD_mean_tsl <- NULL
DD_tsl_hit_rate <- NULL
DD_vsl_hit_rate <- NULL
TYP_mean_vsl <- NULL
TYP_mean_tsl <- NULL
TYP_tsl_hit_rate <- NULL
TYP_vsl_hit_rate <- NULL
number_DD <- NULL
number_TYP <- NULL

for(id in DD){
  DD_mean_vsl<- mean(append(DD_mean_vsl,round(mean(fam_trial_vsl$rt_col[fam_trial_vsl$id==id]))),na.rm=TRUE)
  DD_mean_tsl<- mean(append(DD_mean_tsl,round(mean(fam_trial_tsl$rt_col[fam_trial_tsl$id==id]))),na.rm=TRUE)
  DD_vsl_hit_rate<-round(mean(append(DD_vsl_hit_rate,round(sum(fam_trial_vsl$rt_col[fam_trial_vsl$id==id]!=-1)/24,digits =2)),na.rm=TRUE),digits=2)
  DD_tsl_hit_rate<-round(mean(append(DD_tsl_hit_rate,round(sum(fam_trial_tsl$rt_col[fam_trial_tsl$id==id]!=-1000)/48,digits =2)),na.rm=TRUE),digits=2) 
  number_DD <- length(intersect(list_vsl_id, DD))
}

for(id in TYP){
  TYP_mean_vsl<-mean(append(TYP_mean_vsl,round(mean(fam_trial_vsl$rt_col[fam_trial_vsl$id==id]))),na.rm=TRUE)
  TYP_mean_tsl<-mean(append(TYP_mean_tsl,round(mean(fam_trial_tsl$rt_col[fam_trial_tsl$id==id]))),na.rm=TRUE)
  TYP_vsl_hit_rate<-round(mean(append(TYP_vsl_hit_rate,round(sum(fam_trial_vsl$rt_col[fam_trial_vsl$id==id]!=-1)/24,digits =2)),na.rm=TRUE),digits=2)
  TYP_tsl_hit_rate<-round(mean(append(TYP_tsl_hit_rate,round(sum(fam_trial_tsl$rt_col[fam_trial_tsl$id==id]!=-1000)/48,digits =2)),na.rm=TRUE),digits=2)
  number_TYP <- length(intersect(list_vsl_id, TYP))
}

DD_col <- rbind(DD_mean_tsl,DD_mean_vsl,DD_tsl_hit_rate,DD_vsl_hit_rate,number_DD)
TYP_col <- rbind(TYP_mean_tsl,TYP_mean_vsl,TYP_tsl_hit_rate,TYP_vsl_hit_rate,number_TYP)
compare_table <- cbind(DD_col,TYP_col)
colnames(compare_table) <- c("Dylexia","Typical")
rownames(compare_table) <- c("RT_TSL","RT_VSL","Hit_rate_tsl","Hit_rate_vsl","Number of participants")
print(kable(compare_table))
par(mfrow=c(1,2))

qplot(reindex,rt_col,data=fam_trial_vsl,facets=(. ~ fam_trial_vsl$group_cond),color= group_cond, main="VSL RT by group", ylab="Response time", xlab="Trial index") + geom_smooth(method='lm') 
qplot(reindex,rt_col,data=fam_trial_tsl,facets=(. ~ fam_trial_tsl$group_cond),color= group_cond,main="TSL RT by group",ylab="Response time", xlab="Trial index") + geom_smooth(method='lm') 

```

#Compute accuracy
```{r,echo=FALSE}
vsl_acc <- vsl[which(vsl$trial_index<614 & vsl$trial_index>309),]
tsl_acc <- tsl[which(tsl$trial_index<831 & tsl$trial_index>608),]
vsl_cond <- NULL
for (i in seq(from=1,to=length(vsl$cond),by=533)){vsl_cond<-append(vsl_cond,as.character(vsl[i,]$cond))}
tsl_cond <- NULL
for (i in seq(from=1,to=length(tsl$cond),by=832)){tsl_cond<-append(tsl_cond,as.character(tsl[i,]$cond))}

ans <- NULL
keyv <- NULL
subj <- NULL
cond<- NULL

#vsl acc
row_numberv <- which(vsl_acc$key_press != -1 & vsl_acc$stimulus=="")
for (i in row_numberv){
  ans<-append(ans,vsl_acc[i,]$key_press)
  subj <- append(subj,vsl_acc[i,]$par_id)
  cond <- append(cond,vsl_acc[i,]$group)
}

vsl_accuracy <- data.frame(ans,subj,cond)

#tsl acc
ans <- NULL
keyt <- NULL
subj <- NULL
cond<- NULL

row_numbert <- which(tsl_acc$key_press != -1 & (tsl_acc$trial_index-613)%%7==0)
for (i in row_numbert){
  ans<-append(ans,tsl_acc[i,]$key_press)
  subj <- append(subj,tsl_acc[i,]$par_id)
  cond <- append(cond,vsl_acc[i,]$group)
  
}

tsl_accuracy <- data.frame(ans,subj,cond)

for(cond in vsl_cond){
  if (cond=="lang1"){keyv<-append(keyv,language_1)}
  else if (cond=="lang2"){keyv<-append(keyv,language_2)}}

for(cond in tsl_cond){
  if (cond=="lang1"){keyt<-append(keyt,language_1)}
  else if (cond=="lang2"){keyt<-append(keyt,language_2)}}



vsl_accuracy$key <- keyv
tsl_accuracy$key <- keyt

vsl_accuracy$ans <- gsub(50,2,vsl_accuracy$ans)
vsl_accuracy$ans <- gsub(49,1,vsl_accuracy$ans)

tsl_accuracy$ans <- gsub(37,1,tsl_accuracy$ans)
tsl_accuracy$ans <- gsub(39,2,tsl_accuracy$ans)

corr <- NULL
corrt <- NULL

for (i in seq(from=1,to=length(vsl_accuracy$ans),by=1)) {corr<-append(corr,as.numeric(vsl_accuracy[i,]$ans==vsl_accuracy[i,]$key))}
vsl_accuracy$corr <- corr
subj_corr <- NULL
for (id in list_vsl_id) {subj_corr <- append(subj_corr,round(sum(vsl_accuracy$corr[vsl_accuracy$subj==id])/32,digits=3))}
vsl_acc_table <- data.frame(list_vsl_id,subj_corr,vsl_cond)

for (i in seq(from=1,to=length(tsl_accuracy$ans),by=1)) {corrt<-append(corrt,as.numeric(tsl_accuracy[i,]$ans==tsl_accuracy[i,]$key))}
tsl_accuracy$corr <- corrt
subj_corrt <- NULL
for (id in list_tsl_id) {subj_corrt <- append(subj_corrt,round(sum(tsl_accuracy$corr[tsl_accuracy$subj==id])/32,digits=3))}
tsl_acc_table <- data.frame(list_tsl_id,subj_corrt,tsl_cond)

DD_acc_vsl <- NULL
DD_acc_tsl <- NULL
TYP_acc_vsl <- NULL
TYP_acc_tsl <- NULL

for(id in DD){
  DD_acc_vsl<- mean(append(DD_acc_vsl,vsl_acc_table$subj_corr[vsl_acc_table$list_vsl_id==id]),na.rm=TRUE)
  DD_acc_tsl<- mean(append(DD_acc_tsl,tsl_acc_table$subj_corr[tsl_acc_table$list_tsl_id==id]),na.rm=TRUE)
}

for(id in TYP){
  TYP_acc_vsl<- mean(append(TYP_acc_vsl,vsl_acc_table$subj_corr[vsl_acc_table$list_vsl_id==id]),na.rm=TRUE)
  TYP_acc_tsl<- mean(append(TYP_acc_tsl,tsl_acc_table$subj_corr[tsl_acc_table$list_tsl_id==id]),na.rm=TRUE)
}
DD_acc_col <- rbind(DD_acc_tsl,DD_acc_vsl)
TYP_acc_col <- rbind(TYP_acc_tsl,TYP_acc_vsl)
compare_acc_table <- cbind(DD_acc_col,TYP_acc_col)
colnames(compare_acc_table) <- c("Dylexia", "Typical")
rownames(compare_acc_table) <- c("TSL accuracy","VSL accuracy")
```
#VSL Accuracy across subjects
```{r,echo=FALSE}
print(kable(vsl_acc_table))
```
#TSL Accuracy across subjects
```{r,echo=FALSE}
print(kable(tsl_acc_table))
```

#Compare accuracy between Dylexia and Typical group
```{r,echo=FALSE}
print(kable(compare_acc_table))

```

