# General Guideline for EEG File Processing
First set up the subjects excel file (adult_subjects.xlsx). This is a single column excel sheet with subject codes that match the subject names listed on your raw data folders.

Next, setup your directory file (directory.m). This sets up the various paths from which we will input the raw data and to which we will output the processed data.

You are now ready to begin pre-processing your data. Starting from the *Preprocessing steps*, EEG data first gets filtered, rereferenced, component-identified, component-removed, epoched and binned.Then ERP will be computed.

All the raw EEG files are saved at Y:\projects\blast\data\eeg\Analysis\rawdata. In the Analysis\rawdata folder, each subject should have their own folder named with their subject ID. If there isn't one for a new subject, create one. Put the raw data of the three runs in the corresponding folder.

All the processing Matlab scripts are saved in Y:\projects\blast\data\eeg\Analysis\Matlab_Scripts

## EEG Analysis Pipeline Scripts

To start preprocessing, open the *'blast_adult_processing'* script. The same run of multiple subjects can be preprocessed at once in this script. 

This script starts the EEG adult data processing. It sets up the variables (e.g. run, epoch length, filter low pass and hight pass, etc.) that will be used later in the following sections of procesing. 

Establish all your variables of interest at the beginning of the script (e.g. run, epoch length, filter, etc.)

For each section of the script, you will establish which subjects you want to analyze. s{k} is the subject in your excel document. You can think about this as the column is k and each subject is s. In line 16, you can change which subject to start at in the list.  

Run the script one section at a time. The following portion of this README file breaks down the purpose of each section:

## Preprocessing steps
This script filters and references the raw data. Using the high pass and low pass varaibles above, it filters out the data that is outside of the low pass- high pass range. It also references the data to the M1 and M2 electrodes.

If the script is successfully run, you should see the file named as 'subjectID_run#_fl_rr.set' in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\wkdir

## Manual Inspectation of the Preprocessed Data 
Manual inspectation and removal of bad block of the data should be done after preprocessing and before runinng ICA. Save file that is checked with the name: **'subject_run#_fl_rr_check.set'**.

## Run ICA
ICA goes through the raw data and identifies and seperates the raw data into different components. It identifies things such as noises or activations.

You should see *'subjectID_ica.set'* file in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\wkdir 

## Manual Rejection of Components
Components, such as eyeblinks, are marked here and will later be rejected.

Save manually rejected file as: **'subject_run#_clean.set'**

## Epoching steps
This script marks stimulus-relavant chunks in the processed data so far. The variable epoch_length at the very beginning of this *EEG Analysis Pipeline Scripts* sets up where the marking should begin and end relative to the onset of a stimulus.

## Merge component rejected files
This script will only be run on subjects that have **'clean.set'** files from **all three runs**. If the script is successfully run, you should see the file named as *'subjectID_merged_clean.set'* in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\wkdir

## Create eventlist, apply binlist, extract epochs, and artifact rejection
This script puts the eventcodes for each stimulus into different bins and extracts the epoched data and finally rejects the components.

If the script is successfully run, you should see the files named as **'subjectID_epoch_ar.set'** and **'AR_summary_subjectID_epoch_ar.txt'** in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\wkdir

The file **'subjectID_epoch_ar.set'** contains the epoched, artifect-rejected, and bin-applied EEG data. 
The **'AR_summary_subjectID_epoch_ar.txt'** is a summary about how much percentage of data is rejected.

## Create ERP  
This rejects all the epochs that have been marked as bad in the artifact rejection and averages the good, remaining trials together to create an averaged ERP on the individual level.

If the script is successfully run, you should see the file named as **'subjectID_erp'** in the corresponding subject folder in Y:\projects\blast\data\eeg\Analysis\erpset folder. 

## Average individual ERPs together into group
This portion of the script loads all the individual ERP files into ERPlab and averages them together to create a group ERP that may then be plotted. 
