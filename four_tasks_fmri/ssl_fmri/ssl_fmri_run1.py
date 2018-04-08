#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Wed Apr 26 08:10:22 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

# the experiment contains Three runs. each run contains three conditions: random, sequential and silence; Each condition contains 192 syllables (16 repetitions x 4 words x 3 syllables) 
# or (96 x TR) seconds. Each run has 24 mini-blocks (8 mini-blocks per each condition), interspersed pseudorandomly. 
# the third run will have a test session at the end.

# adjust TA: line 1268, 1317, 1344, 1356
# once TA is set, need to change the duration of the silence.wav too.
# 485 TRs per run, 5 TRs at the beginning (not included in the analyses). [not necessary any more]
# timing issue: first TRS not presented.
# need to change the response buttons (not space key anymore)
# need to re-record the instruction

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
expName = 'ssl'  # from the Builder filename that created this script
expInfo = {u'target': u'', u'PartID': u''} # block: R(andom) and S(equential); language: 1 or 2; target: if language 1, then bi, pu, du, da; if block 2, then ku, tu, pi, do.
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['Run'] = "1"
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

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instr1_text = visual.TextStim(win=win, ori=0, name='instr1_text',
    text='Press the spacebar to begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr1_sound = sound.Sound(u'ssl_instr1.wav', secs=-1)
instr1_sound.setVolume(1)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instr2_text = visual.TextStim(win=win, ori=0, name='instr2_text',
    text=u"Hi! We're going to listen to an alien language today.",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr2_sound = sound.Sound(u'ssl_instr2.wav', secs=-1)
instr2_sound.setVolume(1)

# Initialize components for Routine "instr3"
instr3Clock = core.Clock()
instr3_text = visual.TextStim(win=win, ori=0, name='instr3_text',
    text=u'This is Meeple!',    font=u'Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr3_image = visual.ImageStim(win=win, name='instr3_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr3_sound = sound.Sound(u'ssl_instr3.wav', secs=-1)
instr3_sound.setVolume(1)

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
instr4_text = visual.TextStim(win=win, ori=0, name='instr4_text',
    text=u"Meeple is from Planet B. We're going to listen to Meeple speak her alien language.",    font=u'Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr4_image = visual.ImageStim(win=win, name='instr4_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr4_sound = sound.Sound(u'ssl_instr4.wav', secs=-1)
instr4_sound.setVolume(1)

# Initialize components for Routine "instr5"
instr5Clock = core.Clock()
instr5_text = visual.TextStim(win=win, ori=0, name='instr5_text',
    text=u'Meeple is going to say her favorite word for you now. Listen carefully!',    font=u'Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr5_image = visual.ImageStim(win=win, name='instr5_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr5_sound = sound.Sound(u'ssl_instr5.wav', secs=-1)
instr5_sound.setVolume(1)

# Initialize components for Routine "target_syllable"
target_syllableClock = core.Clock()
target_syllable_image = visual.ImageStim(win=win, name='target_syllable_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
target_syllable_sound = sound.Sound('%s.wav' % str(expInfo['target']), secs=-1)
target_syllable_sound.setVolume(1)

# Initialize components for Routine "instr6"
instr6Clock = core.Clock()
instr6_text = visual.TextStim(win=win, ori=0, name='instr6_text',
    text=u"When you hear Meeple say her favorite word, press the spacebar as soon as you can. Let's practice!",    font=u'Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr6_image = visual.ImageStim(win=win, name='instr6_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr6_sound = sound.Sound(u'ssl_instr6.wav', secs=-1)
instr6_sound.setVolume(1)

# Initialize components for Routine "target_practice"
target_practiceClock = core.Clock()
target_practice_text = visual.TextStim(win=win, ori=0, name='target_practice_text',
    text='Press space!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
target_practice_sound = sound.Sound('%s.wav' % str(expInfo['target']), secs=-1)
target_practice_sound.setVolume(1)

# Initialize components for Routine "instr7"
instr7Clock = core.Clock()
instr7_text = visual.TextStim(win=win, ori=0, name='instr7_text',
    text=u"Good job! Now Meeple is going to say many words in her alien language. Remember to press the spacebar whenever you hear Meeple's favorite word!",    font=u'Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr7_image = visual.ImageStim(win=win, name='instr7_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instr7_sound = sound.Sound(u'ssl_instr7.wav', secs=-1)
instr7_sound.setVolume(1)

# Initialize components for Routine "first_TA"
first_TAClock = core.Clock()
TA_first = visual.TextStim(win=win, ori=0, name='TA_first',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fam_trials"
fam_trialsClock = core.Clock()
fam_trials_sound = sound.Sound('A', secs=-1)
fam_trials_sound.setVolume(1)
fam_trials_image = visual.ImageStim(win=win, name='fam_trials_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr8"
instr8Clock = core.Clock()
instr8_text = visual.TextStim(win=win, ori=0, name='instr8_text',
    text=u'Great, you did it!',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr8_sound = sound.Sound(u'ssl_instr8.wav', secs=-1)
instr8_sound.setVolume(1)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr1_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr1_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr1Components = []
instr1Components.append(instr1_text)
instr1Components.append(instr1_key_resp)
instr1Components.append(instr1_sound)
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1_text* updates
    if t >= 0.0 and instr1_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1_text.tStart = t  # underestimates by a little under one frame
        instr1_text.frameNStart = frameN  # exact frame index
        instr1_text.setAutoDraw(True)
    
    # *instr1_key_resp* updates
    if t >= 0.0 and instr1_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1_key_resp.tStart = t  # underestimates by a little under one frame
        instr1_key_resp.frameNStart = frameN  # exact frame index
        instr1_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr1_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr1_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr1_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr1_key_resp.rt = instr1_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop instr1_sound
    if t >= 0.0 and instr1_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1_sound.tStart = t  # underestimates by a little under one frame
        instr1_sound.frameNStart = frameN  # exact frame index
        instr1_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr1_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr2"-------
t = 0
instr2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr2_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr2_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr2Components = []
instr2Components.append(instr2_text)
instr2Components.append(instr2_key_resp)
instr2Components.append(instr2_sound)
for thisComponent in instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2_text* updates
    if t >= 0.0 and instr2_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2_text.tStart = t  # underestimates by a little under one frame
        instr2_text.frameNStart = frameN  # exact frame index
        instr2_text.setAutoDraw(True)
    
    # *instr2_key_resp* updates
    if t >= 0.0 and instr2_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2_key_resp.tStart = t  # underestimates by a little under one frame
        instr2_key_resp.frameNStart = frameN  # exact frame index
        instr2_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr2_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr2_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr2_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr2_key_resp.rt = instr2_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop instr2_sound
    if t >= 0.0 and instr2_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2_sound.tStart = t  # underestimates by a little under one frame
        instr2_sound.frameNStart = frameN  # exact frame index
        instr2_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr2_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr3"-------
t = 0
instr3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr3_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr3_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr3Components = []
instr3Components.append(instr3_text)
instr3Components.append(instr3_key_resp)
instr3Components.append(instr3_image)
instr3Components.append(instr3_sound)
for thisComponent in instr3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr3_text* updates
    if t >= 0.0 and instr3_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr3_text.tStart = t  # underestimates by a little under one frame
        instr3_text.frameNStart = frameN  # exact frame index
        instr3_text.setAutoDraw(True)
    
    # *instr3_key_resp* updates
    if t >= 0.0 and instr3_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr3_key_resp.tStart = t  # underestimates by a little under one frame
        instr3_key_resp.frameNStart = frameN  # exact frame index
        instr3_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr3_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr3_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr3_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr3_key_resp.rt = instr3_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *instr3_image* updates
    if t >= 0.0 and instr3_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr3_image.tStart = t  # underestimates by a little under one frame
        instr3_image.frameNStart = frameN  # exact frame index
        instr3_image.setAutoDraw(True)
    # start/stop instr3_sound
    if t >= 0.0 and instr3_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr3_sound.tStart = t  # underestimates by a little under one frame
        instr3_sound.frameNStart = frameN  # exact frame index
        instr3_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3"-------
for thisComponent in instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr3_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr4"-------
t = 0
instr4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr4_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr4_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr4Components = []
instr4Components.append(instr4_text)
instr4Components.append(instr4_key_resp)
instr4Components.append(instr4_image)
instr4Components.append(instr4_sound)
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
    
    # *instr4_text* updates
    if t >= 0.0 and instr4_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr4_text.tStart = t  # underestimates by a little under one frame
        instr4_text.frameNStart = frameN  # exact frame index
        instr4_text.setAutoDraw(True)
    
    # *instr4_key_resp* updates
    if t >= 0.0 and instr4_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr4_key_resp.tStart = t  # underestimates by a little under one frame
        instr4_key_resp.frameNStart = frameN  # exact frame index
        instr4_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr4_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr4_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr4_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr4_key_resp.rt = instr4_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *instr4_image* updates
    if t >= 0.0 and instr4_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr4_image.tStart = t  # underestimates by a little under one frame
        instr4_image.frameNStart = frameN  # exact frame index
        instr4_image.setAutoDraw(True)
    # start/stop instr4_sound
    if t >= 0.0 and instr4_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr4_sound.tStart = t  # underestimates by a little under one frame
        instr4_sound.frameNStart = frameN  # exact frame index
        instr4_sound.play()  # start the sound (it finishes automatically)
    
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
instr4_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr5"-------
t = 0
instr5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr5_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr5_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr5Components = []
instr5Components.append(instr5_text)
instr5Components.append(instr5_key_resp)
instr5Components.append(instr5_image)
instr5Components.append(instr5_sound)
for thisComponent in instr5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr5_text* updates
    if t >= 0.0 and instr5_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr5_text.tStart = t  # underestimates by a little under one frame
        instr5_text.frameNStart = frameN  # exact frame index
        instr5_text.setAutoDraw(True)
    
    # *instr5_key_resp* updates
    if t >= 0.0 and instr5_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr5_key_resp.tStart = t  # underestimates by a little under one frame
        instr5_key_resp.frameNStart = frameN  # exact frame index
        instr5_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr5_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr5_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr5_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr5_key_resp.rt = instr5_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *instr5_image* updates
    if t >= 0.0 and instr5_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr5_image.tStart = t  # underestimates by a little under one frame
        instr5_image.frameNStart = frameN  # exact frame index
        instr5_image.setAutoDraw(True)
    # start/stop instr5_sound
    if t >= 0.0 and instr5_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr5_sound.tStart = t  # underestimates by a little under one frame
        instr5_sound.frameNStart = frameN  # exact frame index
        instr5_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr5"-------
for thisComponent in instr5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
instr5_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "target_syllable"-------
t = 0
target_syllableClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
target_syllable_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
target_syllable_key_resp.status = NOT_STARTED
# keep track of which components have finished
target_syllableComponents = []
target_syllableComponents.append(target_syllable_image)
target_syllableComponents.append(target_syllable_key_resp)
target_syllableComponents.append(target_syllable_sound)
for thisComponent in target_syllableComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_syllable"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_syllableClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *target_syllable_image* updates
    if t >= 0.0 and target_syllable_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_syllable_image.tStart = t  # underestimates by a little under one frame
        target_syllable_image.frameNStart = frameN  # exact frame index
        target_syllable_image.setAutoDraw(True)
    
    # *target_syllable_key_resp* updates
    if t >= 0.0 and target_syllable_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_syllable_key_resp.tStart = t  # underestimates by a little under one frame
        target_syllable_key_resp.frameNStart = frameN  # exact frame index
        target_syllable_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(target_syllable_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if target_syllable_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            target_syllable_key_resp.keys = theseKeys[-1]  # just the last key pressed
            target_syllable_key_resp.rt = target_syllable_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop target_syllable_sound
    if t >= 0.0 and target_syllable_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_syllable_sound.tStart = t  # underestimates by a little under one frame
        target_syllable_sound.frameNStart = frameN  # exact frame index
        target_syllable_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_syllableComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_syllable"-------
for thisComponent in target_syllableComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
target_syllable_sound.stop() #ensure sound has stopped at end of routine
# the Routine "target_syllable" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr6"-------
t = 0
instr6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr6_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr6_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr6Components = []
instr6Components.append(instr6_text)
instr6Components.append(instr6_key_resp)
instr6Components.append(instr6_image)
instr6Components.append(instr6_sound)
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr6_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr6_key_resp.rt = instr6_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *instr6_image* updates
    if t >= 0.0 and instr6_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr6_image.tStart = t  # underestimates by a little under one frame
        instr6_image.frameNStart = frameN  # exact frame index
        instr6_image.setAutoDraw(True)
    # start/stop instr6_sound
    if t >= 0.0 and instr6_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr6_sound.tStart = t  # underestimates by a little under one frame
        instr6_sound.frameNStart = frameN  # exact frame index
        instr6_sound.play()  # start the sound (it finishes automatically)
    
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

#------Prepare to start Routine "target_practice"-------
t = 0
target_practiceClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
target_practice_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
target_practice_key_resp.status = NOT_STARTED
# keep track of which components have finished
target_practiceComponents = []
target_practiceComponents.append(target_practice_text)
target_practiceComponents.append(target_practice_key_resp)
target_practiceComponents.append(target_practice_sound)
for thisComponent in target_practiceComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_practice"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_practiceClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *target_practice_text* updates
    if t >= 0.0 and target_practice_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_practice_text.tStart = t  # underestimates by a little under one frame
        target_practice_text.frameNStart = frameN  # exact frame index
        target_practice_text.setAutoDraw(True)
    
    # *target_practice_key_resp* updates
    if t >= 0.0 and target_practice_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_practice_key_resp.tStart = t  # underestimates by a little under one frame
        target_practice_key_resp.frameNStart = frameN  # exact frame index
        target_practice_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(target_practice_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if target_practice_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            target_practice_key_resp.keys = theseKeys[-1]  # just the last key pressed
            target_practice_key_resp.rt = target_practice_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop target_practice_sound
    if t >= 0.0 and target_practice_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_practice_sound.tStart = t  # underestimates by a little under one frame
        target_practice_sound.frameNStart = frameN  # exact frame index
        target_practice_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_practice"-------
for thisComponent in target_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
target_practice_sound.stop() #ensure sound has stopped at end of routine
# the Routine "target_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr7"-------
t = 0
instr7Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
wait_for_trigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
wait_for_trigger.status = NOT_STARTED
# keep track of which components have finished
instr7Components = []
instr7Components.append(instr7_text)
instr7Components.append(instr7_image)
instr7Components.append(wait_for_trigger)
instr7Components.append(instr7_sound)
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
    
    # *wait_for_trigger* updates
    if t >= 0.0 and wait_for_trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        wait_for_trigger.tStart = t  # underestimates by a little under one frame
        wait_for_trigger.frameNStart = frameN  # exact frame index
        wait_for_trigger.status = STARTED
        # keyboard checking is just starting
        wait_for_trigger.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if wait_for_trigger.status == STARTED:  # only update if being drawn
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
        if len(theseKeys) > 0:  # at least one key was pressed
            wait_for_trigger.keys = theseKeys[-1]  # just the last key pressed
            wait_for_trigger.rt = wait_for_trigger.clock.getTime()
            # abort routine on response
            continueRoutine = False
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            wait_for_trigger.keys = theseKeys[-1]  # just the last key pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop instr7_sound
    if t >= 0.0 and instr7_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr7_sound.tStart = t  # underestimates by a little under one frame
        instr7_sound.frameNStart = frameN  # exact frame index
        instr7_sound.play()  # start the sound (it finishes automatically)
    
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
instr7_sound.stop()
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
fam_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'ssl_run%s.csv'%(str(expInfo['Run']))),
    seed=None, name='fam_trials_loop')
thisExp.addLoop(fam_trials_loop)  # add the loop to the experiment
thisFam_trials_loop = fam_trials_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisFam_trials_loop.rgb)
if thisFam_trials_loop != None:
    for paramName in thisFam_trials_loop.keys():
        exec(paramName + '= thisFam_trials_loop.' + paramName)

for thisFam_trials_loop in fam_trials_loop:
    currentLoop = fam_trials_loop
    # abbreviate parameter names if possible (e.g. rgb = thisFam_trials_loop.rgb)
    if thisFam_trials_loop != None:
        for paramName in thisFam_trials_loop.keys():
            exec(paramName + '= thisFam_trials_loop.' + paramName)
    
    #------Prepare to start Routine "fam_trials"-------
    t = 0
    fam_trialsClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    fam_trials_sound.setSound(soundFile, secs=0.46)
    fam_trials_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    fam_trials_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    fam_trialsComponents = []
    fam_trialsComponents.append(fam_trials_sound)
    fam_trialsComponents.append(fam_trials_key_resp)
    fam_trialsComponents.append(fam_trials_image)
    for thisComponent in fam_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fam_trials"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fam_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop fam_trials_sound
        if t >= 0.0 and fam_trials_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            fam_trials_sound.tStart = t  # underestimates by a little under one frame
            fam_trials_sound.frameNStart = frameN  # exact frame index
            fam_trials_sound.play()  # start the sound (it finishes automatically)
        if fam_trials_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            fam_trials_sound.stop()  # stop the sound (if longer than duration)
        
        # *fam_trials_key_resp* updates
        if t >= 0.0 and fam_trials_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            fam_trials_key_resp.tStart = t  # underestimates by a little under one frame
            fam_trials_key_resp.frameNStart = frameN  # exact frame index
            fam_trials_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(fam_trials_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if fam_trials_key_resp.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
            fam_trials_key_resp.status = STOPPED
        if fam_trials_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                fam_trials_key_resp.keys = theseKeys[-1]  # just the last key pressed
                fam_trials_key_resp.rt = fam_trials_key_resp.clock.getTime()
        
        # *fam_trials_image* updates
        if t >= 0.0 and fam_trials_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            fam_trials_image.tStart = t  # underestimates by a little under one frame
            fam_trials_image.frameNStart = frameN  # exact frame index
            fam_trials_image.setAutoDraw(True)
        if fam_trials_image.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
            fam_trials_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fam_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fam_trials"-------
    for thisComponent in fam_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fam_trials_sound.stop() #ensure sound has stopped at end of routine
    # check responses
    if fam_trials_key_resp.keys in ['', [], None]:  # No response was made
       fam_trials_key_resp.keys=None
    # store data for fam_trials_loop (TrialHandler)
    fam_trials_loop.addData('fam_trials_key_resp.keys',fam_trials_key_resp.keys)
    if fam_trials_key_resp.keys != None:  # we had a response
        fam_trials_loop.addData('fam_trials_key_resp.rt', fam_trials_key_resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'fam_trials_loop'


#------Prepare to start Routine "instr8"-------
t = 0
instr8Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr8_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr8_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr8Components = []
instr8Components.append(instr8_text)
instr8Components.append(instr8_key_resp)
instr8Components.append(instr8_sound)
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
    
    # *instr8_text* updates
    if t >= 0.0 and instr8_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr8_text.tStart = t  # underestimates by a little under one frame
        instr8_text.frameNStart = frameN  # exact frame index
        instr8_text.setAutoDraw(True)
    
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr8_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr8_key_resp.rt = instr8_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop instr8_sound
    if t >= 0.0 and instr8_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr8_sound.tStart = t  # underestimates by a little under one frame
        instr8_sound.frameNStart = frameN  # exact frame index
        instr8_sound.play()  # start the sound (it finishes automatically)
    
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


thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()