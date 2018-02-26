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
import random

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'vl'  # from the Builder filename that created this script
expInfo = {u'PartID': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' %(expInfo['PartID'], expName)


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

ltarget = ['W','Y','A','C']
vtarget = ['Alien6','Alien13','Alien9','Alien22']
random.shuffle(vtarget)
random.shuffle(ltarget)

firstTarg = vtarget[1]
secondTarg = ltarget[1]


# Initialize components for Routine "start"
startClock = core.Clock()
start_text = visual.TextStim(win=win, ori=0, name='start_text',
    text=u"Are you ready? Let's get started!",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "firstTarget"
firstTargetClock = core.Clock()
firstTarget_image = visual.ImageStim(win=win, name='firstTarget_image',
    image=u'%s.png' % str(firstTarg), mask=None,
    ori=0, pos=[0, -0.3], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
firstTarget_text = visual.TextStim(win=win, ori=0, name='firstTarget_text',
    text='Press the button when you see this!',    font='Arial',
    pos=[0, 0.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
firstTarget_sound = sound.Sound(u'reminder.wav', secs=-1)
firstTarget_sound.setVolume(1)


# Initialize components for Routine "secondTarget"
secondTargetClock = core.Clock()
secondTarget_image = visual.ImageStim(win=win, name='secondTarget_image',
    image='%s.png' % str(secondTarg), mask=None,
    ori=0, pos=[0, -0.3], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
secondTarget_text = visual.TextStim(win=win, ori=0, name='secondTarget_text',
    text='Press the button when you see this!',    font='Arial',
    pos=[-.0, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
secondTarget_sound = sound.Sound(u'reminder.wav', secs=-1)
secondTarget_sound.setVolume(1)

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

# Initialize components for Routine "vsl1"
vsl1Clock = core.Clock()
vsl1_image = visual.ImageStim(win=win, name='vsl1_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
vsl1_blank_image = visual.ImageStim(win=win, name='vsl1_blank_image',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "vsl2"
vsl2Clock = core.Clock()
vsl2_image = visual.ImageStim(win=win, name='vsl2_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
vsl2_blank_image = visual.ImageStim(win=win, name='vsl2_blank_image',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "vsl3"
vsl3Clock = core.Clock()
vsl3_image = visual.ImageStim(win=win, name='vsl3_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
vsl3_blank_image = visual.ImageStim(win=win, name='vsl3_blank_image',
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

# Initialize components for Routine "vsl4"
vsl4Clock = core.Clock()
vsl4_image = visual.ImageStim(win=win, name='vsl4_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
vsl4_blank_image = visual.ImageStim(win=win, name='vsl4_blank_image',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "vsl5"
vsl5Clock = core.Clock()
vsl5_image = visual.ImageStim(win=win, name='vsl5_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
vsl5_blank_image = visual.ImageStim(win=win, name='vsl5_blank_image',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "vsl6"
vsl6Clock = core.Clock()
vsl6_image = visual.ImageStim(win=win, name='vsl6_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
vsl6_blank_image = visual.ImageStim(win=win, name='vsl6_blank_image',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "vsl_question"
vsl_questionClock = core.Clock()
vsl_question_text = visual.TextStim(win=win, ori=0, name='vsl_question_text',
    text=u'Which group lined up together? Press the green button for first and red button for second. ',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
    
blockList= ['sv_1','sv_2','sv_3','sv_4','sv_5','sv_6','rl_1','rl_2','rl_3','rl_4','rl_5','rl_6']
    
random.shuffle(blockList)


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

for fileName in blockList:
    if (fileName[1:2]=='l'):
        #------Prepare to start Routine "secondTarget"-------
        t = 0
        secondTargetClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.00000)
        # update component parameters for each repeat
        secondTarget_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        secondTarget_key_resp.status = NOT_STARTED
        # keep track of which components have finished
        secondTargetComponents = []
        secondTargetComponents.append(secondTarget_sound)
        
        for thisComponent in secondTargetComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
            
            #-------Start Routine "secondTarget"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = secondTargetClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
             
            # *secondTarget_image* updates
            if t >= 0.0 and secondTarget_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                secondTarget_image.tStart = t  # underestimates by a little under one frame
                secondTarget_image.frameNStart = frameN  # exact frame index
                secondTarget_image.draw()
                
            # *secondTarget_text* updates
            if t >= 0.0 and secondTarget_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                secondTarget_text.tStart = t  # underestimates by a little under one frame
                secondTarget_text.frameNStart = frameN  # exact frame index
                secondTarget_text.draw()
        
            
            # start/stop secondTarget_sound
            if t >= 0.0 and secondTarget_sound.status == NOT_STARTED:
                # keep track of start time/frame for later
                secondTarget_sound.tStart = t  # underestimates by a little under one frame
                secondTarget_sound.frameNStart = frameN  # exact frame index
                secondTarget_sound.play()  # start the sound (it finishes automatically)
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in secondTargetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            
        #-------Ending Routine "secondTarget"-------
        for thisComponent in secondTargetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
        secondTarget_sound.stop() #ensure sound has stopped at end of routine
        # the Routine "secondTarget" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
            
            
            
            
        # set up handler to look after randomisation of conditions etc
        l_block_trial_loop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'%s.xlsx'%(str(fileName))),
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
            
            
            
    elif (fileName[1:2] == 'v'):
        #------Prepare to start Routine "firstTarget"-------
        t = 0
        firstTargetClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.00000)
        # update component parameters for each repeat
        firstTarget_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        firstTarget_key_resp.status = NOT_STARTED
        # keep track of which components have finished
        firstTargetComponents = []
        firstTargetComponents.append(firstTarget_sound)
        
        for thisComponent in firstTargetComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "firstTarget"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = firstTargetClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
             
            # *firstTarget_image* updates
            if t >= 0.0 and firstTarget_image.status == NOT_STARTED:
                # keep track of start time/frame for later
                firstTarget_image.tStart = t  # underestimates by a little under one frame
                firstTarget_image.frameNStart = frameN  # exact frame index
                firstTarget_image.draw()
                
            # *firstTarget_text* updates
            if t >= 0.0 and firstTarget_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                firstTarget_text.tStart = t  # underestimates by a little under one frame
                firstTarget_text.frameNStart = frameN  # exact frame index
                firstTarget_text.draw()
        
        
            # start/stop firstTarget_sound
            if t >= 0.0 and firstTarget_sound.status == NOT_STARTED:
                # keep track of start time/frame for later
                firstTarget_sound.tStart = t  # underestimates by a little under one frame
                firstTarget_sound.frameNStart = frameN  # exact frame index
                firstTarget_sound.play()  # start the sound (it finishes automatically)
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in firstTargetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "firstTarget"-------
        for thisComponent in firstTargetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
        firstTarget_sound.stop() #ensure sound has stopped at end of routine
        # the Routine "firstTarget" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
         
        # set up handler to look after randomisation of conditions etc
        v_block_trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'%s.xlsx'%(str(fileName))),
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
vsl_block = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'visuak_forced_test.xlsx'),
    seed=None, name='vsl_block')
thisExp.addLoop(vsl_block)  # add the loop to the experiment
thisForced_test_1_block = vsl_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisForced_test_1_block.rgb)
if thisForced_test_1_block != None:
    for paramName in thisForced_test_1_block.keys():
        exec(paramName + '= thisForced_test_1_block.' + paramName)

for thisForced_test_1_block in vsl_block:
    currentLoop = vsl_block
    # abbreviate parameter names if possible (e.g. rgb = thisForced_test_1_block.rgb)
    if thisForced_test_1_block != None:
        for paramName in thisForced_test_1_block.keys():
            exec(paramName + '= thisForced_test_1_block.' + paramName)
    
    #------Prepare to start Routine "vsl1"-------
    t = 0
    vsl1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    vsl1_image.setImage(vsl1)
    # keep track of which components have finished
    vsl1Components = []
    vsl1Components.append(vsl1_image)
    vsl1Components.append(vsl1_blank_image)
    for thisComponent in vsl1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "vsl1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = vsl1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vsl1_image* updates
        if t >= 0.0 and vsl1_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl1_image.tStart = t  # underestimates by a little under one frame
            vsl1_image.frameNStart = frameN  # exact frame index
            vsl1_image.setAutoDraw(True)
        if vsl1_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl1_image.setAutoDraw(False)
        
        # *vsl1_blank_image* updates
        if t >= 0.8 and vsl1_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl1_blank_image.tStart = t  # underestimates by a little under one frame
            vsl1_blank_image.frameNStart = frameN  # exact frame index
            vsl1_blank_image.setAutoDraw(True)
        if vsl1_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl1_blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vsl1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "vsl1"-------
    for thisComponent in vsl1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "vsl2"-------
    t = 0
    vsl2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    vsl2_image.setImage(vsl2)
    # keep track of which components have finished
    vsl2Components = []
    vsl2Components.append(vsl2_image)
    vsl2Components.append(vsl2_blank_image)
    for thisComponent in vsl2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "vsl2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = vsl2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vsl2_image* updates
        if t >= 0.0 and vsl2_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl2_image.tStart = t  # underestimates by a little under one frame
            vsl2_image.frameNStart = frameN  # exact frame index
            vsl2_image.setAutoDraw(True)
        if vsl2_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl2_image.setAutoDraw(False)
        
        # *vsl2_blank_image* updates
        if t >= 0.8 and vsl2_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl2_blank_image.tStart = t  # underestimates by a little under one frame
            vsl2_blank_image.frameNStart = frameN  # exact frame index
            vsl2_blank_image.setAutoDraw(True)
        if vsl2_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl2_blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vsl2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "vsl2"-------
    for thisComponent in vsl2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "vsl3"-------
    t = 0
    vsl3Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    vsl3_image.setImage(vsl3)
    # keep track of which components have finished
    vsl3Components = []
    vsl3Components.append(vsl3_image)
    vsl3Components.append(vsl3_blank_image)
    for thisComponent in vsl3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "vsl3"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = vsl3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vsl3_image* updates
        if t >= 0.0 and vsl3_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl3_image.tStart = t  # underestimates by a little under one frame
            vsl3_image.frameNStart = frameN  # exact frame index
            vsl3_image.setAutoDraw(True)
        if vsl3_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl3_image.setAutoDraw(False)
        
        # *vsl3_blank_image* updates
        if t >= 0.8 and vsl3_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl3_blank_image.tStart = t  # underestimates by a little under one frame
            vsl3_blank_image.frameNStart = frameN  # exact frame index
            vsl3_blank_image.setAutoDraw(True)
        if vsl3_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl3_blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vsl3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "vsl3"-------
    for thisComponent in vsl3Components:
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
    
    #------Prepare to start Routine "vsl4"-------
    t = 0
    vsl4Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    vsl4_image.setImage(vsl4)
    # keep track of which components have finished
    vsl4Components = []
    vsl4Components.append(vsl4_image)
    vsl4Components.append(vsl4_blank_image)
    for thisComponent in vsl4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "vsl4"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = vsl4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vsl4_image* updates
        if t >= 0.0 and vsl4_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl4_image.tStart = t  # underestimates by a little under one frame
            vsl4_image.frameNStart = frameN  # exact frame index
            vsl4_image.setAutoDraw(True)
        if vsl4_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl4_image.setAutoDraw(False)
        
        # *vsl4_blank_image* updates
        if t >= 0.8 and vsl4_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl4_blank_image.tStart = t  # underestimates by a little under one frame
            vsl4_blank_image.frameNStart = frameN  # exact frame index
            vsl4_blank_image.setAutoDraw(True)
        if vsl4_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl4_blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vsl4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "vsl4"-------
    for thisComponent in vsl4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "vsl5"-------
    t = 0
    vsl5Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    vsl5_image.setImage(vsl5)
    # keep track of which components have finished
    vsl5Components = []
    vsl5Components.append(vsl5_image)
    vsl5Components.append(vsl5_blank_image)
    for thisComponent in vsl5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "vsl5"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = vsl5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vsl5_image* updates
        if t >= 0.0 and vsl5_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl5_image.tStart = t  # underestimates by a little under one frame
            vsl5_image.frameNStart = frameN  # exact frame index
            vsl5_image.setAutoDraw(True)
        if vsl5_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl5_image.setAutoDraw(False)
        
        # *vsl5_blank_image* updates
        if t >= 0.8 and vsl5_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl5_blank_image.tStart = t  # underestimates by a little under one frame
            vsl5_blank_image.frameNStart = frameN  # exact frame index
            vsl5_blank_image.setAutoDraw(True)
        if vsl5_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl5_blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vsl5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "vsl5"-------
    for thisComponent in vsl5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "vsl6"-------
    t = 0
    vsl6Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    vsl6_image.setImage(vsl6)
    # keep track of which components have finished
    vsl6Components = []
    vsl6Components.append(vsl6_image)
    vsl6Components.append(vsl6_blank_image)
    for thisComponent in vsl6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "vsl6"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = vsl6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vsl6_image* updates
        if t >= 0.0 and vsl6_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl6_image.tStart = t  # underestimates by a little under one frame
            vsl6_image.frameNStart = frameN  # exact frame index
            vsl6_image.setAutoDraw(True)
        if vsl6_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl6_image.setAutoDraw(False)
        
        # *vsl6_blank_image* updates
        if t >= 0.8 and vsl6_blank_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl6_blank_image.tStart = t  # underestimates by a little under one frame
            vsl6_blank_image.frameNStart = frameN  # exact frame index
            vsl6_blank_image.setAutoDraw(True)
        if vsl6_blank_image.status == STARTED and t >= (0.8 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            vsl6_blank_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vsl6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "vsl6"-------
    for thisComponent in vsl6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "vsl_question"-------
    t = 0
    vsl_questionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    vsl_question_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    vsl_question_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    vsl_questionComponents = []
    vsl_questionComponents.append(vsl_question_text)
    vsl_questionComponents.append(vsl_question_key_resp)
    for thisComponent in vsl_questionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "vsl_question"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = vsl_questionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vsl_question_text* updates
        if t >= 0.0 and vsl_question_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl_question_text.tStart = t  # underestimates by a little under one frame
            vsl_question_text.frameNStart = frameN  # exact frame index
            vsl_question_text.setAutoDraw(True)
        
        # *vsl_question_key_resp* updates
        if t >= 0.0 and vsl_question_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            vsl_question_key_resp.tStart = t  # underestimates by a little under one frame
            vsl_question_key_resp.frameNStart = frameN  # exact frame index
            vsl_question_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(vsl_question_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if vsl_question_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4', 3])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                vsl_question_key_resp.keys = theseKeys[-1]  # just the last key pressed
                vsl_question_key_resp.rt = vsl_question_key_resp.clock.getTime()
                # was this 'correct'?
                if (vsl_question_key_resp.keys == str(vslcorrAns)) or (vsl_question_key_resp.keys == vslcorrAns):
                    vsl_question_key_resp.corr = 1
                else:
                    vsl_question_key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vsl_questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "vsl_question"-------
    for thisComponent in vsl_questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if vsl_question_key_resp.keys in ['', [], None]:  # No response was made
       vsl_question_key_resp.keys=None
       # was no response the correct answer?!
       if str(vslcorrAns).lower() == 'none': vsl_question_key_resp.corr = 1  # correct non-response
       else: vsl_question_key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for forced_test_1_block (TrialHandler)
    vsl_block.addData('vsl_question_key_resp.keys',vsl_question_key_resp.keys)
    vsl_block.addData('vsl_question_key_resp.corr', vsl_question_key_resp.corr)
    if vsl_question_key_resp.keys != None:  # we had a response
        vsl_block.addData('vsl_question_key_resp.rt', vsl_question_key_resp.rt)
    # the Routine "vsl_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
