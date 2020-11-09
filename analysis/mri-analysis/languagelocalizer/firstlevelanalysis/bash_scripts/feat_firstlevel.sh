#!/bin/bash
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>Feat_first_level_mac_log1.out 2>&1

cd /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis

flist=$(cat /Users/qigroup/mnt/sylvian/blast/data/derivatives/fsl/firstlevelanalysis/bash_scripts/langloc.order1.adult.subjlist.txt)

for subject in $flist;
	do
		Feat sub-blasta${subject}/langloc_order1_design.fsf;
done
