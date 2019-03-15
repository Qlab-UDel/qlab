# **Extracting gray matter measures**
This tutorial will show you how to extract your gray matter volume (GMV) and cortical thickness (CT) measures from your freesurfer reconstructed data.  This step comes after the final reconstruction step (using the recon-all -autorecon-all command). Therefore, in this tutorial whenever I refer to reconstructed data, I am referring to the output files that Freesurfer creates and fills in during the recon-all process.   
## **Overview**
Freesurfer provides a very simple and organized method for extracting gray matter measures after reconstruction.  The output is a text file which you can open in Excel (make sure you specify that it is tab delimited in excel to open the file).  These outputs will include each subject’s CT or GMV (based on which scripts below you run) for each region in the desikan killiany atlas. These outputs are particularly useful when you want to run region of interest (ROI) based analyses.
# **To Start**
## **Set up your subject's directory**
Setting up your subject's directory informs Freesurfer where you want your created files to go.  Make sure you go to the directory (main folder) where all the participant’s reconstructed data are (so you should see all your subjects' folders here, make sure you do not go into just one subject's folder). Then, you should designate where you want the output files to go (usually I just put them in this same central location as where the reconstructed data are, since freesurfer tends to work better when I do this) using the export command.
````
cd /home/qigroup/Documents/projects/<path_where_reconstructed_data_are>
export SUBJECTS_DIR=/home/qigroup/Documents/projects/<path_where_you_want_the_output_to_go>
````
To double check that you have set the correct subject’s directory you can run the command:
````
echo $SUBJECTS_DIR
````
You should then see the path you set: /home/qigroup/Documents/projects/<path_where_you_want_the_output_to_go>
## **Extracting cortical surface data**
For CT or GMV measures along the parcellated surface (gyri and sulci of cerebral cortex), you can run the following commands, where you need to include each Freesurfer’s subject IDs, with 1 space between each subject. Each command only gets data from one hemisphere (right hemisphere: rh or left hemisphere: lh) and one measure (thickness or volume) at a time.
### **Extracting cortical thickness data**
Here are the commands you would run for extracting the cortical thickness for the right hemisphere and left hemisphere:
````
aparcstats2table --subjects <subject_1_ID>  <subject_2_ID>  --hemi rh --meas thickness --tablefile <filename>.txt
aparcstats2table --subjects <subject_1_ID>  <subject_2_ID>  --hemi lh --meas thickness --tablefile <filename>.txt
````
### **Extracting gray matter volume data**
Here are the commands you would run for extracting the gray matter volume for the right hemisphere and left hemisphere:
````
aparcstats2table --subjects <subject_1_ID>  <subject_2_ID>  --hemi rh --meas volume --tablefile <filename>.txt
aparcstats2table --subjects <subject_1_ID>  <subject_2_ID>  --hemi lh --meas volume --tablefile <filename>.txt
````
## **Extracting subcortical and total intracranial volume data**
For GMV of subcortical structures, and to get estimated intracranial volume (eTIV), you only need to run one script since it includes both right and left hemisphere data.  The estimated intracranial volume is the estimated total volume for each person's brain.  You should always include particiants' eTIV measure as a control variable so that you control for the fact that people with bigger brains may have larger volumes or thicker cortices in regions of interest as compared to people with smaller brains.  
Here is the command for extracting the gray matter volume in subcortical regions across both hemispheres as well as the eTIV:
````
asegstats2table --subjects  <subject_1_ID>  <subject_2_ID> --meas volume --tablefile <filename>.txt
````

