# Creating fMRI Event Files
## Locating and Organizing Behavioral Event Data

Currently behavioral data is located in:
smb://qilab.ling.udel.edu//data/projects/blast/data/mri/in-scanner-behavior

Create an organized copy following current format in:
Macintosh HD/Users/qigroup/Documents/project/blast/in-scanner
-Copy the output_behavioral_template (main in-scanner folder) to the subject’s folder (change template to the subject ID)
-Open the ASL folder
 - Open the subject’s first auditory.csv file
 - Column F identifies whether they began with random ‘R’, structured ‘S’, or blank 'B'
 - Column A identifies whether they began with tone (e.g. 1A) or speech (e.g. pa)
   - If random is paired with tone in a particular file, it will be with tone throughout that file
   - silence is paired with blank 'B'
 
-In the subject’s new output_behavioral file you created, record this information into columns E and F
 - In column G input which file this came from (A1=auditory run 1; V2=visual run 2)
 - Do this for all the participant's 4 runs (auditory)
 
-Repeat for the VSL folder
 - Adding to the same output_behavioral file
 - Open the subject’s first visual.csv file
 - Column F identifies whether they began with random ‘R’, structured ‘S’, or blank 'B'
 - Column A identifies whether they began with image (e.g. Alien9) or letter (e.g.D)
 
**Important Note**: Be sure that spelling is consistent for trial_type. The following should always be used, should never be pluralized, and should be spelled correctly:
   - tone
   - speech
   - image
   - letter
   - silence
   
The below image is an example of what this step completed should look like:
![alt text](https://github.com/juliagoolia28/qlabfmripipe/blob/first-level_analysis/event_data_image.png)

-----------------------------If the below has been completed on 2 participants, stop here ------------------------------
## Formatting Log Files
-Locate .log file
 - Rename by adding _log to the end of the filename
 - Change the extension to .csv
 - Click ‘use .csv’ on the box that pops up
-Format the .csv sheet
 - Highlight column A
 - Select Data/Text to Columns
 - In the popup window, select Delimited then Next
 - In the next window, select Tab AND Space, then Finish
-Save the file (Continue)

## Creating event files that are compatible for first-level fMRI Analysis
-You want to locate the very first keypress made by the participant:
  - Start at the beginning of the file
  - Select column D
  - Command+ F ‘5’ 
  - Locate first Keypress and record value in column A (referred to as keypress val)

-You now want to locate each block:
  - Select column D
  - Command + F ‘auditory_run’ for ASL or ‘visual_run’ for VSL
  - Locate the first single TRUE in column F and identify the time this event occurred (column A) which is referred to as event onset val
  - In Column G
    - Subtract the event onset val from the event offset val
    - Copy and paste this value into the output_behavioral_subjectID sheet under column C ‘duration’
    
-Repeat this section for the remaining events in this file.
-Once you are done with this file, return to the “formatting log files” section and complete both sections on all auditory and visual sections until the output_behaivoral file is complete.

**Be sure to save throughout**

**Update the participant checklist with notes as you complete each subject**



 
