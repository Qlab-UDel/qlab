# General Guideline for MRI file processing
* All the dicoms files should be saved at `/Users/qigroup/Documents/projects/{projectname}/dicoms/`
* The EP2D_DIFF_SMS_ABCD_TENSOR_* series are not currently convertable by heudiconv. Please mv this folder to ./tensor/{subj}/.
* All the nifti files should be saved at `/Users/qigroup/Documents/projects/{projectname}/niftis/`
* Backup all the dicoms to our lab server: `/data/projects/{projectname}`

## To convert dicoms to BIDS formatted nifti
### Make sure docker is running on the imac
### On the terminal, type:
```
cd /Users/qigroup/Documents/projects/{projectname}/
docker pull nipy/heudiconv
docker run --rm -it --entrypoint=bash -v $(pwd):/data nipy/heudiconv:latest
```
Now you will be inside of the container. Type:
```
cd /data
mkdir niftis
source activate neuro
```
The first step is to run a dry pass (no conversion), which will stack and group the dicoms into series.
```
heudiconv -d /data/dicoms/{subject}/*/*/*.IMA -s subjectID -f convertall -c none -o /data/niftis
```
Within /output/.heudiconv/subjectID/info, you will find a dicominfo.tsv. We will convert this file to specify bids format.

### create the heuristic file at /data/projectname_heuristic.py
example here: <http://nipy.org/heudiconv/#22>

### run the conversion
```
rm -r -f /data/niftis/*
heudiconv -d /data/dicoms/{subject}/*/*/*.IMA -s subjectID -f /data/projectname_heuristic.py -c dcm2niix -b -o /data/niftis
```

