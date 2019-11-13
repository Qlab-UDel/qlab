# SL-analysis

Script to analyze data from SL-online experiments

- ABCD_analysis: script to analyze the ABCD project (compare dylexia with typical population)
- blast-web-sl: scripts to clean raw data, and scripts for analyzing cleaned raw data are in specific conference folders 
- blast-web-sl/ blast_web_lsl_cleaning: script to extract the response time for online LSL experiment
- blast-web-sl/ rt_hit_trial_count_by_subject: script to count how many hit trials each participant has during the SL exposure phase
- correlation_analysis: script to check for correlation between each task
- fmri_pilot_analysis: very basic script to look at the reaction time and accuracy in simple behavioral experiment done in the fmri scanner. This analysis was for the older version of fmri experiment, and need to be updated in order to be used for the newer versions of the experiment.
- mturk_vsl, mturk_lsl, mturk_tsl, mturk_ssl: script to analyze the data from the online experiment with participants recruited from MTurk
- scf_cleaning: script to extract the important information from the screening form
- wj3_cleaning: script to extract the information from the wj3 task

## Changes in blast-web-sl analysis scripts:

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