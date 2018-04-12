# -------------------------- Header Parameters --------------------------

scenario = "MMN";

write_codes = EXPARAM( "Write Codes" );

screen_width_distance = EXPARAM( "Physical Screen Width" );
screen_height_distance = EXPARAM( "Physical Screen Height" );
screen_distance = EXPARAM( "Viewing Distance" );

default_background_color = EXPARAM( "Default Background Color" );
default_font = EXPARAM( "Default Font" );
default_font_size = EXPARAM( "Default Font Size" );
default_text_color = EXPARAM( "Default Font Color" );

active_buttons = 1;
response_matching = simple_matching;

stimulus_properties = 
	event_name, string,
	trial_number, number,
	stim_number, number,
	stim_type, string,
	p_code, number,
	ISI_duration, number;
event_code_delimiter = ";";

# ------------------------------- SDL Part ------------------------------
begin;

ellipse_graphic {
	color = EXPARAM( "Fixation Point Color" );
	ellipse_height = EXPARAM( "Fixation Point Size" );
	ellipse_width = EXPARAM( "Fixation Point Size" );
} fix_ellipse;

trial {
	#monitor_videos = false;
	stimulus_event {
		sound {
			wavefile {
				preload = false;
			};
		};
	} stim_event;
} stim_trial;

trial {
	trial_type = specific_response;
	terminator_button = 1;
	trial_duration = forever;
	
	picture{
		text { 
			caption = "rest";
			preload = false;
		} instruct_text;
		x = 0; 
		y = 0;
	} instruct_pic;
} instruct_trial;
	
trial {
	#monitor_videos = false;

	stimulus_event {
		picture {} ISI_pic;
		code = "ISI";
	} ISI_event;
} ISI_trial;

trial {
	picture {
		text {
			caption = "Ready";
			preload = false;
		} ready_text;
		x = 0;
		y = 0;
	} ready_pic;
} ready_trial;
	
# ----------------------------- PCL Program -----------------------------
begin_pcl;

include_once "../../Library/lib_visual_utilities.pcl";
include_once "../../Library/lib_utilities.pcl";

# --- CONSTANTS --- #

string STIM_EVENT_CODE = "Stim";

int STD_IDX = 1;
int DEV_IDX = 2;

int MAX_PORT_VAL = 255;

string VIDEO_CODE = "Video";

string STD_COND = "Standard";
string DEV_COND = "Deviant";

string CHARACTER_WRAP = "Character";

# --- Set up fixed stimulus parameters ---

string language = parameter_manager.get_string( "Language" );
language_file lang = load_language_file( scenario_directory + language + ".xml" );
bool char_wrap = ( get_lang_item( lang, "Word Wrap Mode" ).lower() == CHARACTER_WRAP.lower() );
double font_size = parameter_manager.get_double( "Default Font Size" );

# --- Stimulus setup ---

if ( parameter_manager.get_bool( "Show Fixation Point" ) ) then
	ISI_pic.add_part( fix_ellipse, 0, 0 );
end;

# Make some sounds
array<sound> stim_snds[2];
stim_snds[STD_IDX] = parameter_manager.get_sound( "Standard Sound" );
stim_snds[DEV_IDX] = parameter_manager.get_sound( "Deviant Sound" );
stim_snds[STD_IDX].get_wavefile().load();
stim_snds[DEV_IDX].get_wavefile().load();

if ( parameter_manager.get_bool( "Generate Sounds" ) ) then
	# Initialize some values
	double ramp_up_time = parameter_manager.get_double( "Rise Time" );
	double ramp_down_time = parameter_manager.get_double( "Fall Time" );

	# Make the rise/fall ramps
	asg::line ramp_down = new asg::line( ramp_down_time, 1.0, 0.0 );
	asg::line ramp_up = new asg::line( ramp_up_time, 0.0, 1.0 );

	# Make the waveform data
	double std_duration = parameter_manager.get_double( "Standard Duration" );
	double dev_duration = parameter_manager.get_double( "Deviant Duration" );
	asg::sine std_data = new asg::sine( std_duration, parameter_manager.get_double( "Standard Frequency" ), 0.0 );
	asg::sine dev_data = new asg::sine( dev_duration, parameter_manager.get_double( "Deviant Frequency" ), 0.0 );
	asg::waveform_data std_wf = new asg::waveform_data( std_data );
	asg::waveform_data dev_wf = new asg::waveform_data( dev_data );
	
	# Check that the rise and fall times are legal
	double ramp_time = ramp_up_time + ramp_down_time;
	if ( ramp_time > std_duration ) || ( ramp_time > dev_duration ) then
		exit( "The total rise and fall time is greater than the sound duration." );
	end;

	# Multiply by the rise/fall times
	std_wf.multiply_segment( ramp_up, 0.0 );
	std_wf.multiply_segment( ramp_down, std_wf.duration() - ramp_down_time );
	dev_wf.multiply_segment( ramp_up, 0.0 );
	dev_wf.multiply_segment( ramp_down, dev_wf.duration() - ramp_down_time );

	# Now make the sound objects
	stim_snds[STD_IDX] = new sound( new wavefile( std_wf, std_wf ) );
	stim_snds[DEV_IDX] = new sound( new wavefile( dev_wf, dev_wf ) );
end;

# Set the attenuation on the sounds
begin
	double std_atten = 1.0 - ( double( parameter_manager.get_int( "Standard Volume" ) ) / 100.0 );
	double dev_atten = 1.0 - ( double( parameter_manager.get_int( "Deviant Volume" ) ) / 100.0 );
	stim_snds[STD_IDX].set_attenuation( std_atten );
	stim_snds[DEV_IDX].set_attenuation( dev_atten );
end;

# --- sub present_instructions ---

sub
	present_instructions( string instruct_string )
begin
	full_size_word_wrap( instruct_string, font_size, char_wrap, instruct_text );
	instruct_trial.present();
	default.present();
end;

# --- sub ready_set_go ---

trial_refresh_fix( ready_trial, parameter_manager.get_int( "Ready Duration" ) );

array<string> ready_caps[3];
ready_caps[1] = get_lang_item( lang, "Ready Caption" );
ready_caps[2] = get_lang_item( lang, "Set Caption" );
ready_caps[3] = get_lang_item( lang, "Go Caption" );

sub
	ready_set_go
begin
	loop
		int i = 1
	until
		i > ready_caps.count()
	begin
		ready_text.set_caption( ready_caps[i], true );
		ready_trial.present();
		i = i + 1;
	end;
end;

# --- sub show_video ---

/*sub
	show_video( array<video,1>& vids, int vid_number )
begin
	video_player.play( vids[vid_number], VIDEO_CODE + string( vid_number ) );
end;*/

# --- Make a trial sequence

array<int> trial_sequence[0];
int min_start = parameter_manager.get_int( "Min Standards at Start" );

begin
	# Get some trial counts
	int total_trials = parameter_manager.get_int( "Total Trials" );
	int std_trials = int( ceil( parameter_manager.get_double( "Standard Proportion" ) * double(total_trials) ) );
	int dev_trials = total_trials - std_trials;

	# Figure out some of the restrictions
	int min_end = parameter_manager.get_int( "Min Standards at End" );
	int min_between = parameter_manager.get_int( "Min Standards between Deviants" );

	# Make sure there are enough trials to meet the restrictions
	int set_aside_stds = min_start + min_end + ( dev_trials * min_between );
	int remaining_stds = std_trials - set_aside_stds;
	if ( remaining_stds < 0 ) then
		exit( "There are not enough standard trials to create a legal sequence with the current settings." );
	end;
	
	# First we'll build a short sequence that ensures there are 
	# enough targets between each distractor. For every distractor 
	# we add "min_between" targets
	array<int> distractor_seq[min_between + 1];
	distractor_seq.fill( 1, 0, STD_IDX, 0 );
	distractor_seq[distractor_seq.count()] = DEV_IDX;

	# Set up a sequence of targets at the start
	array<int> start_seq[min_start];
	start_seq.fill( 1, 0, STD_IDX, 0 );

	# Set up a sequence of targets at the end
	array<int> end_seq[min_end];
	if ( min_end > 0 ) then
		end_seq.fill( 1, 0, STD_IDX, 0 );
	end;

	# Now build a temporary tgt/dist sequence.
	# This will get "expanded" later because for each distractor that
	# comes up, we'll add in "min_between" targets preceding it
	array<int> temp_seq[remaining_stds + dev_trials];
	temp_seq.fill( 1, 0, DEV_IDX, 0 );
	temp_seq.fill( 1, remaining_stds, STD_IDX, 0 );
	temp_seq.shuffle();

	# Now build the actual sequence. Add the initial target sequence, 
	# then add in the temp sequence that contains the distractors, 
	# then add in the final target sequence at the end
	trial_sequence.append( start_seq );
	loop
		int i = 1
	until
		i > temp_seq.count()
	begin
		if ( temp_seq[i] == STD_IDX ) then
			trial_sequence.add( STD_IDX );
		else
			trial_sequence.append( distractor_seq );
		end;
		i = i + 1;
	end;
	trial_sequence.append( end_seq );
end;

# --- Video setup ---

# Grab the videos
bool show_vids = parameter_manager.get_bool( "Show Videos" );
bool preload_vids = parameter_manager.get_bool( "Preload Videos" );
/*array<video> my_vids[0];
parameter_manager.get_videos( "Video Files", my_vids );*/

/*if ( show_vids ) then
	# Exit if they didn't specify a video
	if ( my_vids.count() == 0 ) then
		exit( "You must specify at least one video in 'Video Files'" );
	end;
	
	# Initialize some values
	bool use_audio = parameter_manager.get_bool( "Use Audio from Video" );
	double vid_height = parameter_manager.get_double( "Video Height" );
	double vid_width = parameter_manager.get_double( "Video Width" );

	# Prepare the videos and set the audio if requested
	loop
		int i = 1
	until
		i > my_vids.count()
	begin
		my_vids[i].set_use_audio( use_audio );
		if ( vid_height > 0.0 ) then
			my_vids[i].set_height( vid_height );
		end;
		if ( vid_width > 0.0 ) then
			my_vids[i].set_width( vid_width );
		end;
		if ( preload_vids ) then
			my_vids[i].prepare();
		end;
		i = i + 1;
	end;
end;*/

# --- Main Sequence --- #

string instructions = get_lang_item( lang, "Instructions" );
if ( !show_vids ) then
	instructions = get_lang_item( lang, "No Video Instructions" );
end;

# Get the ISI
array<int> ISI_range[0];
parameter_manager.get_ints( "ISI Range", ISI_range );
if ( ISI_range.count() != 2 ) then
	exit( "You must specify exactly two values in 'ISI Range'" );
end;

# Get the port codes
array<int> port_codes[2];
port_codes[STD_IDX] = parameter_manager.get_int( "Standard Port Code" );
port_codes[DEV_IDX] = parameter_manager.get_int( "Deviant Port Code" );

# Get the event codes
array<string> event_codes[2];
event_codes[STD_IDX] = STD_COND;
event_codes[DEV_IDX] = DEV_COND;

# Prepare a video if necessary
/*if ( show_vids ) then
	my_vids[1].prepare();
end;*/

# Show the instructions
present_instructions( instructions );
ready_set_go();

# Start the video running
/*if ( show_vids ) then
	show_video( my_vids, 1 );
else
	ISI_pic.present();
end;*/

# Loop to present trial sequence
loop
	array<int> ctrs[2] = { 1,1 };
	bool next_prepared = false;
	int vid_ctr = 1;
	int i = 1
until
	i > trial_sequence.count()
begin
	# Check if this video is still playing, and play the
	# subsequent video if there is one, and increment the ctr
	if ( show_vids ) then
		/*if ( !my_vids[vid_ctr].playing() ) && ( vid_ctr < my_vids.count() ) then
			vid_ctr = vid_ctr + 1;
			show_video( my_vids, vid_ctr );
			next_prepared = false;
		end;*/
	end;
	
	# Check whether std or deviant
	int this_stim = trial_sequence[i];
	
	# Set the ISI
	trial_refresh_fix( ISI_trial, random( ISI_range[1], ISI_range[2] ) );
	
	# Set the ISI duration and the stimulus
	stim_event.set_stimulus( stim_snds[this_stim] );
	
	# Set the port code; we add a special prefix for the first stimulus presentation
	int p_code = port_codes[this_stim];
	if ( i <= min_start ) then
		p_code = p_code + 100;
	end;
	stim_event.set_port_code( p_code );
	
	# Set the event code
	stim_event.set_event_code(
		STIM_EVENT_CODE + ";" +
		string( i ) + ";" +
		string( ctrs[this_stim] ) + ";" +
		event_codes[this_stim] + ";" +
		string( p_code ) + ";" +
		string( ISI_trial.duration() )
	);
	
	# Present the trial
	stim_trial.present();
	
	# Use some ISI time to prepare the next video if necessary
	/*if ( show_vids ) then
		if ( !next_prepared ) && ( !preload_vids ) then
			int start = clock.time();
			if ( vid_ctr < my_vids.count() ) then
				my_vids[vid_ctr + 1].prepare();
			end;
			next_prepared = true;
			int ttime = clock.time() - start;
			if ( ttime < ISI_trial.duration() ) then
				ISI_trial.set_duration( ISI_trial.duration() - ttime );
			else
				ISI_trial.set_duration( ISI_trial.STIMULI_LENGTH );
			end;
		end;
	end;*/

	# Show the ISI
	ISI_trial.present();

	ctrs[this_stim] = ctrs[this_stim] + 1;
	i = i + 1;
end;
present_instructions( get_lang_item( lang, "Completion Screen Caption" ) );