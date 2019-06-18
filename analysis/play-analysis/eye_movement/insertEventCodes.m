
%%%%% BEFORE RUNNING THIS SCRIPT %%%%%

% Ensure that you have imported the data from Brain Vision into EEGLAB. The 
% script runs on the currently active dataset.


%%%%% SET OPTIONS %%%%%

% File with event code list
fname = 'eventCodes.csv';

% Row/column where event codes start (remember, MATLAB starts counting at 0!)
eventCodes = csvread(fname,1,5); 

% Channel number in EEG file that contains stimulus events
auxch = 32;

% Threshold for event onsets
th = 5000;

% Minimum time between events (in time points; depends on your sampling rate)
minTime = 500;

% Time window for threshold
thTime = 2;

% Start time (i.e., when to start looking for events)
startTime = 1;

%%%% END OF USER OPTIONS %%%%%


% Center AUX channel at zero (to remove any voltage offsets)
aux = EEG.data(auxch,:);
meanAux = mean(aux);
aux = aux - meanAux;
EEG.data(auxch,:) = aux;

% Remove existing events
EEG.event = [];

% Find values that exceed voltage threshold
npts = length(aux);
nevents = length(EEG.event);
checkPts = ones(1,npts);
practiceCount = 0;
initialEvents = nevents;
current = 1;
for i = 1:length(aux)-1
    if i>startTime
        if checkPts(i)
            minValue = min(aux(i:i+thTime-1));
            maxValue = max(aux(i:i+thTime-1));
            diff = maxValue - minValue;
            if diff>th
                disp(['Found ' num2str(current) ' events'])
                EEG.event(current).latency = i;
                EEG.event(current).type = eventCodes(current);
                current = current + 1;
                checkPts(i:i+minTime) = 0;
            end
        end
    end
end

% Check that number of events found is correct
if (length(EEG.event)-initialEvents) ~= length(eventCodes)
    error('Missing events in EEG or behavioral data')
end