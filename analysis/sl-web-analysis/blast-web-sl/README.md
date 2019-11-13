# Script to analyze data from SL-online experiments

## child_raw_data_cleaning_scripts folder

- scripts to clean raw online SL data for children data
- These are saved on NAS: `/Volumes/data/projects/blast/r_scripts/blast_web_sl`

## adult_raw_data_cleaning_scripts folder

- scripts to clean raw online SL data for adult data
- These are saved on NAS: `/Volumes/data/projects/blast/data/online_sl/adult_analysis_script`
(Will find a better location to save the adult scripts after discussion)

## Specific conference folders
- scripts for statistical analysis for cleaned raw data 

(The reason why they are grouped in specific conferences are because they have specific sample and results. Back up for raw data input will be in a different place).

## cleaned_data folder

**This is what you need for statiscal analysis**

- The cleaned data are here. These are just copies from NAS. See below to find where they are saved on NAS. Please use data output from NAS for most updated and accurate results.

## rt_hit_trial_count_by_subject.R (used for removing outliers for RT analysis)

- script to count how many hit trials each participant has during the exposure phase


# How to use the scripts?

## Children data:

1. Run all scripts in child_raw_data_cleaning_scripts folder first to clean the raw data:

**The LSL script has to be run in this order:**

**First, blast_web_lsl_cleaning.R**
Then, blast_web_lsl_predictable_2afc.R, blast_web_lsl_random_2afc.R, blast_web_lsl_rt_analysis.R (order does not matter here.)

2. Find the cleaned children raw data at:

```
/Volumes/data/projects/blast/data_summaries/blast_online_child/breakdown/
```

## Adult data:

1. Run all scripts in adult_raw_data_cleaning_scripts folder first to clean the raw data:

**The LSL script has to be run in this order:**

**First, blast_web_lsl_cleaning.R**
Then, blast_web_lsl_predictable_2afc.R, blast_web_lsl_random_2afc.R, blast_web_lsl_rt_analysis.R (order does not matter here.)

2. Find the cleaned adult raw data at:

```
/Volumes/data/projects/blast/data_summaries/blast_online_adult/breakdown/
```

  

# Changes in blast-web-sl analysis scripts:

**Changes in task and analysis script from Fall 2018? (need to confirm)**

- Fixed SSL for the number of stimuli in the exposure phase (previously, lacking the very last stimulus)
- Fixed LSL randomization in the two-alternative-force-choice test phase (previously, LSL test phase answers are not randomized, see answer keys in LSL scripts)
- Fixed LSL presentation time from 1000ms-letter and 1000ms-blank to 800ms-letter and 200ms-blank

**Changes in task and analysis script from Spring 2019?**

- RT analysis now takes one stimulus-preceding and one stimulus-following as time window (-480ms to +960ms for auditory task; -1000 to +2000ms for visual task)

**Changes in task and analysis script from Sep 2019**

- From June/11/2019, the two-alternative-force-choice test phase in all blast web sl tasks are changed into a counterbalanced design, so that in the test phase, target triplet and foil triplet are counterbalanced (4 target triplet types x 4 foil triplet types x 2 orders they can occur in a trial = 32 trials in total in the test phase). Thus, answer keys are changed for accuracy and entropy calculations. Scripts from now account for both answer keys before June 2019 and after June 2019.

- RT Slope is now scaled. Reaction time in each individual hit trial is first scaled and then linear regression is run on scaled individual RTs to get a scaled RT slope.

**Still In Progress**

- Still need to check d-prime and etc., in the RT analysis. Mean RT and RT slope are up to date.
