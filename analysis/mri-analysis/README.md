# General Guideline for MRI file processing

## All the analysis are currently conducted on the sylvian server.
* All the dicoms files should be saved at `/home/nas/projects/{projectname}/dicoms/`
* All the nifti files should be saved at `/home/qigroup/Documents/projects/{projectname}/bids/` which is regularly backed up to our nas server.

## Transfer dicoms to be converted to nifti, to correct folder:
```
rsync -chavzP --stats /home/nas/projects/{projectname}/dicoms/SUBJECTID /home/qigroup/Documents/projects/blast/data/mri/imaging/dicoms
```

## To convert dicoms to BIDS formatted nifti
### On the terminal, type:
```
cd /home/qigroup/Documents/projects/{projectname}/
docker run --rm -it --entrypoint=bash -v $(pwd):/data nipy/heudiconv:latest
```
Now you will be inside of the container. Type:
```
cd /data
```
### run the conversion
## anything in all caps must be edited
```
heudiconv -d /data/data/mri/imaging/dicoms/{subject}/*/*/*.IMA -s SUBJECTID -f /data/conversion/PROJECTNAME_heuristics.py -c dcm2niix -b -o /data/data/bids
```
If this is the first time you are running heudiconv, the first step is to run a dry pass (no conversion), which will stack and group the dicoms into series.
```
heudiconv -d /data/dicoms/{subject}/*/*/*.IMA -s subjectID -f convertall -c none -o /data/bids
```
Within /output/.heudiconv/subjectID/info, you will find a dicominfo.tsv. We will convert this file to specify bids format.

### create the heuristic file at /data/projectname_heuristic.py
example here: <http://nipy.org/heudiconv/#22>
for most updated bids specification: <http://bids.neuroimaging.io/bids_spec.pdf>

## Edit Freesurfer outputs
### Use the freesurfer editing GUI
`python /home/qigroup/Documents/projects/blast/scripts/edit_freesurfer_surface.py`
### For more documentation and tips, see the lab wiki: <https://github.com/Qlab-UDel/qlab/wiki/FreeSurfer-Overview> and the official wiki: <http://ftp.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki>

###To validate BIDS files, see the BIDS validator: <http://incf.github.io/bids-validator/>
