% This script is to extract the minimum activation of the top 10%
% activation in ASL random vs. rest contrasts so that subject-specific
% parcels/ voxels can be extracted from the resampled conn_tool_box dorsal
% attention network
function run_froi_resp_mag(opts)

%% Measure response magnitudes in frois

opts.PROJECT_DIR = '/Volumes/data/projects/blast/data/mri/imaging/scott_gcss_lpsa/';
opts.PARCEL_DIR = [opts.PROJECT_DIR 'data/dorsal_attention_parcel/conn_resampled_parcel/'];
% 
opts.SUBJ_NAME_LIST = [opts.PROJECT_DIR 'data/asl_attention/langloc_child.txt'];
opts.SUBJ_DEFINE_DATA_DIR = [opts.PROJECT_DIR 'data/asl_attention/child/'];
% 
opts.RESULTS_DIR = [opts.PROJECT_DIR 'data/asl_attention/'];
if ~exist(opts.RESULTS_DIR,'dir')
    mkdir(opts.RESULTS_DIR)
end
% 
 % Conditions to measure
 % Please change the subject ID ranges here
opts.SUBJ_IDS = 1:117;
opts.VOL_VALS = 1

%% Load parcels
ck = dir(opts.PARCEL_DIR)
ck(1,:) = []
ck(1,:) = []
for i = 1:length(opts.VOL_VALS)
    PARCEL_NUM_STR{i} =[ck(i).name];
    match = ['.nii', '.gz'];
    PARCEL_NUM_STR{i} = erase(PARCEL_NUM_STR{i},match)
end
disp(PARCEL_NUM_STR)
disp(PARCEL_NUM_STR{1})


for i = 1:length(opts.VOL_VALS);
    parcel = MRIread([opts.PARCEL_DIR ck(i).name],0);
    PARCEL_VOL = parcel.vol;
    PARCEL_VOLS{i} = PARCEL_VOL;
end



%% For each parcel...

n_subjs = length(opts.SUBJ_IDS);
n_parcels = length(opts.VOL_VALS);

% For each subject
for i = 1:n_subjs

    % Load stat map for defining frois
    DEFINE_VOL = MRIread([opts.SUBJ_DEFINE_DATA_DIR num2str(opts.SUBJ_IDS(i)) '_stat-z_statmap.nii.gz'],0);
    % Load cope(s) for measuring response
    % For each parcel
    for j = 1:n_parcels;
        temp_mask = PARCEL_VOLS{1,j};
        mean_in_roi(i,j) = MeanCopeFROI(temp_mask,DEFINE_VOL.vol);
        
    end

end


%% Setup results structure
ID = fileread(opts.SUBJ_NAME_LIST);
SUBJ_ID_STR = strsplit(ID)
results = array2table(mean_in_roi,'VariableNames',PARCEL_NUM_STR,'RowNames',SUBJ_ID_STR);
disp(results)

writetable(results, '/Volumes/data/projects/blast/data/mri/imaging/scott_gcss_lpsa/data/asl_attention/child_dan_minimum_top_10_data_03_17.csv', 'WriteRowNames', true)

end

function mean_in_roi = MeanCopeFROI(parcel_mask_vol,defining_vol)

% Mask defining volume with parcel
% Parcel mask should just be ones and zeros
voxel_idxs_in_parcel = find(parcel_mask_vol);

% Find top 10% of voxels
defining_data_voxel_values = defining_vol(voxel_idxs_in_parcel);
[~,sorted_voxel_idxs] = sort(defining_data_voxel_values,1,'descend');

n_voxels = length(voxel_idxs_in_parcel);
tenpct_n_voxels = round(n_voxels*0.10);

tenpct_sorted_voxel_idxs = sorted_voxel_idxs(1:tenpct_n_voxels);

get_min = defining_data_voxel_values(tenpct_sorted_voxel_idxs)
mean_in_roi = min(get_min)
end