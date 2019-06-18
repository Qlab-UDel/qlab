%Load subject excel file
% establish working directory 
blast_dir_PC;

highpass=0.1; %set high pass filter
lowpass=80; %set low pass filter

[d,s,r]=xlsread('child_subjects.xlsx');
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
run= '_run1'

for k=3:length(s);

datasetname =[s{k} run];

EEG = pop_loadxdf([rawdir s{k} filesep datasetname '.xdf'], 'streamtype', 'EEG', 'exclude_markerstreams', {});
[ALLEEG, EEG, CURRENTSET] = eeg_store( ALLEEG, EEG, 0 );

EEG = pop_eegfiltnew(EEG, highpass,lowpass,16500,0,[],1);
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl'],'gui','off'); 
EEG = eeg_checkset( EEG );

EEG=pop_chanedit(EEG, 'load',[],'lookup','C:\\Users\\brainstim\\Documents\\MATLAB\\eeglab14_1_1b\\plugins\\dipfit2.3\\standard_BESA\\standard-10-5-cap385.elp');
EEG = eeg_checkset( EEG );

EEG = pop_reref( EEG, [13 16] );
[ALLEEG EEG CURRENTSET] = pop_newset(ALLEEG, EEG, CURRENTSET,'setname',[datasetname '_fl_rr'],'gui','off'); 
EEG = eeg_checkset( EEG );

EEG = pop_saveset( EEG, [workdir s{k} filesep datasetname '_fl_rr']);
end