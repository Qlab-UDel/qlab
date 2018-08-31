# qlabfmripipe
The following comes from the fmriprep github installation page. 
The goal of this repository is to specify pre-processing, first-level, and second-level analyses using BIDS format. 
The paths specified in this repository are specific to the Q-Lab at the University of Delaware.

fMRIprep Installation Process (https://fmriprep.readthedocs.io/en/latest/installation.html):
  1. In the terminal you need to setup the environment to install fmriprep
  ```
    $ pip install --user --upgrade fmriprep-docker
  ```
  2. If Freesurfer is located in your Applications folder, be sure to set it up in Docker:
     - Click on Docker
     - Select Preferences
     - Select File Sharing
     - Add your Applications folder
    
Running fMRIprep Pre-Processing (change SUBJECTID):
```
fmriprep-docker /Users/qigroup/Documents/project/blast/bids /Users/qigroup/Documents/project/blast/bids participant --participant_label SUBJECTID --no-freesurfer --fs-license-file /Applications/freesurfer/license.txt
```
