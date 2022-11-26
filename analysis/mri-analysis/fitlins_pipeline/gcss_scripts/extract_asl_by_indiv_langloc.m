% Adult ASL Activation Extraction based on Individualized LangLoc Masks (GCSS Method)
% 022 and 029 and 040 have ASL, but do not have langloc
% Please refer to indiv_langloc_sl.m for specific information
DIR_LIST = dir ('/Volumes/data-1/projects/blast/data/mri/imaging/scott_gcss_lpsa/data/indiv_langloc_output/asl/adult/');

for i = 1:length(DIR_LIST)

    EXT_DIGIT = regexp(DIR_LIST(i).name,'\d*','Match')

    if not(isempty(EXT_DIGIT)) 
        if not(ismember(EXT_DIGIT, '022')) 
            % indiv_langloc_sl(opts, group, prefix, part_id)
            indiv_langloc_sl(opts, 'adult', 'blast_a_', DIR_LIST(i).name)  
        end
    end
end

indiv_langloc_sl(opts, 'adult', 'blast_a_', '044')  

% Child ASL Activation Extraction based on Individualized LangLoc Masks (GCSS Method)

DIR_LIST = dir ('/Volumes/data-1/projects/blast/data/mri/imaging/scott_gcss_lpsa/data/indiv_langloc_output/asl/child/');

for i = 1:length(DIR_LIST)

    EXT_DIGIT = regexp(DIR_LIST(i).name,'\d*','Match')

    if not(isempty(EXT_DIGIT)) 
        if not(ismember(EXT_DIGIT, '034')) 
            indiv_langloc_sl(opts, 'child', 'blast_c_', DIR_LIST(i).name)  
        end
    end
end

indiv_langloc_sl(opts, 'child', 'blast_c_', '170') 