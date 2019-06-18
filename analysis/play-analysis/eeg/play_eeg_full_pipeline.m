%% set up file and folders
% establish working directory 
play_dir;

highpass=0.1; %set high pass filter
lowpass=80; %set low pass filter
current_run = '_run3'; % establish current run
epoch_baseline = -100.0 %epoch baseline
epoch_end = 600.0 %epoch offset

% establish subject list
for s = [1:25] %edit for subject of interest (can run multiple at once)

    % get subject info, same name as subjects.m (function)
    [subject] = blast_subjects(s);
    subject
    datasetname = [subject current_run] %create consistent naming scheme for subject dataset

%% Preprocessing steps
% Step 1: load file, filter, referencing, run ica, apply channel location
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    eeglab('redraw');
    EEG = pop_loadxdf([rawdir subject filesep datasetname '.xdf'], 'streamtype', 'EEG', 'exclude_markerstreams', {});
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_raw'],'gui','off'); 
    EEG = eeg_checkset( EEG );
    EEG = pop_eegfiltnew(EEG, highpass,lowpass,16500,0,[],1);
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl'],'gui','off'); 
    EEG = eeg_checkset( EEG );
    EEG=pop_chanedit(EEG, 'load',[],'lookup','/Users/Rachel/Documents/eeglab14_1_2b/plugins/dipfit2.3/standard_BESA/standard-10-5-cap385.elp');
    EEG = eeg_checkset( EEG );
    EEG = pop_reref( EEG, [13 16] );
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl_rr'],'gui','off'); 
    EEG = eeg_checkset( EEG );
    EEG = pop_saveset( EEG, [workdir subject filesep datasetname '_fl_rr']);
end

%Manual inspection of the data and removal of bad blocks/interpolation of bad electrodes occurs in between these steps. 
%Save manually inspected file as: **'subject_run#_fl_rr_check.set'**

%% Run ICA
for s = [1]
    % get subject info, same name as subjects.m (function)
    [subject] = blast_subjects(s);
    subject
    
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    EEG = pop_loadset('filename',[subject current run '_fl_rr_check.set'],'filepath',[workdir subject filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = pop_runica(EEG, 'extended',1,'interupt','on');
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl_rr_ica'],'gui','off');
    EEG = pop_saveset( EEG, [workdir subject filesep datasetname '_ica']);
end

%Manual rejection of components occurs in between these steps
%Save manually rejected file as: **'subject_run#_clean.set'**

%% set up file and folders
% establish working directory 
blast_dir_PC;

% establish subject list
for s = [23] %edit for subject of interest (can run multiple at once)

    clear ALLEEG
    
    % get subject info, same name as subjects.m (function)
    [subject] = blast_subjects(s);
    subject

%% Epoching Steps
% Merge 3 runs into one dataset
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    EEG = pop_loadset('filename',[subject '_run1_clean.set'],'filepath',[workdir subject filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = pop_loadset('filename',[subject '_run2_clean.set'],'filepath',[workdir subject filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = pop_loadset('filename',[subject '_run3_clean.set'],'filepath',[workdir subject filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    EEG = eeg_checkset( EEG );
    EEG = pop_mergeset( ALLEEG, [1:3], 0);
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'gui','off'); 
    EEG = pop_saveset( EEG, [workdir subject filesep subject '_merged_clean']);
    
% Create eventlist, apply binlist, extract epochs, and artifact rejection
    EEG  = pop_creabasiceventlist( EEG , 'AlphanumericCleaning', 'on', 'BoundaryNumeric', { -99 }, 'BoundaryString', { 'boundary' }, 'Eventlist', [txtdir subject filesep 'eventlist.txt'] ); 
    EEG = eeg_checkset( EEG );
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'gui','off'); 
    EEG  = pop_binlister( EEG , 'BDF', [txtdir 'blast_binlist.txt'], 'ExportEL', [txtdir subject filesep 'binlist.txt'],'ImportEL', [txtdir subject filesep 'eventlist.txt'], 'IndexEL',  1, 'SendEL2', 'EEG&Text', 'Voutput', 'EEG' );
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = pop_epochbin( EEG , [epoch_baseline  epoch_end],  'pre'); 
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG  = pop_artmwppth( EEG , 'Channel',  1:22, 'Flag',  1, 'Threshold',  100, 'Twindow', [epoch_baseline epoch_end], 'Windowsize',  200, 'Windowstep',  100 ); 
    [ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET ,'savenew',[workdir subject filesep subject '_epoch_ar.set'],'gui','off'); 
    EEG = pop_summary_AR_eeg_detection(EEG, [workdir subject filesep 'AR_summary_' subject '_epoch_ar.txt']); 
    [EEG, MPD] = getardetection(EEG, 1);
end

%% Create ERP from erp.set file
for s = [1] %edit for subject of interest (can run multiple at once)
    
    % get subject info, same name as subjects.m (function)
    [subject] = blast_subjects(s);
    subject

    %% create erp set
    EEG = pop_loadset('filename',[subject '_epoch_ar.set'],'filepath',[workdir subject filesep]);
    [ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );
    ERP = pop_averager( ALLEEG , 'Criterion', 'good', 'DSindex',1, 'ExcludeBoundary', 'on', 'SEM', 'on' );
    ERP = pop_savemyerp(ERP, 'erpname', subject, 'filename', [subject '.erp'], 'filepath', [erpdir subject filesep], 'Warning', 'on');   
end

%Down filter indvidual erp date and run bin/channel operations
for s = [1:16 18:31] %edit for subject of interest (can run multiple at once)

    datasetname= [subject '.erp']
    outputname= [subject '_op.erp']
    
    ERP = pop_filterp( ERP,  1:22 , 'Cutoff',  30, 'Design', 'butter', 'Filter', 'lowpass', 'Order',  2 );
    %Run bin operation to compute MMN
    ERP = pop_binoperator( ERP, {  'b16 = (b1+b2)/2 label all standards',  'b17 = (b4+b5+b7+b8)/4 label all deviants',...
      'b18 = (b4+b5)/2 label voice deviant ',  'b19 = (b7+b8)/2 label syllable deviant',  'b20 = (b5+b7)/2 label high freq deviant',...
      'b21 = (b4+b8)/2 label low freq deviant'});
    ERP = pop_erpchanoperator( ERP, {  'ch23 = (ch1+ch3+ch4+ch8+ch9+ch13+ch15+ch16+ch20)/9 label left',  'ch24 = ch2+ch6+ch7+ch11+ch12+ch14+ch18+ch19+ch21/9 label right',  'ch25 = ch1+ch2+ch3+ch4+ch5+ch6+ch7/7 label frontal', 'ch26 = ch8+ch9+ch10+ch11+ch12+ch13+ch14/7 label central', 'ch27 = ch15+ch16+ch17+ch18+ch19+ch20+ch21+ch22/8 label parietal', 'ch28 = ch1+ch3+ch4/3 label left frontal', 'ch29 = ch2+ch6+ch7/3 label right frontal', 'ch30 = ch8+ch9+ch13/3 label left central', 'ch31 = ch11+ch12+ch14/3 label right central', 'ch32 = ch15+ch16+ch20/3 label left parietal','ch33 = ch18+ch19+ch21/3 label right parietal'} ,...
     'ErrorMsg', 'popup', 'KeepLocations',  0, 'Warning', 'on' );
     ERP = pop_savemyerp(ERP, 'erpname', datasetname, 'filename', outputname, 'filepath',[erpdir subject filesep]);
 end
     
%% Average individual ERPs together into group
grandavg_filename= 'grand_avg_N27.erp'
txtfile = 'load_erpset_n27.txt' %all individual subject erp files with path to file
    ERP = pop_gaverager( [anadir txtfile] , 'ExcludeNullBin', 'on', 'SEM', 'on' );
    ERP = pop_savemyerp(ERP,...
 'erpname', 'grandavg_erp', 'filename', [grandavg_filename], 'filepath', [erpdir], 'Warning',...
 'on');