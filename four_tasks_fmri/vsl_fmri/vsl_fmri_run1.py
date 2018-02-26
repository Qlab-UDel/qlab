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
expName = 'vsl'  # from the Builder filename that created this script
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
    monitor=u'testMonitor', color=u'white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "first_instruction"
first_instructionClock = core.Clock()
first_instruction_text = visual.TextStim(win=win, ori=0, name='first_instruction_text',
    text=u'Parts of the experiment require that you press the spacebar to continue. Please remember to always listen to and read the instructions completely before pressing the spacebar.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
first_instruction_sound = sound.Sound(u'first_instruction.wav', secs=-1)
first_instruction_sound.setVolume(1)

# Initialize components for Routine "explain_aliens_task"
explain_aliens_taskClock = core.Clock()
explain_aliens_task_text = visual.TextStim(win=win, ori=0, name='explain_aliens_task_text',
    text=u'Hi there! Today you are going to see some aliens line up to enter a cool spaceship. We need you to help us keep track of a very special alien as the aliens line up to enter the spaceship. We\u2019ll show you the alien now.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
explain_aliens_task_sound = sound.Sound(u'explain_aliens.wav', secs=-1)
explain_aliens_task_sound.setVolume(1)

# Initialize components for Routine "show_target_alien"
show_target_alienClock = core.Clock()
show_target_alien_image = visual.ImageStim(win=win, name='show_target_alien_image',
    image=u'Alien%s.BMP' % str(expInfo['target']), mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "spaceship1"
spaceship1Clock = core.Clock()
spaceship1_image = visual.ImageStim(win=win, name='spaceship1_image',
    image=u'Spaceship1.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
spaceship1_sound = sound.Sound(u'spaceship1.wav', secs=-1)
spaceship1_sound.setVolume(1)

# Initialize components for Routine "spaceship2"
spaceship2Clock = core.Clock()
spaceship2_image = visual.ImageStim(win=win, name='spaceship2_image',
    image=u'Spaceship2.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "spaceship3"
spaceship3Clock = core.Clock()
spaceship3_image = visual.ImageStim(win=win, name='spaceship3_image',
    image=u'Spaceship3.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
spaceship3_sound = sound.Sound(u'spaceship3.wav', secs=-1)
spaceship3_sound.setVolume(1)

# Initialize components for Routine "ladder1"
ladder1Clock = core.Clock()
ladder1_image = visual.ImageStim(win=win, name='ladder1_image',
    image=u'Ladder1.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ladder1_sound = sound.Sound(u'ladder1.wav', secs=-1)
ladder1_sound.setVolume(1)

# Initialize components for Routine "ladder2"
ladder2Clock = core.Clock()
ladder2_image = visual.ImageStim(win=win, name='ladder2_image',
    image=u'Ladder2.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ladder2_sound = sound.Sound(u'ladder2.wav', secs=-1)
ladder2_sound.setVolume(1)

# Initialize components for Routine "ladder3"
ladder3Clock = core.Clock()
ladder3_image = visual.ImageStim(win=win, name='ladder3_image',
    image=u'Ladder3.bmp', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ladder3_sound = sound.Sound(u'ladder3.wav', secs=-1)
ladder3_sound.setVolume(1)

# Initialize components for Routine "target_alien_reminder"
target_alien_reminderClock = core.Clock()
target_alien_reminder_image = visual.ImageStim(win=win, name='target_alien_reminder_image',
    image=u'Alien%s.BMP' % str(expInfo['target']), mask=None,
    ori=0, pos=[0, -0.3], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
target_alien_reminder_text = visual.TextStim(win=win, ori=0, name='target_alien_reminder_text',
    text=u'Remember, this is the special alien to keep track of. The aliens will appear one at a time on the screen as they line up. To keep track of our special alien, press the spacebar whenever you see it. ',    font=u'Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
target_alien_reminder_sound = sound.Sound(u'target_alien_reminder.wav', secs=-1)
target_alien_reminder_sound.setVolume(1)

# Initialize components for Routine "fam_block_trial"
fam_block_trialClock = core.Clock()
fam_block_trial_image = visual.ImageStim(win=win, name='fam_block_trial_image',
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

#------Prepare to start Routine "first_instruction"-------
t = 0
first_instructionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
first_instruction_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
first_instruction_key_resp.status = NOT_STARTED
# keep track of which components have finished
first_instructionComponents = []
first_instructionComponents.append(first_instruction_text)
first_instructionComponents.append(first_instruction_sound)
first_instructionComponents.append(first_instruction_key_resp)
for thisComponent in first_instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "first_instruction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = first_instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *first_instruction_text* updates
    if t >= 0.0 and first_instruction_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        first_instruction_text.tStart = t  # underestimates by a little under one frame
        first_instruction_text.frameNStart = frameN  # exact frame index
        first_instruction_text.setAutoDraw(True)
    # start/stop first_instruction_sound
    if t >= 0.0 and first_instruction_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        first_instruction_sound.tStart = t  # underestimates by a little under one frame
        first_instruction_sound.frameNStart = frameN  # exact frame index
        first_instruction_sound.play()  # start the sound (it finishes automatically)
    
    # *first_instruction_key_resp* updates
    if t >= 0.0 and first_instruction_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        first_instruction_key_resp.tStart = t  # underestimates by a little under one frame
        first_instruction_key_resp.frameNStart = frameN  # exact frame index
        first_instruction_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(first_instruction_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if first_instruction_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            first_instruction_key_resp.keys = theseKeys[-1]  # just the last key pressed
            first_instruction_key_resp.rt = first_instruction_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in first_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "first_instruction"-------
for thisComponent in first_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
first_instruction_sound.stop() #ensure sound has stopped at end of routine
# the Routine "first_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "explain_aliens_task"-------
t = 0
explain_aliens_taskClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
explain_aliens_task_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
explain_aliens_task_key_resp.status = NOT_STARTED
# keep track of which components have finished
explain_aliens_taskComponents = []
explain_aliens_taskComponents.append(explain_aliens_task_text)
explain_aliens_taskComponents.append(explain_aliens_task_sound)
explain_aliens_taskComponents.append(explain_aliens_task_key_resp)
for thisComponent in explain_aliens_taskComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "explain_aliens_task"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = explain_aliens_taskClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *explain_aliens_task_text* updates
    if t >= 0.0 and explain_aliens_task_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        explain_aliens_task_text.tStart = t  # underestimates by a little under one frame
        explain_aliens_task_text.frameNStart = frameN  # exact frame index
        explain_aliens_task_text.setAutoDraw(True)
    # start/stop explain_aliens_task_sound
    if t >= 0.0 and explain_aliens_task_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        explain_aliens_task_sound.tStart = t  # underestimates by a little under one frame
        explain_aliens_task_sound.frameNStart = frameN  # exact frame index
        explain_aliens_task_sound.play()  # start the sound (it finishes automatically)
    
    # *explain_aliens_task_key_resp* updates
    if t >= 0.0 and explain_aliens_task_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        explain_aliens_task_key_resp.tStart = t  # underestimates by a little under one frame
        explain_aliens_task_key_resp.frameNStart = frameN  # exact frame index
        explain_aliens_task_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(explain_aliens_task_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if explain_aliens_task_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            explain_aliens_task_key_resp.keys = theseKeys[-1]  # just the last key pressed
            explain_aliens_task_key_resp.rt = explain_aliens_task_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in explain_aliens_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "explain_aliens_task"-------
for thisComponent in explain_aliens_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
explain_aliens_task_sound.stop() #ensure sound has stopped at end of routine
# the Routine "explain_aliens_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "show_target_alien"-------
t = 0
show_target_alienClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
show_target_alien_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
show_target_alien_key_resp.status = NOT_STARTED
# keep track of which components have finished
show_target_alienComponents = []
show_target_alienComponents.append(show_target_alien_image)
show_target_alienComponents.append(show_target_alien_key_resp)
for thisComponent in show_target_alienComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "show_target_alien"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = show_target_alienClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *show_target_alien_image* updates
    if t >= 0.0 and show_target_alien_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        show_target_alien_image.tStart = t  # underestimates by a little under one frame
        show_target_alien_image.frameNStart = frameN  # exact frame index
        show_target_alien_image.setAutoDraw(True)
    
    # *show_target_alien_key_resp* updates
    if t >= 0.0 and show_target_alien_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        show_target_alien_key_resp.tStart = t  # underestimates by a little under one frame
        show_target_alien_key_resp.frameNStart = frameN  # exact frame index
        show_target_alien_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(show_target_alien_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if show_target_alien_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            show_target_alien_key_resp.keys = theseKeys[-1]  # just the last key pressed
            show_target_alien_key_resp.rt = show_target_alien_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in show_target_alienComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "show_target_alien"-------
for thisComponent in show_target_alienComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "show_target_alien" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "spaceship1"-------
t = 0
spaceship1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
spaceship1_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
spaceship1_key_resp.status = NOT_STARTED
# keep track of which components have finished
spaceship1Components = []
spaceship1Components.append(spaceship1_image)
spaceship1Components.append(spaceship1_sound)
spaceship1Components.append(spaceship1_key_resp)
for thisComponent in spaceship1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "spaceship1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = spaceship1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *spaceship1_image* updates
    if t >= 0.0 and spaceship1_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceship1_image.tStart = t  # underestimates by a little under one frame
        spaceship1_image.frameNStart = frameN  # exact frame index
        spaceship1_image.setAutoDraw(True)
    # start/stop spaceship1_sound
    if t >= 0.0 and spaceship1_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceship1_sound.tStart = t  # underestimates by a little under one frame
        spaceship1_sound.frameNStart = frameN  # exact frame index
        spaceship1_sound.play()  # start the sound (it finishes automatically)
    
    # *spaceship1_key_resp* updates
    if t >= 0.0 and spaceship1_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceship1_key_resp.tStart = t  # underestimates by a little under one frame
        spaceship1_key_resp.frameNStart = frameN  # exact frame index
        spaceship1_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spaceship1_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if spaceship1_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            spaceship1_key_resp.keys = theseKeys[-1]  # just the last key pressed
            spaceship1_key_resp.rt = spaceship1_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in spaceship1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "spaceship1"-------
for thisComponent in spaceship1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
spaceship1_sound.stop() #ensure sound has stopped at end of routine
# the Routine "spaceship1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "spaceship2"-------
t = 0
spaceship2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
spaceship2_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
spaceship2_key_resp.status = NOT_STARTED
# keep track of which components have finished
spaceship2Components = []
spaceship2Components.append(spaceship2_image)
spaceship2Components.append(spaceship2_key_resp)
for thisComponent in spaceship2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "spaceship2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = spaceship2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *spaceship2_image* updates
    if t >= 0.0 and spaceship2_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceship2_image.tStart = t  # underestimates by a little under one frame
        spaceship2_image.frameNStart = frameN  # exact frame index
        spaceship2_image.setAutoDraw(True)
    
    # *spaceship2_key_resp* updates
    if t >= 0.0 and spaceship2_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceship2_key_resp.tStart = t  # underestimates by a little under one frame
        spaceship2_key_resp.frameNStart = frameN  # exact frame index
        spaceship2_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spaceship2_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if spaceship2_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            spaceship2_key_resp.keys = theseKeys[-1]  # just the last key pressed
            spaceship2_key_resp.rt = spaceship2_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in spaceship2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "spaceship2"-------
for thisComponent in spaceship2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "spaceship2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "spaceship3"-------
t = 0
spaceship3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
spaceship3_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
spaceship3_key_resp.status = NOT_STARTED
# keep track of which components have finished
spaceship3Components = []
spaceship3Components.append(spaceship3_image)
spaceship3Components.append(spaceship3_sound)
spaceship3Components.append(spaceship3_key_resp)
for thisComponent in spaceship3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "spaceship3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = spaceship3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *spaceship3_image* updates
    if t >= 0.0 and spaceship3_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceship3_image.tStart = t  # underestimates by a little under one frame
        spaceship3_image.frameNStart = frameN  # exact frame index
        spaceship3_image.setAutoDraw(True)
    # start/stop spaceship3_sound
    if t >= 0.0 and spaceship3_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceship3_sound.tStart = t  # underestimates by a little under one frame
        spaceship3_sound.frameNStart = frameN  # exact frame index
        spaceship3_sound.play()  # start the sound (it finishes automatically)
    
    # *spaceship3_key_resp* updates
    if t >= 0.0 and spaceship3_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        spaceship3_key_resp.tStart = t  # underestimates by a little under one frame
        spaceship3_key_resp.frameNStart = frameN  # exact frame index
        spaceship3_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(spaceship3_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if spaceship3_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            spaceship3_key_resp.keys = theseKeys[-1]  # just the last key pressed
            spaceship3_key_resp.rt = spaceship3_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in spaceship3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "spaceship3"-------
for thisComponent in spaceship3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
spaceship3_sound.stop() #ensure sound has stopped at end of routine
# the Routine "spaceship3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "ladder1"-------
t = 0
ladder1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ladder1_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
ladder1_key_resp.status = NOT_STARTED
# keep track of which components have finished
ladder1Components = []
ladder1Components.append(ladder1_image)
ladder1Components.append(ladder1_sound)
ladder1Components.append(ladder1_key_resp)
for thisComponent in ladder1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ladder1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ladder1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ladder1_image* updates
    if t >= 0.0 and ladder1_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder1_image.tStart = t  # underestimates by a little under one frame
        ladder1_image.frameNStart = frameN  # exact frame index
        ladder1_image.setAutoDraw(True)
    # start/stop ladder1_sound
    if t >= 0.0 and ladder1_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder1_sound.tStart = t  # underestimates by a little under one frame
        ladder1_sound.frameNStart = frameN  # exact frame index
        ladder1_sound.play()  # start the sound (it finishes automatically)
    
    # *ladder1_key_resp* updates
    if t >= 0.0 and ladder1_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder1_key_resp.tStart = t  # underestimates by a little under one frame
        ladder1_key_resp.frameNStart = frameN  # exact frame index
        ladder1_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ladder1_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ladder1_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ladder1_key_resp.keys = theseKeys[-1]  # just the last key pressed
            ladder1_key_resp.rt = ladder1_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ladder1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ladder1"-------
for thisComponent in ladder1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
ladder1_sound.stop() #ensure sound has stopped at end of routine
# the Routine "ladder1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "ladder2"-------
t = 0
ladder2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ladder2_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
ladder2_key_resp.status = NOT_STARTED
# keep track of which components have finished
ladder2Components = []
ladder2Components.append(ladder2_image)
ladder2Components.append(ladder2_sound)
ladder2Components.append(ladder2_key_resp)
for thisComponent in ladder2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ladder2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ladder2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ladder2_image* updates
    if t >= 0.0 and ladder2_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder2_image.tStart = t  # underestimates by a little under one frame
        ladder2_image.frameNStart = frameN  # exact frame index
        ladder2_image.setAutoDraw(True)
    # start/stop ladder2_sound
    if t >= 0.0 and ladder2_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder2_sound.tStart = t  # underestimates by a little under one frame
        ladder2_sound.frameNStart = frameN  # exact frame index
        ladder2_sound.play()  # start the sound (it finishes automatically)
    
    # *ladder2_key_resp* updates
    if t >= 0.0 and ladder2_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder2_key_resp.tStart = t  # underestimates by a little under one frame
        ladder2_key_resp.frameNStart = frameN  # exact frame index
        ladder2_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ladder2_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ladder2_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ladder2_key_resp.keys = theseKeys[-1]  # just the last key pressed
            ladder2_key_resp.rt = ladder2_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ladder2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ladder2"-------
for thisComponent in ladder2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
ladder2_sound.stop() #ensure sound has stopped at end of routine
# the Routine "ladder2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "ladder3"-------
t = 0
ladder3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ladder3_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
ladder3_key_resp.status = NOT_STARTED
# keep track of which components have finished
ladder3Components = []
ladder3Components.append(ladder3_image)
ladder3Components.append(ladder3_sound)
ladder3Components.append(ladder3_key_resp)
for thisComponent in ladder3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ladder3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ladder3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ladder3_image* updates
    if t >= 0.0 and ladder3_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder3_image.tStart = t  # underestimates by a little under one frame
        ladder3_image.frameNStart = frameN  # exact frame index
        ladder3_image.setAutoDraw(True)
    # start/stop ladder3_sound
    if t >= 0.0 and ladder3_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder3_sound.tStart = t  # underestimates by a little under one frame
        ladder3_sound.frameNStart = frameN  # exact frame index
        ladder3_sound.play()  # start the sound (it finishes automatically)
    
    # *ladder3_key_resp* updates
    if t >= 0.0 and ladder3_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        ladder3_key_resp.tStart = t  # underestimates by a little under one frame
        ladder3_key_resp.frameNStart = frameN  # exact frame index
        ladder3_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ladder3_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ladder3_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ladder3_key_resp.keys = theseKeys[-1]  # just the last key pressed
            ladder3_key_resp.rt = ladder3_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ladder3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "ladder3"-------
for thisComponent in ladder3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
ladder3_sound.stop() #ensure sound has stopped at end of routine
# the Routine "ladder3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "target_alien_reminder"-------
t = 0
target_alien_reminderClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
target_alien_reminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
target_alien_reminder_key_resp.status = NOT_STARTED
# keep track of which components have finished
target_alien_reminderComponents = []
target_alien_reminderComponents.append(target_alien_reminder_image)
target_alien_reminderComponents.append(target_alien_reminder_text)
target_alien_reminderComponents.append(target_alien_reminder_key_resp)
target_alien_reminderComponents.append(target_alien_reminder_sound)
for thisComponent in target_alien_reminderComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_alien_reminder"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_alien_reminderClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *target_alien_reminder_image* updates
    if t >= 0.0 and target_alien_reminder_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_alien_reminder_image.tStart = t  # underestimates by a little under one frame
        target_alien_reminder_image.frameNStart = frameN  # exact frame index
        target_alien_reminder_image.setAutoDraw(True)
    
    # *target_alien_reminder_text* updates
    if t >= 0.0 and target_alien_reminder_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_alien_reminder_text.tStart = t  # underestimates by a little under one frame
        target_alien_reminder_text.frameNStart = frameN  # exact frame index
        target_alien_reminder_text.setAutoDraw(True)
    
    # *target_alien_reminder_key_resp* updates
    if t >= 0.0 and target_alien_reminder_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_alien_reminder_key_resp.tStart = t  # underestimates by a little under one frame
        target_alien_reminder_key_resp.frameNStart = frameN  # exact frame index
        target_alien_reminder_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(target_alien_reminder_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if target_alien_reminder_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            target_alien_reminder_key_resp.keys = theseKeys[-1]  # just the last key pressed
            target_alien_reminder_key_resp.rt = target_alien_reminder_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop target_alien_reminder_sound
    if t >= 0.0 and target_alien_reminder_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        target_alien_reminder_sound.tStart = t  # underestimates by a little under one frame
        target_alien_reminder_sound.frameNStart = frameN  # exact frame index
        target_alien_reminder_sound.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_alien_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_alien_reminder"-------
for thisComponent in target_alien_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
target_alien_reminder_sound.stop() #ensure sound has stopped at end of routine
# the Routine "target_alien_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
fam_block_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'vsl_run1.xlsx'),
    seed=None, name='fam_block_trials')
thisExp.addLoop(fam_block_trials)  # add the loop to the experiment
thisFam_block_trial = fam_block_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisFam_block_trial.rgb)
if thisFam_block_trial != None:
    for paramName in thisFam_block_trial.keys():
        exec(paramName + '= thisFam_block_trial.' + paramName)

for thisFam_block_trial in fam_block_trials:
    currentLoop = fam_block_trials
    # abbreviate parameter names if possible (e.g. rgb = thisFam_block_trial.rgb)
    if thisFam_block_trial != None:
        for paramName in thisFam_block_trial.keys():
            exec(paramName + '= thisFam_block_trial.' + paramName)
    
    #------Prepare to start Routine "fam_block_trial"-------
    t = 0
    fam_block_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    fam_block_trial_image.setImage(image)
    fam_block_trial_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    fam_block_trial_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    fam_block_trialComponents = []
    fam_block_trialComponents.append(fam_block_trial_image)
    fam_block_trialComponents.append(fam_block_trial_key_resp)
    fam_block_trialComponents.append(blank_image)
    for thisComponent in fam_block_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fam_block_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fam_block_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fam_block_trial_image* updates
        if t >= 0.0 and fam_block_trial_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            fam_block_trial_image.tStart = t  # underestimates by a little under one frame
            fam_block_trial_image.frameNStart = frameN  # exact frame index
            fam_block_trial_image.setAutoDraw(True)
        if fam_block_trial_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            fam_block_trial_image.setAutoDraw(False)
        
        # *fam_block_trial_key_resp* updates
        if t >= 0.0 and fam_block_trial_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            fam_block_trial_key_resp.tStart = t  # underestimates by a little under one frame
            fam_block_trial_key_resp.frameNStart = frameN  # exact frame index
            fam_block_trial_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(fam_block_trial_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if fam_block_trial_key_resp.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            fam_block_trial_key_resp.status = STOPPED
        if fam_block_trial_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                fam_block_trial_key_resp.keys = theseKeys[-1]  # just the last key pressed
                fam_block_trial_key_resp.rt = fam_block_trial_key_resp.clock.getTime()
        
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
        for thisComponent in fam_block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fam_block_trial"-------
    for thisComponent in fam_block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if fam_block_trial_key_resp.keys in ['', [], None]:  # No response was made
       fam_block_trial_key_resp.keys=None
    # store data for fam_block_trials (TrialHandler)
    fam_block_trials.addData('fam_block_trial_key_resp.keys',fam_block_trial_key_resp.keys)
    if fam_block_trial_key_resp.keys != None:  # we had a response
        fam_block_trials.addData('fam_block_trial_key_resp.rt', fam_block_trial_key_resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'fam_block_trials'


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
