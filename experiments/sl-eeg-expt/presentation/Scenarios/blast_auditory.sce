# -------------------------- Header Parameters --------------------------

scenario = "blast_auditory";

write_codes = EXPARAM( "Send Port Codes" );

screen_width_distance = EXPARAM( "Display Width" );
screen_height_distance = EXPARAM( "Display Height" );
screen_distance = EXPARAM( "Viewing Distance" );

default_background_color = EXPARAM( "Background Color" );
default_font = EXPARAM( "Non-Stimulus Font" );
default_font_size = EXPARAM( "Non-Stimulus Font Size" );
default_text_color = EXPARAM( "Non-Stimulus Font Color" );

active_buttons = 2;
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
	monitor_videos = false;
	stimulus_event {
		sound {
			wavefile {
				preload = false;
			};
		};
	} stim_event;
} stim_trial;


bitmap { filename = "C:\\Users\\qlabu\\Documents\\experiments\\eeg_exp\\blast\\blast_auditory\\Stimuli\\robots1.bmp" ;} robot;
trial {
	trial_type = specific_response;
	terminator_button = 1;
	trial_duration = forever;
	
	picture{
		bitmap robot;
		x=0;y=-2;
		text { 
			caption = "rest";
			preload = false;
		} instruct_text;
		x = 0; 
		y = 4;
	} instruct_pic;
} instruct_trial;
	
trial {
	monitor_videos = false;

	stimulus_event {
		picture {} ISI_pic;
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

string VIDEO_CODE = "Video";

string CHARACTER_WRAP = "Character";


# --- Set up fixed stimulus parameters ---

string language = parameter_manager.get_string( "Language" );
language_file lang = load_language_file( scenario_directory + language + ".xml" );
bool char_wrap = ( get_lang_item( lang, "Word Wrap Mode" ).lower() == CHARACTER_WRAP.lower() );
double font_size = parameter_manager.get_double( "Non-Stimulus Font Size" );

# --- Stimulus setup ---

if ( parameter_manager.get_bool( "Show Fixation Point" ) ) then
	ISI_pic.add_part( fix_ellipse, 0, 0 );
end;


# Make some sounds
array<sound> stim_snds[0];
parameter_manager.get_sounds("Sound", stim_snds);

# Make events
array<string> event_code[0];
parameter_manager.get_strings("Event", event_code);
# --- sub present_instructions ---

sub
	present_instructions( string instruct_string )
begin
	full_size_word_wrap( instruct_string, font_size, char_wrap, instruct_text );
	instruct_trial.present();
	default.present();
end;

# --- sub ready_set_go ---

int ready_dur = parameter_manager.get_int( "Ready-Set-Go Duration" );
trial_refresh_fix( ready_trial, ready_dur );

array<string> ready_caps[3];
ready_caps[1] = get_lang_item( lang, "Ready Caption" );
ready_caps[2] = get_lang_item( lang, "Set Caption" );
ready_caps[3] = get_lang_item( lang, "Go Caption" );

sub
	ready_set_go
begin
	if ( ready_dur > 0 ) then
		loop
			int i = 1
		until
			i > ready_caps.count()
		begin
			full_size_word_wrap( ready_caps[i], font_size, char_wrap, ready_text );
			ready_trial.present();
			i = i + 1;
		end;
	end;
end;

# --- sub show_video ---

sub
	show_video( array<video,1>& vids, int vid_number )
begin
	video_player.play( vids[vid_number], VIDEO_CODE + string( vid_number ) );
end;

# --- Video setup ---

# Grab the videos
bool show_vids = parameter_manager.get_bool( "Show Video" );
bool preload_vids = parameter_manager.get_bool( "Preload Video" );
array<video> my_vids[0];
parameter_manager.get_videos( "Video Files", my_vids );

if ( show_vids ) then
	# Exit if they didn't specify a video
	if ( my_vids.count() == 0 ) then
		exit( "Error: At least one video must be specified in 'Video Files'" );
	end;
	
	# Initialize some values
	bool use_audio = false;
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
end;

# --- Main Sequence --- #

string instructions = get_lang_item( lang, "Instructions" );
if ( !show_vids ) then
	instructions = get_lang_item( lang, "No Video Instructions" );
end;

# Get the ISI
array<int> ISI_range[0];
parameter_manager.get_ints( "ISI Range", ISI_range );
if ( ISI_range.count() != 2 ) then
	exit( "Error: Two values must be specified in 'ISI Range'" );
end;

# Prepare a video if necessary
if ( show_vids ) then
	my_vids[1].prepare();
end;

# Show the instructions
present_instructions( instructions );
ready_set_go();

# Start the video running
if ( show_vids ) then
	show_video( my_vids, 1 );
else
	ISI_pic.present();
end;

# Loop to present trial sequence
loop
	array<int> ctrs[2] = { 1,1 };
	bool next_prepared = false;
	int vid_ctr = 1;
	int i = 1
until
	i > stim_snds.count()
begin
	# Check if this video is still playing, and play the
	# subsequent video if there is one, and increment the ctr
	if ( show_vids ) then
		if ( !my_vids[vid_ctr].playing() ) && ( vid_ctr < my_vids.count() ) then
			vid_ctr = vid_ctr + 1;
			show_video( my_vids, vid_ctr );
			next_prepared = false;
		end;
	end;
	

	
	# Set the ISI
	trial_refresh_fix( ISI_trial, random( ISI_range[1], ISI_range[2] ) );
	
	# Set the ISI duration and the stimulus
	stim_event.set_stimulus(stim_snds[i]);
	
		
	# Set the event code
	stim_event.set_event_code(event_code[i]);
	
	# Present the trial
	stim_trial.present();
	
	# Use some ISI time to prepare the next video if necessary
	if ( show_vids ) then
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
	end;

	# Show the ISI
	ISI_trial.present();
	i = i + 1

end;

# Stop any currently playing video
loop
	int i = 1
until
	i > my_vids.count()
begin
	if ( my_vids[i].playing() ) then
		video_player.stop( my_vids[i] );
	end;
	i = i + 1;
end;

# Show the exit screen
present_instructions( get_lang_item( lang, "Completion Screen Caption" ) );