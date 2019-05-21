#  BLAST Online Session LSL Data Cleaning
#  Violet Kozloff
#  October 10th, 2018 
#  Adapted from lsl_rt_clean_file by An Nguyen
#  This script cleans LSL files from the online session of the BLAST experiment
#  NOTE: Before running, make sure all files contain "responses" column (may need to be added manually)
#  TO DO: Make sure it can accept the weird files with no "responses" column
#  ****************************************************************************
  
lsl <- read.csv("/Users/vkozloff/Documents/blast_adult_web_sl_data/original/lsl_original/blast_a_006_lsl.csv")

if(lsl[1,11]!=""){
  # Separates the responses into keypress, rt, and stimulus; puts this all into "rep"
  rep <- unlist(strsplit(paste(lsl[9,11]), split=',', fixed=TRUE))
  # Otherwise the reponses are in column 2
} else {
  # Separates the responses into keypress, rt, and stimulus; puts this all into "rep"
  rep <- unlist(strsplit(paste(lsl[10,2]), split=',', fixed=TRUE))
}

#extract animation
# If the responses column is column 11
if(lsl[1,11]!=""){
  # stimuli_all splits the stimulus from the time it was presented.
  # Is shows the whole animation sequence that the participant saw (as an array)
  ani_stim <- unlist(strsplit(paste(lsl[9,10]), split=',', fixed=TRUE))
  # Otherwise the animation_sequence is in column 11
} else{
  ani_stim <- unlist(strsplit(paste(lsl[10,11]), split=',', fixed=TRUE))
}

  
  key= NULL
  rt  <- NULL
  stim_press <- NULL
  stim_disp <- NULL
  time <- NULL
  for (j in seq(from=2, to=length(rep), by=3)) {
    rt<- append(rt,as.numeric(unlist(strsplit(paste(rep[j]), split=':'))[2]))
  }
  
  
  for (k in seq(from=3, to=length(rep), by=3)) {
    stim_press<- append(stim_press, gsub('.{2}$','',unlist(strsplit(paste(rep[k]), split=':\"', fixed=TRUE))[2]))
    
  }
  
  for (i in seq(from=1, to=length(ani_stim), by=2)) {
    stim_disp<- rbind(stim_disp, gsub('.{1}$','',unlist(strsplit(paste(ani_stim[i]), split=':\"', fixed=TRUE))[2]))}
  
  for (n in seq(from=2, to=length(ani_stim), by=2)) {
    time<- rbind(time, gsub('.{1}$','',unlist(strsplit(paste(ani_stim[n]), split=':', fixed=TRUE))[2]))}
  
  table1 <- data.frame(rt,stim_press)
  table2<-data.frame(stim_disp,time)
  
  table2 <- table2[1:576,]
  table2$col2 <- "NA"
  table2$col1 <- "NA"
  table1$stim_press <- paste(table1$stim_press)
  table2$stim_disp <- paste(table2$stim_disp)
  table2$time <- as.numeric(paste(table2$time))
  for (i in seq(from=1,to =length(table1$stim_press),by=1)) {
    temp1 <- table1[i,]
    index <- 0
    min <- .Machine$integer.max
    
    for  (j in seq(from=1,to =length(table2$stim_disp),by=1)) {
      temp2 <- table2[j,]
      if (temp2[3]=="NA") {
        if (temp1[2]==temp2[1]){
          if (abs(temp1[1]-temp2[2]) < min){
            min <- abs(temp2[2]-temp1[1])
            index <- j}
        }
      }
    }
    table2$col1[index] <- temp1[1]
    table2$col2[index] <- temp1[2]}
  table2$target <- lsl$targ[1]
  table2$cond <- lsl$cond[1]
  table2$time<-as.numeric(table2$time)
  table2$time<-as.numeric(col1$col1)
  table2$rt <- (table2$time-table2$col1)
  table2$par_id <- rep(gsub('.{2}$','',unlist(strsplit(paste(lsl$response[1]), split=':"', fixed=TRUE))[2]),length(lsl$responses[1]))
  table2<-as.matrix(table2)
  write.csv(table2,file=as.character(file))
}

for (file in files)
{
  cleandata(paste0(path,file))
}



```


