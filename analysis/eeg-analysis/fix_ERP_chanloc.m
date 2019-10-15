%% Fix chanlocs when ref is still included
% establish working directory 
blast_dir_PC;

[d,s,r]=xlsread('adult_subjects.xlsx');
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;

% establish subject list
for k=25:length(s); %edit for subject of interest (can run multiple at once)
    clear ERP ALLERP
    
    [ERP ALLERP] = pop_loaderp( 'filename', 'blast_a_001_3runs_filt_chanop.erp', 'filepath', [erpdir 'blast_erp_filt_chanop' filesep]);
    [ERP ALLERP] = pop_loaderp( 'filename', [s{k} '_3runs_filt_chanop.erp'], 'filepath', [erpdir 'blast_erp_filt_chanop' filesep]);
    ALLERP(2).chanlocs=ALLERP(1).chanlocs
    ERP.chanlocs=ALLERP(1).chanlocs
    ERP = pop_savemyerp(ERP, 'erpname', s{k}, 'filename', [s{k} '_3runs_filt_chanop.erp'], 'filepath', [erpdir 'blast_erp_filt_chanop' filesep]);                                                                                                                                                                                                                     
end