# General Guideline for EEG File Processing

All the raw EEG files are saved at Y:\projects\blast\data\eeg\rawdata

Before starting any processing, move the raw EEG files from  Y:\projects\blast\data\eeg\rawdata to Y:\projects\blast\data\eeg\Analysis\rawdata. In the Analysis\rawdata folder, each subject should have their own folder named with their subject ID. If there isn't one for a new subject, create one. Put the raw data for the three runs in the corresponding folder.

All the processing Matlab scripts are saved in Y:\projects\blast\data\eeg\Analysis\Matlab_Scripts

## Edit Subject Script

Open *'blast_subjects'* script.

On Matlab, change the numbers in the parenthesis to **(s, (1:(the # of the last subject we have run))**

```Matlab
% get data path
if ismember(s,(1:25))
```

Add the new subject following the format **below**. **Do NOT** delete the existing subject numbers on the script. Remember to save the script after you edited it.

```Matlab
elseif s == 25
    subject = 'blast_a_025';
end
```

## Start Preprocessing

To start preprocessing, open the *'blast_preproc_PC'* script. The same run of multiple subjects can be preprocessed at once in this script.

Change the run number in **current_run='_run#'**. 

```Matlab
current_run = '_run3'; % establish current run
```

Change the subject number in: **for s = [#]**. If you are running subject 1 to 3, for example, change it in this format: **for s = [1:3]**. 

```Matlab
% establish subject list
for s = [1] %edit for subject of interest (can run multiple at once)
```

After changing the subject number. Run the script. If the script is successfully run, you should see the file named as **'subjectID_run#_fl_rr.set'** in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\wkdir

## Manual Inspectation of the Preprocessed Data 

Manual inspectation and removal of bad block of the data should be done after preprocessing and before runinng ICA. Save file that is checked with the name: **'subject_run#_fl_rr_check.set'**.

## Run ICA

Open TBA script

Change the subject number in the line **below**: 

```Matlab
for s = [1]
```

Run the script. You should see *'subjectID_ica.set'* file in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\wkdir 

## Manual Rejection of Components

(Ask Jojo, Rachael, Julie how to do this step.) Save manually rejected file as: **'subject_run#_clean.set'**

## Merge component rejected files

Open *'blast_merge_datasets_PC'* script in Matlab. Change the subject number in **for s = [#]**. This script will only be run on subjects that have **'clean.set'** files from **all three runs**. 

```Matlab
for s = [1]
```

If the script is successfully run, you should see the file named as *'subjectID_merged_clean.set'* in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\wkdir

## Run Epoching

Open *'blast_eventlist_PC'* script in Matlab. Change the subject number in **for s = [#]**.

```Matlab
% establish subject list
for s = [2] %edit for subject of interest (can run multiple at once)
```

If the script is successfully run, you should see the files named as **'subjectID_epoch_ar.set'** and **'AR_summary_subjectID_epoch_ar.txt'** in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\wkdir

## Create ERP  

Open TBA script in Matlab. Change the subject number in **for s = [#]**.

```Matlab
% establish subject list
for s = [1] %edit for subject of interest (can run multiple at once)
```

If the script is successfully run, you should see the file named as TBA

## Average ERP
TBA
