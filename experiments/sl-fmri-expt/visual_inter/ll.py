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
expName = 'll'  # from the Builder filename that created this script
expInfo = {u'PartID': u''} # block: R(andom) and S(equential); language: 1 or 2; target: if language 1, then bi, pu, du, da; if block 2, then ku, tu, pi, do.
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

ltarget1 = ['B','F','U','R']
ltarget2 = ['W','Y','A','C']
random.shuffle(ltarget1)
random.shuffle(ltarget2)

firstTarg = ltarget1[1]
secondTarg = ltarget2[1]


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



#LSL TEST
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

# Initialize components for Routine "lsl_instr10"
lsl_instr10Clock = core.Clock()
lsl_instr10_sound = sound.Sound(u'lsl_instr10.wav', secs=-1)
lsl_instr10_sound.setVolume(1)
lsl_instr10_text = visual.TextStim(win=win, ori=0, name='lsl_instr10_text',
    text=u'We are going to ask you if you remember which groups of signs Klaptoo usually showed together during the parade.',    font=u'Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)
lsl_instr10_image = visual.ImageStim(win=win, name='lsl_instr10_image',
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

# Initialize components for Routine "lsl1"
lsl1Clock = core.Clock()
lsl1_image = visual.ImageStim(win=win, name='lsl1_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
lsl1_blank = visual.ImageStim(win=win, name='lsl1_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "lsl2"
lsl2Clock = core.Clock()
lsl2_image = visual.ImageStim(win=win, name='lsl2_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
lsl2_blank = visual.ImageStim(win=win, name='lsl2_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "lsl3"
lsl3Clock = core.Clock()
lsl3_image = visual.ImageStim(win=win, name='lsl3_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
lsl3_blank = visual.ImageStim(win=win, name='lsl3_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "lsl_triplet_pause"
lsl_triplet_pauseClock = core.Clock()
lsl_triplet_pause_image = visual.ImageStim(win=win, name='lsl_triplet_pause_image',
    image=u'white.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "lsl4"
lsl4Clock = core.Clock()
lsl4_image = visual.ImageStim(win=win, name='lsl4_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
lsl4_blank = visual.ImageStim(win=win, name='lsl4_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "lsl5"
lsl5Clock = core.Clock()
lsl5_image = visual.ImageStim(win=win, name='lsl5_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
lsl5_blank = visual.ImageStim(win=win, name='lsl5_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "lsl6"
lsl6Clock = core.Clock()
lsl6_image = visual.ImageStim(win=win, name='lsl6_image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
lsl6_blank = visual.ImageStim(win=win, name='lsl6_blank',
    image=u'blank.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "lsl_question"
lsl_questionClock = core.Clock()
lsl_question_text = visual.TextStim(win=win, ori=0, name='lsl_question_text',
    text=u'Which group went together? Press the green button for first and red button for second.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
    
    
blockList= ['sl_1','sl_2','sl_3','sl_4','sl_5','sl_6','rl_1','rl_2','rl_3','rl_4','rl_5','rl_6']    
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
    if (fileName[0:1]=='r'):
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
            
            
            
            
    elif (fileName[0:1] == 's'):
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

#------Prepare to start Routine "lsl_instr10"-------
t = 0
lsl_instr10Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
lsl_instr10_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
lsl_instr10_key_resp.status = NOT_STARTED
# keep track of which components have finished
lsl_instr10Components = []
lsl_instr10Components.append(lsl_instr10_sound)
lsl_instr10Components.append(lsl_instr10_text)
lsl_instr10Components.append(lsl_instr10_image)
lsl_instr10Components.append(lsl_instr10_key_resp)
for thisComponent in lsl_instr10Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "lsl_instr10"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = lsl_instr10Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop lsl_instr10_sound
    if t >= 0.0 and lsl_instr10_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        lsl_instr10_sound.tStart = t  # underestimates by a little under one frame
        lsl_instr10_sound.frameNStart = frameN  # exact frame index
        lsl_instr10_sound.play()  # start the sound (it finishes automatically)
    
    # *lsl_instr10_text* updates
    if t >= 0.0 and lsl_instr10_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        lsl_instr10_text.tStart = t  # underestimates by a little under one frame
        lsl_instr10_text.frameNStart = frameN  # exact frame index
        lsl_instr10_text.setAutoDraw(True)
    
    # *lsl_instr10_image* updates
    if t >= 0.0 and lsl_instr10_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        lsl_instr10_image.tStart = t  # underestimates by a little under one frame
        lsl_instr10_image.frameNStart = frameN  # exact frame index
        lsl_instr10_image.setAutoDraw(True)
    
    # *lsl_instr10_key_resp* updates
    if t >= 0.0 and lsl_instr10_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        lsl_instr10_key_resp.tStart = t  # underestimates by a little under one frame
        lsl_instr10_key_resp.frameNStart = frameN  # exact frame index
        lsl_instr10_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(lsl_instr10_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if lsl_instr10_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            lsl_instr10_key_resp.keys = theseKeys[-1]  # just the last key pressed
            lsl_instr10_key_resp.rt = lsl_instr10_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lsl_instr10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "lsl_instr10"-------
for thisComponent in lsl_instr10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
lsl_instr10_sound.stop() #ensure sound has stopped at end of routine
# the Routine "lsl_instr10" was not non-slip safe, so reset the non-slip timer
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
lsl_block = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'letter_forced_choice.xlsx'),
    seed=None, name='lsl_block')
thisExp.addLoop(lsl_block)  # add the loop to the experiment
thisForced_test_trial = lsl_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisForced_test_trial.rgb)
if thisForced_test_trial != None:
    for paramName in thisForced_test_trial.keys():
        exec(paramName + '= thisForced_test_trial.' + paramName)

for thisForced_test_trial in lsl_block:
    currentLoop = lsl_block
    # abbreviate parameter names if possible (e.g. rgb = thisForced_test_trial.rgb)
    if thisForced_test_trial != None:
        for paramName in thisForced_test_trial.keys():
            exec(paramName + '= thisForced_test_trial.' + paramName)
    
    #------Prepare to start Routine "lsl1"-------
    t = 0
    lsl1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    lsl1_image.setImage(letter1)
    # keep track of which components have finished
    lsl1Components = []
    lsl1Components.append(lsl1_image)
    lsl1Components.append(lsl1_blank)
    for thisComponent in lsl1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lsl1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lsl1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lsl1_image* updates
        if t >= 0.0 and lsl1_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl1_image.tStart = t  # underestimates by a little under one frame
            lsl1_image.frameNStart = frameN  # exact frame index
            lsl1_image.setAutoDraw(True)
        if lsl1_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl1_image.setAutoDraw(False)
        
        # *lsl1_blank* updates
        if t >= 0.79 and lsl1_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl1_blank.tStart = t  # underestimates by a little under one frame
            lsl1_blank.frameNStart = frameN  # exact frame index
            lsl1_blank.setAutoDraw(True)
        if lsl1_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl1_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lsl1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lsl1"-------
    for thisComponent in lsl1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "lsl2"-------
    t = 0
    lsl2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    lsl2_image.setImage(letter2)
    # keep track of which components have finished
    lsl2Components = []
    lsl2Components.append(lsl2_image)
    lsl2Components.append(lsl2_blank)
    for thisComponent in lsl2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lsl2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lsl2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lsl2_image* updates
        if t >= 0.0 and lsl2_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl2_image.tStart = t  # underestimates by a little under one frame
            lsl2_image.frameNStart = frameN  # exact frame index
            lsl2_image.setAutoDraw(True)
        if lsl2_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl2_image.setAutoDraw(False)
        
        # *lsl2_blank* updates
        if t >= 0.79 and lsl2_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl2_blank.tStart = t  # underestimates by a little under one frame
            lsl2_blank.frameNStart = frameN  # exact frame index
            lsl2_blank.setAutoDraw(True)
        if lsl2_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl2_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lsl2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lsl2"-------
    for thisComponent in lsl2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "lsl3"-------
    t = 0
    lsl3Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    lsl3_image.setImage(letter3)
    # keep track of which components have finished
    lsl3Components = []
    lsl3Components.append(lsl3_image)
    lsl3Components.append(lsl3_blank)
    for thisComponent in lsl3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lsl3"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lsl3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lsl3_image* updates
        if t >= 0.0 and lsl3_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl3_image.tStart = t  # underestimates by a little under one frame
            lsl3_image.frameNStart = frameN  # exact frame index
            lsl3_image.setAutoDraw(True)
        if lsl3_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl3_image.setAutoDraw(False)
        
        # *lsl3_blank* updates
        if t >= 0.79 and lsl3_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl3_blank.tStart = t  # underestimates by a little under one frame
            lsl3_blank.frameNStart = frameN  # exact frame index
            lsl3_blank.setAutoDraw(True)
        if lsl3_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl3_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lsl3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lsl3"-------
    for thisComponent in lsl3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "lsl_triplet_pause"-------
    t = 0
    lsl_triplet_pauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    lsl_triplet_pauseComponents = []
    lsl_triplet_pauseComponents.append(lsl_triplet_pause_image)
    for thisComponent in lsl_triplet_pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lsl_triplet_pause"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lsl_triplet_pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lsl_triplet_pause_image* updates
        if t >= 0.0 and lsl_triplet_pause_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl_triplet_pause_image.tStart = t  # underestimates by a little under one frame
            lsl_triplet_pause_image.frameNStart = frameN  # exact frame index
            lsl_triplet_pause_image.setAutoDraw(True)
        if lsl_triplet_pause_image.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl_triplet_pause_image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lsl_triplet_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lsl_triplet_pause"-------
    for thisComponent in lsl_triplet_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "lsl4"-------
    t = 0
    lsl4Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    lsl4_image.setImage(letter4)
    # keep track of which components have finished
    lsl4Components = []
    lsl4Components.append(lsl4_image)
    lsl4Components.append(lsl4_blank)
    for thisComponent in lsl4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lsl4"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lsl4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lsl4_image* updates
        if t >= 0.0 and lsl4_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl4_image.tStart = t  # underestimates by a little under one frame
            lsl4_image.frameNStart = frameN  # exact frame index
            lsl4_image.setAutoDraw(True)
        if lsl4_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl4_image.setAutoDraw(False)
        
        # *lsl4_blank* updates
        if t >= 0.79 and lsl4_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl4_blank.tStart = t  # underestimates by a little under one frame
            lsl4_blank.frameNStart = frameN  # exact frame index
            lsl4_blank.setAutoDraw(True)
        if lsl4_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl4_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lsl4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lsl4"-------
    for thisComponent in lsl4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "lsl5"-------
    t = 0
    lsl5Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    lsl5_image.setImage(letter5)
    # keep track of which components have finished
    lsl5Components = []
    lsl5Components.append(lsl5_image)
    lsl5Components.append(lsl5_blank)
    for thisComponent in lsl5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lsl5"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lsl5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lsl5_image* updates
        if t >= 0.0 and lsl5_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl5_image.tStart = t  # underestimates by a little under one frame
            lsl5_image.frameNStart = frameN  # exact frame index
            lsl5_image.setAutoDraw(True)
        if lsl5_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl5_image.setAutoDraw(False)
        
        # *lsl5_blank* updates
        if t >= 0.79 and lsl5_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl5_blank.tStart = t  # underestimates by a little under one frame
            lsl5_blank.frameNStart = frameN  # exact frame index
            lsl5_blank.setAutoDraw(True)
        if lsl5_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl5_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lsl5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lsl5"-------
    for thisComponent in lsl5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "lsl6"-------
    t = 0
    lsl6Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    lsl6_image.setImage(letter6)
    # keep track of which components have finished
    lsl6Components = []
    lsl6Components.append(lsl6_image)
    lsl6Components.append(lsl6_blank)
    for thisComponent in lsl6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lsl6"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lsl6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lsl6_image* updates
        if t >= 0.0 and lsl6_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl6_image.tStart = t  # underestimates by a little under one frame
            lsl6_image.frameNStart = frameN  # exact frame index
            lsl6_image.setAutoDraw(True)
        if lsl6_image.status == STARTED and t >= (0.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl6_image.setAutoDraw(False)
        
        # *lsl6_blank* updates
        if t >= 0.79 and lsl6_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl6_blank.tStart = t  # underestimates by a little under one frame
            lsl6_blank.frameNStart = frameN  # exact frame index
            lsl6_blank.setAutoDraw(True)
        if lsl6_blank.status == STARTED and t >= (0.79 + (0.21-win.monitorFramePeriod*0.75)): #most of one frame period left
            lsl6_blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lsl6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lsl6"-------
    for thisComponent in lsl6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "lsl_question"-------
    t = 0
    lsl_questionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    lsl_question_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    lsl_question_key_resp.status = NOT_STARTED
    # keep track of which components have finished
    lsl_questionComponents = []
    lsl_questionComponents.append(lsl_question_text)
    lsl_questionComponents.append(lsl_question_key_resp)
    for thisComponent in lsl_questionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lsl_question"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = lsl_questionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lsl_question_text* updates
        if t >= 0.0 and lsl_question_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl_question_text.tStart = t  # underestimates by a little under one frame
            lsl_question_text.frameNStart = frameN  # exact frame index
            lsl_question_text.setAutoDraw(True)
        
        # *lsl_question_key_resp* updates
        if t >= 0.0 and lsl_question_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            lsl_question_key_resp.tStart = t  # underestimates by a little under one frame
            lsl_question_key_resp.frameNStart = frameN  # exact frame index
            lsl_question_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(lsl_question_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if lsl_question_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                lsl_question_key_resp.keys = theseKeys[-1]  # just the last key pressed
                lsl_question_key_resp.rt = lsl_question_key_resp.clock.getTime()
                # was this 'correct'?
                if (lsl_question_key_resp.keys == str(lslcorrAns)) or (lsl_question_key_resp.keys == lslcorrAns):
                    lsl_question_key_resp.corr = 1
                else:
                    lsl_question_key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lsl_questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lsl_question"-------
    for thisComponent in lsl_questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if lsl_question_key_resp.keys in ['', [], None]:  # No response was made
       lsl_question_key_resp.keys=None
       # was no response the correct answer?!
       if str(lslcorrAns).lower() == 'none': lsl_question_key_resp.corr = 1  # correct non-response
       else: lsl_question_key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for forced_test_trials (TrialHandler)
    lsl_block.addData('lsl_question_key_resp.keys',lsl_question_key_resp.keys)
    lsl_block.addData('lsl_question_key_resp.corr', lsl_question_key_resp.corr)
    if lsl_question_key_resp.keys != None:  # we had a response
        lsl_block.addData('lsl_question_key_resp.rt', lsl_question_key_resp.rt)
    # the Routine "lsl_question" was not non-slip safe, so reset the non-slip timer
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
