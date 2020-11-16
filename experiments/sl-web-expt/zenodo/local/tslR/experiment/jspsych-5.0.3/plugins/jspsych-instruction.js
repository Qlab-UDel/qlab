 /* jspsych-back-button.js
 * An Nguyen
 *
 * This plugin allows user to go back to the previous trial
 * Use it to show back-button, provide performance feedback, etc...
 *
 * 
 *
 */

jsPsych.plugins.back-button = (function() {

  var plugin = {};

  plugin.trial = function(display_element, trial) {
  
    trial.key_correct = '1';
    trial.key_incorrect = '0';	
    trial.key_forward = trial.key_forward || 'rightarrow';
    trial.key_backward = trial.key_backward || 'leftarrow';
    trial.allow_backward = (typeof trial.allow_backward === 'undefined') ? true : trial.allow_backward;
    trial.allow_keys = (typeof trial.allow_keys === 'undefined') ? true : trial.allow_keys;
    trial.show_clickable_nav = (typeof trial.show_clickable_nav === 'undefined') ? false : trial.show_clickable_nav;

    // if any trial variables are functions
    // this evaluates the function and replaces
    // it with the output of the function
    trial = jsPsych.pluginAPI.evaluateFunctionParameters(trial);

    var current_page = 0;

    var view_history = [];
           var responses = [];
    var current_stim = "";


    var start_time = (new Date()).getTime();

    var last_page_update_time = start_time;

    function show_current_page() {
      display_element.html(trial.pages[current_page]);
	current_stim = trial.pages[(current_page-1)];

      if (trial.show_clickable_nav) {

        var nav_html = "<div class='jspsych-back-button-nav'>";
        if (current_page != 0 && trial.allow_backward) {
          nav_html += "<button id='jspsych-back-button-back' class='jspsych-btn'>&lt; Previous</button>";
        }
        nav_html += "<button id='jspsych-back-button-next' class='jspsych-btn'>Next &gt;</button></div>"

        display_element.append(nav_html);

        if (current_page != 0 && trial.allow_backward) {
          $('#jspsych-back-button-back').on('click', function() {
            clear_button_handlers();
            back();
          });
        }

        $('#jspsych-back-button-next').on('click', function() {
          clear_button_handlers();
          next();
        });

      }

    }

    function clear_button_handlers() {
      $('#jspsych-back-button-next').off('click');
      $('#jspsych-back-button-back').off('click');
    }

    function next() {

      add_current_page_to_view_history()

      current_page++;

      // if done, finish up...
      if (current_page >= trial.pages.length) {
        endTrial();
      } else {
        show_current_page();
      }

      // record when image was shown
      //animation_sequence.push({
        //"stimulus": current_stim,
        //"time": (new Date()).getTime() - startTime
      //});
    }

    function back() {

      add_current_page_to_view_history()

      current_page--;

      show_current_page();
    }

    function add_current_page_to_view_history() {

      var current_time = (new Date()).getTime();

      var page_view_time = current_time - last_page_update_time;

      view_history.push({
        page_index: current_page,
        viewing_time: page_view_time
      });

      last_page_update_time = current_time;
    }
    
    

    function endTrial() {

      if (trial.allow_keys) {
        jsPsych.pluginAPI.cancelKeyboardResponse(keyboard_listener);
      }

      display_element.html('');
      var trial_data = {
        "responses": JSON.stringify(responses)
      };
      jsPsych.finishTrial(trial_data);
  
    }

    var after_response = function(info) {

      // have to reinitialize this instead of letting it persist to prevent accidental skips of pages by holding down keys too long
      keyboard_listener = jsPsych.pluginAPI.getKeyboardResponse({
        callback_function: after_response,
        valid_responses: [trial.key_forward, trial.key_backward,trial.key_correct,trial.key_incorrect],
        rt_method: 'date',
        persist: false,
        allow_held_key: false
      });
      // check if key is forwards or backwards and update page
      if (info.key === trial.key_backward || info.key === jsPsych.pluginAPI.convertKeyCharacterToKeyCode(trial.key_backward)) {
        if (current_page !== 0 && trial.allow_backward) {
          back();
        }
      }
     

      if (info.key === trial.key_forward || info.key === trial.key_correct || info.key === trial.key_incorrect || info.key === jsPsych.pluginAPI.convertKeyCharacterToKeyCode(trial.key_correct) || info.key === jsPsych.pluginAPI.convertKeyCharacterToKeyCode(trial.key_incorrect) || info.key === jsPsych.pluginAPI.convertKeyCharacterToKeyCode(trial.key_forward)) {
        next();
      }
      
       responses.push({
        key_press: info.key,
        rt: info.rt,
        stimulus: current_stim, 
      });
    var trdata = {"responses": JSON.stringify(responses)};
   
      jsPsych.data.write(responses)


    };

    show_current_page();

    if (trial.allow_keys) {
      var keyboard_listener = jsPsych.pluginAPI.getKeyboardResponse({
        callback_function: after_response,
        valid_responses: [trial.key_forward, trial.key_backward,trial.key_correct,trial.key_incorrect],
        rt_method: 'date',
        persist: false
      });
    }
  };

  return plugin;
})();
