%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is a script example for preprocessing steps, including:
% Load DataSet,Filter, Re-reference, Run ICA, Create Eventlist,Assign Bins,Epoch & Baseline Correction,Automatic Artifact Detection
%cd /qlab/Project/play/analysis/script
% !! Initiate matlab without the GUI window by typing the following command to a terminal window
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;
clc;

highpass=0.1; %set high pass filter
lowpass=80; %set low pass filter
epoch_baseline = -100.0 %epoch baseline
epoch_end = 600.0 %epoch offset

% Step1: Initial launching of the EEGLAB.

[ALLEEG EEG CURRENTSET ALLCOM]=eeglab; 

% Step2: Open the subject list file (.txt)

fid=fopen('../subjlist_all.txt'); 

% Step3: readin filename for each subject line by line until the end of the file
% Step 1: load file, filter, referencing, run ica, apply channel location


while feof (fid)==0
line= fgetl (fid);
SUB=line(1:7);
NM_HEOG=line(9:10);
BINFILE='play_exp1_bins.txt';

generalfile_input_filepath = [pwd '/'];
indfile_input_filepath = [pwd '/'];
output_filepath = [pwd '/'];

%EEG = pop_loadset('filename', [SUB,'_SVF_merged.set'],'filepath',indfile_input_filepath); 

EEG = pop_chanedit(EEG, 'load',{'/usr/local/MATLAB/eeglab/plugins/dipfit2.2/standard_BESA/standard-10-5-cap385.elp'});
EEG = pop_eegchanoperator( EEG, {  ' nch1 = ch1 - ( (ch18+ch24)/2 ) Label FP1'   ' nch2 = ch2 - ( (ch18+ch24)/2 ) Label FP2'   ' nch3 = ch3 - ( (ch18+ch24)/2 ) Label F7'   ' nch4 = ch4 - ( (ch18+ch24)/2 ) Label F3'   ' nch5 = ch5 - ( (ch18+ch24)/2 ) Label FZ'   ' nch6 = ch6 - ( (ch18+ch24)/2 ) Label F4'   ' nch7 = ch7 - ( (ch18+ch24)/2 ) Label F8'   ' nch8 = ch8 - ( (ch18+ch24)/2 ) Label FT7'   ' nch9 = ch9 - ( (ch18+ch24)/2 ) Label FC3'   ' nch10 = ch10 - ( (ch18+ch24)/2 ) Label FCZ'   ' nch11 = ch11 - ( (ch18+ch24)/2 ) Label FC4'   ' nch12 = ch12 - ( (ch18+ch24)/2 ) Label FT8'   ' nch13 = ch13 - ( (ch18+ch24)/2 ) Label T7'   ' nch14 = ch14 - ( (ch18+ch24)/2 ) Label C3'   ' nch15 = ch15 - ( (ch18+ch24)/2 ) Label CZ'   ' nch16 = ch16 - ( (ch18+ch24)/2 ) Label C4'   ' nch17 = ch17 - ( (ch18+ch24)/2 ) Label T8'   ' nch18 = ch18 - ( (ch18+ch24)/2 ) Label M1'   ' nch19 = ch19 - ( (ch18+ch24)/2 ) Label TP7'   ' nch20 = ch20 - ( (ch18+ch24)/2 ) Label CP3'   ' nch21 = ch21 - ( (ch18+ch24)/2 ) Label CPZ'   ' nch22 = ch22 - ( (ch18+ch24)/2 ) Label CP4'   ' nch23 = ch23 - ( (ch18+ch24)/2 ) Label TP8'   ' nch24 = ch24 - ( (ch18+ch24)/2 ) Label M2'   ' nch25 = ch25 - ( (ch18+ch24)/2 ) Label P7'   ' nch26 = ch26 - ( (ch18+ch24)/2 ) Label P3'   ' nch27 = ch27 - ( (ch18+ch24)/2 ) Label PZ'   ' nch28 = ch28 - ( (ch18+ch24)/2 ) Label P4'   ' nch29 = ch29 - ( (ch18+ch24)/2 ) Label P8'   ' nch30 = ch30 - ( (ch18+ch24)/2 ) Label O1'   ' nch31 = ch31 - ( (ch18+ch24)/2 ) Label OZ'   ' nch32 = ch32 - ( (ch18+ch24)/2 ) Label O2'   ' nch33 = ch33 Label HEO'   ' nch34 = ch34 Label VEO'   });

EEG  = pop_creabasiceventlist( EEG , 'AlphanumericCleaning', 'on', 'Eventlist', [output_filepath SUB '_elist.txt'], 'Newboundary', { -99 }, 'Stringboundary', { 'boundary' }, 'Warning', 'on' );

for j=1:length([EEG.EVENTLIST.eventinfo.code])-1
    if and(EEG.EVENTLIST.eventinfo(j).code > 200, EEG.EVENTLIST.eventinfo(j).code < 209)
       num=num2str(EEG.EVENTLIST.eventinfo(j).code);
        EEG.EVENTLIST.eventinfo(j+1).code = EEG.EVENTLIST.eventinfo(j+1).code+1000*str2num(num(end));
end;
end;
        
% change the unique codes in the original data set into something that 
% can be uniquely identified without the preceding or following code. 
% In this example, we use the pollowing codes as a basis for making changes on their following codes:
% m_unamb_NP: 201--> add 1000 to the code of its following code
% m_unamb_VP: 202--> add 2000 to the code of its following code
% m_amb_NP: 203--> add 3000 to the code of its following code
% m_amb_VP: 204--> add 4000 to the code of its following code
% mis_unamb_NP: 205--> add 5000 to the code of its following code
% mis_unamb_VP: 206--> add 6000 to the code of its following code
% mis_amb_NP: 207--> add 7000 to the code of its following code
% mis_amb_VP: 208--> add 8000 to the code of its following code

EEG = pop_binlister( EEG , 'BDF', [generalfile_input_filepath BINFILE], 'ExportEL', [output_filepath SUB '_elist.txt'], 'ImportEL', 'no', 'Saveas', 'on', 'SendEL2', 'EEG&Text', 'UpdateEEG', 'on', 'Warning', 'on' );

EEG = pop_epochbin( EEG , [-200.0  1700.0],  'pre');

EEG  = pop_artmwppth( EEG , 'Channel',  34, 'Flag', [ 1 2], 'Review', 'off', 'Threshold',  100, 'Twindow', [ -200 1199], 'Windowsize',  200, 'Windowstep',  100 );

EEG  = pop_artstep( EEG , 'Channel',  33, 'Flag', [ 1 3], 'Review', 'off', 'Threshold', str2num(NM_HEOG), 'Twindow', [0 200], 'Windowsize',  200, 'Windowstep',  50 );
EEG  = pop_artstep( EEG , 'Channel',  33, 'Flag', [ 1 3], 'Review', 'off', 'Threshold', 100, 'Twindow', [ -200 1199], 'Windowsize',  200, 'Windowstep',  50 );

EEG  = pop_artextval( EEG , 'Channel',  [1:34], 'Flag', [ 1 4], 'Review', 'off', 'Threshold', [ -100 100], 'Twindow', [ -200 1199] );

EEG  = pop_basicfilter( EEG,  1:34 , 'Cutoff',  30, 'Design', 'butter', 'Filter', 'lowpass', 'Order',  2 );

EEG = pop_chanedit(EEG, 'lookup','/usr/local/MATLAB/eeglab/plugins/dipfit2.2/standard_BESA/standard-10-5-cap385.elp');

EEG = pop_saveset( EEG, 'filename',[SUB '_rr_elist_bin_epbaseline_AD_lp30.set'],'filepath',output_filepath);

end;
