
% initialization script

%clear previous variables
clc;
Screen('CloseAll')

%get subject name
subjID = input('Subject ID: ','s');

%get run number
p.runNumber = input('Run number (1 or 2): ', 's');

%make p.runNumber double so you can run sprintf on it
p.runNumber = str2double(p.runNumber);

%initialize button responses
KbName('UnifyKeyNames');
escapeKey = KbName('ESCAPE');

%check Java
warning off
PsychJavaTrouble;
warning on

%initialize functions
dummy=GetSecs;  % Force GetSecs and WaitSecs into memory to avoid latency later on:
WaitSecs(0.1);

%OpenGL support
AssertOpenGL;

%initialize triggers
%send_trigger(0,0.002); %initialize triggers

%open psychportaudio and load audio   
%PsychPortAudio('Close') %close all open ports GAC
InitializePsychSound(1); % Initialize PsychPortAudio
devices = PsychPortAudio('GetDevices');
deviceid = 25;% 25 strix
reqlatencyclass = 1;%%%%1 ????????????????????? % class 2 empirically the best
buffersize=0;
samplingRate = 44100;
p.ahandle = PsychPortAudio('Open', deviceid,[], reqlatencyclass, samplingRate, 2,buffersize);

 








