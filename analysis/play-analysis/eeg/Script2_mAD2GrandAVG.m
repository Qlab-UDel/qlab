generalfile_input_filepath = [pwd '/'];
output_filepath = [pwd '/'];
indfile_input_filepath = [pwd '/'];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
delete ('grandavglist_SVF_FS+.txt');
delete ('Allsub_AD_summary.txt');
fid=fopen('../subjlist_all.txt');
fid2=fopen('grandavglist_SVF_FS+.txt','a');
fid3=fopen('Allsub_AD_summary.txt','a');

while feof (fid)==0
line = fgetl (fid);
SUB = line (1:7);

%to average unmanually ADed files to see preliminary data pattern
%EEG = pop_loadset('filename',[SUB '_rr_elist_bin_epbaseline_AD_lp30.set'],'filepath',indfile_input_filepath);

%to average manually ADed files
EEG = pop_loadset('filename',[SUB '_rr_elist_bin_epbaseline_AD_lp30_man.set'],'filepath',indfile_input_filepath);

ERP = pop_averager( EEG , 'Criterion', 'good', 'DSindex',1, 'Stdev', 'on', 'Warning', 'on' );

ERP = pop_savemyerp(ERP, 'erpname', SUB, 'filename', [SUB '_SVF_FSplus.erp'], 'filepath', output_filepath, 'warning', 'off');
fprintf(fid2,'%s%s_SVF_FS.erp\n',output_filepath,SUB)

pop_summary_AR_erp_detection(ERP, [output_filepath SUB '_SVF_FSplus_AD_summary.txt']);

fprintf(fid3,'%s\n',SUB) %Print the subject number to 'Allsub_AD_summary.txt'
fid4=fopen([output_filepath SUB '_SVF_FS_AD_summary.txt']); %open this subject's AD_summary file
while feof(fid4)==0  %read and print eaach line to Allsub_AD_summary till the end of the subject's AD_summary file
line= fgetl (fid4);
fprintf(fid3,'%s\n',line) %put a line breaker after each line
end;

fprintf(fid3,'\n\n'); % put two line breakers after each subject's data
end; %end of the while command
fclose ('all');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

ALLERP = buildERPstruct([]);
ERP = pop_gaverager( ALLERP , 'Criterion',20, 'Loadlist', [generalfile_input_filepath 'grandavglist_SVF_FS+.txt'], 'Stdev', 'on', 'Warning', 'on' );
ERP = pop_savemyerp(ERP, 'erpname', 'grandavg_SVF_FS+.erp', 'filename', 'grandavg_SVF_FS+.erp', 'filepath', output_filepath, 'warning', 'on');

