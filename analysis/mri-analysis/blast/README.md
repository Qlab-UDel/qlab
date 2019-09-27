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

## Pre-processing data with fMRI prep 

Before running the following steps, ensure that the following has happened:
1. Heudiconv has been run so that data is in BIDS format
2. The fieldmap inclusion script has been run to ensure 'add intended for' is listed accurately in .json files.

### Adult Pre-Processing of fMRI data 
Running fMRIprep Pre-Processing (change SUBJECTID):
```
docker run -ti --rm -v /home/qigroup/Documents/projects/blast/data/bids:/data:ro -v
/home/qigroup/Documents/projects/blast/data/derivatives:/out -v
/home/qigroup/Documents/projects/blast/license.txt:/opt/freesurfer/license.txt
poldracklab/fmriprep:latest /data /out participant --participant_label SUBJECTID
```

### Child Pre-Processing of fMRI data
Running fMRIprep Pre-Processing for Structural data ONLY (change SUBJECTID):
```
docker run -ti --rm -v /home/qigroup/Documents/projects/blast/data/bids:/data:ro -v /home/qigroup/Documents/projects/blast/data/derivatives:/out -v /home/qigroup/Documents/projects/blast/license.txt:/opt/freesurfer/license.txt 
poldracklab/fmriprep:1.3.1 /data /out participant --participant_label SUBJECTID --anat-only
```
Using Qoala-T, evaluate quality of structural data and manually edit if necessary.

Running fMRIprep Pre-Processing (change SUBJECTID):
```
docker run -ti --rm -v /home/qigroup/Documents/projects/blast/data/bids:/data:ro -v /home/qigroup/Documents/projects/blast/data/derivatives:/out -v /home/qigroup/Documents/projects/blast/license.txt:/opt/freesurfer/license.txt 
poldracklab/fmriprep:1.3.1 /data /out participant --participant_label SUBJECTID
```