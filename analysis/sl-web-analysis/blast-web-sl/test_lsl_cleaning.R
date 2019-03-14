# Prepare workspace ------------------------------------------------------------

# Set directory
setwd("/Users/vkozloff/Documents/qlab/analysis/sl-web-analysis/blast-web-sl")
# Remove objects in environment
rm(list=ls())

# Prepare files ------------------------------------------------------------

# Read in files
presented_stimuli <-read.csv("/Users/vkozloff/Desktop/presented_stimuli.csv")
responded_stimuli <-read.csv("/Users/vkozloff/Desktop/responded_stimuli.csv")

#Select relevant columns
presented_stimuli<-data.frame(as.character(presented_stimuli$stim_disp),presented_stimuli$time,presented_stimuli$targ, presented_stimuli$part_id)
responded_stimuli<-data.frame(as.character(responded_stimuli$stim_press),responded_stimuli$rt)
#Standardize column names
names(presented_stimuli) <- c("stimulus", "presentation_time", "targ", "part_id")
names(responded_stimuli) <- c("stimulus", "keypress_time")
# Standardize column content
presented_stimuli$stimulus <- paste(presented_stimuli$stimulus)
responded_stimuli$stimulus <- paste(responded_stimuli$stimulus)
presented_stimuli$keypress_time <- "NA"
#Remove any blank rows
responded_stimuli <- responded_stimuli[which(responded_stimuli$keypress_time!="NA"),]

# For each stimulus, find the presentation time of following stimulus
offset_time <- NULL
for (i in seq(from=1,to =length(presented_stimuli$stimulus),by=1)) {
offset_time<-rbind(offset_time, presented_stimuli$presentation_time[i+1])
  }

presented_stimuli<-cbind(presented_stimuli, offset_time)

oops<-0
case1<-0
case2<-0

for (i in seq(from=1,to =length(responded_stimuli$stimulus),by=1)) {
  correct_pres_stim <- max(which(presented_stimuli$presentation_time<responded_stimuli$keypress_time[i]))
  if(responded_stimuli$stimulus[i]!="image/image/blank.png"){
    presented_stimuli$keypress_time[correct_pres_stim]<-responded_stimuli$keypress_time[i]-presented_stimuli$presentation_time[correct_pres_stim]
    case1<-case1+1
      }
  else{
    presented_stimuli$keypress_time[correct_pres_stim]<-responded_stimuli$keypress_time[i]-presented_stimuli$presentation_time[correct_pres_stim-1]
    case2<-case2+1 
    }
}

moop<- matchup (responded_stimuli, responded_offset)
  



# Match keypress time from responded_stimuli to the corresponding stimulus in presented stimuli---------------

# initialize case variables to check unaddressed edge cases
case_a<-0
case_b<-0
edge_case<-0

# initialize presented_stimuli row index
i <- 1
# initialize responded_stimuli row index
j <- 1

# For each row of the responded stimuli
by(responded_stimuli, 1:nrow(responded_stimuli), )



# Loop through the responded stimuli
while (j<length(responded_stimuli$stimulus)){
  # Loop through presented stimuli
  i<-1
  while (i<length(presented_stimuli$stimulus)){
    # Check that it's not yet the last presented stimulus
    if(i<length(presented_stimuli$stimulus)){
      # If a responded stimulus's keypress time falls between the presentation times of two presented stimuli
      if((responded_stimuli[j,2]>presented_stimuli[i,2]) & (responded_stimuli[j,2] < presented_stimuli[i+1,2]) 
         # And the responded stimulus matches the first presented stimulus
         & responded_stimuli[j,1]==presented_stimuli[i,1]){
        # Fill the earlier presented stimulus's keypress_time with the keypress_time of the responded stimulus
        presented_stimuli[i,5] <- responded_stimuli[j,2]-presented_stimuli[i,2]
        case_a<- case_a+1}
      }
    # At the final row of the presented stimuli
    else if (i==length(presented_stimuli$stimulus)){
    # If a responded stimulus's keypress time falls comes after the display time of a presented stimulus
    if((responded_stimuli[j,2]>presented_stimuli[i,2]) 
       # And the responded stimulus matches the presented stimulus
       & responded_stimuli[j,1]==presented_stimuli[i,1]){
      # Fill the presented stimulus's keypress_time with the keypress_time of the responded stimulus
      presented_stimuli[i,3] <- responded_stimuli[j,2]
      case_b<-case_b+1
      }
    }
    # Catch any unusual edge cases
    else{edge_case<-edge_case+1}
    i<-i+1
    }
  j<-j+1
}


presented_stimuli$rt <- "none_yet"

test <- NULL
testy <- presented_stimuli[which(presented_stimuli$keypress_time=="NA"),]

# Internal check: these variables can help make sure all cases are accounted for (no extra edge cases)
case1<-0
case2<-0
case3<-0
case4<-0

for (test_row in length(presented_stimuli$stimulus)){
  # If the participant responded to the stimulus, record that reaction time
  if(!is.na(presented_stimuli$keypress_time[test_row]))
    {presented_stimuli$rt[test_row]<-as.numeric(presented_stimuli$keypress_time[test_row])-as.numeric(presented_stimuli$presentation_time[test_row])
    case1<-case1+1}
  # If it's the final stimulus, record the keypress value as the reaction time
  else if (test_row==length(letter_rows))
    {presented_stimuli$rt[test_row]<-presented_stimuli$keypress_time[test_row]
    case2<-case2+1}
  # If the stimulus has a blank keypress value and so does the following stimulus, record its NA keypress value
  else if (presented_stimuli$keypress_time[test_row]=="NA" & is.na(presented_stimuli$keypress_time[test_row+1])) 
    {presented_stimuli$rt[test_row]<-presented_stimuli$keypress_time[test_row]
    case3<-case3+1}
  # If the stimulus has a blank keypress value and so does the following stimulus, subtract the stimulus presentation
  # time from the following stimulus's keypress
  else if (presented_stimuli$keypress_time[test_row]=="NA" & !(presented_stimuli$keypress_time[test_row+1]=="NA")) 
    {presented_stimuli$rt[test_row]<-(as.numeric(presented_stimuli$keypress_time[test_row+1])-(presented_stimuli$presentation_time[test_row]))
    case4<-case4+1}
  # Internal check: all edge cases should be accounted for. If edge_case > 0, a case is unaddressed.
  else 
    {edge_case<-edge_case+1}
}



no_blanks <- presented_stimuli[which(presented_stimuli$stimulus!="blank"),]

# Internal check: See if there were any unaddressed edge_cases
View(length(edge_case))
