#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Thu May 26 18:30:18 2016
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
expName = 'tsl'  # from the Builder filename that created this script
expInfo = {u'target': u'', u'PartID': u''} # block: R(andom) and S(equential); language: 1 or 2; target: if language 1, then bi, pu, du, da; if block 2, then ku, tu, pi, do.
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
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr3_5"
instr3_5Clock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text="Now just relax and enjoy Klaptoo's\nmusic! You don't have to watch the\nscreen. Remember to press the \nspacebar whenever you hear Klaptoo's\nfavorite note. Let's start!",    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_15 = visual.ImageStim(win=win, name='image_15',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_30 = sound.Sound('new_instr_7.wav', secs=-1)
sound_30.setVolume(1)

# Initialize components for Routine "trial"
trialClock = core.Clock()
tone = sound.Sound('A', secs=-1)
tone.setVolume(1)
alien = visual.ImageStim(win=win, name='alien',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Great, you did it!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_31 = sound.Sound('instr_8.wav', secs=-1)
sound_31.setVolume(1)



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


#------Prepare to start Routine "instr3_5"-------
t = 0
instr3_5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_13.status = NOT_STARTED
# keep track of which components have finished
instr3_5Components = []
instr3_5Components.append(text_11)
instr3_5Components.append(key_resp_13)
instr3_5Components.append(image_15)
instr3_5Components.append(sound_30)
for thisComponent in instr3_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # underestimates by a little under one frame
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_15* updates
    if t >= 0.0 and image_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_15.tStart = t  # underestimates by a little under one frame
        image_15.frameNStart = frameN  # exact frame index
        image_15.setAutoDraw(True)
    # start/stop sound_30
    if t >= 0.0 and sound_30.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_30.tStart = t  # underestimates by a little under one frame
        sound_30.frameNStart = frameN  # exact frame index
        sound_30.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_5"-------
for thisComponent in instr3_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_30.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'asl_run2.xlsx'),
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1.keys():
        exec(paramName + '= thisTrial_1.' + paramName)

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1.keys():
            exec(paramName + '= thisTrial_1.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    tone.setSound(soundFile, secs=0.46)
    target_tone_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    target_tone_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(tone)
    trialComponents.append(alien)
    trialComponents.append(target_tone_key_resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop tone
        if t >= 0.0 and tone.status == NOT_STARTED:
            # keep track of start time/frame for later
            tone.tStart = t  # underestimates by a little under one frame
            tone.frameNStart = frameN  # exact frame index
            tone.play()  # start the sound (it finishes automatically)
        if tone.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            tone.stop()  # stop the sound (if longer than duration)
        
        # *alien* updates
        if t >= 0.0 and alien.status == NOT_STARTED:
            # keep track of start time/frame for later
            alien.tStart = t  # underestimates by a little under one frame
            alien.frameNStart = frameN  # exact frame index
            alien.setAutoDraw(True)
        if alien.status == STARTED and t >= (0.0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            alien.setAutoDraw(False)
        
        # *target_tone_key_resp* updates
        if t >= 0.0 and target_tone_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            target_tone_key_resp.tStart = t  # underestimates by a little under one frame
            target_tone_key_resp.frameNStart = frameN  # exact frame index
            target_tone_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(target_tone_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if target_tone_key_resp.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            target_tone_key_resp.status = STOPPED
        if target_tone_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                target_tone_key_resp.keys = theseKeys[-1]  # just the last key pressed
                target_tone_key_resp.rt = target_tone_key_resp.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tone.stop() #ensure sound has stopped at end of routine
    # check responses
    if target_tone_key_resp.keys in ['', [], None]:  # No response was made
       target_tone_key_resp.keys=None
    # store data for trials_1 (TrialHandler)
    trials_1.addData('target_tone_key_resp.keys',target_tone_key_resp.keys)
    if target_tone_key_resp.keys != None:  # we had a response
        trials_1.addData('target_tone_key_resp.rt', target_tone_key_resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_1'


#------Prepare to start Routine "instr4"-------
t = 0
instr4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
instr4Components = []
instr4Components.append(text_2)
instr4Components.append(key_resp_4)
instr4Components.append(sound_31)
for thisComponent in instr4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_31
    if t >= 0.0 and sound_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_31.tStart = t  # underestimates by a little under one frame
        sound_31.frameNStart = frameN  # exact frame index
        sound_31.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr4"-------
for thisComponent in instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_31.stop() #ensure sound has stopped at end of routine
# the Routine "instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
