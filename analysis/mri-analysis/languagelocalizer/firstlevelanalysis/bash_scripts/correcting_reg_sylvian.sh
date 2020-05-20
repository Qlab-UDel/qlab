#!/bin/bash
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>log_correcting_reg_2.out 2>&1

cd /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis

rlist=$(cat /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis/bash_scripts/langloc.run.list.txt)
flist=$(cat /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis/bash_scripts/langloc.all.adult.subjlist.txt)

for run in $rlist
 do
	for subject in $flist;
		do
			cp correcting_reg sub-blasta${subject}/sub-blasta${subject}_task-langloc_run-${run}_space-MNI152NLin2009cAsym_desc-preproc_bold_langloc.feat;
			cd sub-blasta${subject}_task-langloc_run-${run}_space-MNI152NLin2009cAsym_desc-preproc_bold_langloc.feat;
			sh correcting_reg;
			cd /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis;
	done
done
