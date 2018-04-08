#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Wed Apr 26 09:23:33 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'visual'  # from the Builder filename that created this script
expInfo = {u'ltarget': u'',u'vtarget': u'', u'PartID': u''} # block: R(andom) and S(equential); language: 1 or 2; target: if language 1, then bi, pu, du, da; if block 2, then ku, tu, pi, do.
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['Run'] = "3"
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['PartID'], expName, expInfo['Run'])
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'grey', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess



# Initialize components for Routine "start"
startClock = core.Clock()
start_text = visual.TextStim(win=win, ori=0, name='start_text',
    text=u"Are you ready? Let's get started!",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "vreminder"
vreminderClock = core.Clock()
vreminder_image = visual.ImageStim(win=win, name='vreminder_image',
    image=u'Alien%s.BMP' % str(expInfo['vtarget']), mask=None,
    ori=0, pos=[0, -0.3], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
vreminder_text = visual.TextStim(win=win, ori=0, name='vreminder_text',
    text='Press the button when you see this!',    font='Arial',
    pos=[0, .2], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
vreminder_sound = sound.Sound(u'reminder.wav', secs=-1)
vreminder_sound.setVolume(1)


# Initialize components for Routine "lreminder"
lreminderClock = core.Clock()
lreminder_image = visual.ImageStim(win=win, name='lreminder_image',
    image='%s.png' % str(expInfo['ltarget']), mask=None,
    ori=0, pos=[0, -0.3], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
lreminder_text = visual.TextStim(win=win, ori=0, name='lreminder_text',
    text='Press the button when you see this!',    font='Arial',
    pos=[-.0, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
lreminder_sound = sound.Sound(u'reminder.wav', secs=-1)
lreminder_sound.setVolume(1)

# Initialize components for Routine "l_block_trial"
l_block_trialClock = core.Clock()
l_block_trial_image = visual.ImageStim(win=win, name='l_block_trial_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
l_block_trial_blank = visual.ImageStim(win=win, name='l_block_trial_blank',
    image=u'blanka.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)



# Initialize components for Routine "v_block_trial"
v_block_trialClock = core.Clock()
v_block_trial_image = visual.ImageStim(win=win, name='v_block_trial_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
blank_image = visual.ImageStim(win=win, name='blank_image',
    image=u'blank.PNG', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "instr6"
instr6Clock = core.Clock()
instr6_sound = sound.Sound(u'lsl_instr6.wav', secs=-1)
instr6_sound.setVolume(1)
instr6_text = visual.TextStim(win=win, ori=0, name='instr6_text',
    text=u'Great job! Now we have a new task for you. Be sure to pay attention to the instructions.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instr7"
instr7Clock = core.Clock()
instr7_sound = sound.Sound(u'lsl_instr7.wav', secs=-1)
instr7_sound.setVolume(1)
instr7_text = visual.TextStim(win=win, ori=0, name='instr7_text',
    text=u'Sometimes Klaptoo always showed some signs together.',    font=u'Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
instr7_image = visual.ImageStim(win=win, name='instr7_image',
    image=u'line_of_letters.png', mask=None,
    ori=0, pos=[0, -0.8], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr8"
instr8Clock = core.Clock()
instr8_sound = sound.Sound(u'lsl_instr8.wav', secs=-1)
instr8_sound.setVolume(1)
instr8_text = visual.TextStim(win=win, ori=0, name='instr8_text',
    text=u'Look carefully below. Can you see three signs that always go together?',    font=u'Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
instr8_image = visual.ImageStim(win=win, name='instr8_image',
    image=u'line_of_letters.png', mask=None,
    ori=0, pos=[0, -0.8], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr9"
instr9Clock = core.Clock()
instr9_sound = sound.Sound(u'lsl_instr9.wav', secs=-1)
instr9_sound.setVolume(1)
instr9_text = visual.TextStim(win=win, ori=0, name='instr9_text',
    text=u'Some signs never went together.',    font=u'Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
instr9_image = visual.ImageStim(win=win, name='instr9_image',
    image=u'line_of_letters.png', mask=None,
    ori=0, pos=[0, -0.8], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr10"
instr10Clock = core.Clock()
instr10_sound = sound.Sound(u'lsl_instr10.wav', secs=-1)
instr10_sound.setVolume(1)
instr10_text = visual.TextStim(win=win, ori=0, name='instr10_text',
    text=u'We are going to ask you if you remember which groups of signs Klaptoo usually showed together during the parade.',    font=u'Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
instr10_image = visual.ImageStim(win=win, name='instr10_image',
    image=u'line_of_letters.png', mask=None,
    ori=0, pos=[0, -0.8], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr11"
instr11Clock = core.Clock()
instr11_sound = sound.Sound(u'lsl_instr11.wav', secs=-1)
instr11_sound.setVolume(1)
instr11_text1 = visual.TextStim(win=win, ori=0, name='instr11_text1',
    text=u'For example, we might ask if Klaptoo always showed this group of signs together:',    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
instr11_image1 = visual.ImageStim(win=win, name='instr11_image1',
    image=u'good_triplet.png', mask=None,
    ori=0, pos=[0, 0.35], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr11_text2 = visual.TextStim(win=win, ori=0, name='instr11_text2',
    text=u'or if he always showed this group of signs together:',    font=u'Arial',
    pos=[0, 0.05], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-3.0)
instr11_image2 = visual.ImageStim(win=win, name='instr11_image2',
    image=u'bad_triplet.png', mask=None,
    ori=0, pos=[0, -0.35], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
instr11_image3 = visual.ImageStim(win=win, name='instr11_image3',
    image=u'line_of_letters.png', mask=None,
    ori=0, pos=[0, -0.8], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "instr12"
instr12Clock = core.Clock()
instr12_sound = sound.Sound(u'lsl_instr12.wav', secs=-1)
instr12_sound.setVolume(1)
instr12_text = visual.TextStim(win=win, ori=0, name='instr12_text',
    text=u'Klaptoo is going to show you signs one at a time. The first three will belong to one group of signs that might have been shown together, and the last three will belong to another group of signs that might have been shown together. Your job is to decide which of the two groups Klaptoo always showed together during the parade.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "test1"
test1Clock = core.Clock()
test1_image = visual.ImageStim(win=win, name='test1_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test1_blank = visual.ImageStim(win=win, name='test1_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "test2"
test2Clock = core.Clock()
test2_image = visual.ImageStim(win=win, name='test2_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test2_blank = visual.ImageStim(win=win, name='test2_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "test3"
test3Clock = core.Clock()
test3_image = visual.ImageStim(win=win, name='test3_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test3_blank = visual.ImageStim(win=win, name='test3_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "triplet_pause"
triplet_pauseClock = core.Clock()
triplet_pause_image = visual.ImageStim(win=win, name='triplet_pause_image',
    image=u'white.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "test4"
test4Clock = core.Clock()
test4_image = visual.ImageStim(win=win, name='test4_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test4_blank = visual.ImageStim(win=win, name='test4_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "test5"
test5Clock = core.Clock()
test5_image = visual.ImageStim(win=win, name='test5_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test5_blank = visual.ImageStim(win=win, name='test5_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "test6"
test6Clock = core.Clock()
test6_image = visual.ImageStim(win=win, name='test6_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test6_blank = visual.ImageStim(win=win, name='test6_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "question"
questionClock = core.Clock()
question_text = visual.TextStim(win=win, ori=0, name='question_text',
    text=u'Which group went together? Press the green button for first and red button for second.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "blank_block_trial"
blank_block_trialClock = core.Clock()
blank_block_trial_image = visual.ImageStim(win=win, name='blank_block_trial_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 



#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
start_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
start_key_resp.status = NOT_STARTED
# keep track of which components have finished
startComponents = []
startComponents.append(start_text)
startComponents.append(start_key_resp)
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "start"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text* updates
    if t >= 0.0 and start_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_text.tStart = t  # underestimates by a little under one frame
        start_text.frameNStart = frameN  # exact frame index
        start_text.setAutoDraw(True)
    
    # *start_key_resp* updates
    if t >= 0.0 and start_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_key_resp.tStart = t  # underestimates by a little under one frame
        start_key_resp.frameNStart = frameN  # exact frame index
        start_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(start_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if start_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            start_key_resp.keys = theseKeys[-1]  # just the last key pressed
            start_key_resp.rt = start_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


#------Prepare to start Routine "lreminder"-------
t = 0
lreminderClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
lreminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
lreminder_key_resp.status = NOT_STARTED
# keep track of which components have finished
lreminderComponents = []
lreminderComponents.append(lreminder_sound)

for thisComponent in lreminderComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "lreminder"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = lreminderClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
     
    # *lreminder_image* updates
    if t >= 0.0 and lreminder_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_image.tStart = t  # underestimates by a little under one frame
        lreminder_image.frameNStart = frameN  # exact frame index
        lreminder_image.draw()
        
    # *lreminder_text* updates
    if t >= 0.0 and lreminder_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_text.tStart = t  # underestimates by a little under one frame
        lreminder_text.frameNStart = frameN  # exact frame index
        lreminder_text.draw()


    # start/stop lreminder_sound
    if t >= 0.0 and lreminder_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_sound.tStart = t  # underestimates by a little under one frame
        lreminder_sound.frameNStart = frameN  # exact frame index
        lreminder_sound.play()  # start the sound (it finishes automatically)
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lreminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "lreminder"-------
for thisComponent in lreminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
lreminder_sound.stop() #ensure sound has stopped at end of routine
# the Routine "lreminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




# set up handler to look after randomisation of conditions etc
l_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visual_run3_1.xlsx'),
    seed=None, name='l_block_trial_loop')
thisExp.addLoop(l_block_trial_loop)  # add the loop to the experiment
thisL_block_trial_loop = l_block_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisL_block_trial_loop.rgb)
if thisL_block_trial_loop != None:
    for paramName in thisL_block_trial_loop.keys():
        exec(paramName + '= thisL_block_trial_loop.' + paramName)

for thisL_block_trial_loop in l_block_trial_loop:
    currentLoop = l_block_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisL_block_trial_loop.rgb)
    if thisL_block_trial_loop != None:
        for paramName in thisL_block_trial_loop.keys():
            exec(paramName + '= thisL_block_trial_loop.' + paramName)
    
#------Prepare to start Routine "l_block_trial"-------
    t = 0
    l_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    l_block_trial_image.setImage(image)
    
    l_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    l_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    l_block_trialComponents = []
    l_block_trialComponents.append(l_block_trial_image)
    l_block_trialComponents.append(l_block_trial_blank)
    l_block_trialComponents.append(l_block_trial_key_resp)
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "l_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = l_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *l_block_trial_image* updates
        if t >= 0.0 and l_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_image.tStart = t  # underestimates by a little under one frame
            l_block_trial_image.frameNStart = frameN  # exact frame index
            l_block_trial_image.setAutoDraw(True)
        if l_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_image.setAutoDraw(False)
        
        # *l_block_trial_blank* updates
        if t >= 0.79 and l_block_trial_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_blank.tStart = t  # underestimates by a little under one frame
            l_block_trial_blank.frameNStart = frameN  # exact frame index
            l_block_trial_blank.setAutoDraw(True)
        if l_block_trial_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_blank.setAutoDraw(False)
        
        # *l_block_trial_key_resp* updates
        if t >= 0.0 and l_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            l_block_trial_key_resp.frameNStart = frameN  # exact frame index
            l_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(l_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if l_block_trial_key_resp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_key_resp.status = STOPPED
        if l_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                l_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                l_block_trial_key_resp.rt = l_block_trial_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in l_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "l_block_trial"-------
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if l_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       l_block_trial_key_resp.keys=None
    # store data for l_block_trial_loop (TrialHandler)
    l_block_trial_loop.addData('l_block_trial_key_resp.keys',l_block_trial_key_resp.keys)
    if l_block_trial_key_resp.keys != None:  # we had a response
        l_block_trial_loop.addData('l_block_trial_key_resp.rt', l_block_trial_key_resp.rt)
    thisExp.nextEntry()


# set up handler to look after randomisation of conditions etc
blank_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'blank1.xlsx'),
    seed=None, name='blank_block_trial_loop')
thisExp.addLoop(blank_block_trial_loop)  # add the loop to the experiment
thisBlank_block_trial_loop = blank_block_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlank_block_trial_loop.rgb)
if thisBlank_block_trial_loop != None:
    for paramName in thisBlank_block_trial_loop.keys():
        exec(paramName + '= thisBlank_block_trial_loop.' + paramName)

for thisBlank_block_trial_loop in blank_block_trial_loop:
    currentLoop = blank_block_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlank_block_trial_loop.rgb)
    if thisBlank_block_trial_loop != None:
        for paramName in thisBlank_block_trial_loop.keys():
            exec(paramName + '= thisBlank_block_trial_loop.' + paramName)
    
#------Prepare to start Routine "blank_block_trial"-------
    t = 0
    blank_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    blank_block_trial_image.setImage(image)
    blank_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    blank_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    blank_block_trialComponents = []
    blank_block_trialComponents.append(blank_block_trial_image)
    blank_block_trialComponents.append(blank_block_trial_key_resp)
    for thisComponent in blank_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "blank_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_block_trial_image* updates
        if t >= 0.0 and blank_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_block_trial_image.tStart = t  # underestimates by a little under one frame
            blank_block_trial_image.frameNStart = frameN  # exact frame index
            blank_block_trial_image.setAutoDraw(True)
        if blank_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_block_trial_image.setAutoDraw(False)
        
        
        # *blank_block_trial_key_resp* updates
        if t >= 0.0 and blank_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            blank_block_trial_key_resp.frameNStart = frameN  # exact frame index
            blank_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(blank_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if blank_block_trial_key_resp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_block_trial_key_resp.status = STOPPED
        if blank_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                blank_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                blank_block_trial_key_resp.rt = blank_block_trial_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "blank_block_trial"-------
    for thisComponent in blank_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if blank_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       blank_block_trial_key_resp.keys=None
    # store data for blank_block_trial_loop (TrialHandler)
    blank_block_trial_loop.addData('blank_block_trial_key_resp.keys',blank_block_trial_key_resp.keys)
    if blank_block_trial_key_resp.keys != None:  # we had a response
        blank_block_trial_loop.addData('blank_block_trial_key_resp.rt', blank_block_trial_key_resp.rt)
    thisExp.nextEntry()


#------Prepare to start Routine "vreminder"-------
t = 0
vreminderClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
vreminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
vreminder_key_resp.status = NOT_STARTED
# keep track of which components have finished
vreminderComponents = []
vreminderComponents.append(vreminder_sound)

for thisComponent in vreminderComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "vreminder"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = vreminderClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
     
    # *vreminder_image* updates
    if t >= 0.0 and vreminder_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_image.tStart = t  # underestimates by a little under one frame
        vreminder_image.frameNStart = frameN  # exact frame index
        vreminder_image.draw()
        
    # *vreminder_text* updates
    if t >= 0.0 and vreminder_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_text.tStart = t  # underestimates by a little under one frame
        vreminder_text.frameNStart = frameN  # exact frame index
        vreminder_text.draw()


    # start/stop vreminder_sound
    if t >= 0.0 and vreminder_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_sound.tStart = t  # underestimates by a little under one frame
        vreminder_sound.frameNStart = frameN  # exact frame index
        vreminder_sound.play()  # start the sound (it finishes automatically)
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vreminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "vreminder"-------
for thisComponent in vreminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
vreminder_sound.stop() #ensure sound has stopped at end of routine
# the Routine "vreminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

 
# set up handler to look after randomisation of conditions etc
v_block_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visual_run3_2.xlsx'),
    seed=None, name='v_block_trials')
thisExp.addLoop(v_block_trials)  # add the loop to the experiment
thisV_block_trial = v_block_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisV_block_trial.rgb)
if thisV_block_trial != None:
    for paramName in thisV_block_trial.keys():
        exec(paramName + '= thisV_block_trial.' + paramName)

for thisV_block_trial in v_block_trials:
    currentLoop = v_block_trials
    # abbreviate parameter names if possible (e.g. rgb = thisV_block_trial.rgb)
    if thisV_block_trial != None:
        for paramName in thisV_block_trial.keys():
            exec(paramName + '= thisV_block_trial.' + paramName)
    
    #------Prepare to start Routine "v_block_trial"-------
    t = 0
    v_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    v_block_trial_image.setImage(image)
    v_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    v_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    v_block_trialComponents = []
    v_block_trialComponents.append(v_block_trial_image)
    v_block_trialComponents.append(v_block_trial_key_resp)
    v_block_trialComponents.append(blank_image)
    for thisComponent in v_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "v_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = v_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *v_block_trial_image* updates
        if t >= 0.0 and v_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            v_block_trial_image.tStart = t  # underestimates by a little under one frame
            v_block_trial_image.frameNStart = frameN  # exact frame index
            v_block_trial_image.setAutoDraw(True)
        if v_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            v_block_trial_image.setAutoDraw(False)
        
        # *v_block_trial_key_resp* updates
        if t >= 0.0 and v_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            v_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            v_block_trial_key_resp.frameNStart = frameN  # exact frame index
            v_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(v_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if v_block_trial_key_resp.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            v_block_trial_key_resp.status = STOPPED
        if v_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                v_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                v_block_trial_key_resp.rt = v_block_trial_key_resp.clock.getTime()
        
        # *blank_image* updates
        if t >= 0.8 and blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_image.tStart = t  # underestimates by a little under one frame
            blank_image.frameNStart = frameN  # exact frame index
            blank_image.setAutoDraw(True)
        if blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in v_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "v_block_trial"-------
    for thisComponent in v_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if v_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       v_block_trial_key_resp.keys=None
    # store data for v_block_trials (TrialHandler)
    v_block_trials.addData('v_block_trial_key_resp.keys',v_block_trial_key_resp.keys)
    if v_block_trial_key_resp.keys != None:  # we had a response
        v_block_trials.addData('v_block_trial_key_resp.rt', v_block_trial_key_resp.rt)
    thisExp.nextEntry()
    

    
#------Prepare to start Routine "lreminder"-------
t = 0
lreminderClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
lreminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
lreminder_key_resp.status = NOT_STARTED
# keep track of which components have finished
lreminderComponents = []
lreminderComponents.append(lreminder_sound)

for thisComponent in lreminderComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "lreminder"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = lreminderClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
     
    # *lreminder_image* updates
    if t >= 0.0 and lreminder_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_image.tStart = t  # underestimates by a little under one frame
        lreminder_image.frameNStart = frameN  # exact frame index
        lreminder_image.draw()
        
    # *lreminder_text* updates
    if t >= 0.0 and lreminder_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_text.tStart = t  # underestimates by a little under one frame
        lreminder_text.frameNStart = frameN  # exact frame index
        lreminder_text.draw()


    # start/stop lreminder_sound
    if t >= 0.0 and lreminder_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_sound.tStart = t  # underestimates by a little under one frame
        lreminder_sound.frameNStart = frameN  # exact frame index
        lreminder_sound.play()  # start the sound (it finishes automatically)
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lreminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "lreminder"-------
for thisComponent in lreminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
lreminder_sound.stop() #ensure sound has stopped at end of routine
# the Routine "lreminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




# set up handler to look after randomisation of conditions etc
l_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visual_run3_3_1.xlsx'),
    seed=None, name='l_block_trial_loop')
thisExp.addLoop(l_block_trial_loop)  # add the loop to the experiment
thisL_block_trial_loop = l_block_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisL_block_trial_loop.rgb)
if thisL_block_trial_loop != None:
    for paramName in thisL_block_trial_loop.keys():
        exec(paramName + '= thisL_block_trial_loop.' + paramName)

for thisL_block_trial_loop in l_block_trial_loop:
    currentLoop = l_block_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisL_block_trial_loop.rgb)
    if thisL_block_trial_loop != None:
        for paramName in thisL_block_trial_loop.keys():
            exec(paramName + '= thisL_block_trial_loop.' + paramName)
    
#------Prepare to start Routine "l_block_trial"-------
    t = 0
    l_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    l_block_trial_image.setImage(image)
    
    l_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    l_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    l_block_trialComponents = []
    l_block_trialComponents.append(l_block_trial_image)
    l_block_trialComponents.append(l_block_trial_blank)
    l_block_trialComponents.append(l_block_trial_key_resp)
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "l_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = l_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *l_block_trial_image* updates
        if t >= 0.0 and l_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_image.tStart = t  # underestimates by a little under one frame
            l_block_trial_image.frameNStart = frameN  # exact frame index
            l_block_trial_image.setAutoDraw(True)
        if l_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_image.setAutoDraw(False)
        
        # *l_block_trial_blank* updates
        if t >= 0.79 and l_block_trial_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_blank.tStart = t  # underestimates by a little under one frame
            l_block_trial_blank.frameNStart = frameN  # exact frame index
            l_block_trial_blank.setAutoDraw(True)
        if l_block_trial_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_blank.setAutoDraw(False)
        
        # *l_block_trial_key_resp* updates
        if t >= 0.0 and l_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            l_block_trial_key_resp.frameNStart = frameN  # exact frame index
            l_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(l_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if l_block_trial_key_resp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_key_resp.status = STOPPED
        if l_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                l_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                l_block_trial_key_resp.rt = l_block_trial_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in l_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "l_block_trial"-------
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if l_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       l_block_trial_key_resp.keys=None
    # store data for l_block_trial_loop (TrialHandler)
    l_block_trial_loop.addData('l_block_trial_key_resp.keys',l_block_trial_key_resp.keys)
    if l_block_trial_key_resp.keys != None:  # we had a response
        l_block_trial_loop.addData('l_block_trial_key_resp.rt', l_block_trial_key_resp.rt)
    thisExp.nextEntry()


# set up handler to look after randomisation of conditions etc
blank_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'blank1.xlsx'),
    seed=None, name='blank_block_trial_loop')
thisExp.addLoop(blank_block_trial_loop)  # add the loop to the experiment
thisBlank_block_trial_loop = blank_block_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlank_block_trial_loop.rgb)
if thisBlank_block_trial_loop != None:
    for paramName in thisBlank_block_trial_loop.keys():
        exec(paramName + '= thisBlank_block_trial_loop.' + paramName)

for thisBlank_block_trial_loop in blank_block_trial_loop:
    currentLoop = blank_block_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlank_block_trial_loop.rgb)
    if thisBlank_block_trial_loop != None:
        for paramName in thisBlank_block_trial_loop.keys():
            exec(paramName + '= thisBlank_block_trial_loop.' + paramName)
    
#------Prepare to start Routine "blank_block_trial"-------
    t = 0
    blank_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    blank_block_trial_image.setImage(image)
    blank_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    blank_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    blank_block_trialComponents = []
    blank_block_trialComponents.append(blank_block_trial_image)
    blank_block_trialComponents.append(blank_block_trial_key_resp)
    for thisComponent in blank_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "blank_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_block_trial_image* updates
        if t >= 0.0 and blank_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_block_trial_image.tStart = t  # underestimates by a little under one frame
            blank_block_trial_image.frameNStart = frameN  # exact frame index
            blank_block_trial_image.setAutoDraw(True)
        if blank_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_block_trial_image.setAutoDraw(False)
        
        
        # *blank_block_trial_key_resp* updates
        if t >= 0.0 and blank_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            blank_block_trial_key_resp.frameNStart = frameN  # exact frame index
            blank_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(blank_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if blank_block_trial_key_resp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_block_trial_key_resp.status = STOPPED
        if blank_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                blank_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                blank_block_trial_key_resp.rt = blank_block_trial_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "blank_block_trial"-------
    for thisComponent in blank_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if blank_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       blank_block_trial_key_resp.keys=None
    # store data for blank_block_trial_loop (TrialHandler)
    blank_block_trial_loop.addData('blank_block_trial_key_resp.keys',blank_block_trial_key_resp.keys)
    if blank_block_trial_key_resp.keys != None:  # we had a response
        blank_block_trial_loop.addData('blank_block_trial_key_resp.rt', blank_block_trial_key_resp.rt)
    thisExp.nextEntry()



# set up handler to look after randomisation of conditions etc
l_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visual_run3_3_2.xlsx'),
    seed=None, name='l_block_trial_loop')
thisExp.addLoop(l_block_trial_loop)  # add the loop to the experiment
thisL_block_trial_loop = l_block_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisL_block_trial_loop.rgb)
if thisL_block_trial_loop != None:
    for paramName in thisL_block_trial_loop.keys():
        exec(paramName + '= thisL_block_trial_loop.' + paramName)

for thisL_block_trial_loop in l_block_trial_loop:
    currentLoop = l_block_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisL_block_trial_loop.rgb)
    if thisL_block_trial_loop != None:
        for paramName in thisL_block_trial_loop.keys():
            exec(paramName + '= thisL_block_trial_loop.' + paramName)
    
#------Prepare to start Routine "l_block_trial"-------
    t = 0
    l_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    l_block_trial_image.setImage(image)
    
    l_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    l_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    l_block_trialComponents = []
    l_block_trialComponents.append(l_block_trial_image)
    l_block_trialComponents.append(l_block_trial_blank)
    l_block_trialComponents.append(l_block_trial_key_resp)
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "l_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = l_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *l_block_trial_image* updates
        if t >= 0.0 and l_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_image.tStart = t  # underestimates by a little under one frame
            l_block_trial_image.frameNStart = frameN  # exact frame index
            l_block_trial_image.setAutoDraw(True)
        if l_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_image.setAutoDraw(False)
        
        # *l_block_trial_blank* updates
        if t >= 0.79 and l_block_trial_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_blank.tStart = t  # underestimates by a little under one frame
            l_block_trial_blank.frameNStart = frameN  # exact frame index
            l_block_trial_blank.setAutoDraw(True)
        if l_block_trial_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_blank.setAutoDraw(False)
        
        # *l_block_trial_key_resp* updates
        if t >= 0.0 and l_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            l_block_trial_key_resp.frameNStart = frameN  # exact frame index
            l_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(l_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if l_block_trial_key_resp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_key_resp.status = STOPPED
        if l_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                l_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                l_block_trial_key_resp.rt = l_block_trial_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in l_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "l_block_trial"-------
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if l_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       l_block_trial_key_resp.keys=None
    # store data for l_block_trial_loop (TrialHandler)
    l_block_trial_loop.addData('l_block_trial_key_resp.keys',l_block_trial_key_resp.keys)
    if l_block_trial_key_resp.keys != None:  # we had a response
        l_block_trial_loop.addData('l_block_trial_key_resp.rt', l_block_trial_key_resp.rt)
    thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
blank_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'blank1.xlsx'),
    seed=None, name='blank_block_trial_loop')
thisExp.addLoop(blank_block_trial_loop)  # add the loop to the experiment
thisBlank_block_trial_loop = blank_block_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlank_block_trial_loop.rgb)
if thisBlank_block_trial_loop != None:
    for paramName in thisBlank_block_trial_loop.keys():
        exec(paramName + '= thisBlank_block_trial_loop.' + paramName)

for thisBlank_block_trial_loop in blank_block_trial_loop:
    currentLoop = blank_block_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlank_block_trial_loop.rgb)
    if thisBlank_block_trial_loop != None:
        for paramName in thisBlank_block_trial_loop.keys():
            exec(paramName + '= thisBlank_block_trial_loop.' + paramName)
    
#------Prepare to start Routine "blank_block_trial"-------
    t = 0
    blank_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    blank_block_trial_image.setImage(image)
    blank_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    blank_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    blank_block_trialComponents = []
    blank_block_trialComponents.append(blank_block_trial_image)
    blank_block_trialComponents.append(blank_block_trial_key_resp)
    for thisComponent in blank_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "blank_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_block_trial_image* updates
        if t >= 0.0 and blank_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_block_trial_image.tStart = t  # underestimates by a little under one frame
            blank_block_trial_image.frameNStart = frameN  # exact frame index
            blank_block_trial_image.setAutoDraw(True)
        if blank_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_block_trial_image.setAutoDraw(False)
        
        
        # *blank_block_trial_key_resp* updates
        if t >= 0.0 and blank_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            blank_block_trial_key_resp.frameNStart = frameN  # exact frame index
            blank_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(blank_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if blank_block_trial_key_resp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_block_trial_key_resp.status = STOPPED
        if blank_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                blank_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                blank_block_trial_key_resp.rt = blank_block_trial_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "blank_block_trial"-------
    for thisComponent in blank_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if blank_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       blank_block_trial_key_resp.keys=None
    # store data for blank_block_trial_loop (TrialHandler)
    blank_block_trial_loop.addData('blank_block_trial_key_resp.keys',blank_block_trial_key_resp.keys)
    if blank_block_trial_key_resp.keys != None:  # we had a response
        blank_block_trial_loop.addData('blank_block_trial_key_resp.rt', blank_block_trial_key_resp.rt)
    thisExp.nextEntry()



# set up handler to look after randomisation of conditions etc
l_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visual_run3_3_3.xlsx'),
    seed=None, name='l_block_trial_loop')
thisExp.addLoop(l_block_trial_loop)  # add the loop to the experiment
thisL_block_trial_loop = l_block_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisL_block_trial_loop.rgb)
if thisL_block_trial_loop != None:
    for paramName in thisL_block_trial_loop.keys():
        exec(paramName + '= thisL_block_trial_loop.' + paramName)

for thisL_block_trial_loop in l_block_trial_loop:
    currentLoop = l_block_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisL_block_trial_loop.rgb)
    if thisL_block_trial_loop != None:
        for paramName in thisL_block_trial_loop.keys():
            exec(paramName + '= thisL_block_trial_loop.' + paramName)
    
#------Prepare to start Routine "l_block_trial"-------
    t = 0
    l_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    l_block_trial_image.setImage(image)
    
    l_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    l_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    l_block_trialComponents = []
    l_block_trialComponents.append(l_block_trial_image)
    l_block_trialComponents.append(l_block_trial_blank)
    l_block_trialComponents.append(l_block_trial_key_resp)
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "l_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = l_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *l_block_trial_image* updates
        if t >= 0.0 and l_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_image.tStart = t  # underestimates by a little under one frame
            l_block_trial_image.frameNStart = frameN  # exact frame index
            l_block_trial_image.setAutoDraw(True)
        if l_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_image.setAutoDraw(False)
        
        # *l_block_trial_blank* updates
        if t >= 0.79 and l_block_trial_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_blank.tStart = t  # underestimates by a little under one frame
            l_block_trial_blank.frameNStart = frameN  # exact frame index
            l_block_trial_blank.setAutoDraw(True)
        if l_block_trial_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_blank.setAutoDraw(False)
        
        # *l_block_trial_key_resp* updates
        if t >= 0.0 and l_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            l_block_trial_key_resp.frameNStart = frameN  # exact frame index
            l_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(l_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if l_block_trial_key_resp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_key_resp.status = STOPPED
        if l_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                l_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                l_block_trial_key_resp.rt = l_block_trial_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in l_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "l_block_trial"-------
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if l_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       l_block_trial_key_resp.keys=None
    # store data for l_block_trial_loop (TrialHandler)
    l_block_trial_loop.addData('l_block_trial_key_resp.keys',l_block_trial_key_resp.keys)
    if l_block_trial_key_resp.keys != None:  # we had a response
        l_block_trial_loop.addData('l_block_trial_key_resp.rt', l_block_trial_key_resp.rt)
    thisExp.nextEntry()
    
#------Prepare to start Routine "vreminder"-------
t = 0
vreminderClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
vreminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
vreminder_key_resp.status = NOT_STARTED
# keep track of which components have finished
vreminderComponents = []
vreminderComponents.append(vreminder_sound)

for thisComponent in vreminderComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "vreminder"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = vreminderClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
     
    # *vreminder_image* updates
    if t >= 0.0 and vreminder_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_image.tStart = t  # underestimates by a little under one frame
        vreminder_image.frameNStart = frameN  # exact frame index
        vreminder_image.draw()
        
    # *vreminder_text* updates
    if t >= 0.0 and vreminder_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_text.tStart = t  # underestimates by a little under one frame
        vreminder_text.frameNStart = frameN  # exact frame index
        vreminder_text.draw()


    # start/stop vreminder_sound
    if t >= 0.0 and vreminder_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_sound.tStart = t  # underestimates by a little under one frame
        vreminder_sound.frameNStart = frameN  # exact frame index
        vreminder_sound.play()  # start the sound (it finishes automatically)
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vreminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "vreminder"-------
for thisComponent in vreminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
vreminder_sound.stop() #ensure sound has stopped at end of routine
# the Routine "vreminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

 
# set up handler to look after randomisation of conditions etc
v_block_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visual_run3_4.xlsx'),
    seed=None, name='v_block_trials')
thisExp.addLoop(v_block_trials)  # add the loop to the experiment
thisV_block_trial = v_block_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisV_block_trial.rgb)
if thisV_block_trial != None:
    for paramName in thisV_block_trial.keys():
        exec(paramName + '= thisV_block_trial.' + paramName)

for thisV_block_trial in v_block_trials:
    currentLoop = v_block_trials
    # abbreviate parameter names if possible (e.g. rgb = thisV_block_trial.rgb)
    if thisV_block_trial != None:
        for paramName in thisV_block_trial.keys():
            exec(paramName + '= thisV_block_trial.' + paramName)
    
    #------Prepare to start Routine "v_block_trial"-------
    t = 0
    v_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    v_block_trial_image.setImage(image)
    v_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    v_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    v_block_trialComponents = []
    v_block_trialComponents.append(v_block_trial_image)
    v_block_trialComponents.append(v_block_trial_key_resp)
    v_block_trialComponents.append(blank_image)
    for thisComponent in v_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "v_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = v_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *v_block_trial_image* updates
        if t >= 0.0 and v_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            v_block_trial_image.tStart = t  # underestimates by a little under one frame
            v_block_trial_image.frameNStart = frameN  # exact frame index
            v_block_trial_image.setAutoDraw(True)
        if v_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            v_block_trial_image.setAutoDraw(False)
        
        # *v_block_trial_key_resp* updates
        if t >= 0.0 and v_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            v_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            v_block_trial_key_resp.frameNStart = frameN  # exact frame index
            v_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(v_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if v_block_trial_key_resp.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            v_block_trial_key_resp.status = STOPPED
        if v_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                v_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                v_block_trial_key_resp.rt = v_block_trial_key_resp.clock.getTime()
        
        # *blank_image* updates
        if t >= 0.8 and blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_image.tStart = t  # underestimates by a little under one frame
            blank_image.frameNStart = frameN  # exact frame index
            blank_image.setAutoDraw(True)
        if blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in v_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "v_block_trial"-------
    for thisComponent in v_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if v_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       v_block_trial_key_resp.keys=None
    # store data for v_block_trials (TrialHandler)
    v_block_trials.addData('v_block_trial_key_resp.keys',v_block_trial_key_resp.keys)
    if v_block_trial_key_resp.keys != None:  # we had a response
        v_block_trials.addData('v_block_trial_key_resp.rt', v_block_trial_key_resp.rt)
    thisExp.nextEntry()
    
    

#------Prepare to start Routine "lreminder"-------
t = 0
lreminderClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
lreminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
lreminder_key_resp.status = NOT_STARTED
# keep track of which components have finished
lreminderComponents = []
lreminderComponents.append(lreminder_sound)

for thisComponent in lreminderComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "lreminder"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = lreminderClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
     
    # *lreminder_image* updates
    if t >= 0.0 and lreminder_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_image.tStart = t  # underestimates by a little under one frame
        lreminder_image.frameNStart = frameN  # exact frame index
        lreminder_image.draw()
        
    # *lreminder_text* updates
    if t >= 0.0 and lreminder_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_text.tStart = t  # underestimates by a little under one frame
        lreminder_text.frameNStart = frameN  # exact frame index
        lreminder_text.draw()


    # start/stop lreminder_sound
    if t >= 0.0 and lreminder_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        lreminder_sound.tStart = t  # underestimates by a little under one frame
        lreminder_sound.frameNStart = frameN  # exact frame index
        lreminder_sound.play()  # start the sound (it finishes automatically)
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lreminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "lreminder"-------
for thisComponent in lreminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
lreminder_sound.stop() #ensure sound has stopped at end of routine
# the Routine "lreminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




# set up handler to look after randomisation of conditions etc
l_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visual_run3_5.xlsx'),
    seed=None, name='l_block_trial_loop')
thisExp.addLoop(l_block_trial_loop)  # add the loop to the experiment
thisL_block_trial_loop = l_block_trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisL_block_trial_loop.rgb)
if thisL_block_trial_loop != None:
    for paramName in thisL_block_trial_loop.keys():
        exec(paramName + '= thisL_block_trial_loop.' + paramName)

for thisL_block_trial_loop in l_block_trial_loop:
    currentLoop = l_block_trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisL_block_trial_loop.rgb)
    if thisL_block_trial_loop != None:
        for paramName in thisL_block_trial_loop.keys():
            exec(paramName + '= thisL_block_trial_loop.' + paramName)
    
#------Prepare to start Routine "l_block_trial"-------
    t = 0
    l_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    l_block_trial_image.setImage(image)
    
    l_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    l_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    l_block_trialComponents = []
    l_block_trialComponents.append(l_block_trial_image)
    l_block_trialComponents.append(l_block_trial_blank)
    l_block_trialComponents.append(l_block_trial_key_resp)
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "l_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = l_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *l_block_trial_image* updates
        if t >= 0.0 and l_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_image.tStart = t  # underestimates by a little under one frame
            l_block_trial_image.frameNStart = frameN  # exact frame index
            l_block_trial_image.setAutoDraw(True)
        if l_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_image.setAutoDraw(False)
        
        # *l_block_trial_blank* updates
        if t >= 0.79 and l_block_trial_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_blank.tStart = t  # underestimates by a little under one frame
            l_block_trial_blank.frameNStart = frameN  # exact frame index
            l_block_trial_blank.setAutoDraw(True)
        if l_block_trial_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_blank.setAutoDraw(False)
        
        # *l_block_trial_key_resp* updates
        if t >= 0.0 and l_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            l_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            l_block_trial_key_resp.frameNStart = frameN  # exact frame index
            l_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(l_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if l_block_trial_key_resp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            l_block_trial_key_resp.status = STOPPED
        if l_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                l_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                l_block_trial_key_resp.rt = l_block_trial_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in l_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "l_block_trial"-------
    for thisComponent in l_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if l_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       l_block_trial_key_resp.keys=None
    # store data for l_block_trial_loop (TrialHandler)
    l_block_trial_loop.addData('l_block_trial_key_resp.keys',l_block_trial_key_resp.keys)
    if l_block_trial_key_resp.keys != None:  # we had a response
        l_block_trial_loop.addData('l_block_trial_key_resp.rt', l_block_trial_key_resp.rt)
    thisExp.nextEntry()



#------Prepare to start Routine "vreminder"-------
t = 0
vreminderClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
vreminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
vreminder_key_resp.status = NOT_STARTED
# keep track of which components have finished
vreminderComponents = []
vreminderComponents.append(vreminder_sound)

for thisComponent in vreminderComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "vreminder"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = vreminderClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
     
    # *vreminder_image* updates
    if t >= 0.0 and vreminder_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_image.tStart = t  # underestimates by a little under one frame
        vreminder_image.frameNStart = frameN  # exact frame index
        vreminder_image.draw()
        
    # *vreminder_text* updates
    if t >= 0.0 and vreminder_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_text.tStart = t  # underestimates by a little under one frame
        vreminder_text.frameNStart = frameN  # exact frame index
        vreminder_text.draw()


    # start/stop vreminder_sound
    if t >= 0.0 and vreminder_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        vreminder_sound.tStart = t  # underestimates by a little under one frame
        vreminder_sound.frameNStart = frameN  # exact frame index
        vreminder_sound.play()  # start the sound (it finishes automatically)
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in vreminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "vreminder"-------
for thisComponent in vreminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
vreminder_sound.stop() #ensure sound has stopped at end of routine
# the Routine "vreminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

 
# set up handler to look after randomisation of conditions etc
v_block_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visual_run3_6.xlsx'),
    seed=None, name='v_block_trials')
thisExp.addLoop(v_block_trials)  # add the loop to the experiment
thisV_block_trial = v_block_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisV_block_trial.rgb)
if thisV_block_trial != None:
    for paramName in thisV_block_trial.keys():
        exec(paramName + '= thisV_block_trial.' + paramName)

for thisV_block_trial in v_block_trials:
    currentLoop = v_block_trials
    # abbreviate parameter names if possible (e.g. rgb = thisV_block_trial.rgb)
    if thisV_block_trial != None:
        for paramName in thisV_block_trial.keys():
            exec(paramName + '= thisV_block_trial.' + paramName)
    
    #------Prepare to start Routine "v_block_trial"-------
    t = 0
    v_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    v_block_trial_image.setImage(image)
    v_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    v_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    v_block_trialComponents = []
    v_block_trialComponents.append(v_block_trial_image)
    v_block_trialComponents.append(v_block_trial_key_resp)
    v_block_trialComponents.append(blank_image)
    for thisComponent in v_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "v_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = v_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *v_block_trial_image* updates
        if t >= 0.0 and v_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            v_block_trial_image.tStart = t  # underestimates by a little under one frame
            v_block_trial_image.frameNStart = frameN  # exact frame index
            v_block_trial_image.setAutoDraw(True)
        if v_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            v_block_trial_image.setAutoDraw(False)
        
        # *v_block_trial_key_resp* updates
        if t >= 0.0 and v_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            v_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            v_block_trial_key_resp.frameNStart = frameN  # exact frame index
            v_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(v_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if v_block_trial_key_resp.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            v_block_trial_key_resp.status = STOPPED
        if v_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                v_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                v_block_trial_key_resp.rt = v_block_trial_key_resp.clock.getTime()
        
        # *blank_image* updates
        if t >= 0.8 and blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_image.tStart = t  # underestimates by a little under one frame
            blank_image.frameNStart = frameN  # exact frame index
            blank_image.setAutoDraw(True)
        if blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in v_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "v_block_trial"-------
    for thisComponent in v_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if v_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       v_block_trial_key_resp.keys=None
    # store data for v_block_trials (TrialHandler)
    v_block_trials.addData('v_block_trial_key_resp.keys',v_block_trial_key_resp.keys)
    if v_block_trial_key_resp.keys != None:  # we had a response
        v_block_trials.addData('v_block_trial_key_resp.rt', v_block_trial_key_resp.rt)
    thisExp.nextEntry()
    
    


#------Prepare to start Routine "instr6"-------
t = 0
instr6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr6_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr6_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr6Components = []
instr6Components.append(instr6_sound)
instr6Components.append(instr6_text)
instr6Components.append(instr6_key_resp)
for thisComponent in instr6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop instr6_sound
    if t >= 0.0 and instr6_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr6_sound.tStart = t  # underestimates by a little under one frame
        instr6_sound.frameNStart = frameN  # exact frame index
        instr6_sound.play()  # start the sound (it finishes automatically)
    
    # *instr6_text* updates
    if t >= 0.0 and instr6_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr6_text.tStart = t  # underestimates by a little under one frame
        instr6_text.frameNStart = frameN  # exact frame index
        instr6_text.setAutoDraw(True)
    
    # *instr6_key_resp* updates
    if t >= 0.0 and instr6_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr6_key_resp.tStart = t  # underestimates by a little under one frame
        instr6_key_resp.frameNStart = frameN  # exact frame index
        instr6_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr6_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr6_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr6_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr6_key_resp.rt = instr6_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr6"-------
for thisComponent in instr6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr6_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr7"-------
t = 0
instr7Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr7_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr7_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr7Components = []
instr7Components.append(instr7_sound)
instr7Components.append(instr7_text)
instr7Components.append(instr7_image)
instr7Components.append(instr7_key_resp)
for thisComponent in instr7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr7"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop instr7_sound
    if t >= 0.0 and instr7_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr7_sound.tStart = t  # underestimates by a little under one frame
        instr7_sound.frameNStart = frameN  # exact frame index
        instr7_sound.play()  # start the sound (it finishes automatically)
    
    # *instr7_text* updates
    if t >= 0.0 and instr7_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr7_text.tStart = t  # underestimates by a little under one frame
        instr7_text.frameNStart = frameN  # exact frame index
        instr7_text.setAutoDraw(True)
    
    # *instr7_image* updates
    if t >= 0.0 and instr7_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr7_image.tStart = t  # underestimates by a little under one frame
        instr7_image.frameNStart = frameN  # exact frame index
        instr7_image.setAutoDraw(True)
    
    # *instr7_key_resp* updates
    if t >= 0.0 and instr7_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr7_key_resp.tStart = t  # underestimates by a little under one frame
        instr7_key_resp.frameNStart = frameN  # exact frame index
        instr7_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr7_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr7_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr7_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr7_key_resp.rt = instr7_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr7"-------
for thisComponent in instr7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr7_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr8"-------
t = 0
instr8Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr8_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr8_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr8Components = []
instr8Components.append(instr8_sound)
instr8Components.append(instr8_text)
instr8Components.append(instr8_image)
instr8Components.append(instr8_key_resp)
for thisComponent in instr8Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr8"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr8Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop instr8_sound
    if t >= 0.0 and instr8_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr8_sound.tStart = t  # underestimates by a little under one frame
        instr8_sound.frameNStart = frameN  # exact frame index
        instr8_sound.play()  # start the sound (it finishes automatically)
    
    # *instr8_text* updates
    if t >= 0.0 and instr8_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr8_text.tStart = t  # underestimates by a little under one frame
        instr8_text.frameNStart = frameN  # exact frame index
        instr8_text.setAutoDraw(True)
    
    # *instr8_image* updates
    if t >= 0.0 and instr8_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr8_image.tStart = t  # underestimates by a little under one frame
        instr8_image.frameNStart = frameN  # exact frame index
        instr8_image.setAutoDraw(True)
    
    # *instr8_key_resp* updates
    if t >= 0.0 and instr8_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr8_key_resp.tStart = t  # underestimates by a little under one frame
        instr8_key_resp.frameNStart = frameN  # exact frame index
        instr8_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr8_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr8_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr8_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr8_key_resp.rt = instr8_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr8"-------
for thisComponent in instr8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr8_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr9"-------
t = 0
instr9Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr9_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr9_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr9Components = []
instr9Components.append(instr9_sound)
instr9Components.append(instr9_text)
instr9Components.append(instr9_image)
instr9Components.append(instr9_key_resp)
for thisComponent in instr9Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr9"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr9Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop instr9_sound
    if t >= 0.0 and instr9_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr9_sound.tStart = t  # underestimates by a little under one frame
        instr9_sound.frameNStart = frameN  # exact frame index
        instr9_sound.play()  # start the sound (it finishes automatically)
    
    # *instr9_text* updates
    if t >= 0.0 and instr9_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr9_text.tStart = t  # underestimates by a little under one frame
        instr9_text.frameNStart = frameN  # exact frame index
        instr9_text.setAutoDraw(True)
    
    # *instr9_image* updates
    if t >= 0.0 and instr9_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr9_image.tStart = t  # underestimates by a little under one frame
        instr9_image.frameNStart = frameN  # exact frame index
        instr9_image.setAutoDraw(True)
    
    # *instr9_key_resp* updates
    if t >= 0.0 and instr9_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr9_key_resp.tStart = t  # underestimates by a little under one frame
        instr9_key_resp.frameNStart = frameN  # exact frame index
        instr9_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr9_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr9_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr9_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr9_key_resp.rt = instr9_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr9"-------
for thisComponent in instr9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr9_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr10"-------
t = 0
instr10Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr10_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr10_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr10Components = []
instr10Components.append(instr10_sound)
instr10Components.append(instr10_text)
instr10Components.append(instr10_image)
instr10Components.append(instr10_key_resp)
for thisComponent in instr10Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr10"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr10Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop instr10_sound
    if t >= 0.0 and instr10_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr10_sound.tStart = t  # underestimates by a little under one frame
        instr10_sound.frameNStart = frameN  # exact frame index
        instr10_sound.play()  # start the sound (it finishes automatically)
    
    # *instr10_text* updates
    if t >= 0.0 and instr10_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr10_text.tStart = t  # underestimates by a little under one frame
        instr10_text.frameNStart = frameN  # exact frame index
        instr10_text.setAutoDraw(True)
    
    # *instr10_image* updates
    if t >= 0.0 and instr10_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr10_image.tStart = t  # underestimates by a little under one frame
        instr10_image.frameNStart = frameN  # exact frame index
        instr10_image.setAutoDraw(True)
    
    # *instr10_key_resp* updates
    if t >= 0.0 and instr10_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr10_key_resp.tStart = t  # underestimates by a little under one frame
        instr10_key_resp.frameNStart = frameN  # exact frame index
        instr10_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr10_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr10_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr10_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr10_key_resp.rt = instr10_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr10"-------
for thisComponent in instr10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr10_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr11"-------
t = 0
instr11Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr11_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr11_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr11Components = []
instr11Components.append(instr11_sound)
instr11Components.append(instr11_text1)
instr11Components.append(instr11_image1)
instr11Components.append(instr11_text2)
instr11Components.append(instr11_image2)
instr11Components.append(instr11_image3)
instr11Components.append(instr11_key_resp)
for thisComponent in instr11Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr11"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr11Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop instr11_sound
    if t >= 0.0 and instr11_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr11_sound.tStart = t  # underestimates by a little under one frame
        instr11_sound.frameNStart = frameN  # exact frame index
        instr11_sound.play()  # start the sound (it finishes automatically)
    
    # *instr11_text1* updates
    if t >= 0.0 and instr11_text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr11_text1.tStart = t  # underestimates by a little under one frame
        instr11_text1.frameNStart = frameN  # exact frame index
        instr11_text1.setAutoDraw(True)
    
    # *instr11_image1* updates
    if t >= 0.0 and instr11_image1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr11_image1.tStart = t  # underestimates by a little under one frame
        instr11_image1.frameNStart = frameN  # exact frame index
        instr11_image1.setAutoDraw(True)
    
    # *instr11_text2* updates
    if t >= 0.0 and instr11_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr11_text2.tStart = t  # underestimates by a little under one frame
        instr11_text2.frameNStart = frameN  # exact frame index
        instr11_text2.setAutoDraw(True)
    
    # *instr11_image2* updates
    if t >= 0.0 and instr11_image2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr11_image2.tStart = t  # underestimates by a little under one frame
        instr11_image2.frameNStart = frameN  # exact frame index
        instr11_image2.setAutoDraw(True)
    
    # *instr11_image3* updates
    if t >= 0.0 and instr11_image3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr11_image3.tStart = t  # underestimates by a little under one frame
        instr11_image3.frameNStart = frameN  # exact frame index
        instr11_image3.setAutoDraw(True)
    
    # *instr11_key_resp* updates
    if t >= 0.0 and instr11_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr11_key_resp.tStart = t  # underestimates by a little under one frame
        instr11_key_resp.frameNStart = frameN  # exact frame index
        instr11_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr11_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr11_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr11_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr11_key_resp.rt = instr11_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr11"-------
for thisComponent in instr11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr11_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr12"-------
t = 0
instr12Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr12_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr12_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr12Components = []
instr12Components.append(instr12_sound)
instr12Components.append(instr12_text)
instr12Components.append(instr12_key_resp)
for thisComponent in instr12Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr12"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr12Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop instr12_sound
    if t >= 0.0 and instr12_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr12_sound.tStart = t  # underestimates by a little under one frame
        instr12_sound.frameNStart = frameN  # exact frame index
        instr12_sound.play()  # start the sound (it finishes automatically)
    
    # *instr12_text* updates
    if t >= 0.0 and instr12_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr12_text.tStart = t  # underestimates by a little under one frame
        instr12_text.frameNStart = frameN  # exact frame index
        instr12_text.setAutoDraw(True)
    
    # *instr12_key_resp* updates
    if t >= 0.0 and instr12_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr12_key_resp.tStart = t  # underestimates by a little under one frame
        instr12_key_resp.frameNStart = frameN  # exact frame index
        instr12_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr12_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr12_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr12_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr12_key_resp.rt = instr12_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr12"-------
for thisComponent in instr12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr12_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
forced_test_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'S_forced_test_1.xlsx'),
    seed=None, name='forced_test_trials')
thisExp.addLoop(forced_test_trials)  # add the loop to the experiment
thisForced_test_trial = forced_test_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisForced_test_trial.rgb)
if thisForced_test_trial != None:
    for paramName in thisForced_test_trial.keys():
        exec(paramName + '= thisForced_test_trial.' + paramName)

for thisForced_test_trial in forced_test_trials:
    currentLoop = forced_test_trials
    # abbreviate parameter names if possible (e.g. rgb = thisForced_test_trial.rgb)
    if thisForced_test_trial != None:
        for paramName in thisForced_test_trial.keys():
            exec(paramName + '= thisForced_test_trial.' + paramName)
    
    #------Prepare to start Routine "test1"-------
    t = 0
    test1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    test1_image.setImage(letter1)
    # keep track of which components have finished
    test1Components = []
    test1Components.append(test1_image)
    test1Components.append(test1_blank)
    for thisComponent in test1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test1_image* updates
        if t >= 0.0 and test1_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test1_image.tStart = t  # underestimates by a little under one frame
            test1_image.frameNStart = frameN  # exact frame index
            test1_image.setAutoDraw(True)
        if test1_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            test1_image.setAutoDraw(False)
        
        # *test1_blank* updates
        if t >= 0.79 and test1_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            test1_blank.tStart = t  # underestimates by a little under one frame
            test1_blank.frameNStart = frameN  # exact frame index
            test1_blank.setAutoDraw(True)
        if test1_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            test1_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test1"-------
    for thisComponent in test1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test2"-------
    t = 0
    test2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    test2_image.setImage(letter2)
    # keep track of which components have finished
    test2Components = []
    test2Components.append(test2_image)
    test2Components.append(test2_blank)
    for thisComponent in test2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test2_image* updates
        if t >= 0.0 and test2_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test2_image.tStart = t  # underestimates by a little under one frame
            test2_image.frameNStart = frameN  # exact frame index
            test2_image.setAutoDraw(True)
        if test2_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            test2_image.setAutoDraw(False)
        
        # *test2_blank* updates
        if t >= 0.79 and test2_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            test2_blank.tStart = t  # underestimates by a little under one frame
            test2_blank.frameNStart = frameN  # exact frame index
            test2_blank.setAutoDraw(True)
        if test2_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            test2_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test2"-------
    for thisComponent in test2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test3"-------
    t = 0
    test3Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    test3_image.setImage(letter3)
    # keep track of which components have finished
    test3Components = []
    test3Components.append(test3_image)
    test3Components.append(test3_blank)
    for thisComponent in test3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test3"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test3_image* updates
        if t >= 0.0 and test3_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test3_image.tStart = t  # underestimates by a little under one frame
            test3_image.frameNStart = frameN  # exact frame index
            test3_image.setAutoDraw(True)
        if test3_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            test3_image.setAutoDraw(False)
        
        # *test3_blank* updates
        if t >= 0.79 and test3_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            test3_blank.tStart = t  # underestimates by a little under one frame
            test3_blank.frameNStart = frameN  # exact frame index
            test3_blank.setAutoDraw(True)
        if test3_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            test3_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test3"-------
    for thisComponent in test3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "triplet_pause"-------
    t = 0
    triplet_pauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    triplet_pauseComponents = []
    triplet_pauseComponents.append(triplet_pause_image)
    for thisComponent in triplet_pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "triplet_pause"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = triplet_pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *triplet_pause_image* updates
        if t >= 0.0 and triplet_pause_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            triplet_pause_image.tStart = t  # underestimates by a little under one frame
            triplet_pause_image.frameNStart = frameN  # exact frame index
            triplet_pause_image.setAutoDraw(True)
        if triplet_pause_image.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            triplet_pause_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in triplet_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "triplet_pause"-------
    for thisComponent in triplet_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test4"-------
    t = 0
    test4Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    test4_image.setImage(letter4)
    # keep track of which components have finished
    test4Components = []
    test4Components.append(test4_image)
    test4Components.append(test4_blank)
    for thisComponent in test4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test4"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test4_image* updates
        if t >= 0.0 and test4_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test4_image.tStart = t  # underestimates by a little under one frame
            test4_image.frameNStart = frameN  # exact frame index
            test4_image.setAutoDraw(True)
        if test4_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            test4_image.setAutoDraw(False)
        
        # *test4_blank* updates
        if t >= 0.79 and test4_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            test4_blank.tStart = t  # underestimates by a little under one frame
            test4_blank.frameNStart = frameN  # exact frame index
            test4_blank.setAutoDraw(True)
        if test4_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            test4_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test4"-------
    for thisComponent in test4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test5"-------
    t = 0
    test5Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    test5_image.setImage(letter5)
    # keep track of which components have finished
    test5Components = []
    test5Components.append(test5_image)
    test5Components.append(test5_blank)
    for thisComponent in test5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test5"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test5_image* updates
        if t >= 0.0 and test5_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test5_image.tStart = t  # underestimates by a little under one frame
            test5_image.frameNStart = frameN  # exact frame index
            test5_image.setAutoDraw(True)
        if test5_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            test5_image.setAutoDraw(False)
        
        # *test5_blank* updates
        if t >= 0.79 and test5_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            test5_blank.tStart = t  # underestimates by a little under one frame
            test5_blank.frameNStart = frameN  # exact frame index
            test5_blank.setAutoDraw(True)
        if test5_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            test5_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test5"-------
    for thisComponent in test5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test6"-------
    t = 0
    test6Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    test6_image.setImage(letter6)
    # keep track of which components have finished
    test6Components = []
    test6Components.append(test6_image)
    test6Components.append(test6_blank)
    for thisComponent in test6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test6"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test6_image* updates
        if t >= 0.0 and test6_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test6_image.tStart = t  # underestimates by a little under one frame
            test6_image.frameNStart = frameN  # exact frame index
            test6_image.setAutoDraw(True)
        if test6_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            test6_image.setAutoDraw(False)
        
        # *test6_blank* updates
        if t >= 0.79 and test6_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            test6_blank.tStart = t  # underestimates by a little under one frame
            test6_blank.frameNStart = frameN  # exact frame index
            test6_blank.setAutoDraw(True)
        if test6_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            test6_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test6"-------
    for thisComponent in test6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "question"-------
    t = 0
    questionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    question_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    question_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    questionComponents = []
    questionComponents.append(question_text)
    questionComponents.append(question_key_resp)
    for thisComponent in questionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "question"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = questionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_text* updates
        if t >= 0.0 and question_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            question_text.tStart = t  # underestimates by a little under one frame
            question_text.frameNStart = frameN  # exact frame index
            question_text.setAutoDraw(True)
        
        # *question_key_resp* updates
        if t >= 0.0 and question_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            question_key_resp.tStart = t  # underestimates by a little under one frame
            question_key_resp.frameNStart = frameN  # exact frame index
            question_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(question_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if question_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                question_key_resp.keys = theseKeys[-1]  # just the last key pressed
                question_key_resp.rt = question_key_resp.clock.getTime()
                # was this 'correct'?
                if (question_key_resp.keys == str(corrAns)) or (question_key_resp.keys == corrAns):
                    question_key_resp.corr = 1
                else:
                    question_key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "question"-------
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if question_key_resp.keys in ['', [], None]:  # No response was made
       question_key_resp.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': question_key_resp.corr = 1  # correct non-response
       else: question_key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for forced_test_trials (TrialHandler)
    forced_test_trials.addData('question_key_resp.keys',question_key_resp.keys)
    forced_test_trials.addData('question_key_resp.corr', question_key_resp.corr)
    if question_key_resp.keys != None:  # we had a response
        forced_test_trials.addData('question_key_resp.rt', question_key_resp.rt)
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'forced_test_trials'



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
