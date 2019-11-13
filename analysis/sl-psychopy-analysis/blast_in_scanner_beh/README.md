# BLAST In-Scanner Behavioral Analysis for Raw Data

This R script automates the behavioral data analysis process for BLAST in-scanner data collected with Psychopy. 
It uses information about the results from participant's keypresses to find mean reaction time and reaction time from the two-alternative forced-choice task.
Calculations are peformed for visual and auditory data from linguistic and non-linguistic domains in random and structured blocks 

* The working directory is set as the location where the data is saved on NAS:
```
Volumes/data/projects/blast/data/mri/in_scanner_behavioral/adult/sl_raw_data
```
* The script is saved in NAS
```
data/projects/blast/r_scripts/blast_scanner_sl/blast_in_scanner_beh.R
```

```
* The cleaned data output is stored on NAS:
```
/Volumes/data/projects/blast/data_summaries/blast_in_lab_adult/behavioral/adult_in_scanner_auditory_behavioral.csv
/Volumes/data/projects/blast/data_summaries/blast_in_lab_adult/behavioral/adult_in_scanner_visual_behavioral.csv
```
* The cleaned data output is pushed to cleaned_data folder here on github (RT slope are not scaled, will rerun if scaling is needed (11/12/2019))

- Auditory data: adult_in_scanner_auditory_behavioral.csv
- Visual data: adult_in_scanner_visual_behavioral.csv


# Steps of In-Scanner Analysis

## Step 1. Extract and prepare data

## Prepare environment
* Install packages and load libraries
* Set working directory
```
/Volumes/data/projects/blast/data/mri/in_scanner_behavioral/adult/sl_raw_data
```
Remove objects in environment

## Extract and prepare auditory data
* Extract relevant columns of auditory data
* Check for extra or incorrect auditory targets
* Prepare auditory data for use

## Extract and prepare visual data
* Extract relevant columns of visual data
* Check for extra or incorrect visual targets
* Prepare visual data for use

# Step 2. Find Auditory Reaction Time Means and Slopes

## Identify response times to target stimuli.

* Isolate target rows

```
auditory_targets
```

* Isolate participants' response times.

* Combine the reaction time data into one dataframe. Contains all targets from the exposure phase and their true auditory_rts (includes any response within 480 ms of a target)
Note: reaction times are in milliseconds

```
exp_auditory_targets <- data.frame(auditory_part_id, auditory_condition, auditory_modality, auditory_task, auditory_rt)
```

Note: This code does not currently account for alternating auditory targets and keypresses

* Find the number of RTs for each participant

* Internal check: make sure that all RTs are valid, ie. fall within 1 SOA of the stimulus. Alert user if not.

```
auditory_rt_check
```

## Calculate auditory mean reaction times

```
exp_auditory_mean_rts
```

## Calculate auditory reaction time slopes
* Reindex the targets by type (random syllable, structured tone, etc) for each participant
```
exp_auditory_targets$index
```

* Calculate reaction time slopes

* Bind all auditory output
```
auditory_output
```

* Write all auditory output to NAS

```
/data/projects/blast/data_summaries/blast_in_lab_adult/behavioral/
```

NOTE: The copy of the script pushed to Github does not currently calculate RT slope and mean RT for visual data. The copy on NAS has a working version of this functionality (true for Nov/ 2019?)

# stat_analysis folder

- Script for analyzing processed raw data.

