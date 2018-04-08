
% Auditory Mismatch Experiment
% About
% Zhenghan Qi
% Greg Ciccarelli, July 20, 2015

%set current path
addpath('./helper');
addpath('../util');
Screen('Preference', 'SkipSyncTests', 1); %GAC
clear;

%parameters of the experiment
p.debug_mode = 0;


p.audio_latency=0.012; %when trying 0.015 it gets worse
p.text_size = 35;
p.text_font = 'Times New Roman';
p.taskNumber = 32;
p.taskName = 'mmnZqi';

%experiment preamble (all initialization code)
initializationScriptMmnZqi;

stimListFile = fopen(fullfile('.','stimuli', ['block' num2str(p.runNumber) '_meg.csv']));
stimList = textscan(stimListFile,'%s %s %s %s %s %s',...
    'headerlines',1,'delimiter',',');
fclose(stimListFile);

if p.debug_mode
    nSequencies = 5;
else
    nSequencies = numel(stimList{1});
end


for i = 1:nSequencies
    fileNameAudio = fullfile('.', 'stimuli', 'normalized-180-ns', ...
        [stimList{2}{i} '_' stimList{3}{i}], ...
        [stimList{2}{i} num2str(stimList{4}{i}) '.wav']);
    p.trigger = str2double(stimList{5}{i});
    %play song
    playAudio(p,fileNameAudio)
    
end

%make header to label columns of data output
% header = {'RunNumber','TrialNumber','Word','TylerWuggy','nSyllable'};
% triggerTimingHeader = {'RunNumber','TrialNumber','absolute time [s]','triggerCode','triggerLabel'};

info.parameters = p;
% info.triggerTiming = triggerTiming;
% info.triggerTimingHeader = triggerTimingHeader;
info.about = 'Auditory mismatch negativity protocol to be implemented with MEG';
info.subjectID = subjID;
info.function = mfilename('fullpath');
info.ProcessedTime = now();

%label columns of data with units
unit = {'a.u.','a.u.','a.u.','a.u.','a.u.'};

%make final output structure
% output.data = data;
% output.header = header;
output.info = info;
% output.unit = unit;

%save final output structure
file_path_save = fullfile('..', 'Results');
file_name_save = [datestr(now,'yyyymmddHHMMSS') subjID ...
    sprintf('%03d', p.taskNumber) '_R' sprintf('%03d', p.runNumber) '_' p.taskName];

if ~exist(file_path_save,'dir')
    mkdir(file_path_save)
end

save(fullfile(file_path_save,file_name_save),'-struct','output')

