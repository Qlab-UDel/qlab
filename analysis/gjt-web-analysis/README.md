## GJT Analysis
This MATLAB code automates the GJT scoring process for BLAST and SPOLI participants. It uses information about the results from participant's online GJT test and their age to determine their standard score. 
# General Guideline for GJT Analysis
* The working directory is set as:
```
/Volumes/data-1/projects/blast/matlab_scripts/gjt_analysis/ 
```
* code is saved in NAS, and needs files saved in NAS in order to run
* The files needed to run this code are: 
  * raw SPOLI data: `/Volumes/data-1/projects/spoli/raw_sl_data`
  * raw BLAST data: `/Volumes/data-1/projects/blast/data/online_sl/blast_child`
  * gjt standard score conversion table: `/Volumes/data-1/projects/blast/matlab_scripts/gjt_standard_score_conversion_table`
  * SPOLI participant ages: `/Volumes/data-1/projects/blast/demographic_data/spoli_ages.xlsx`
  * BLAST participant ages: `/Volumes/data-1/projects/blast/demographic_data/blast_ages.xlsx` 
  
# Steps of GJT Automation 

## Step 1.
* Set the working directory as the folder where the code is saved
* Define the location of SPOLI and BLAST raw data files where it is saved on NAS
```
spoli_folder = '/Volumes/data-1/projects/spoli/raw_sl_data';
blast_folder = '/Volumes/data-1/projects/blast/data/online_sl/blast_child';
```
## Step 2. 
Define the location of the spreadsheets with SPOLI and BLAST subject's ages 
```
spoli_age_path = '/Volumes/data-1/projects/blast/demographic_data/spoli_ages.xlsx';
blast_age_path = '/Volumes/data-1/projects/blast/demographic_data/blast_ages.xlsx';
```
## Step 3. 
Create empty lists for the raw score, standard score, participant IDs, number of hits, and number of false alarms. The for loops in future steps will add values to these empty lists
## Step 4.
Calculate the raw score for each participant. Then, create a table containing the participant ID, hit rate, and false alarm rate. 
```
%Combine scores
scores=horzcat(string(ids), hits, false_alarms, a_prime_round);
%create table
titled_scores = array2table(scores, 'VariableNames', {'part_id', 'hit_rate', 'false_alarm_rate', 'a_prime'});
 ```
 ## Step 5. 
 * Match the participant's age to their ID. Use ages and raw score to calculate standard score through a for loop. 
 * If the participant's age is missing from the spreadsheet, the script excludes it from the for loop that calculates standard score, and outputs and error message in the final output table. *Check spelling of participant*

## Step 6. 
* Create a table which includes participant ID, hit rate, false alarm rate, raw score, and standard score. 
* Save the scores to NAS in the data_summaries folder: 
```
writetable(scores_table,'/Volumes/data-1/projects/blast/data_summaries/blast_online_child/breakdown/gjt_score.csv');
 ```
