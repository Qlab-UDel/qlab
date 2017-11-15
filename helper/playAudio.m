function playAudio(p,fileNameAudio)
% function play_AV(p,t,trigger_v,trigger_a)
%
% Play audio visual stimuli with offset t (in sec)
%

%prepare load
[y, Fs] = audioread(fileNameAudio);
%[y, Fs] = wavread(fileNameAudio);
y = [y y]; % Expects stero channel, but input is mono


%prepare audio
PsychPortAudio('FillBuffer', p.ahandle, y');
PsychPortAudio('Start', p.ahandle, 1, inf, 0);

%play audio
PsychPortAudio('RescheduleStart', p.ahandle, 0, 0, 1);

dt = 0.005;
WaitSecs(p.audio_latency)
%send_trigger(p.trigger,dt);

% Set a stop time x seconds from the execution of this line and poll the keyboard/input device until then
stop = GetSecs + 0.5;
refractoryOkFlag = true;
refractoryOkTime = 0;
while GetSecs < stop
    [keyIsDown, secs, keyCode] = KbCheck;
%     if keyIsDown
%         break; % End the while loop
%     end
    if keyIsDown && refractoryOkFlag
        send_trigger(100,dt);
        refractoryOkFlag = false;
        refractoryOkTime = GetSecs + 0.25;
    end
    if GetSecs > refractoryOkTime
        refractoryOkFlag = true;
    end
    WaitSecs(0.01); % It is a good habit not to poll as fast as possible
end












    
    
        
    




