import os

def create_key(template, outtype=('nii.gz','dicom'), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return (template, outtype, annotation_classes)


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where
    allowed template fields - follow python string module:
    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    t1 = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    t2 = create_key('sub-{subject}/anat/sub-{subject}_T2w')
    rest = create_key('sub-{subject}/func/sub-{subject}_task-rest_run-{item:02d}_bold')
    langloc = create_key('sub-{subject}/func/sub-{subject}_task-langloc_run-{item:02d}_bold')
    vsl = create_key('sub-{subject}/func/sub-{subject}_task-vsl_run-{item:02d}_bold')
    asl = create_key('sub-{subject}/func/sub-{subject}_task-asl_run-{item:02d}_bold')
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_run-{item:02d}_dwi')

    phasediff_rest = create_key('sub-{subject}/fmap/sub-{subject}_acq-rest_run-{item:02d}_phasediff')
    mag_rest = create_key('sub-{subject}/fmap/sub-{subject}_acq-rest_run-{item:02d}_magnitude')
    fmap_dwi = create_key('sub-{subject}/fmap/sub-{subject}_acq-dwi_dir-{dir}_run-{item:02d}_epi')
    phasediff_langloc = create_key('sub-{subject}/fmap/sub-{subject}_acq-langloc_run-{item:02d}_phasediff')
    mag_langloc = create_key('sub-{subject}/fmap/sub-{subject}_acq-langloc_run-{item:02d}_magnitude')
    phasediff_sl = create_key('sub-{subject}/fmap/sub-{subject}_acq-sl_run-{item:02d}_phasediff')
    mag_sl = create_key('sub-{subject}/fmap/sub-{subject}_acq-sl_run-{item:02d}_magnitude')

    info = {t1:[], t2:[], rest:[], langloc:[], vsl:[], asl:[], dwi:[], phasediff_rest:[], mag_rest:[],phasediff_langloc:[],mag_langloc:[],fmap_dwi:[], phasediff_sl:[], mag_sl:[]}

    for idx, s in enumerate(seqinfo):
        if ((s.dim3 == 160) or (s.dim3 == 176)) and (s.dim4 == 1) and ('T1' in s.protocol_name):
            info[t1] = [s.series_id]
        if (s.dim3 == 176) and ('T2w' in s.protocol_name):
            info[t2] = [s.series_id]
        if (s.dim4 >= 99) and ('ep2d_diff_sms_abcd' in s.protocol_name):
            info[dwi].append({'item': s.series_id})
        if (s.dim4 == 1) and ('ep2d_diff_sms_abcd_ap' in s.protocol_name):
            info[fmap_dwi].append({'item': s.series_id, 'dir': 'AP'})
        if (s.dim4 == 1) and ('ep2d_diff_sms_abcd_pa' in s.protocol_name):
            info[fmap_dwi].append({'item': s.series_id, 'dir': 'PA'})
        if (s.dim4 == 383) and ('ep2d_bold_sms_abcd' in s.protocol_name):
            info[rest].append({'item': s.series_id})
        if (s.dim4 == 1) and (s.dim3 == 65) and ('gre_field_mapping_2.4mm' in s.protocol_name):
            info[phasediff_rest].append({'item': s.series_id})
        if (s.dim4 == 1) and (s.dim3 == 130) and ('gre_field_mapping_2.4mm' in s.protocol_name):
            info[mag_rest].append({'item': s.series_id})
        if (s.dim4 == 450) and ('langLoc' in s.protocol_name):
            info[langloc].append({'item': s.series_id})
        if (s.dim4 == 1) and (s.dim3 == 45) and ('taskbold_field_mapping_3mm' in s.protocol_name):
            info[phasediff_langloc].append({'item': s.series_id})
        if (s.dim4 == 1) and (s.dim3 == 90) and ('taskbold_field_mapping_3mm' in s.protocol_name):
            info[mag_langloc].append({'item': s.series_id})
        if (s.dim4 == 465) and (not s.is_motion_corrected) and ('vsl' in s.protocol_name):
            info[vsl].append({'item': s.series_id})
        if (s.dim4 == 480) and (not s.is_motion_corrected) and ('asl' in s.protocol_name):
            info[asl].append({'item': s.series_id})
        if (s.dim4 == 1) and (s.dim3 == 55) and ('gre_field_mapping_2.5mm' in s.protocol_name):
            info[phasediff_sl].append({'item': s.series_id})
        if (s.dim4 == 1) and (s.dim3 == 110) and ('gre_field_mapping_2.5mm' in s.protocol_name):
            info[mag_sl].append({'item': s.series_id})
    return info
