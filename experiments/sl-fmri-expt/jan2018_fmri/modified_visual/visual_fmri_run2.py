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
expInfo['Run'] = "2"
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
    pos=[0, 0.2], height=0.1, wrapWidth=None,
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
    trialList=data.importConditions(u'visual_run2_1.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_2.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_3.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_4_1.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_4_2.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_4_3.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_5.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_6.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_6_1.xlsx'),
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
    trialList=data.importConditions(u'visual_run2_7.xlsx'),
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
    
    

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
