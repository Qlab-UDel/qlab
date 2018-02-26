#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Thu Mar 16 10:41:59 2017
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
expInfo['Run'] = "6"
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


# Initialize components for Routine "end_fam_block"
end_fam_blockClock = core.Clock()
end_fam_block_text = visual.TextStim(win=win, ori=0, name='end_fam_block_text',
    text=u'Great job! Now we have a new task for you. Be sure to pay attention to the instructions.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
end_fam_block_sound = sound.Sound(u'pretest.wav', secs=-1)
end_fam_block_sound.setVolume(1)

# Initialize components for Routine "pretest_instr1"
pretest_instr1Clock = core.Clock()
pretest_instr1_image = visual.ImageStim(win=win, name='pretest_instr1_image',
    image=u'Ladder4.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pretest_instr1_sound = sound.Sound(u'pretest_instr1.wav', secs=-1)
pretest_instr1_sound.setVolume(1)

# Initialize components for Routine "pretest_instr2"
pretest_instr2Clock = core.Clock()
pretest_instr2_image = visual.ImageStim(win=win, name='pretest_instr2_image',
    image=u'Ladder5.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pretest_instr2_sound = sound.Sound(u'pretest_instr2.wav', secs=-1)
pretest_instr2_sound.setVolume(1)

# Initialize components for Routine "pretest_instr3"
pretest_instr3Clock = core.Clock()
pretest_instr3_image = visual.ImageStim(win=win, name='pretest_instr3_image',
    image=u'Ladder7.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pretest_instr3_sound = sound.Sound(u'pretest_instr3.wav', secs=-1)
pretest_instr3_sound.setVolume(1)

# Initialize components for Routine "pretest_instr4"
pretest_instr4Clock = core.Clock()
pretest_instr4_image = visual.ImageStim(win=win, name='pretest_instr4_image',
    image=u'Ladder8.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pretest_instr4_sound = sound.Sound(u'pretest_instr4.wav', secs=-1)
pretest_instr4_sound.setVolume(1)

# Initialize components for Routine "pretest_instr5"
pretest_instr5Clock = core.Clock()
pretest_instr5_image = visual.ImageStim(win=win, name='pretest_instr5_image',
    image=u'Ladder9.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pretest_instr5_sound = sound.Sound(u'pretest_instr5.wav', secs=-1)
pretest_instr5_sound.setVolume(1)

# Initialize components for Routine "pretest_instr6"
pretest_instr6Clock = core.Clock()
pretest_instr6_text = visual.TextStim(win=win, ori=0, name='pretest_instr6_text',
    text=u'We\u2019re going to show you aliens one at a time. The first three will belong to one group of aliens that might have lined up together, and the last three will belong to another group of aliens that might have lined up together. Your job is to decide which of the two groups lined up together.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
pretest_instr6_sound = sound.Sound(u'pretest_instr6.wav', secs=-1)
pretest_instr6_sound.setVolume(1)

# Initialize components for Routine "test1"
test1Clock = core.Clock()
test1_image = visual.ImageStim(win=win, name='test1_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test1_blank_image = visual.ImageStim(win=win, name='test1_blank_image',
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
test2_blank_image = visual.ImageStim(win=win, name='test2_blank_image',
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
test3_blank_image = visual.ImageStim(win=win, name='test3_blank_image',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "test_pause"
test_pauseClock = core.Clock()
test_pause_image = visual.ImageStim(win=win, name='test_pause_image',
    image=u'blank.png', mask=None,
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
test4_blank_image = visual.ImageStim(win=win, name='test4_blank_image',
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
test5_blank_image = visual.ImageStim(win=win, name='test5_blank_image',
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
test6_blank_image = visual.ImageStim(win=win, name='test6_blank_image',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "question"
questionClock = core.Clock()
question_text = visual.TextStim(win=win, ori=0, name='question_text',
    text=u'Which group lined up together? Press the green button for first and red button for second. ',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, ori=0, name='end_text',
    text=u"Great, you're all done! Thank you :)\nPress any key to exit.",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
end_sound = sound.Sound(u'instr_22.wav', secs=-1)
end_sound.setVolume(1)

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
    trialList=data.importConditions(u'visual_run6_1.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_2_1.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_2_2.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_2_3.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_3.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_4_1.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_4_2.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_4_3.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_5.xlsx'),
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
    trialList=data.importConditions(u'visual_run6_6.xlsx'),
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

#------Prepare to start Routine "end_fam_block"-------
t = 0
end_fam_blockClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
end_fam_block_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
end_fam_block_key_resp.status = NOT_STARTED
# keep track of which components have finished
end_fam_blockComponents = []
end_fam_blockComponents.append(end_fam_block_text)
end_fam_blockComponents.append(end_fam_block_key_resp)
end_fam_blockComponents.append(end_fam_block_sound)
for thisComponent in end_fam_blockComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end_fam_block"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = end_fam_blockClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_fam_block_text* updates
    if t >= 0.0 and end_fam_block_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_fam_block_text.tStart = t  # underestimates by a little under one frame
        end_fam_block_text.frameNStart = frameN  # exact frame index
        end_fam_block_text.setAutoDraw(True)
    
    # *end_fam_block_key_resp* updates
    if t >= 0.0 and end_fam_block_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_fam_block_key_resp.tStart = t  # underestimates by a little under one frame
        end_fam_block_key_resp.frameNStart = frameN  # exact frame index
        end_fam_block_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_fam_block_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_fam_block_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_fam_block_key_resp.keys = theseKeys[-1]  # just the last key pressed
            end_fam_block_key_resp.rt = end_fam_block_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop end_fam_block_sound
    if t >= 0.0 and end_fam_block_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_fam_block_sound.tStart = t  # underestimates by a little under one frame
        end_fam_block_sound.frameNStart = frameN  # exact frame index
        end_fam_block_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_fam_blockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end_fam_block"-------
for thisComponent in end_fam_blockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_fam_block_key_resp.keys in ['', [], None]:  # No response was made
   end_fam_block_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('end_fam_block_key_resp.keys',end_fam_block_key_resp.keys)
if end_fam_block_key_resp.keys != None:  # we had a response
    thisExp.addData('end_fam_block_key_resp.rt', end_fam_block_key_resp.rt)
thisExp.nextEntry()
end_fam_block_sound.stop() #ensure sound has stopped at end of routine
# the Routine "end_fam_block" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "pretest_instr1"-------
t = 0
pretest_instr1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
pretest_instr1_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
pretest_instr1_key_resp.status = NOT_STARTED
# keep track of which components have finished
pretest_instr1Components = []
pretest_instr1Components.append(pretest_instr1_image)
pretest_instr1Components.append(pretest_instr1_sound)
pretest_instr1Components.append(pretest_instr1_key_resp)
for thisComponent in pretest_instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pretest_instr1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pretest_instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pretest_instr1_image* updates
    if t >= 0.0 and pretest_instr1_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr1_image.tStart = t  # underestimates by a little under one frame
        pretest_instr1_image.frameNStart = frameN  # exact frame index
        pretest_instr1_image.setAutoDraw(True)
    # start/stop pretest_instr1_sound
    if t >= 0.0 and pretest_instr1_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr1_sound.tStart = t  # underestimates by a little under one frame
        pretest_instr1_sound.frameNStart = frameN  # exact frame index
        pretest_instr1_sound.play()  # start the sound (it finishes automatically)
    
    # *pretest_instr1_key_resp* updates
    if t >= 0.0 and pretest_instr1_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr1_key_resp.tStart = t  # underestimates by a little under one frame
        pretest_instr1_key_resp.frameNStart = frameN  # exact frame index
        pretest_instr1_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(pretest_instr1_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if pretest_instr1_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            pretest_instr1_key_resp.keys = theseKeys[-1]  # just the last key pressed
            pretest_instr1_key_resp.rt = pretest_instr1_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretest_instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pretest_instr1"-------
for thisComponent in pretest_instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
pretest_instr1_sound.stop() #ensure sound has stopped at end of routine
# the Routine "pretest_instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "pretest_instr2"-------
t = 0
pretest_instr2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
pretest_instr2_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
pretest_instr2_key_resp.status = NOT_STARTED
# keep track of which components have finished
pretest_instr2Components = []
pretest_instr2Components.append(pretest_instr2_image)
pretest_instr2Components.append(pretest_instr2_sound)
pretest_instr2Components.append(pretest_instr2_key_resp)
for thisComponent in pretest_instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pretest_instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pretest_instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pretest_instr2_image* updates
    if t >= 0.0 and pretest_instr2_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr2_image.tStart = t  # underestimates by a little under one frame
        pretest_instr2_image.frameNStart = frameN  # exact frame index
        pretest_instr2_image.setAutoDraw(True)
    # start/stop pretest_instr2_sound
    if t >= 0.0 and pretest_instr2_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr2_sound.tStart = t  # underestimates by a little under one frame
        pretest_instr2_sound.frameNStart = frameN  # exact frame index
        pretest_instr2_sound.play()  # start the sound (it finishes automatically)
    
    # *pretest_instr2_key_resp* updates
    if t >= 0.0 and pretest_instr2_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr2_key_resp.tStart = t  # underestimates by a little under one frame
        pretest_instr2_key_resp.frameNStart = frameN  # exact frame index
        pretest_instr2_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(pretest_instr2_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if pretest_instr2_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            pretest_instr2_key_resp.keys = theseKeys[-1]  # just the last key pressed
            pretest_instr2_key_resp.rt = pretest_instr2_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretest_instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pretest_instr2"-------
for thisComponent in pretest_instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
pretest_instr2_sound.stop() #ensure sound has stopped at end of routine
# the Routine "pretest_instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "pretest_instr3"-------
t = 0
pretest_instr3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
pretest_instr3_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
pretest_instr3_key_resp.status = NOT_STARTED
# keep track of which components have finished
pretest_instr3Components = []
pretest_instr3Components.append(pretest_instr3_image)
pretest_instr3Components.append(pretest_instr3_sound)
pretest_instr3Components.append(pretest_instr3_key_resp)
for thisComponent in pretest_instr3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pretest_instr3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pretest_instr3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pretest_instr3_image* updates
    if t >= 0.0 and pretest_instr3_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr3_image.tStart = t  # underestimates by a little under one frame
        pretest_instr3_image.frameNStart = frameN  # exact frame index
        pretest_instr3_image.setAutoDraw(True)
    # start/stop pretest_instr3_sound
    if t >= 0.0 and pretest_instr3_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr3_sound.tStart = t  # underestimates by a little under one frame
        pretest_instr3_sound.frameNStart = frameN  # exact frame index
        pretest_instr3_sound.play()  # start the sound (it finishes automatically)
    
    # *pretest_instr3_key_resp* updates
    if t >= 0.0 and pretest_instr3_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr3_key_resp.tStart = t  # underestimates by a little under one frame
        pretest_instr3_key_resp.frameNStart = frameN  # exact frame index
        pretest_instr3_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(pretest_instr3_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if pretest_instr3_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            pretest_instr3_key_resp.keys = theseKeys[-1]  # just the last key pressed
            pretest_instr3_key_resp.rt = pretest_instr3_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretest_instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pretest_instr3"-------
for thisComponent in pretest_instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
pretest_instr3_sound.stop() #ensure sound has stopped at end of routine
# the Routine "pretest_instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "pretest_instr4"-------
t = 0
pretest_instr4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
pretest_instr4_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
pretest_instr4_key_resp.status = NOT_STARTED
# keep track of which components have finished
pretest_instr4Components = []
pretest_instr4Components.append(pretest_instr4_image)
pretest_instr4Components.append(pretest_instr4_sound)
pretest_instr4Components.append(pretest_instr4_key_resp)
for thisComponent in pretest_instr4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pretest_instr4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pretest_instr4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pretest_instr4_image* updates
    if t >= 0.0 and pretest_instr4_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr4_image.tStart = t  # underestimates by a little under one frame
        pretest_instr4_image.frameNStart = frameN  # exact frame index
        pretest_instr4_image.setAutoDraw(True)
    # start/stop pretest_instr4_sound
    if t >= 0.0 and pretest_instr4_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr4_sound.tStart = t  # underestimates by a little under one frame
        pretest_instr4_sound.frameNStart = frameN  # exact frame index
        pretest_instr4_sound.play()  # start the sound (it finishes automatically)
    
    # *pretest_instr4_key_resp* updates
    if t >= 0.0 and pretest_instr4_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr4_key_resp.tStart = t  # underestimates by a little under one frame
        pretest_instr4_key_resp.frameNStart = frameN  # exact frame index
        pretest_instr4_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(pretest_instr4_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if pretest_instr4_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            pretest_instr4_key_resp.keys = theseKeys[-1]  # just the last key pressed
            pretest_instr4_key_resp.rt = pretest_instr4_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretest_instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pretest_instr4"-------
for thisComponent in pretest_instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
pretest_instr4_sound.stop() #ensure sound has stopped at end of routine
# the Routine "pretest_instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "pretest_instr5"-------
t = 0
pretest_instr5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
pretest_instr5_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
pretest_instr5_key_resp.status = NOT_STARTED
# keep track of which components have finished
pretest_instr5Components = []
pretest_instr5Components.append(pretest_instr5_image)
pretest_instr5Components.append(pretest_instr5_sound)
pretest_instr5Components.append(pretest_instr5_key_resp)
for thisComponent in pretest_instr5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pretest_instr5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pretest_instr5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pretest_instr5_image* updates
    if t >= 0.0 and pretest_instr5_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr5_image.tStart = t  # underestimates by a little under one frame
        pretest_instr5_image.frameNStart = frameN  # exact frame index
        pretest_instr5_image.setAutoDraw(True)
    # start/stop pretest_instr5_sound
    if t >= 0.0 and pretest_instr5_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr5_sound.tStart = t  # underestimates by a little under one frame
        pretest_instr5_sound.frameNStart = frameN  # exact frame index
        pretest_instr5_sound.play()  # start the sound (it finishes automatically)
    
    # *pretest_instr5_key_resp* updates
    if t >= 0.0 and pretest_instr5_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr5_key_resp.tStart = t  # underestimates by a little under one frame
        pretest_instr5_key_resp.frameNStart = frameN  # exact frame index
        pretest_instr5_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(pretest_instr5_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if pretest_instr5_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            pretest_instr5_key_resp.keys = theseKeys[-1]  # just the last key pressed
            pretest_instr5_key_resp.rt = pretest_instr5_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretest_instr5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pretest_instr5"-------
for thisComponent in pretest_instr5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
pretest_instr5_sound.stop() #ensure sound has stopped at end of routine
# the Routine "pretest_instr5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "pretest_instr6"-------
t = 0
pretest_instr6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
pretest_instr6_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
pretest_instr6_key_resp.status = NOT_STARTED
# keep track of which components have finished
pretest_instr6Components = []
pretest_instr6Components.append(pretest_instr6_text)
pretest_instr6Components.append(pretest_instr6_sound)
pretest_instr6Components.append(pretest_instr6_key_resp)
for thisComponent in pretest_instr6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pretest_instr6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pretest_instr6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pretest_instr6_text* updates
    if t >= 0.0 and pretest_instr6_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr6_text.tStart = t  # underestimates by a little under one frame
        pretest_instr6_text.frameNStart = frameN  # exact frame index
        pretest_instr6_text.setAutoDraw(True)
    # start/stop pretest_instr6_sound
    if t >= 0.0 and pretest_instr6_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr6_sound.tStart = t  # underestimates by a little under one frame
        pretest_instr6_sound.frameNStart = frameN  # exact frame index
        pretest_instr6_sound.play()  # start the sound (it finishes automatically)
    
    # *pretest_instr6_key_resp* updates
    if t >= 0.0 and pretest_instr6_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        pretest_instr6_key_resp.tStart = t  # underestimates by a little under one frame
        pretest_instr6_key_resp.frameNStart = frameN  # exact frame index
        pretest_instr6_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(pretest_instr6_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if pretest_instr6_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            pretest_instr6_key_resp.keys = theseKeys[-1]  # just the last key pressed
            pretest_instr6_key_resp.rt = pretest_instr6_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretest_instr6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "pretest_instr6"-------
for thisComponent in pretest_instr6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
pretest_instr6_sound.stop() #ensure sound has stopped at end of routine
# the Routine "pretest_instr6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
forced_test_1_block = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'S_forced_test_2.xlsx'),
    seed=None, name='forced_test_1_block')
thisExp.addLoop(forced_test_1_block)  # add the loop to the experiment
thisForced_test_1_block = forced_test_1_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisForced_test_1_block.rgb)
if thisForced_test_1_block != None:
    for paramName in thisForced_test_1_block.keys():
        exec(paramName + '= thisForced_test_1_block.' + paramName)

for thisForced_test_1_block in forced_test_1_block:
    currentLoop = forced_test_1_block
    # abbreviate parameter names if possible (e.g. rgb = thisForced_test_1_block.rgb)
    if thisForced_test_1_block != None:
        for paramName in thisForced_test_1_block.keys():
            exec(paramName + '= thisForced_test_1_block.' + paramName)
    
    #------Prepare to start Routine "test1"-------
    t = 0
    test1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    test1_image.setImage(image1)
    # keep track of which components have finished
    test1Components = []
    test1Components.append(test1_image)
    test1Components.append(test1_blank_image)
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
        
        # *test1_blank_image* updates
        if t >= 0.8 and test1_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test1_blank_image.tStart = t  # underestimates by a little under one frame
            test1_blank_image.frameNStart = frameN  # exact frame index
            test1_blank_image.setAutoDraw(True)
        if test1_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            test1_blank_image.setAutoDraw(False)
        
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
    test2_image.setImage(image2)
    # keep track of which components have finished
    test2Components = []
    test2Components.append(test2_image)
    test2Components.append(test2_blank_image)
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
        
        # *test2_blank_image* updates
        if t >= 0.8 and test2_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test2_blank_image.tStart = t  # underestimates by a little under one frame
            test2_blank_image.frameNStart = frameN  # exact frame index
            test2_blank_image.setAutoDraw(True)
        if test2_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            test2_blank_image.setAutoDraw(False)
        
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
    test3_image.setImage(image3)
    # keep track of which components have finished
    test3Components = []
    test3Components.append(test3_image)
    test3Components.append(test3_blank_image)
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
        
        # *test3_blank_image* updates
        if t >= 0.8 and test3_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test3_blank_image.tStart = t  # underestimates by a little under one frame
            test3_blank_image.frameNStart = frameN  # exact frame index
            test3_blank_image.setAutoDraw(True)
        if test3_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            test3_blank_image.setAutoDraw(False)
        
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
    
    #------Prepare to start Routine "test_pause"-------
    t = 0
    test_pauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    test_pauseComponents = []
    test_pauseComponents.append(test_pause_image)
    for thisComponent in test_pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test_pause"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test_pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_pause_image* updates
        if t >= 0.0 and test_pause_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_pause_image.tStart = t  # underestimates by a little under one frame
            test_pause_image.frameNStart = frameN  # exact frame index
            test_pause_image.setAutoDraw(True)
        if test_pause_image.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            test_pause_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test_pause"-------
    for thisComponent in test_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test4"-------
    t = 0
    test4Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    test4_image.setImage(image4)
    # keep track of which components have finished
    test4Components = []
    test4Components.append(test4_image)
    test4Components.append(test4_blank_image)
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
        
        # *test4_blank_image* updates
        if t >= 0.8 and test4_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test4_blank_image.tStart = t  # underestimates by a little under one frame
            test4_blank_image.frameNStart = frameN  # exact frame index
            test4_blank_image.setAutoDraw(True)
        if test4_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            test4_blank_image.setAutoDraw(False)
        
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
    test5_image.setImage(image5)
    # keep track of which components have finished
    test5Components = []
    test5Components.append(test5_image)
    test5Components.append(test5_blank_image)
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
        
        # *test5_blank_image* updates
        if t >= 0.8 and test5_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test5_blank_image.tStart = t  # underestimates by a little under one frame
            test5_blank_image.frameNStart = frameN  # exact frame index
            test5_blank_image.setAutoDraw(True)
        if test5_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            test5_blank_image.setAutoDraw(False)
        
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
    test6_image.setImage(image6)
    # keep track of which components have finished
    test6Components = []
    test6Components.append(test6_image)
    test6Components.append(test6_blank_image)
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
        
        # *test6_blank_image* updates
        if t >= 0.8 and test6_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            test6_blank_image.tStart = t  # underestimates by a little under one frame
            test6_blank_image.frameNStart = frameN  # exact frame index
            test6_blank_image.setAutoDraw(True)
        if test6_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            test6_blank_image.setAutoDraw(False)
        
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
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4', 3])
            
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
    # store data for forced_test_1_block (TrialHandler)
    forced_test_1_block.addData('question_key_resp.keys',question_key_resp.keys)
    forced_test_1_block.addData('question_key_resp.corr', question_key_resp.corr)
    if question_key_resp.keys != None:  # we had a response
        forced_test_1_block.addData('question_key_resp.rt', question_key_resp.rt)
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
end_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
end_key_resp.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(end_text)
endComponents.append(end_sound)
endComponents.append(end_key_resp)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if t >= 0.0 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t  # underestimates by a little under one frame
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    # start/stop end_sound
    if t >= 0.0 and end_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_sound.tStart = t  # underestimates by a little under one frame
        end_sound.frameNStart = frameN  # exact frame index
        end_sound.play()  # start the sound (it finishes automatically)
    
    # *end_key_resp* updates
    if t >= 0.0 and end_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_key_resp.tStart = t  # underestimates by a little under one frame
        end_key_resp.frameNStart = frameN  # exact frame index
        end_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_key_resp.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_key_resp.keys = theseKeys[-1]  # just the last key pressed
            end_key_resp.rt = end_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
end_sound.stop() #ensure sound has stopped at end of routine

# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
