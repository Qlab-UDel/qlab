#!/usr/bin /env python2
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
expName = 'auditory'  # from the Builder filename that created this script
expInfo = {u'starget': u'', u'ttarget': u'', u'PartID': u''} # block: R(andom) and S(equential); target: then bi, pu, du, da; 
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['Run'] = "4"
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
    monitor='testMonitor', color='grey', colorSpace='rgb',
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
    text="Are you ready for the game? Let's get started. Remember to press the button when you hear Meeple's favorite word or note.",    font='Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_15 = visual.ImageStim(win=win, name='image_15',
    image='Alien21.png', mask=None,
    ori=0, pos=[.5, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "sreminder"
sreminderClock = core.Clock()
sreminder_sound = sound.Sound('reminder_%s.wav' % str(expInfo['starget']), secs=-1)
sreminder_sound.setVolume(1)

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
    image=u'Alien21.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "trial"
trialClock = core.Clock()
tone = sound.Sound('A', secs=-1)
tone.setVolume(1)
alien = visual.ImageStim(win=win, name='alien',
    image='Alien24.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "treminder"
treminderClock = core.Clock()
treminder_text = visual.TextStim(win=win, ori=0, name='treminder_text',
    text='Now press the button when you hear this!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
treminder_sound = sound.Sound('reminder_%s.wav' % str(expInfo['ttarget']), secs=-1)
treminder_sound.setVolume(1)

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Great, you did it!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_31 = sound.Sound('instr_8.wav', secs=-1)
sound_31.setVolume(1)

# Initialize components for Routine "instr5"
instr5Clock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='Now look at these two aliens:',    font='Arial',
    pos=[0, .8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_12 = visual.ImageStim(win=win, name='image_12',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_32 = sound.Sound('instr_9.wav', secs=-1)
sound_32.setVolume(1)

# Initialize components for Routine "instr6"
instr6Clock = core.Clock()
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text="Each of these aliens will play \na very short piece of music in \neach trial. Please try your best \nto identify which piece sounds \nmore like Meeple's music. If you \ndon't know the answer, just give \nyour best guess! \n\nPress the green button if the first \npiece of music sounds more like the \nmusic Meeple  made, and press the red button if the second piece of music \nsounds more like the music \nMeeple made.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_33 = sound.Sound('new_test.wav', secs=-1)
sound_33.setVolume(1)


# Initialize components for Routine "test"
testClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)
image_2 = visual.ImageStim(win=win, name='image_2',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text="Which song is like Meeple's? \nPress the green button for first and red button for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test2"
test2Clock = core.Clock()
sound_7 = sound.Sound('A', secs=-1)
sound_7.setVolume(1)
image_3 = visual.ImageStim(win=win, name='image_3',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_14 = visual.TextStim(win=win, ori=0, name='text_14',
    text="Which song is like Meeple's? \nPress the green button for first and red button for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test3"
test3Clock = core.Clock()
sound_8 = sound.Sound('A', secs=-1)
sound_8.setVolume(1)
image_4 = visual.ImageStim(win=win, name='image_4',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_15 = visual.TextStim(win=win, ori=0, name='text_15',
    text="Which song is like Meeple's? \nPress the green button for first and red button for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "triplet_pause"
triplet_pauseClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
image_5 = visual.ImageStim(win=win, name='image_5',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_16 = visual.TextStim(win=win, ori=0, name='text_16',
    text="Which song is like Meeple's? \nPress the green button for first and red button for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test4"
test4Clock = core.Clock()
sound_9 = sound.Sound('A', secs=-1)
sound_9.setVolume(1)
image_6 = visual.ImageStim(win=win, name='image_6',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_17 = visual.TextStim(win=win, ori=0, name='text_17',
    text="Which song is like Meeple's? \nPress the green button for first and red button for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test5"
test5Clock = core.Clock()
sound_10 = sound.Sound('A', secs=-1)
sound_10.setVolume(1)
image_7 = visual.ImageStim(win=win, name='image_7',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_18 = visual.TextStim(win=win, ori=0, name='text_18',
    text="Which song is like Meeple's? \nPress the green button for first and red button for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test6"
test6Clock = core.Clock()
sound_11 = sound.Sound('A', secs=-1)
sound_11.setVolume(1)
image_8 = visual.ImageStim(win=win, name='image_8',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_19 = visual.TextStim(win=win, ori=0, name='text_19',
    text="Which song is like Meeple's? \nPress he green button for first and red button for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "question"
questionClock = core.Clock()
image_9 = visual.ImageStim(win=win, name='image_9',
    image='2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_20 = visual.TextStim(win=win, ori=0, name='text_20',
    text="Which song is like Meeple's? \nPress the green button for first and red button for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "five_s_gap"
five_s_gapClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='Please wait...',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text="Great, you're all done! Thank you :)\nPress any key to exit.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_42 = sound.Sound('instr_22.wav', secs=-1)
sound_42.setVolume(1)



blockList = ['1','2','3','4','5','6']
random.shuffle(blockList)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


for fileName in blockList:
        if (int(fileName[-1:])%2 != 0):
            #------Prepare to start Routine "treminder"-------
            t = 0
            treminderClock.reset()  # clock 
            frameN = -1
            routineTimer.add(4.0000)
            
            # update component parameters for each repeat
            treminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            treminder_key_resp.status = NOT_STARTED
            # keep track of which components have finished
            treminderComponents = []
            treminderComponents.append(treminder_sound)
            
            for thisComponent in treminderComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "treminder"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = treminderClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                 
                    
                # start/stop treminder_sound
                if t >= 0.0 and treminder_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    treminder_sound.tStart = t  # underestimates by a little under one frame
                    treminder_sound.frameNStart = frameN  # exact frame index
                    treminder_sound.play()  # start the sound (it finishes automatically)
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in treminderComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "treminder"-------
            for thisComponent in treminderComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            treminder_sound.stop() #ensure sound has stopped at end of routine
            # the Routine "treminder" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            
            # set up handler to look after randomisation of conditions etc
            trials_1 = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(u'auditory_run4_%s.csv'%(str(fileName))),
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
                routineTimer.add(0.480000)
                # update component parameters for each repeat
                tone.setSound(soundFile, secs=0.46)
                random_block_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
                random_block_key_resp.status = NOT_STARTED
                # keep track of which components have finished
                trialComponents = []
                trialComponents.append(tone)
                trialComponents.append(alien)
                trialComponents.append(random_block_key_resp)
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
                    
                    # *random_block_key_resp* updates
                    if t >= 0.0 and random_block_key_resp.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        random_block_key_resp.tStart = t  # underestimates by a little under one frame
                        random_block_key_resp.frameNStart = frameN  # exact frame index
                        random_block_key_resp.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(random_block_key_resp.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if random_block_key_resp.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                        random_block_key_resp.status = STOPPED
                    if random_block_key_resp.status == STARTED:
                        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            random_block_key_resp.keys = theseKeys[-1]  # just the last key pressed
                            random_block_key_resp.rt = random_block_key_resp.clock.getTime()
                    
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
                if random_block_key_resp.keys in ['', [], None]:  # No response was made
                   random_block_key_resp.keys=None
                # store data for trials_1 (TrialHandler)
                trials_1.addData('tone_block_key_resp.keys',random_block_key_resp.keys)
                if random_block_key_resp.keys != None:  # we had a response
                    trials_1.addData('tone_block_key_resp.rt', random_block_key_resp.rt)
                thisExp.nextEntry()
            
        elif (int(fileName[-1:])%2 == 0):
            #------Prepare to start Routine "sreminder"-------
            t = 0
            sreminderClock.reset()  # clock 
            frameN = -1
            routineTimer.add(4.0000)
            
            # update component parameters for each repeat
            sreminder_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            sreminder_key_resp.status = NOT_STARTED
            # keep track of which components have finished
            sreminderComponents = []
            sreminderComponents.append(sreminder_sound)
            
            for thisComponent in sreminderComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "sreminder"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sreminderClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                 
                    
                # start/stop sreminder_sound
                if t >= 0.0 and sreminder_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    sreminder_sound.tStart = t  # underestimates by a little under one frame
                    sreminder_sound.frameNStart = frameN  # exact frame index
                    sreminder_sound.play()  # start the sound (it finishes automatically)
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sreminderComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "sreminder"-------
            for thisComponent in sreminderComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            sreminder_sound.stop() #ensure sound has stopped at end of routine
            # the Routine "sreminder" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            
            # set up handler to look after randomisation of conditions etc
            fam_trials_loop = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(u'auditory_run4_%s.csv'%(str(fileName))),
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
                structured_block_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
                structured_block_key_resp.status = NOT_STARTED
                # keep track of which components have finished
                fam_trialsComponents = []
                fam_trialsComponents.append(fam_trials_sound)
                fam_trialsComponents.append(structured_block_key_resp)
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
                    
                    # *structured_block_key_resp* updates
                    if t >= 0.0 and structured_block_key_resp.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        structured_block_key_resp.tStart = t  # underestimates by a little under one frame
                        structured_block_key_resp.frameNStart = frameN  # exact frame index
                        structured_block_key_resp.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(structured_block_key_resp.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if structured_block_key_resp.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
                        structured_block_key_resp.status = STOPPED
                    if structured_block_key_resp.status == STARTED:
                        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            structured_block_key_resp.keys = theseKeys[-1]  # just the last key pressed
                            structured_block_key_resp.rt = structured_block_key_resp.clock.getTime()
                    
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
                if structured_block_key_resp.keys in ['', [], None]:  # No response was made
                   structured_block_key_resp.keys=None
                # store data for fam_trials_loop (TrialHandler)
                fam_trials_loop.addData('sound_block_key_resp.keys',structured_block_key_resp.keys)
                if structured_block_key_resp.keys != None:  # we had a response
                    fam_trials_loop.addData('sound_block_key_resp.rt', structured_block_key_resp.rt)
                thisExp.nextEntry()
    



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
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
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

#------Prepare to start Routine "instr5"-------
t = 0
instr5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_8.status = NOT_STARTED
# keep track of which components have finished
instr5Components = []
instr5Components.append(text_6)
instr5Components.append(key_resp_8)
instr5Components.append(image_12)
instr5Components.append(sound_32)
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
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t  # underestimates by a little under one frame
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_12* updates
    if t >= 0.0 and image_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_12.tStart = t  # underestimates by a little under one frame
        image_12.frameNStart = frameN  # exact frame index
        image_12.setAutoDraw(True)
    # start/stop sound_32
    if t >= 0.0 and sound_32.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_32.tStart = t  # underestimates by a little under one frame
        sound_32.frameNStart = frameN  # exact frame index
        sound_32.play()  # start the sound (it finishes automatically)
    
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
sound_32.stop() #ensure sound has stopped at end of routine
# the Routine "instr5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr6"-------
t = 0
instr6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_15 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_15.status = NOT_STARTED
# keep track of which components have finished
instr6Components = []
instr6Components.append(text_12)
instr6Components.append(key_resp_15)
instr6Components.append(sound_33)
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
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # underestimates by a little under one frame
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    
    # *key_resp_15* updates
    if t >= 0.0 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t  # underestimates by a little under one frame
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_33
    if t >= 0.0 and sound_33.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_33.tStart = t  # underestimates by a little under one frame
        sound_33.frameNStart = frameN  # exact frame index
        sound_33.play()  # start the sound (it finishes automatically)
    
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
sound_33.stop() #ensure sound has stopped at end of routine
# the Routine "instr6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# set up handler to look after randomisation of conditions etc
twoAFC_1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'S_forced_test_2.xlsx'),
    seed=None, name='twoAFC_1')
thisExp.addLoop(twoAFC_1)  # add the loop to the experiment
thisTwoAFC_1 = twoAFC_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTwoAFC_1.rgb)
if thisTwoAFC_1 != None:
    for paramName in thisTwoAFC_1.keys():
        exec(paramName + '= thisTwoAFC_1.' + paramName)

for thisTwoAFC_1 in twoAFC_1:
    currentLoop = twoAFC_1
    # abbreviate parameter names if possible (e.g. rgb = thisTwoAFC_1.rgb)
    if thisTwoAFC_1 != None:
        for paramName in thisTwoAFC_1.keys():
            exec(paramName + '= thisTwoAFC_1.' + paramName)
    
    #------Prepare to start Routine "test"-------
    t = 0
    testClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    sound_1.setSound(soundFile1, secs=.46)
    # keep track of which components have finished
    testComponents = []
    testComponents.append(sound_1)
    testComponents.append(image_2)
    testComponents.append(text_13)
    for thisComponent in testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if t >= 0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        if image_2.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_2.setAutoDraw(False)
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t  # underestimates by a little under one frame
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        if text_13.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_13.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test2"-------
    t = 0
    test2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    sound_7.setSound(soundFile2, secs=0.46)
    # keep track of which components have finished
    test2Components = []
    test2Components.append(sound_7)
    test2Components.append(image_3)
    test2Components.append(text_14)
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
        # start/stop sound_7
        if t >= 0 and sound_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_7.tStart = t  # underestimates by a little under one frame
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.play()  # start the sound (it finishes automatically)
        if sound_7.status == STARTED and t >= (0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_7.stop()  # stop the sound (if longer than duration)
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        if image_3.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_3.setAutoDraw(False)
        
        # *text_14* updates
        if t >= 0.0 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t  # underestimates by a little under one frame
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        if text_14.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_14.setAutoDraw(False)
        
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
    sound_7.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test3"-------
    t = 0
    test3Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    sound_8.setSound(soundFile3, secs=.46)
    # keep track of which components have finished
    test3Components = []
    test3Components.append(sound_8)
    test3Components.append(image_4)
    test3Components.append(text_15)
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
        # start/stop sound_8
        if t >= 0 and sound_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_8.tStart = t  # underestimates by a little under one frame
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.play()  # start the sound (it finishes automatically)
        if sound_8.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_8.stop()  # stop the sound (if longer than duration)
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t  # underestimates by a little under one frame
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        if image_4.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_4.setAutoDraw(False)
        
        # *text_15* updates
        if t >= 0.0 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t  # underestimates by a little under one frame
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        if text_15.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_15.setAutoDraw(False)
        
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
    sound_8.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "triplet_pause"-------
    t = 0
    triplet_pauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    # keep track of which components have finished
    triplet_pauseComponents = []
    triplet_pauseComponents.append(ISI)
    triplet_pauseComponents.append(image_5)
    triplet_pauseComponents.append(text_16)
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
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t  # underestimates by a little under one frame
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        if image_5.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_5.setAutoDraw(False)
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t  # underestimates by a little under one frame
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        if text_16.status == STARTED and t >= (0.0 + (0.48-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_16.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.48)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
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
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    sound_9.setSound(soundFile4, secs=.46)
    # keep track of which components have finished
    test4Components = []
    test4Components.append(sound_9)
    test4Components.append(image_6)
    test4Components.append(text_17)
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
        # start/stop sound_9
        if t >= 0 and sound_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_9.tStart = t  # underestimates by a little under one frame
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.play()  # start the sound (it finishes automatically)
        if sound_9.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_9.stop()  # stop the sound (if longer than duration)
        
        # *image_6* updates
        if t >= 0.0 and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_6.tStart = t  # underestimates by a little under one frame
            image_6.frameNStart = frameN  # exact frame index
            image_6.setAutoDraw(True)
        if image_6.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_6.setAutoDraw(False)
        
        # *text_17* updates
        if t >= 0.0 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t  # underestimates by a little under one frame
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        if text_17.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_17.setAutoDraw(False)
        
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
    sound_9.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test5"-------
    t = 0
    test5Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    sound_10.setSound(soundFile5, secs=.46)
    # keep track of which components have finished
    test5Components = []
    test5Components.append(sound_10)
    test5Components.append(image_7)
    test5Components.append(text_18)
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
        # start/stop sound_10
        if t >= 0 and sound_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_10.tStart = t  # underestimates by a little under one frame
            sound_10.frameNStart = frameN  # exact frame index
            sound_10.play()  # start the sound (it finishes automatically)
        if sound_10.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_10.stop()  # stop the sound (if longer than duration)
        
        # *image_7* updates
        if t >= 0.0 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t  # underestimates by a little under one frame
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        if image_7.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_7.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 0.0 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t  # underestimates by a little under one frame
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        if text_18.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_18.setAutoDraw(False)
        
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
    sound_10.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test6"-------
    t = 0
    test6Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.480000)
    # update component parameters for each repeat
    sound_11.setSound(soundFile6, secs=.46)
    # keep track of which components have finished
    test6Components = []
    test6Components.append(sound_11)
    test6Components.append(image_8)
    test6Components.append(text_19)
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
        # start/stop sound_11
        if t >= 0 and sound_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_11.tStart = t  # underestimates by a little under one frame
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.play()  # start the sound (it finishes automatically)
        if sound_11.status == STARTED and t >= (0 + (.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_11.stop()  # stop the sound (if longer than duration)
        
        # *image_8* updates
        if t >= 0.0 and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t  # underestimates by a little under one frame
            image_8.frameNStart = frameN  # exact frame index
            image_8.setAutoDraw(True)
        if image_8.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_8.setAutoDraw(False)
        
        # *text_19* updates
        if t >= 0.0 and text_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_19.tStart = t  # underestimates by a little under one frame
            text_19.frameNStart = frameN  # exact frame index
            text_19.setAutoDraw(True)
        if text_19.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_19.setAutoDraw(False)
        
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
    sound_11.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "question"-------
    t = 0
    questionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_6.status = NOT_STARTED
    # keep track of which components have finished
    questionComponents = []
    questionComponents.append(key_resp_6)
    questionComponents.append(image_9)
    questionComponents.append(text_20)
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
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # underestimates by a little under one frame
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # was this 'correct'?
                if (key_resp_6.keys == str(corrAns)) or (key_resp_6.keys == corrAns):
                    key_resp_6.corr = 1
                else:
                    key_resp_6.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image_9* updates
        if t >= 0.0 and image_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_9.tStart = t  # underestimates by a little under one frame
            image_9.frameNStart = frameN  # exact frame index
            image_9.setAutoDraw(True)
        
        # *text_20* updates
        if t >= 0.0 and text_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_20.tStart = t  # underestimates by a little under one frame
            text_20.frameNStart = frameN  # exact frame index
            text_20.setAutoDraw(True)
        
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
    if key_resp_6.keys in ['', [], None]:  # No response was made
       key_resp_6.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_6.corr = 1  # correct non-response
       else: key_resp_6.corr = 0  # failed to respond (incorrectly)
    # store data for twoAFC_1 (TrialHandler)
    twoAFC_1.addData('key_resp_6.keys',key_resp_6.keys)
    twoAFC_1.addData('key_resp_6.corr', key_resp_6.corr)
    if key_resp_6.keys != None:  # we had a response
        twoAFC_1.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "five_s_gap"-------
    t = 0
    five_s_gapClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    five_s_gapComponents = []
    five_s_gapComponents.append(text_4)
    for thisComponent in five_s_gapComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "five_s_gap"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = five_s_gapClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        if text_4.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in five_s_gapComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "five_s_gap"-------
    for thisComponent in five_s_gapComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    routineTimer.reset()

# completed 1 repeats of 'twoAFC_1'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(text_5)
endComponents.append(key_resp_7)
endComponents.append(sound_42)
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
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_42
    if t >= 0.0 and sound_42.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_42.tStart = t  # underestimates by a little under one frame
        sound_42.frameNStart = frameN  # exact frame index
        sound_42.play()  # start the sound (it finishes automatically)
    
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
sound_42.stop() #ensure sound has stopped at end of routine
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

    
    
    
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
