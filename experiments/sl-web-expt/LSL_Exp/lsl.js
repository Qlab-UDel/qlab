
  var par_id = {
    type: 'survey-text',
    questions: ['Enter your participant ID'],
    timing_post_trial: 1000
    };

   String.prototype.format = function () {
    var i = 0, args = arguments;
    return this.replace(/{}/g, function () {
        return typeof args[i] != 'undefined' ? args[i++] : '';
    });
    };
	var cond_assign = jsPsych.randomization.sample(['lang1','lang2'],1)[0];
	var datetime = jsPsych.startTime();
	var rand_targ = ['F','B','H','G'];
	var rand_targ2 = ['A','C','E','H'];
		
	var pick_targ = function(targType) {
                    return targType[Math.floor(Math.random()*targType.length)];}
					
	if (cond_assign === 'lang1') {
		var target = pick_targ(rand_targ);
	} else if (cond_assign === 'lang2') {
		var target = pick_targ(rand_targ2);}
	
	/* define instructions block */
	  var instr1 = {
    type: 'single-audio',
    stimulus: 'sound/lsl_instr1.wav',
    prompt: "<p><center>Parts of the experiment require that you press the spacebar to continue. Please remember to always listen to and read the instructions completely before pressing the spacebar.</center></p> ",
    choices: ['space'],
    timing_response: -1,
    response_ends_trial: true
  };
	
	var instr2 = {
    type: 'single-audio',
    stimulus: 'sound/lsl_instr2.wav',
      prompt: "<p><center>Hi there! We're going to watch a parade today.</center></p> ",
    choices: ['space'],
    timing_response: -1,
    response_ends_trial: true
};

	var instr3 = {
		type: 'single-audio',
		stimulus: 'sound/lsl_instr3.wav',
		  prompt: "<p><center>This is Klaptoo!</center></p> <img src='../tone_images/klaptoo.png' style='position:fixed;top:20%;left:42%;'>",
		choices: ['space'],
		timing_response: -1,
		response_ends_trial: true
	};

	var instr4 = {
		type: 'single-audio',
		stimulus: 'sound/lsl_instr4.wav',
		  prompt: "<p>Klaptoo is going to hold up signs for the parade. We need you to help us keep track of his favorite sign. We'll show you Klaptoo's favorite sign now.</p><img src='../tone_images/klaptoo.png' style='position:fixed;top:20%;left:42%;'>",
		choices: ['space'],
		timing_response: -1,
		response_ends_trial: true
	};
		
    var target_image = 'image/{}.png'.format(target)
   
    var targ = {
	  type: 'single-stim',
	  stimulus: target_image,
	  choices: ['space'],
	  timing_response: -1,
	  response_ends_trial: true
	};
	
	   
	var instr5a = {
		type: 'single-audio',
		stimulus: 'sound/lsl_instr5a.wav',
		prompt: "<p>Klaptoo is going to show you many signs now. Remember, this is the special sign to keep track of. </p>",
		choices: ['space'],
		timing_response: -1,
		response_ends_trial: true
	};
	
	var instr5b = {
		type: 'single-audio',
		stimulus: 'sound/lsl_instr5b.wav',
		prompt: "<p>Klaptoo will show you one sign at a time on the screen. To keep track of Klaptoo's favorite sign, press the spacebar whenever you see it.</p>",
		choices: ['space'],
		timing_response: -1,
		response_ends_trial: true
	};

	
	
	//reading the image file
   	
    	function textFileToArray(filename)
	{
   	 var reader = (window.XMLHttpRequest != null ) 
               ? new XMLHttpRequest() 
               : new ActiveXObject("Microsoft.XMLHTTP");
    	 reader.open("GET", filename, false );
   	 reader.send( );
   	 return reader.responseText.split('\n'); 
	}
	
	var blank = 'image/blank.png';
	//check condition
	if (cond_assign === 'lang1') {
		var image = textFileToArray('S_fam_seq_1.txt');}
	else if (cond_assign === 'lang2') {
		var image = textFileToArray('S_fam_seq_2.txt');}
		
		
	//putting the sound file into the experimental block
	var trials = [];
	for (var i = 0; i < image.length; i++) {
		trials.push(image[i])
		trials.push(blank);
	}


	var block = {
	  type: 'animation',
	  stimuli: trials,
	  frame_time: 400,
	  choices: ['space']
	}


	var instr6 = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr6.wav',
	    prompt: "<p><center>Great job! Now we have a new task for you. Be sure to pay attention to the instructions.</center></p>",
	    choices: ['space'],
	    timing_response: -1,
	    response_ends_trial: true
	};
	
	var instr7 = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr7.wav',
	      prompt: "<p><center>Sometimes Klaptoo always showed some signs together.</center></p> <img src='image/line_of_letters.png' style='position:fixed;top:30%;left:10%;'>",
	    choices: ['space'],
	    timing_response: -1,
	    response_ends_trial: true
	};	    

	var instr8 = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr8.wav',
	    prompt: "<p><center>Look carefully below. Can you see three signs that always go together?</center></p> <img src='image/line_of_letters.png' style='position:fixed;top:30%;left:10%;'>",
	    choices: ['space'],
	    timing_response: -1,
	    response_ends_trial: true
	    };
            var instr9 = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr9.wav',
	    prompt: "<p><center>Some signs never went together</center></p> <img src='image/line_of_letters.png' style='position:fixed;top:30%;left:10%;'>",
	    choices: ['space'],
	    timing_response: -1,
	    response_ends_trial: true
	    };

            var instr10 = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr10.wav',
	    prompt: "<p><center>We are going to ask you if you remember which groups of signs Klaptoo usually showed together during the parade.</center></p> <img src='image/line_of_letters.png' style='position:fixed;top:30%;left:10%;'>",
	    choices: ['space'],
	    timing_response: -1,
	    response_ends_trial: true
	    }
	    
	    var instr11a = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr11a.wav',
	    prompt: "<p><center>For example, we might ask if Klaptoo always showed this group of signs together: </center></p> <img src='image/good_triplet.png' style='position:fixed;top:20%;left:35%;'>",
	    choices: ['space'],
	    timing_response: -1,
	    response_ends_trial: true
	    }
	    
	    var instr11b = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr11b.wav',
	    prompt: "<p><center>...or if he always showed this group of signs together: </center></p> <img src='image/bad_triplet.png' style='position:fixed;top:20%;left:35%;'>",
	    choices: ['space'],
	    timing_response: -1,
	    response_ends_trial: true
	    }
	    
	        var instr12 = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr12.wav',
	    prompt: "<p><center>Klaptoo is going to show you signs one at a time. The first three will belong to one group of signs that might have been shown together, and the last three will belong to another group of signs that might have been shown together. Your job is to decide which of the two groups Klaptoo always showed together during the parade. </center></p>",
	    choices: ['space'],
	    timing_response: -1,
	    response_ends_trial: true
	    }


	//load all the img files for task 2    
	var img = [];
	img['1'] = 'image/A.png';
	img['2'] = 'image/B.png';
	img['3'] = 'image/C.png';
	img['4'] = 'image/D.png';
	img['5'] = 'image/E.png';
	img['6'] = 'image/F.png';
	img['7'] = 'image/G.png';
	img['8'] = 'image/H.png';
	img['9'] = 'image/J.png';
	img['10'] = 'image/K.png';
	img['11'] = 'image/L.png';
	img['12'] = 'image/M.png';
	img['14'] = 'image/blank.png';

	if (cond_assign === 'lang1') {
	var forced_test = [14,1, 9, [6,0], 1, 10, 7, 13, 5, 11, [8,0], 12, 3, 8, 13, 12, 10, [2,0], 1, 10, 7, 13, 5, 9, [2,0], 5, 11, 8, 13, 12, 3, [8,0], 5, 11, 8, 13, 1, 9, [6,0], 12, 3, 8, 13, 4, 3, [7,0], 4, 11, 6, 13, 12, 3, [8,0], 4, 3, 7, 13, 5, 9, [2,0], 12, 10, 2, 13, 12, 3, [8,0], 12, 10, 2, 13, 5, 11, [8,0], 4, 11, 6, 13, 1, 10, [7,0], 1, 9, 6, 13, 5, 11, [8,0], 5, 9, 2, 13, 4, 3, [7,0], 5, 9, 2, 13, 1, 10, [7,0], 12, 10, 2, 13, 1, 10, [7,0], 5, 11, 8, 13, 12, 10, [2,0], 5, 9, 2, 13, 4, 3, [7,0], 12, 3, 8, 13, 5, 11, [8,0], 1, 10, 7, 13, 1, 9, [6,0], 4, 11, 6, 13, 5, 9, [2,0], 1, 9, 6, 13, 4, 3, [7,0], 1, 10, 7, 13, 12, 3, [8,0], 1, 9, 6, 13, 4, 11, [6,0], 1, 9, 6, 13, 1, 9, [6,0], 5, 9, 2, 13, 5, 9, [2,0], 4, 3, 7, 13, 4, 11, [6,0], 12, 10, 2, 13, 1, 10, [7,0], 4, 3, 7, 13, 12, 10, [2,0], 12, 3, 8, 13, 4, 11, [6,0], 4, 3, 7, 13, 4, 11, [6,0], 5, 11, 8, 13, 12, 10, [2,0], 4, 11, 6, 13]}
	else if (cond_assign === 'lang2') {
	var forced_test = [14,6, 10, [3,0], 6, 9, 8, 13, 6, 10, [3,0], 7, 4, 5, 13, 6, 10, [3,0], 12, 2, 3, 13, 6, 10, [3,0], 11, 10, 1, 13, 7, 9, [1,0], 6, 9, 8, 13, 7, 9, [1,0], 7, 4, 5, 13, 7, 9, [1,0], 12, 2, 3, 13, 7, 9, [1,0], 11, 10, 1, 13, 12, 4, [8,0], 6, 9, 8, 13, 12, 4, [8,0], 7, 4, 5, 13, 12, 4, [8,0], 12, 2, 3, 13, 12, 4, [8,0], 11, 10, 1, 13, 11, 2, [5,0], 6, 9, 8, 13, 11, 2, [5,0], 7, 4, 5, 13, 11, 2, [5,0], 12, 2, 3, 13, 11, 2, [5,0], 11, 10, 1, 13, 6, 9, [8,0], 6, 10, 3, 13, 7, 4, [5,0], 6, 10, 3, 13, 12, 2, [3,0], 6, 10, 3, 13, 11, 10, [1,0], 6, 10, 3, 13, 6, 9, [8,0], 7, 9, 1, 13, 7, 4, [5,0], 7, 9, 1, 13, 12, 2, [3,0], 7, 9, 1, 13, 11, 10, [1,0], 7, 9, 1, 13, 6, 9, [8,0], 12, 4, 8, 13, 7, 4, [5,0], 12, 4, 8, 13, 12, 2, [3,0], 12, 4, 8, 13, 11, 10, [1,0], 12, 4, 8, 13, 6, 9, [8,0], 11, 2, 5, 13, 7, 4, [5,0], 11, 2, 5, 13, 12, 2, [3,0], 11, 2, 5, 13, 11, 10, [1,0], 11, 2, 5, 13]}

var img_block_2 = [];
	for (ii=0; ii<forced_test.length; ii++) {
	    if (ii !== 0 && forced_test[ii] === 13) {
	        img_block_2.push({
	      	 'stimulus': 'image/white.png',
	                          'prompt': "<p><center>Which group went together? Press 1 for first and 2 for second.</center></p>",
	                          'choices': ['1','2'],
	                          'timing_response': 1600000000,
	                          'timing_post_trial': 200,
	                          'response_ends_trial': true});
	    } else if (ii === 0) {
	        img_block_2.push({'stimulus': 'image/white.png',
	        'prompt': '',
	                          'choices': ['1','2'],
	                          'timing_response': 200,
	                          'timing_post_trial': 200,
	                          'response_ends_trial': false});
	
	    } else if (forced_test[ii][1] === 0){
	        img_block_2.push({'stimulus':img[forced_test[ii][0]],
	                          'response_ends_trial': false,
	                          'timing_response': 460,
	                          'timing_post_trial': 1000});
	
	    } else {
	        img_block_2.push({'stimulus':img[forced_test[ii]],
				  'response_ends_trial': false,
				  'timing_response': 660,
				  'timing_post_trial': 100});
	
	   }
	}
		
	var send_time = {
	    type: 'call-function',
	    func: function () {var datetime = jsPsych.startTime(); return datetime;}
	};


	var forced_choice_block = {
	    type: 'single-stim',
	    timeline: img_block_2,
	    timing_response: 360,
	    timing_post_trial: 20,
	    response_ends_trial: false
	}
	
	var end = {
	    type: 'single-audio',
	    stimulus: 'sound/lsl_instr13.wav',
	    prompt: "Great, you're all done! Thank you :) Press any key to exit.",
	    cont_key: ['space'],
	}

		
var datajson = jsPsych.data.dataAsCSV();


	
	jsPsych.data.addProperties({
	        cond: cond_assign,
	        targ: '{}'.format(target),
	        ts: datetime
	});
	
	function saveData(filename, filedata){
	   $.ajax({
	      type:'post',
	      cache: false,
	      url: '../expf/deep/local_data_save.php', // this is the path to the above PHP script
	      data: {filename: filename, filedata: filedata}
	   });
	}

  /* create experiment timeline array */
  var timeline = [];
  timeline.push(par_id);
  timeline.push(instr1);
  timeline.push(instr2);
  timeline.push(instr3);
  timeline.push(instr4);
  timeline.push(targ);
  timeline.push(instr5a);
  timeline.push(targ);
  timeline.push(instr5b);
  timeline.push(block);
  timeline.push(instr6);
  timeline.push(instr7);
  timeline.push(instr8);
  timeline.push(instr9);
  timeline.push(instr10);
  timeline.push(instr11a);
  timeline.push(instr11b);
  timeline.push(forced_choice_block);
  timeline.push(end);
  
	

  /* start the experiment */


  jsPsych.init({
    timeline: timeline,
      fullscreen: true,
   on_finish: function save_data(datajson){
    saveData("{}_lsl.csv".format(jsPsych.data.getTrialsOfType('survey-text')[0].responses.match(/[a-zA-Z0-9]/g).join('').split(/Q0/)[1]), jsPsych.data.dataAsCSV()); 
    var data_table = "lsl_table";
    $.ajax({
        type:'post',
        cache: false,
        url: '../savedata.php',
        data: {
            table: data_table,
            json: JSON.stringify(datajson)
       },
       success: function(output) { console.log(output); }
     });
    
   
       }

});
