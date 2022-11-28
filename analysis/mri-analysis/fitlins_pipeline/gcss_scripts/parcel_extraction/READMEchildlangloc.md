# Group-Constrained Subject-Specific (GCSS) Analysis: Make Parcels, Child Version, Language Localizer

Greetings! As with the more general version, this code is modified from Dr. Terri Scott (https://github.com/tlscott/make_parcels), and can be used to generate a set of parcels from a dataset of individual subject fMRI volumes. Please see the following papers for more on the method:

<li>Fedorenko, E., Hsieh, P.-J., Nieto-Castañon, A., Whitfield-Gabrieli, S. & Kanwisher, N. (2010). A new method for fMRI investigations of language: Defining ROIs functionally in individual subjects. Journal of Neurophysiology, 104(2), 1177-94. DOI: 10.1152/jn.00032.2010.<br> https://pubmed.ncbi.nlm.nih.gov/20410363/</li> 
<li>Julian, J., Fedorenko, E., Webster, J. & Kanwisher, N. (2012). An algorithmic method for functionally defining regions of interest in the ventral visual pathway. Neuroimage, 60(4), 2357-2364. DOI: 10.1016/j.neuroimage.2012.02.055.<br> https://pubmed.ncbi.nlm.nih.gov/22398396/</li>
<br>
And her paper: 
<li>Scott, T.L. and Perrachione, T.K. (2019). Common cortical architectures for phonological working memory identified in individual brains. NeuroImage, 202, 116096. DOI: 10.1016/j.neuroimage.2019.116096.<br> https://pubmed.ncbi.nlm.nih.gov/31415882/</li>

Her code is based on the watershed algorithm included in this SPM toolbox developed by Alfonso Nieto-Castañon: https://www.nitrc.org/projects/spm_ss


This code requires Freesurfer and Matlab, and if you want to make pretty pictures, python + a whole bunch of packages (numpy, nibabel, matplotlib, nilearn...). In order to generate a report with the approximate locations of parcels, she use atlases from FSL. Found here -> https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlases; license here -> https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Licence


To Run:
0) Prior to running, you need to have all the language localizer higher level analysis done. Zstat files should be retrived from subject_flolder > language localizer gfeat file > cope 1 > stats > zstst.nii.gz file for the participant. This file should be copied over for each participant into either the child_data > lang_loc_zstats > TD folder for TD children or the child_data > Lang_loc_zstats > ASD folder for ASD children. They should be renamed as 'x_zstat.nii.gz', with x being the relative number of the participant to the rest of the group - for instance, if you have 18 TD children with higher level language localizer data, you would rename the ztstat for the loweest number of these '1_zstat.nii.gz', then the second lowest '2_zstat.gz', etc up to the highest at '18_zstat.gz.' This would be done seperately for the TD and ASD goup, so each would have a 1_ztstat.nii.gz', a '2_ztat.nii.gz' etc.
1) open make_my_parcels_child.m. Set PROJECT_DIR to the path where this code and all your subfolders you'll need to reference are located. Set the range of i to the number of zstat files you have for your given group - TD or ASD - and set the folder for the FILENAMES in the for loop to the folder for either TD or ASD depending on who you are running. Ensure that matlab has the file path for Applications/freesurfer/matlab loaded in the paths directory. Set the threshold you want based on the desired p value:
p = 0.01 : z = 2.326348
p = 0.001 : z = 3.090232
p = 0.0001 : z = 3.719015
p = 0.00001 : z = 4.264895
Set the percent of subjects needed for significance, and the peak spacing (Amanda has most recently used 6, which this current anaysis matches). Ensure that EXPERIMENT has the desired name for the output files, and that the PATH_TO_RESULTS_DIR aprpoprately goes to either the TD or ASD folder for the ouputs (child_data > langloc_resampled_parcels). This script will then run generate_parcels on the inputs. The output files will be in a folder in the TD or ASD filder entitled _day-Month-year using the current date the program was run to title it.
Note: If you get an error regarding not having a filepath correctly set, fix that by loading the path via get path.
Note: if you get a gunzip error, it is likely either an issue with the file path to the zfiles, the names of the z files themselves being incorrect, or the range of file names being larger than the amount of zstat files you have. Please chedk each of these.
2) To get relative percentage outputs (percent of subjects for whom a given voxel was signifcant) rather than absolute value outputs (number of subjects for whom the given voxel was significant), open terminal, cd into the folder containing the output files for the ASD or TD group you want to run this on, and run:
fslmaths image_to_run.nii.gz -div number_of_subjects_in_group output_image_name.nii
For instance, for the TD group with 18 subjects, if you want teh relative percentage for the thresholded smootehd image, this may look like: 
fslmaths LangLoc_TD_resampled_zthresh3.090232_4voxSpacing_probability_map_thresh2subjs_smoothed.nii.gz -div 18 LangLoc_TD_resampled_zthresh3.090232_4voxSpacing_probability_map_thresh2subjs_smoothed_percent.nii
3) Open Plotting_heterogeneity_parcellations_child_finalized.ipynb. This is best done via Anaconda and the jupyter notebook within that. Ensure for each chdir command that it goes to teh folder appropriate to that group, both in terms of TD vs ASD, and the subfolder with the date of the anaysis you want to run from.  Ensure for each plot_glass_brain that the file you are attempting to access to plot is listed first and that the output_file has the desired output file nanme and format. Prior to running the final analysis, run the boxes for both teh TD and ASD group that do not have output_files (the ones beginning with teh instructions ## Use this to check) to see between the two groups what the highest vmax value - the top the number of teh scale bar to teh side - is. Decide based on that what you wish your vmax to be. For both of the make and export boxes, be sure to set the vmax to that value before running. 



Terri also included a python script, plot_parcels.py, that will generate a pdf that you can see in the images directory.
