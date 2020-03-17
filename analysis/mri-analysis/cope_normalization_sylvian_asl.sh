#This script takes into account lack of counterbalancing of the order of random vs structured across SL tasks in runs 1 & 2 vs runs 3 & 4, this scipt creates the new cope and varcope for new speech greater than tone (originally cope 3, transformation is now cope 7) from first level analyses to be used in higher level and group analyses.

# make a log file which outputs any errors. Change the name of the log file everytime you run this.
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>cope_varcope_normalization_sylvian_asl_log.out 2>&1

# specify which participants you want to run through.  If you want to change the participants, change the contents of the subject.list.txt file
flist=$(cat /home/qigroup/Documents/projects/blast/data/derivatives/fsl/firstlevelanalysis/feat_automated_scripts/subject_list_child_asl.txt)
rlist=$(cat /home/qigroup/Documents/projects/blast/data/derivatives/fsl/firstlevelanalysis/feat_automated_scripts/asl.run.list.txt)

# runs a nested loop where for each participant and the runs you specified, it will calculate the standard deviation of the filtered func file, then calculate the new copes and varcopes that are normalized versions of copes 1 and 2, based on methodology recommended by Jeanette Mumford.  We then move all original copes and varcopes up one folder and rename the new copes and varcopes 5-7 as copes and varcopes 1-3. 

for run in $rlist
 do
        for subject in $flist;
                do
                        cd /home/qigroup/Documents/projects/blast/data/derivatives/fsl/firstlevelanalysis/sub-blastc${subject}/${run}.feat
			fslmaths filtered_func_data.nii.gz -Tstd filtered_func_sd.nii.gz;
			mv filtered_func_sd.nii.gz stats/;
			cd stats/;
			fslmaths cope1.nii.gz -div filtered_func_sd.nii.gz cope5.nii.gz;
			fslmaths cope2.nii.gz -div filtered_func_sd.nii.gz cope6.nii.gz;
			fslmaths cope6.nii.gz -sub cope5.nii.gz cope7.nii.gz;
#			fslmaths filtered_func_sd.nii.gz -sqr filtered_func_sd_sqr.nii.gz;
#			fslmaths varcope1.nii.gz -div filtered_func_sd_sqr.nii.gz varcope5.nii.gz;
#			fslmaths varcope2.nii.gz -div filtered_func_sd_sqr.nii.gz varcope6.nii.gz;
#			fslmaths varcope5.nii.gz -add varcope6.nii.gz addedvc5_6.nii.gz;
#			fslmaths addedvc5_6.nii.gz -div 2 avg_vc5_6.nii.gz;
#                       fslmaths varcope5.nii.gz -sub avg_vc5_6.nii.gz vc5_submean.nii.gz;
#                       fslmaths vc5_submean.nii.gz -sqr vc5_sqdiff.nii.gz;
#                       fslmaths varcope6.nii.gz -sub avg_vc5_6.nii.gz vc6_submean.nii.gz;
#                       fslmaths vc6_submean.nii.gz -sqr vc6_sqdiff.nii.gz;
#                       fslmaths vc6_sqdiff.nii.gz -add vc5_sqdiff.nii.gz added_sq_diff.nii.gz;
#                       fslmaths added_sq_diff.nii.gz -div 2 varcope7.nii.gz;
                        mv cope1.nii.gz ..;
                        mv cope2.nii.gz ..;                       
                        mv cope3.nii.gz ..;
                        mv cope5.nii.gz cope1.nii.gz;
                        mv cope6.nii.gz cope2.nii.gz;
                        mv cope7.nii.gz cope3.nii.gz;
#                       mv varcope1.nii.gz ..;
#                       mv varcope2.nii.gz ..;                       
#                       mv varcope3.nii.gz ..;
#                       mv varcope5.nii.gz varcope1.nii.gz;
#                       mv varcope6.nii.gz varcope2.nii.gz;
#                       mv varcope7.nii.gz varcope3.nii.gz;
	done
done

