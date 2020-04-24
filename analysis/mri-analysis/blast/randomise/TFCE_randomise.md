# How to prepare files for TFCE Randomise and execute

## Copy files from higher level analysis folder:
- Identify cope images of interest at the higher level
- The below example copies files from the ASL Tone condition (cope 1.feat) that are structured>random (cope1.nii.gz). It copies this data to a randomise input files folder. 
```
cp  /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/higherlevelanalysis/*/ASL_norm.gfeat/cope1.feat/stats/cope1.nii.gz /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/grouplevelanalysis/randomise_input_files/adult_tone/stdvrand_cope1/
```
## Merge files together within this folder:
- Data input into Randomise must be a concatenated 4D image
- The below example concatenates across time (-t) for all the files in the folder you created in the above step.
```
fslmerge -t tone_stdvrand_merg *_cope1.nii.gz
```
## Confirm that the merge worked
- Check that there are the correct dimensions (your final dimension should match your N)
```
fslinfo tone_stdvrand_merg.nii.gz
```
## Randomise
- To run Randomise, you will need three files: a mask.nii.gz file, a design.con file, a design.mat file. Examples of these can be found in the folder **Randomise**.
- The standard code for randomise is as follows:
```
randomise -i <4D_input_data> -o <output_rootname> -d design.mat -t design.con -m <mask_image> -n 500 -D -T
```
- Continuing the above example, enter the following code:
```
cd /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/grouplevelanalysis/randomise_input_files/adult_speech/
randomise -i stdvrand_cope2/speech_stdvrand_merg.nii.gz -o /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/grouplevelanalysis/randomise_output_files/speech_stdvrand_TFCE -d design.mat -t design.con -m mask.nii.gz -n 500 -D -T
```
