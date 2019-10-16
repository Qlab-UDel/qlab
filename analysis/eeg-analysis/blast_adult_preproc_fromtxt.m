%Load subject excel file
% establish working directory 
blast_dir_PC;

highpass=0.1; %set high pass filter
lowpass=80; %set low pass filter

[d,s,r]=xlsread('adult_subjects.xlsx');
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
run= '_run_1'

for k=47:length(s);

datasetname =[s{k} run];

EEG = pop_loadxdf([rawdir s{k} filesep datasetname '.xdf'], 'streamtype', 'EEG', 'exclude_markerstreams', {});
[ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );

EEG = pop_eegfiltnew(EEG, highpass,lowpass,16500,0,[],1);
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl'],'gui','off'); 
EEG = eeg_checkset( EEG );

EEG=pop_chanedit(EEG, 'load',[],'lookup','C:\Users\Qlab\Documents\MATLAB\toolbox\eeglab14_1_1b\plugins\dipfit2.3\standard_BESA\standard-10-5-cap385.elp');
EEG = eeg_checkset( EEG );

EEG = pop_reref( EEG, [13 16] );
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl_rr'],'gui','off'); 
EEG = eeg_checkset( EEG );

EEG = pop_saveset( EEG, [workdir s{k} filesep datasetname '_fl_rr']);
end

%% Run ICA
for k=37:length(s);

    datasetname =[s{k} run];
    
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    EEG = pop_loadset('filename',[datasetname '_fl_rr.set'],'filepath',[workdir s{k}]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = pop_runica(EEG, 'extended',1,'interupt','on');
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl_rr_ica'],'gui','off');
    EEG = pop_saveset( EEG, [workdir s{k} filesep datasetname '_ica']);
end

%Manual rejection of components occurs in between these steps
%Save manually rejected file as: **'subject_run#_clean.set'**

%% Merge datasets from run 1-3
% establish subject list

for k=35:length(s);
    clear ALLEEG
    datasetname =[s{k} run];

%% Epoching Steps
% Step 3: create eventlist, apply binlist, extract epochs, and artifact rejection
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
EEG = pop_loadset('filename',[s{k} '_run_1_clean.set'],'filepath',[workdir s{k} filesep]);
[ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
EEG = pop_loadset('filename',[s{k} '_run_2_clean.set'],'filepath',[workdir s{k} filesep]);
[ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
EEG = pop_loadset('filename',[s{k} '_run_3_clean.set'],'filepath',[workdir s{k} filesep]);
[ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
EEG = eeg_checkset( EEG );
EEG = pop_mergeset( ALLEEG, [1:3], 0);
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, 3,'gui','off'); 
EEG = pop_saveset( EEG, [workdir s{k} filesep s{k} '_merged_clean']);
end

%% set up file and folders
% establish working directory 
blast_dir_PC;

epoch_baseline = -100.0 %epoch baseline
epoch_end = 600.0 %epoch offset

[d,s,r]=xlsread('adult_subjects.xlsx');
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
%run= '_run_3'

% establish subject list
for k=40:length(s); %edit for subject of interest (can run multiple at once)
    
    % get subject info, same name as subjects.m (function)
    %datasetname =[s{k} run];
    
% Create eventlist, apply binlist, extract epochs, and artifact rejection
    EEG = pop_loadset('filename',[s{k} '_merged_clean.set'],'filepath',[workdir s{k}]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG  = pop_creabasiceventlist( EEG , 'AlphanumericCleaning', 'on', 'BoundaryNumeric', { -99 }, 'BoundaryString', { 'boundary' }, 'Eventlist', [txtdir s{k} filesep 'eventlist.txt'] ); 
    EEG = eeg_checkset( EEG );
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'gui','off'); 
    EEG  = pop_binlister( EEG , 'BDF', [txtdir 'blast_current_binlist.txt'], 'ExportEL', [txtdir s{k} filesep 'blast_current_binlist.txt'],'ImportEL', [txtdir s{k} filesep 'eventlist.txt'], 'IndexEL',  1, 'SendEL2', 'EEG&Text', 'Voutput', 'EEG' );
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = pop_epochbin( EEG , [epoch_baseline  epoch_end],  'pre'); 
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG  = pop_artmwppth( EEG , 'Channel',  1:22, 'Flag',  1, 'Threshold',  100, 'Twindow', [epoch_baseline epoch_end], 'Windowsize',  200, 'Windowstep',  100 ); 
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET ,'savenew',[workdir s{k} filesep s{k} '_epoch_ar.set'],'gui','off'); 
    EEG = pop_summary_AR_eeg_detection(EEG, [workdir s{k} filesep 'AR_summary_' s{k} '_epoch_ar.txt']); 
    [EEG, MPD] = getardetection(EEG, 1);
    EEG = pop_saveset( EEG, 'filename','erp_binlist.set','filepath',[erpdir s{k}]);
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
end

%% Average individual trials into ERP
% establish working directory 
blast_dir_PC;

[d,s,r]=xlsread('adult_subjects.xlsx');
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;

% establish subject list
for k=2:length(s); %edit for subject of interest (can run multiple at once)
    
% Create eventlist, apply binlist, extract epochs, and artifact rejection
    EEG = pop_loadset('filename','erp_binlist.set','filepath',[erpdir s{k}]);
    ERP = pop_averager(ALLEEG , 'Criterion', 'good', 'DSindex',1, 'ExcludeBoundary', 'on', 'SEM', 'on' );
    ERP = pop_savemyerp(ERP, 'erpname',...
 'blast_erp_3runs', 'filename', 'blast_erp_3runs.erp', 'filepath', [erpdir s{k}], 'Warning',...
 'on');
    clear ALLEEG
end

%% Edit ERP for each individual
% establish working directory 
blast_dir_PC;

[d,s,r]=xlsread('adult_subjects.xlsx');
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;

% establish subject list
for k=1:length(s); %edit for subject of interest (can run multiple at once)
    [ERP ALLERP] = pop_loaderp( 'filename', 'blast_erp_3runs.erp', 'filepath', [erpdir s{k}]);
    ERP = pop_binoperator( ERP, {  'b28 = b4-b1 label MMN voice deviant low freq',  'b29 = b5-b2 label MMN voice deviant high freq',...
      'b30 = b6-b3 label MMN voice deviant equal freq',  'b31 = b7-b1 label MMN syllable deviant high freq',  'b32 = b8-b2 label MMN syllable devaint low freq',...
      'b33 = b9-b3 label MMN syllable deviant equal freq','b34 = b27-b26 label all deviants minus all standards'});
      %Run channel operation to compute average over significant ROIs
   % ERP = pop_erpchanoperator( ERP, { 'ch23 = (ch10+ch11)/2 label = standard v dev early', 'ch24 = (ch1+ch2+ch4+ch5+ch6+ch9+ch10+ch11)/8 label = standard v dev late'} ,...
    % 'ErrorMsg', 'popup', 'KeepLocations',  0, 'Warning', 'on' );
    %Filter ERP at low-pass of 30 Hz
    ERP = pop_filterp( ERP,  1:22 , 'Cutoff',  30, 'Design', 'butter', 'Filter', 'lowpass', 'Order',  2 );
    ERP = pop_savemyerp(ERP, 'erpname', s{k}, 'filename', [s{k} '_3runs_filt_chanop.erp'], 'filepath', [erpdir 'blast_erp_filt_chanop' filesep]);                                                                                                                                                                                                                     
end

%% Average individual ERPs into group ERP
ERP = pop_gaverager( [txtdir 'load_erpset_blast_adults.txt'] , 'ExcludeNullBin', 'on', 'SEM', 'on' );
ERP = pop_savemyerp(ERP,...
 'erpname', 'blast_group_avg', 'filename', 'blast_group_avg.erp', 'filepath', erpdir,...
 'Warning', 'on');