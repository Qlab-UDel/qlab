function indiv_langloc_sl(opts, group, prefix, part_id)

%% Measure response magnitudes in frois
opts.CURRENT_ID = [prefix part_id];
%% To troubleshoot, uncomment the line below:
%% opts.CURRENT_ID = 'blast_a_044';
opts.PROJECT_DIR = '/Volumes/data/projects/blast/data/mri/imaging/scott_gcss_lpsa/';
opts.PARCEL_DIR = [opts.PROJECT_DIR 'data/indiv_langloc_output/bin_resampled_mask/' group '/' part_id '/'];
%% To troubleshoot, uncomment the line below:
%% opts.PARCEL_DIR = [opts.PROJECT_DIR 'data/indiv_langloc_output/bin_resampled_mask/adult/044/'];
opts.SUBJ_DEFINE_DATA_DIR = [opts.PROJECT_DIR 'data/indiv_langloc_output/asl/' group '/' part_id '/'];
%% To troubleshoot, uncomment the line below:
%% opts.SUBJ_DEFINE_DATA_DIR = [opts.PROJECT_DIR 'data/indiv_langloc_output/asl/adult/044/'];
opts.RESULTS_DIR = [opts.PROJECT_DIR 'data/indiv_langloc_output/asl/' group '/results/'];
%% To troubleshoot, uncomment the line below:
%% opts.RESULTS_DIR = [opts.PROJECT_DIR 'data/indiv_langloc_output/asl/adult/results/'];
disp(opts)

if ~exist(opts.RESULTS_DIR,'dir')
    mkdir(opts.RESULTS_DIR)
end
% 
 % Conditions to measure
%opts.COND = {'001'};
% List the z-maps of task of interest for each participant
FILE_LIST = dir([opts.SUBJ_DEFINE_DATA_DIR '*.nii.gz']);
opts.SUBJ_IDS = 1:length(FILE_LIST);

% List the parcels of interest for each participant
PARCEL_LIST = dir([opts.PARCEL_DIR '*.nii.gz']);
PARCEL_N = length(PARCEL_LIST)
opts.VOL_VALS = 1:PARCEL_N

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

n_subjs = length(FILE_LIST);
n_parcels = length(opts.VOL_VALS);

% For each subject
for i = 1:n_subjs
    ID_LIST(i).name = FILE_LIST(i).name 
    
    % Load stat map for defining frois
    DEFINE_VOL = MRIread([opts.SUBJ_DEFINE_DATA_DIR FILE_LIST(i).name],0);
    % For each parcel
    for j = 1:n_parcels;
        temp_mask = PARCEL_VOLS{1,j};
        mean_in_roi(i,j) = MeanCopeFROI(temp_mask,DEFINE_VOL.vol);
        
    end

end


%% Setup results structure
% ID = fileread(opts.SUBJ_NAME_LIST);
% SUBJ_ID_STR = strsplit(ID)
ID = struct2cell(ID_LIST) 
ID = transpose(squeeze(ID))
results = array2table(mean_in_roi,'VariableNames',PARCEL_NUM_STR,'RowNames',ID);
disp(results)
writetable(results, [opts.RESULTS_DIR opts.CURRENT_ID '.csv'], 'WriteRowNames', true)


end

function mean_in_roi = MeanCopeFROI(parcel_mask_vol,defining_vol)

% Mask defining volume with parcel
% Parcel mask should just be ones and zeros
voxel_idxs_in_parcel = find(parcel_mask_vol);

defining_data_voxel_values = defining_vol(voxel_idxs_in_parcel);

mean_in_roi = mean(defining_data_voxel_values)
end