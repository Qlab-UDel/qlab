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

expName = 'auditory_instruction'  # from the Builder filename that created this script


expName = 'auditory'  # from the Builder filename that created this script
# Store info about the experiment session
expInfo = {u'starget': u'', u'ttarget': u'', u'PartID': u''} # block: R(andom) and S(equential); target: then bi, pu, du, da; 
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['Run'] = "1"



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
    text='Press any button to begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instr2_text = visual.TextStim(win=win, ori=0, name='instr2_text',
    text=u"Hi! We're playing a listening game today.",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)


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


# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
instr4_text = visual.TextStim(win=win, ori=0, name='instr4_text',
    text=u"Meeple is from Planet B. We're going to listen to Meeple speak her alien language and play a song for us.",    font=u'Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr4_image = visual.ImageStim(win=win, name='instr4_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


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

# Initialize components for Routine "target_syllable"
target_syllableClock = core.Clock()
target_syllable_image = visual.ImageStim(win=win, name='target_syllable_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
target_syllable_sound = sound.Sound('%s.wav' % str(expInfo['starget']), secs=-1)
target_syllable_sound.setVolume(1)

# Initialize components for Routine "instr6"
instr6Clock = core.Clock()
instr6_text = visual.TextStim(win=win, ori=0, name='instr6_text',
    text=u"When you hear Meeple say her favorite word, press the button as soon as you can. Let's practice!",    font=u'Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr6_image = visual.ImageStim(win=win, name='instr6_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "target_practice"
target_practiceClock = core.Clock()
target_practice_text = visual.TextStim(win=win, ori=0, name='target_practice_text',
    text='Press the button!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
target_practice_sound = sound.Sound('%s.wav' % str(expInfo['starget']), secs=-1)
target_practice_sound.setVolume(1)

# Initialize components for Routine "instr7"
instr7Clock = core.Clock()
instr7_text = visual.TextStim(win=win, ori=0, name='instr7_text',
    text=u"Good job! Meeple will also play her favorite note for us. Listen carefully",    font=u'Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr7_image = visual.ImageStim(win=win, name='instr7_image',
    image=u'Alien11.BMP', mask=None,
    ori=0, pos=[0.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "target_tone"
target_toneClock = core.Clock()
sound_12 = sound.Sound(u'%s.wav' % str(expInfo['ttarget']), secs=-1)
sound_12.setVolume(1)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='Press the button.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instr11"
instr11Clock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text="When you hear Meeple play her favorite note, press the button as soon as you can.",    font='Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_14 = visual.ImageStim(win=win, name='image_14',
    image='Alien11.BMP', mask=None,
    ori=0, pos=[.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr3_6"
instr3_6Clock = core.Clock()
text_41 = visual.TextStim(win=win, ori=0, name='text_41',
    text='Now Meeple is going to play six notes in a row. \nPress space when you hear her favorite note!',    font='Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_31 = visual.ImageStim(win=win, name='image_31',
    image='Alien11.BMP', mask=None,
    ori=0, pos=[.5,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "six_tones_1"
six_tones_1Clock = core.Clock()
sound_43 = sound.Sound('A', secs=-1)
sound_43.setVolume(1)
image_32 = visual.ImageStim(win=win, name='image_32',
    image='Alien11.BMP', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr3_7"
instr3_7Clock = core.Clock()
text_42 = visual.TextStim(win=win, ori=0, name='text_42',
    text="Did you hear it? The fourth\nnote was Meeple's favorite\nnote! Let's listen again...",    font='Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_33 = visual.ImageStim(win=win, name='image_33',
    image='Alien11.BMP', mask=None,
    ori=0, pos=[.5,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "six_tones_1"
six_tones_1Clock = core.Clock()
sound_43 = sound.Sound('A', secs=-1)
sound_43.setVolume(1)
image_32 = visual.ImageStim(win=win, name='image_32',
    image='Alien11.BMP', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr3_5"
instr3_5Clock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text="Are you ready for the game? Let's get started. Remember to press the button when you hear Meeple's favorite word or note.",    font='Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_15 = visual.ImageStim(win=win, name='image_15',
    image='Alien11.BMP', mask=None,
    ori=0, pos=[.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)



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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr1_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr1_key_resp.rt = instr1_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr2_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr2_key_resp.rt = instr2_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
        
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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
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
routineTimer.reset()



#------Prepare to start Routine "target_tone"-------
t = 0
target_toneClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_12.status = NOT_STARTED
# keep track of which components have finished
target_toneComponents = []
target_toneComponents.append(sound_12)
target_toneComponents.append(key_resp_12)
target_toneComponents.append(text_10)
for thisComponent in target_toneComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_tone"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_toneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_12
    if t >= 0.0 and sound_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_12.tStart = t  # underestimates by a little under one frame
        sound_12.frameNStart = frameN  # exact frame index
        sound_12.play()  # start the sound (it finishes automatically)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # underestimates by a little under one frame
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # underestimates by a little under one frame
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_toneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_tone"-------
for thisComponent in target_toneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_12.stop() #ensure sound has stopped at end of routine
# the Routine "target_tone" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


#------Prepare to start Routine "instr11"-------
t = 0
instr11Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_10.status = NOT_STARTED
# keep track of which components have finished
instr11Components = []
instr11Components.append(text_8)
instr11Components.append(image_14)
instr11Components.append(key_resp_10)
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
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # underestimates by a little under one frame
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    
    # *image_14* updates
    if t >= 0.0 and image_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_14.tStart = t  # underestimates by a little under one frame
        image_14.frameNStart = frameN  # exact frame index
        image_14.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t  # underestimates by a little under one frame
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
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
# the Routine "instr11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr3_6"-------
t = 0
instr3_6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_27 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_27.status = NOT_STARTED
# keep track of which components have finished
instr3_6Components = []
instr3_6Components.append(text_41)
instr3_6Components.append(image_31)
instr3_6Components.append(key_resp_27)
for thisComponent in instr3_6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_41* updates
    if t >= 0.0 and text_41.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_41.tStart = t  # underestimates by a little under one frame
        text_41.frameNStart = frameN  # exact frame index
        text_41.setAutoDraw(True)
    
    # *image_31* updates
    if t >= 0.0 and image_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_31.tStart = t  # underestimates by a little under one frame
        image_31.frameNStart = frameN  # exact frame index
        image_31.setAutoDraw(True)
    
    # *key_resp_27* updates
    if t >= 0.0 and key_resp_27.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_27.tStart = t  # underestimates by a little under one frame
        key_resp_27.frameNStart = frameN  # exact frame index
        key_resp_27.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_27.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_6"-------
for thisComponent in instr3_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr3_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'six_tones_%s.xlsx' % str(expInfo['ttarget'])),
    seed=None, name='practice_trials_1')
thisPractice_trial_1 = practice_trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_trial_1.rgb)
if thisPractice_trial_1 != None:
    for paramName in thisPractice_trial_1.keys():
        exec(paramName + '= thisPractice_trial_1.' + paramName)

for thisPractice_trial_1 in practice_trials_1:
    currentLoop = practice_trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial_1.rgb)
    if thisPractice_trial_1 != None:
        for paramName in thisPractice_trial_1.keys():
            exec(paramName + '= thisPractice_trial_1.' + paramName)
    
    #------Prepare to start Routine "six_tones_1"-------
    t = 0
    six_tones_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_43.setSound(soundFile, secs=0.46)
    practice_trial_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    practice_trial_1.status = NOT_STARTED
    # keep track of which components have finished
    six_tones_1Components = []
    six_tones_1Components.append(sound_43)
    six_tones_1Components.append(image_32)
    six_tones_1Components.append(practice_trial_1)
    for thisComponent in six_tones_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "six_tones_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = six_tones_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_43
        if t >= 0.0 and sound_43.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_43.tStart = t  # underestimates by a little under one frame
            sound_43.frameNStart = frameN  # exact frame index
            sound_43.play()  # start the sound (it finishes automatically)
        if sound_43.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_43.stop()  # stop the sound (if longer than duration)
        
        # *image_32* updates
        if t >= 0.0 and image_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_32.tStart = t  # underestimates by a little under one frame
            image_32.frameNStart = frameN  # exact frame index
            image_32.setAutoDraw(True)
        if image_32.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_32.setAutoDraw(False)
        
        # *practice_trial_1* updates
        if t >= 0.0 and practice_trial_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_trial_1.tStart = t  # underestimates by a little under one frame
            practice_trial_1.frameNStart = frameN  # exact frame index
            practice_trial_1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(practice_trial_1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if practice_trial_1.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_trial_1.status = STOPPED
        if practice_trial_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practice_trial_1.keys = theseKeys[-1]  # just the last key pressed
                practice_trial_1.rt = practice_trial_1.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in six_tones_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "six_tones_1"-------
    for thisComponent in six_tones_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_43.stop() #ensure sound has stopped at end of routine
    
# completed 1 repeats of 'practice_trials_1'

#------Prepare to start Routine "instr3_7"-------
t = 0
instr3_7Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_28 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_28.status = NOT_STARTED
# keep track of which components have finished
instr3_7Components = []
instr3_7Components.append(text_42)
instr3_7Components.append(image_33)
instr3_7Components.append(key_resp_28)
for thisComponent in instr3_7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_7"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_42* updates
    if t >= 0.0 and text_42.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_42.tStart = t  # underestimates by a little under one frame
        text_42.frameNStart = frameN  # exact frame index
        text_42.setAutoDraw(True)
    
    # *image_33* updates
    if t >= 0.0 and image_33.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_33.tStart = t  # underestimates by a little under one frame
        image_33.frameNStart = frameN  # exact frame index
        image_33.setAutoDraw(True)
    
    # *key_resp_28* updates
    if t >= 0.0 and key_resp_28.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_28.tStart = t  # underestimates by a little under one frame
        key_resp_28.frameNStart = frameN  # exact frame index
        key_resp_28.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_28.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_7"-------
for thisComponent in instr3_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr3_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'six_tones_%s.xlsx' % str(expInfo['ttarget'])),
    seed=None, name='practice_trials_2')
thisPractice_trial_2 = practice_trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_trial_2.rgb)
if thisPractice_trial_2 != None:
    for paramName in thisPractice_trial_2.keys():
        exec(paramName + '= thisPractice_trial_2.' + paramName)

for thisPractice_trial_2 in practice_trials_2:
    currentLoop = practice_trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial_2.rgb)
    if thisPractice_trial_2 != None:
        for paramName in thisPractice_trial_2.keys():
            exec(paramName + '= thisPractice_trial_2.' + paramName)
    
    #------Prepare to start Routine "six_tones_1"-------
    t = 0
    six_tones_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    sound_43.setSound(soundFile, secs=0.46)
    practice_trial_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    practice_trial_1.status = NOT_STARTED
    # keep track of which components have finished
    six_tones_1Components = []
    six_tones_1Components.append(sound_43)
    six_tones_1Components.append(image_32)
    six_tones_1Components.append(practice_trial_1)
    for thisComponent in six_tones_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "six_tones_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = six_tones_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_43
        if t >= 0.0 and sound_43.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_43.tStart = t  # underestimates by a little under one frame
            sound_43.frameNStart = frameN  # exact frame index
            sound_43.play()  # start the sound (it finishes automatically)
        if sound_43.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_43.stop()  # stop the sound (if longer than duration)
        
        # *image_32* updates
        if t >= 0.0 and image_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_32.tStart = t  # underestimates by a little under one frame
            image_32.frameNStart = frameN  # exact frame index
            image_32.setAutoDraw(True)
        if image_32.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_32.setAutoDraw(False)
        
        # *practice_trial_1* updates
        if t >= 0.0 and practice_trial_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_trial_1.tStart = t  # underestimates by a little under one frame
            practice_trial_1.frameNStart = frameN  # exact frame index
            practice_trial_1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(practice_trial_1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if practice_trial_1.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_trial_1.status = STOPPED
        if practice_trial_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practice_trial_1.keys = theseKeys[-1]  # just the last key pressed
                practice_trial_1.rt = practice_trial_1.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in six_tones_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "six_tones_1"-------
    for thisComponent in six_tones_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_43.stop() #ensure sound has stopped at end of routine
    # check responses
    if practice_trial_1.keys in ['', [], None]:  # No response was made
       practice_trial_1.keys=None
    # store data for practice_trials_2 (TrialHandler)
    practice_trials_2.addData('practice_trial_1.keys',practice_trial_1.keys)
    if practice_trial_1.keys != None:  # we had a response
        practice_trials_2.addData('practice_trial_1.rt', practice_trial_1.rt)
     
# completed 1 repeats of 'practice_trials_2'

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
# the Routine "instr3_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
