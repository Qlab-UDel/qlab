%% set up file and folders
% establish working directory 
blast_dir_PC;

highpass=0.1; %set high pass filter
lowpass=80; %set low pass filter
current_run = '_run3'; % establish current run
epoch_baseline = -100.0 %epoch baseline
epoch_end = 600.0 %epoch offset

[d,s,r]=xlsread('adult_subjects.xlsx');
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
run= '_run1'

% establish s{k} list
for k=1:length(s); %edit for subject of interest (can run multiple at once)

    datasetname =[s{k} run]; %create consistent naming scheme for subject dataset

%% Preprocessing steps
% Step 1: load file, filter, referencing, run ica, apply channel location
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    eeglab('redraw');
    EEG = pop_loadxdf([rawdir s{k} filesep datasetname '.xdf'], 'streamtype', 'EEG', 'exclude_markerstreams', {});
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_raw'],'gui','off'); 
    EEG = eeg_checkset( EEG );
    EEG = pop_eegfiltnew(EEG, highpass,lowpass,16500,0,[],1);
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl'],'gui','off'); 
    EEG = eeg_checkset( EEG );
    EEG=pop_chanedit(EEG, 'load',[],'lookup','C:\\Users\\Qlab\\Documents\\MATLAB\\toolbox\\eeglab14_1_1b\\plugins\\dipfit2.3\\standard_BEM\\elec\\standard_1005.elc');
    EEG = eeg_checkset( EEG );
    EEG = pop_reref( EEG, [13 16] );
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl_rr'],'gui','off'); 
    EEG = eeg_checkset( EEG );
    EEG = pop_saveset( EEG, [workdir s{k} filesep datasetname '_fl_rr']);
end

%Manual inspection of the data and removal of bad blocks/interpolation of bad electrodes occurs in between these steps. 
%Save manually inspected file as: **'subject_run#_fl_rr_check.set'**

%% Run ICA
for k=1:length(s);
    
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    EEG = pop_loadset('filename',[s{k} current run '_fl_rr_check.set'],'filepath',[workdir s{k} filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = pop_runica(EEG, 'extended',1,'interupt','on');
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl_rr_ica'],'gui','off');
    EEG = pop_saveset( EEG, [workdir s{k} filesep datasetname '_ica']);
end

%Manual rejection of components occurs in between these steps
%Save manually rejected file as: **'subject_run#_clean.set'**

%% set up file and folders
% establish working directory 
blast_dir_PC;

% establish s{k} list
for k=1:length(s); %edit for subject of interest (can run multiple at once)

    clear ALLEEG

%% Epoching Steps
% Merge 3 runs into one dataset
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    EEG = pop_loadset('filename',[s{k} '_run1_clean.set'],'filepath',[workdir s{k} filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = pop_loadset('filename',[s{k} '_run2_clean.set'],'filepath',[workdir s{k} filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = pop_loadset('filename',[s{k} '_run3_clean.set'],'filepath',[workdir s{k} filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = eeg_checkset( EEG );
    EEG = pop_mergeset( ALLEEG, [1:3], 0);
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'gui','off'); 
    EEG = pop_saveset( EEG, [workdir s{k} filesep s{k} '_merged_clean']);
    
% Create eventlist, apply binlist, extract epochs, and artifact rejection
    EEG  = pop_creabasiceventlist( EEG , 'AlphanumericCleaning', 'on', 'BoundaryNumeric', { -99 }, 'BoundaryString', { 'boundary' }, 'Eventlist', [txtdir s{k} filesep 'eventlist.txt'] ); 
    EEG = eeg_checkset( EEG );
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'gui','off'); 
    EEG  = pop_binlister( EEG , 'BDF', [txtdir 'blast_binlist.txt'], 'ExportEL', [txtdir s{k} filesep 'binlist.txt'],'ImportEL', [txtdir s{k} filesep 'eventlist.txt'], 'IndexEL',  1, 'SendEL2', 'EEG&Text', 'Voutput', 'EEG' );
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = pop_epochbin( EEG , [epoch_baseline  epoch_end],  'pre'); 
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG  = pop_artmwppth( EEG , 'Channel',  1:22, 'Flag',  1, 'Threshold',  100, 'Twindow', [epoch_baseline epoch_end], 'Windowsize',  200, 'Windowstep',  100 ); 
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET ,'savenew',[workdir s{k} filesep s{k} '_epoch_ar.set'],'gui','off'); 
    EEG = pop_summary_AR_eeg_detection(EEG, [workdir s{k} filesep 'AR_summary_' s{k} '_epoch_ar.txt']); 
    [EEG, MPD] = getardetection(EEG, 1);
end

%% Create ERP from erp.set file
for k=1:length(s); %edit for subject of interest (can run multiple at once)
    %% create erp set
    EEG = pop_loadset('filename',[s{k} '_epoch_ar.set'],'filepath',[workdir s{k} filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    ERP = pop_averager( ALLEEG , 'Criterion', 'good', 'DSindex',1, 'ExcludeBoundary', 'on', 'SEM', 'on' );
    ERP = pop_savemyerp(ERP, 'erpname', s{k}, 'filename', [s{k} '.erp'], 'filepath', [erpdir s{k} filesep], 'Warning', 'on');   
end

%% Average individual ERPs together into group
    ERP = pop_gaverager( [anadir 'load_erpset_n22.txt'] , 'ExcludeNullBin', 'on', 'SEM', 'on' );
    %Filter ERP at low-pass of 30 Hz
    ERP = pop_filterp( ERP,  1:22 , 'Cutoff',  30, 'Design', 'butter', 'Filter', 'lowpass', 'Order',  2 );
    %Run bin operation to compute MMN
    ERP = pop_binoperator( ERP, {  'b10 = b4-b1 label MMN voice deviant low freq',  'b11 = b5-b2 label MMN voice deviant high freq',...
      'b12 = b6-b3 label MMN voice deviant equal freq',  'b13 = b7-b1 label MMN syllable deviant high freq',  'b14 = b8-b2 label MMN syllable devaint low freq',...
      'b15 = b9-b3 label MMN syllable deviant equal freq'});
    %Run channel operation to compute average over left and right anterior ROI
    %Run channel operation to compute average over left and right anterior ROI
    ERP = pop_erpchanoperator( ERP, {  'ch23 = (ch1+ch3+ch4+ch8+ch9+ch13+ch15+ch16+ch20)/9 label left',  'ch24 = (ch2+ch6+ch7+ch11+ch12+ch14+ch18+ch19+ch21)/9 label right',  'ch25 = (ch1+ch2+ch3+ch4+ch5+ch6+ch7)/7 label frontal', 'ch26 = (ch8+ch9+ch10+ch11+ch12+ch13+ch14)/7 label central', 'ch27 = (ch15+ch16+ch17+ch18+ch19+ch20+ch21+ch22)/8 label parietal', 'ch28 = (ch1+ch3+ch4)/3 label left frontal', 'ch29 = (ch2+ch6+ch7)/3 label right frontal', 'ch30 = (ch8+ch9+ch13)/3 label left central', 'ch31 = (ch11+ch12+ch14)/3 label right central', 'ch32 = (ch15+ch16+ch20)/3 label left parietal','ch33 = (ch18+ch19+ch21)/3 label right parietal'} ,...
     'ErrorMsg', 'popup', 'KeepLocations',  0, 'Warning', 'on' );
