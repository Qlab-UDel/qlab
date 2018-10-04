%% Written by Julie M. Schneider 10/4/2018
% All resources can be found at: https://openwetware.org/wiki/Mass_Univariate_ERP_Toolbox:_within-subject_t-tests

%% Creating GND Variables for Mass Univariate Analyses
%If you already have a GND file:
load filename.GND -MAT

%Open GUI for MUT and select ERP files (be sure you are in correct dir)
GND=erplab2GND('gui')

%Establish BIN differences of interest
GND=bin_dif(GND,4,1,'Voice Deviant Low Freq MMN');
GND=bin_dif(GND,5,1,'Voice Deviant High Freq MMN');
GND=bin_dif(GND,8,1,'Syllable Deviant Low Freq MMN');
GND=bin_dif(GND,7,1,'Syllable Deviant High Freq MMN');

%Visualize differences (the numbers pertain to our new bin numbers)
gui_erp(GND,'bin',16);
gui_erp(GND,'bin',17);
gui_erp(GND,'bin',18);
gui_erp(GND,'bin',19);

%% Establish BIN differences based on frequency
GND=bin_dif(GND,17,16,'Voice Deviant Freq MMN');
GND=bin_dif(GND,19,18,'Syllable Deviant Freq MMN');

%Visualize differences (the numbers pertain to our new bin numbers)
gui_erp(GND,'bin',20);
gui_erp(GND,'bin',21);

%% Time point by time point analysis
%%tmax permutation test (Permutation) 
%To determine when and where the ERPs to standards and deviants differ, we will perform a permutation test based on the one-sample/repeated measures t-statistic using every time point at every electrode from 0 to 500 ms post-stimulus, controlling for the FWER 
GND=tmaxGND(GND,20,'time_wind',[0 500],'output_file','vdev_timeperm.txt');
GND=tmaxGND(GND,21,'time_wind',[0 500],'output_file','sdev_timeperm.txt');

%%t-test with control of the false discovery rate (FDR)
GND=tfdrGND(GND,20,'method','by','time_wind',[0 500],'output_file','vdev_fdr.txt');
GND=tfdrGND(GND,21,'method','by','time_wind',[0 500],'output_file','sdev_fdr.txt');

%%cluster mass permutatoin test (Cluster)
%chan_hood relates to neighborhood density (computed as radius * max
%distance in idealized coordinates = max distance in units cm) .61
%corresponds to a 56 cm adult head
GND=clustGND(GND,20,'time_wind',[0 500],'chan_hood',.61,'thresh_p',.05);
GND=clustGND(GND,21,'time_wind',[0 500],'chan_hood',.61,'thresh_p',.05);

%To plot these with a temperature scale to represent graded degree of
%significance. The number corresponds to the raster plot.
sig_raster(GND,3,'use_color','rgb');

%% Mean time window analysis
%%tmax permutation test (Permutation)
%Instead of performing t-tests at every single time point, it is also possible to perform t-test on mean difference wave amplitude in a particular time window.
GND=tmaxGND(GND,20,'time_wind',[70 130],'mean_wind','yes');
GND=tmaxGND(GND,21,'time_wind',[70 130],'mean_wind','yes');

%% Plotting fun tricks
%To reproduce figures without conducting permutation again:
sig_raster(GND,1);
gui_erp(GND,'t_test',1);

%to save raster image
print -f1 -depsc vdevlow_raster
