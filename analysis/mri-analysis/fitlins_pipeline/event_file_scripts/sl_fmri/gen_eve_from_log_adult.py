#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:49:41 2020

@author: wtang
"""

import re
import os

curr_dir = os.path.realpath("/Volumes/data/projects/blast/data/mri/in_scanner_behavioral/sl_raw_data/adult/log_files")
group_name = 'blast_a'

###first create list of subjects
subject_prefixes = group_name
subjects = []
# def find(name, path):
print(os.listdir(curr_dir))
for root, dirs, files in os.walk(curr_dir):
    # print(files)
    for file in files:
        # print(file)
        for prefix in subject_prefixes:
            # there are some hidden .DS_Storage files in the folder
            if prefix in file and not('sub-' in file) and not ('.DS' in file):
                names = file.split("_")[:3]
                # print(names)
                subjects += [names[0]+'_'+names[1]+'_'+names[2]]

subjects = sorted(list(set(subjects)))
print(subjects)

def get_event(data_path, sl_modality, out_path, stim_key, sl_task):
    log_fname = '%s_' + sl_modality + '_%d.log'
    # print(log_fname)

    keywd = ['word', 'location', stim_key, 'repetition', 'trialnum', 'condition']

    tabdist = 8
    ### For each subject (change this to automatic reading of subject list)
    for subject in subjects:
        # print(subject)
        ### For run 1 to 4
        for run in range(5):
            ### Check if the log file exists for the given subject
            in_fname = data_path + log_fname % (subject, run)
            # print(in_fname)
            if os.path.exists(in_fname):
                ### Create the event file names for the given subject
                out_fname_task = 'sub-%s_' + sl_task + '_run_%d_eve.txt'
                out_fname = out_fname_task % (''.join(subject.split('_')), run)
                # print(out_fname)
                ### Open and write to the event file
                with open(out_path + out_fname, 'w') as fid:
                    fid.write('%-*s\t' % (tabdist, 'onset'))
                    for w in keywd:
                        if w == 'condition':
                            fid.write('%-*s\n' % (tabdist, w))
                        else:
                            fid.write('%-*s\t' % (tabdist, w))
                with open(in_fname, 'r') as fid1:
                    start = 0
                    line = fid1.readline()
                    # print(line)
                    with open(out_path + out_fname, 'a') as fid2:
                        while line:
                            if 'Keypress: 5' in line and start == 0:
                                ### Extract the onset time of the first trigger
                                start = float(line.split()[0])
                            if 'New trial' in line:
                                metadata = eval(re.search(r'\{(.*)\}', line).group(0))
                                ### Extract the onset time of each stimuli compared to the first trigger
                                line = fid1.readline()
                                # print("is this next line???", line)
                                onset = float(line.split()[0]) - start
                                fid2.write('%-*s\t' % (tabdist, str(onset)))
                                for w in keywd:
                                    ### Extract the stimuli info of the trial using dictionary method
                                    if w == 'condition':
                                        fid2.write('%-*s\n' % (tabdist, metadata[w]))
                                    elif w == stim_key:
                                        fid2.write('%-*s\t' % (tabdist, metadata[w].split('.')[0]))
                                    else:
                                        if metadata[w] is None:
                                            fid2.write('%-*s\t' % (tabdist, 'None'))
                                        else:
                                            fid2.write('%-*d\t' % (tabdist, metadata[w]))
                            line = fid1.readline()


data_path = '/Volumes/data/projects/blast/data/mri/in_scanner_behavioral/sl_raw_data/adult/log_files/'
out_path = '/Volumes/data/projects/blast/data/derivatives/event_files/adults_new/'

get_event(data_path, 'visual', out_path, 'image', 'vsl')
get_event(data_path, 'auditory', out_path, 'soundFile', 'asl')
