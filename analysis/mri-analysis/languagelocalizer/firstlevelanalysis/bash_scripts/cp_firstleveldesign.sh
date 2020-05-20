#!/bin/bash

# Only use this script if you are running a participant through feat for the first time.  This is a three-step process combined into one script. 

# make a log file which outputs any errors. Change the name of the log file everytime you run this.
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>cp_firstlevel_log_2.out 2>&1

# specify folder where main feat design folders and participant folders exist
cd /home/qigroup/Documents/projects/blast/data/derivatives/fsl/firstlevelanalysis/

# specify which participants you want to run through.  If you want to change the participants, change the contents of the subject.list.txt file
flist=$(cat /home/qigroup/Documents/projects/blast/data/derivatives/fsl/firstlevelanalysis/bash_scripts/langloc.order1.adult.subjlist.txt)

for subject in $flist;
	do
			cp design_files/langloc_order1_design.fsf sub-blasta${subject}/;
			sed -i 's/001/'${subject}'/g' sub-blasta${subject}/langloc_order1_design.fsf
done
