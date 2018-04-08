#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Wed Apr 26 08:10:22 2017
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
expName = 'ssl'  # from the Builder filename that created this script
expInfo = {u'language': u'', u'target': u'', u'PartID': u'', u'block': u''} # block: R(andom) and S(equential); language: 1 or 2; target: if block 1, then bi, pu, du, da; if block 2, then ku, tu, pi, do.
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' %(expInfo['PartID'], expName, expInfo['block'], expInfo['date'])

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

# Initialize components for Routine "instr9"
instr9Clock = core.Clock()
instr9_text = visual.TextStim(win=win, ori=0, name='instr9_text',
    text='Now look at these two aliens:',    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr9_image = visual.ImageStim(win=win, name='instr9_image',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -0.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instr9_sound = sound.Sound(u'ssl_instr9.wav', secs=-1)
instr9_sound.setVolume(1)

# Initialize components for Routine "instr10"
instr10Clock = core.Clock()
instr10_text = visual.TextStim(win=win, ori=0, name='instr10_text',
    text=u"Each of these aliens will say a short phrase. Please try your best to identify which phrase sounds more like Meeple's language. If you don't know the answer, just give your best guess!\n\nPress the left arrow if the first alien's phrase sounds more like Meeple's language, and press the right arrow if the second alien's phrase sounds more like Meeple's language.",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr10_sound = sound.Sound(u'ssl_instr10.wav', secs=-1)
instr10_sound.setVolume(1)

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instr1_text = visual.TextStim(win=win, ori=0, name='instr1_text',
    text='Press the spacebar to begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr1_sound = sound.Sound(u'ssl_instr1.wav', secs=-1)
instr1_sound.setVolume(1)

# Initialize components for Routine "test1"
test1Clock = core.Clock()
test1_image = visual.ImageStim(win=win, name='test1_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test1_sound = sound.Sound('A', secs=-1)
test1_sound.setVolume(1)
test1_text = visual.TextStim(win=win, ori=0, name='test1_text',
    text=u"Which phrase is like Meeple's?\nPress left for first and right for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test2"
test2Clock = core.Clock()
test2_image = visual.ImageStim(win=win, name='test2_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test2_sound = sound.Sound('A', secs=-1)
test2_sound.setVolume(1)
test2_text = visual.TextStim(win=win, ori=0, name='test2_text',
    text=u"Which phrase is like Meeple's?\nPress left for first and right for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test3"
test3Clock = core.Clock()
test3_image = visual.ImageStim(win=win, name='test3_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test3_sound = sound.Sound('A', secs=-1)
test3_sound.setVolume(1)
test3_text = visual.TextStim(win=win, ori=0, name='test3_text',
    text=u"Which phrase is like Meeple's?\nPress left for first and right for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "triplet_pause"
triplet_pauseClock = core.Clock()
triplet_pause_image = visual.ImageStim(win=win, name='triplet_pause_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
triplet_pause_text = visual.TextStim(win=win, ori=0, name='triplet_pause_text',
    text=u"Which phrase is like Meeple's?\nPress left for first and right for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "test4"
test4Clock = core.Clock()
test4_image = visual.ImageStim(win=win, name='test4_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test4_sound = sound.Sound('A', secs=-1)
test4_sound.setVolume(1)
test4_text = visual.TextStim(win=win, ori=0, name='test4_text',
    text=u"Which phrase is like Meeple's?\nPress left for first and right for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test5"
test5Clock = core.Clock()
test5_image = visual.ImageStim(win=win, name='test5_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test5_sound = sound.Sound('A', secs=-1)
test5_sound.setVolume(1)
test5_text = visual.TextStim(win=win, ori=0, name='test5_text',
    text=u"Which phrase is like Meeple's?\nPress left for first and right for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test6"
test6Clock = core.Clock()
test6_image = visual.ImageStim(win=win, name='test6_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
test6_sound = sound.Sound('A', secs=-1)
test6_sound.setVolume(1)
test6_text = visual.TextStim(win=win, ori=0, name='test6_text',
    text=u"Which phrase is like Meeple's?\nPress left for first and right for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "question"
questionClock = core.Clock()
question_image = visual.ImageStim(win=win, name='question_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
question_text = visual.TextStim(win=win, ori=0, name='question_text',
    text=u"Which phrase is like Meeple's?\nPress left for first and right for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "gap"
gapClock = core.Clock()
gap_text = visual.TextStim(win=win, ori=0, name='gap_text',
    text=u'Please wait...',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, ori=0, name='end_text',
    text=u"Great, you're all done! Thank you :) Press any key to exit.",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
end_sound = sound.Sound(u'ssl_instr11.wav', secs=-1)
end_sound.setVolume(1)

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
# check responses
if instr1_key_resp.keys in ['', [], None]:  # No response was made
   instr1_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr1_key_resp.keys',instr1_key_resp.keys)
if instr1_key_resp.keys != None:  # we had a response
    thisExp.addData('instr1_key_resp.rt', instr1_key_resp.rt)
thisExp.nextEntry()
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
# check responses
if instr2_key_resp.keys in ['', [], None]:  # No response was made
   instr2_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr2_key_resp.keys',instr2_key_resp.keys)
if instr2_key_resp.keys != None:  # we had a response
    thisExp.addData('instr2_key_resp.rt', instr2_key_resp.rt)
thisExp.nextEntry()
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
# check responses
if instr3_key_resp.keys in ['', [], None]:  # No response was made
   instr3_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr3_key_resp.keys',instr3_key_resp.keys)
if instr3_key_resp.keys != None:  # we had a response
    thisExp.addData('instr3_key_resp.rt', instr3_key_resp.rt)
thisExp.nextEntry()
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
# check responses
if instr4_key_resp.keys in ['', [], None]:  # No response was made
   instr4_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr4_key_resp.keys',instr4_key_resp.keys)
if instr4_key_resp.keys != None:  # we had a response
    thisExp.addData('instr4_key_resp.rt', instr4_key_resp.rt)
thisExp.nextEntry()
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
# check responses
if instr5_key_resp.keys in ['', [], None]:  # No response was made
   instr5_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr5_key_resp.keys',instr5_key_resp.keys)
if instr5_key_resp.keys != None:  # we had a response
    thisExp.addData('instr5_key_resp.rt', instr5_key_resp.rt)
thisExp.nextEntry()
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
# check responses
if target_syllable_key_resp.keys in ['', [], None]:  # No response was made
   target_syllable_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('target_syllable_key_resp.keys',target_syllable_key_resp.keys)
if target_syllable_key_resp.keys != None:  # we had a response
    thisExp.addData('target_syllable_key_resp.rt', target_syllable_key_resp.rt)
thisExp.nextEntry()
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
# check responses
if instr6_key_resp.keys in ['', [], None]:  # No response was made
   instr6_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr6_key_resp.keys',instr6_key_resp.keys)
if instr6_key_resp.keys != None:  # we had a response
    thisExp.addData('instr6_key_resp.rt', instr6_key_resp.rt)
thisExp.nextEntry()
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
# check responses
if target_practice_key_resp.keys in ['', [], None]:  # No response was made
   target_practice_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('target_practice_key_resp.keys',target_practice_key_resp.keys)
if target_practice_key_resp.keys != None:  # we had a response
    thisExp.addData('target_practice_key_resp.rt', target_practice_key_resp.rt)
thisExp.nextEntry()
target_practice_sound.stop() #ensure sound has stopped at end of routine
# the Routine "target_practice" was not non-slip safe, so reset the non-slip timer
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
instr7Components.append(instr7_text)
instr7Components.append(instr7_image)
instr7Components.append(instr7_key_resp)
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr7_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr7_key_resp.rt = instr7_key_resp.clock.getTime()
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
# check responses
if instr7_key_resp.keys in ['', [], None]:  # No response was made
   instr7_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr7_key_resp.keys',instr7_key_resp.keys)
if instr7_key_resp.keys != None:  # we had a response
    thisExp.addData('instr7_key_resp.rt', instr7_key_resp.rt)
thisExp.nextEntry()
instr7_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
fam_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'%s_fam_seq_%s.xlsx' % (str(expInfo['block']), str(expInfo['language']))),
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
    routineTimer.add(0.460000)
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
# check responses
if instr8_key_resp.keys in ['', [], None]:  # No response was made
   instr8_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr8_key_resp.keys',instr8_key_resp.keys)
if instr8_key_resp.keys != None:  # we had a response
    thisExp.addData('instr8_key_resp.rt', instr8_key_resp.rt)
thisExp.nextEntry()
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
instr9Components.append(instr9_text)
instr9Components.append(instr9_image)
instr9Components.append(instr9_key_resp)
instr9Components.append(instr9_sound)
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr9_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr9_key_resp.rt = instr9_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop instr9_sound
    if t >= 0.0 and instr9_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr9_sound.tStart = t  # underestimates by a little under one frame
        instr9_sound.frameNStart = frameN  # exact frame index
        instr9_sound.play()  # start the sound (it finishes automatically)
    
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
# check responses
if instr9_key_resp.keys in ['', [], None]:  # No response was made
   instr9_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr9_key_resp.keys',instr9_key_resp.keys)
if instr9_key_resp.keys != None:  # we had a response
    thisExp.addData('instr9_key_resp.rt', instr9_key_resp.rt)
thisExp.nextEntry()
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
instr10Components.append(instr10_text)
instr10Components.append(instr10_key_resp)
instr10Components.append(instr10_sound)
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
    
    # *instr10_text* updates
    if t >= 0.0 and instr10_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr10_text.tStart = t  # underestimates by a little under one frame
        instr10_text.frameNStart = frameN  # exact frame index
        instr10_text.setAutoDraw(True)
    
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr10_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr10_key_resp.rt = instr10_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # start/stop instr10_sound
    if t >= 0.0 and instr10_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr10_sound.tStart = t  # underestimates by a little under one frame
        instr10_sound.frameNStart = frameN  # exact frame index
        instr10_sound.play()  # start the sound (it finishes automatically)
    
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
# check responses
if instr10_key_resp.keys in ['', [], None]:  # No response was made
   instr10_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr10_key_resp.keys',instr10_key_resp.keys)
if instr10_key_resp.keys != None:  # we had a response
    thisExp.addData('instr10_key_resp.rt', instr10_key_resp.rt)
thisExp.nextEntry()
instr10_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
# check responses
if instr1_key_resp.keys in ['', [], None]:  # No response was made
   instr1_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr1_key_resp.keys',instr1_key_resp.keys)
if instr1_key_resp.keys != None:  # we had a response
    thisExp.addData('instr1_key_resp.rt', instr1_key_resp.rt)
thisExp.nextEntry()
instr1_sound.stop() #ensure sound has stopped at end of routine
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'%s_forced_test_%s.xlsx' % (str(expInfo['block']), str(expInfo['language']))),
    seed=None, name='test_trials')
thisExp.addLoop(test_trials)  # add the loop to the experiment
thisTest_trial = test_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTest_trial.rgb)
if thisTest_trial != None:
    for paramName in thisTest_trial.keys():
        exec(paramName + '= thisTest_trial.' + paramName)

for thisTest_trial in test_trials:
    currentLoop = test_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
    if thisTest_trial != None:
        for paramName in thisTest_trial.keys():
            exec(paramName + '= thisTest_trial.' + paramName)
    
    #------Prepare to start Routine "test1"-------
    t = 0
    test1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    test1_sound.setSound(soundFile1, secs=0.46)
    # keep track of which components have finished
    test1Components = []
    test1Components.append(test1_image)
    test1Components.append(test1_sound)
    test1Components.append(test1_text)
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
        if test1_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test1_image.setAutoDraw(False)
        # start/stop test1_sound
        if t >= 0.0 and test1_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            test1_sound.tStart = t  # underestimates by a little under one frame
            test1_sound.frameNStart = frameN  # exact frame index
            test1_sound.play()  # start the sound (it finishes automatically)
        if test1_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test1_sound.stop()  # stop the sound (if longer than duration)
        
        # *test1_text* updates
        if t >= 0.0 and test1_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            test1_text.tStart = t  # underestimates by a little under one frame
            test1_text.frameNStart = frameN  # exact frame index
            test1_text.setAutoDraw(True)
        if test1_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test1_text.setAutoDraw(False)
        
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
    test1_sound.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test2"-------
    t = 0
    test2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    test2_sound.setSound(soundFile2, secs=0.46)
    # keep track of which components have finished
    test2Components = []
    test2Components.append(test2_image)
    test2Components.append(test2_sound)
    test2Components.append(test2_text)
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
        if test2_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test2_image.setAutoDraw(False)
        # start/stop test2_sound
        if t >= 0.0 and test2_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            test2_sound.tStart = t  # underestimates by a little under one frame
            test2_sound.frameNStart = frameN  # exact frame index
            test2_sound.play()  # start the sound (it finishes automatically)
        if test2_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test2_sound.stop()  # stop the sound (if longer than duration)
        
        # *test2_text* updates
        if t >= 0.0 and test2_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            test2_text.tStart = t  # underestimates by a little under one frame
            test2_text.frameNStart = frameN  # exact frame index
            test2_text.setAutoDraw(True)
        if test2_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test2_text.setAutoDraw(False)
        
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
    test2_sound.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test3"-------
    t = 0
    test3Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    test3_sound.setSound(soundFile3, secs=0.46)
    # keep track of which components have finished
    test3Components = []
    test3Components.append(test3_image)
    test3Components.append(test3_sound)
    test3Components.append(test3_text)
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
        if test3_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test3_image.setAutoDraw(False)
        # start/stop test3_sound
        if t >= 0.0 and test3_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            test3_sound.tStart = t  # underestimates by a little under one frame
            test3_sound.frameNStart = frameN  # exact frame index
            test3_sound.play()  # start the sound (it finishes automatically)
        if test3_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test3_sound.stop()  # stop the sound (if longer than duration)
        
        # *test3_text* updates
        if t >= 0.0 and test3_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            test3_text.tStart = t  # underestimates by a little under one frame
            test3_text.frameNStart = frameN  # exact frame index
            test3_text.setAutoDraw(True)
        if test3_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test3_text.setAutoDraw(False)
        
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
    test3_sound.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "triplet_pause"-------
    t = 0
    triplet_pauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    triplet_pauseComponents = []
    triplet_pauseComponents.append(triplet_pause_image)
    triplet_pauseComponents.append(triplet_pause_text)
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
        if triplet_pause_image.status == STARTED and t >= (0.0 + (0.75-win.monitorFramePeriod*0.75)): #most of one frame period left
            triplet_pause_image.setAutoDraw(False)
        
        # *triplet_pause_text* updates
        if t >= 0.0 and triplet_pause_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            triplet_pause_text.tStart = t  # underestimates by a little under one frame
            triplet_pause_text.frameNStart = frameN  # exact frame index
            triplet_pause_text.setAutoDraw(True)
        if triplet_pause_text.status == STARTED and t >= (0.0 + (0.75-win.monitorFramePeriod*0.75)): #most of one frame period left
            triplet_pause_text.setAutoDraw(False)
        
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
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    test4_sound.setSound(soundFile4, secs=0.46)
    # keep track of which components have finished
    test4Components = []
    test4Components.append(test4_image)
    test4Components.append(test4_sound)
    test4Components.append(test4_text)
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
        if test4_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test4_image.setAutoDraw(False)
        # start/stop test4_sound
        if t >= 0.0 and test4_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            test4_sound.tStart = t  # underestimates by a little under one frame
            test4_sound.frameNStart = frameN  # exact frame index
            test4_sound.play()  # start the sound (it finishes automatically)
        if test4_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test4_sound.stop()  # stop the sound (if longer than duration)
        
        # *test4_text* updates
        if t >= 0.0 and test4_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            test4_text.tStart = t  # underestimates by a little under one frame
            test4_text.frameNStart = frameN  # exact frame index
            test4_text.setAutoDraw(True)
        if test4_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test4_text.setAutoDraw(False)
        
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
    test4_sound.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test5"-------
    t = 0
    test5Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    test5_sound.setSound(soundFile5, secs=0.46)
    # keep track of which components have finished
    test5Components = []
    test5Components.append(test5_image)
    test5Components.append(test5_sound)
    test5Components.append(test5_text)
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
        if test5_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test5_image.setAutoDraw(False)
        # start/stop test5_sound
        if t >= 0.0 and test5_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            test5_sound.tStart = t  # underestimates by a little under one frame
            test5_sound.frameNStart = frameN  # exact frame index
            test5_sound.play()  # start the sound (it finishes automatically)
        if test5_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test5_sound.stop()  # stop the sound (if longer than duration)
        
        # *test5_text* updates
        if t >= 0.0 and test5_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            test5_text.tStart = t  # underestimates by a little under one frame
            test5_text.frameNStart = frameN  # exact frame index
            test5_text.setAutoDraw(True)
        if test5_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test5_text.setAutoDraw(False)
        
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
    test5_sound.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test6"-------
    t = 0
    test6Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.460000)
    # update component parameters for each repeat
    test6_sound.setSound(soundFile6, secs=0.46)
    # keep track of which components have finished
    test6Components = []
    test6Components.append(test6_image)
    test6Components.append(test6_sound)
    test6Components.append(test6_text)
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
        if test6_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test6_image.setAutoDraw(False)
        # start/stop test6_sound
        if t >= 0.0 and test6_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            test6_sound.tStart = t  # underestimates by a little under one frame
            test6_sound.frameNStart = frameN  # exact frame index
            test6_sound.play()  # start the sound (it finishes automatically)
        if test6_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test6_sound.stop()  # stop the sound (if longer than duration)
        
        # *test6_text* updates
        if t >= 0.0 and test6_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            test6_text.tStart = t  # underestimates by a little under one frame
            test6_text.frameNStart = frameN  # exact frame index
            test6_text.setAutoDraw(True)
        if test6_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            test6_text.setAutoDraw(False)
        
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
    test6_sound.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "question"-------
    t = 0
    questionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    question_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    question_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    questionComponents = []
    questionComponents.append(question_image)
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
        
        # *question_image* updates
        if t >= 0.0 and question_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            question_image.tStart = t  # underestimates by a little under one frame
            question_image.frameNStart = frameN  # exact frame index
            question_image.setAutoDraw(True)
        
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
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
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
    # store data for test_trials (TrialHandler)
    test_trials.addData('question_key_resp.keys',question_key_resp.keys)
    test_trials.addData('question_key_resp.corr', question_key_resp.corr)
    if question_key_resp.keys != None:  # we had a response
        test_trials.addData('question_key_resp.rt', question_key_resp.rt)
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "gap"-------
    t = 0
    gapClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    gapComponents = []
    gapComponents.append(gap_text)
    for thisComponent in gapComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "gap"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = gapClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *gap_text* updates
        if t >= 0.0 and gap_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            gap_text.tStart = t  # underestimates by a little under one frame
            gap_text.frameNStart = frameN  # exact frame index
            gap_text.setAutoDraw(True)
        if gap_text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            gap_text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in gapComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "gap"-------
    for thisComponent in gapComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'test_trials'


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
endComponents.append(end_key_resp)
endComponents.append(end_sound)
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
    # start/stop end_sound
    if t >= 0.0 and end_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_sound.tStart = t  # underestimates by a little under one frame
        end_sound.frameNStart = frameN  # exact frame index
        end_sound.play()  # start the sound (it finishes automatically)
    
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
# check responses
if end_key_resp.keys in ['', [], None]:  # No response was made
   end_key_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('end_key_resp.keys',end_key_resp.keys)
if end_key_resp.keys != None:  # we had a response
    thisExp.addData('end_key_resp.rt', end_key_resp.rt)
thisExp.nextEntry()
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
