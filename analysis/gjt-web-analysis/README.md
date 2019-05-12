## GJT Analysis
This MATLAB code automates the GJT scoring process for BLAST and SPOLI participants. It uses information about the results from participant's online GJT test and their age to determine their standard score. 
# General Guideline for GJT Analysis
* The working directory is set as: cd /Volumes/data-1/projects/blast/matlab_scripts/gjt_sharon_working/
* code is saved in NAS, and needs files saved in NAS in order to run
* The files needed to run this code are: 
  * raw SPOLI data (csv file)
  * raw BLAST data (csv file)* gjt standard score conversion table (csv file)
  * SPOLI participant ages (csv file)
  * BLAST participant ages (csv file)
  
# Steps of GJT Automation 

## Step 1.
* Set the working directory as the folder where the code is saved
* Define the location of SPOLI and BLAST raw data files where it is saved on NAS

## Step 2. 
* Define the location of the spreadsheets with SPOLI and BLAST subject's ages 


```
spoli_age_path = '/Volumes/data-1/projects/blast/demographic_data/spoli_ages.xlsx';
blast_age_path = '/Volumes/data-1/projects/blast/demographic_data/blast_ages.xlsx';
```

 
 
