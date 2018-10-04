function [subject] = blast_subjects(s)
 
% function [datafolder subject capfile badcell] = binding_subjects(s)
% Generates subject name to be used in subsequent scripts
% Julie Schneider (August 24, 2018)

 
% get data path
if ismember(s,(1:25))
   
else
    error('Invalid subject number');
end
 
% initialize badcell empty
badcell = {};
 

if s == 1
    subject = 'blast_a_001';
elseif s == 2
    subject = 'blast_a_002';
elseif s == 3
    subject = 'blast_a_003';
elseif s == 4
    subject = 'blast_a_004';
elseif s == 5
    subject = 'blast_a_005';
elseif s == 6
    subject = 'blast_a_006';
elseif s == 7
    subject = 'blast_a_007';
elseif s == 8
    subject = 'blast_a_008';
elseif s == 9
    subject = 'blast_a_009';
elseif s == 10
    subject = 'blast_a_010';
elseif s == 11
    subject = 'blast_a_011';
elseif s == 12
    subject = 'blast_a_012';
elseif s == 13
    subject = 'blast_a_013';
elseif s == 14
    subject = 'blast_a_014';
elseif s == 15
    subject = 'blast_a_015';
elseif s == 16
    subject = 'blast_a_016';
elseif s == 17
    subject = 'blast_a_017';
elseif s == 18
    subject = 'blast_a_018';
elseif s == 19
    subject = 'blast_a_019';
elseif s == 20
    subject = 'blast_a_020';
elseif s == 21
    subject = 'blast_a_021';
elseif s == 22
    subject = 'blast_a_022';
elseif s == 23
    subject = 'blast_a_023';
elseif s == 24
    subject = 'blast_a_024';
elseif s == 25
    subject = 'blast_a_025';
end



