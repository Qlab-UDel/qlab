#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.75.01), Sat Jan 19 14:09:32 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui, sound
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle, seed
import os  # handy system and path functions
import csv

import ctypes
#####################################################
#for parallel port control and function for sending triggers for EEG, works on PC
from ctypes import windll 
p=windll.inpout32 
timer=core.Clock()
def sendEEGTrig(trigger):
    trigger=ctypes.c_long(trigger)
    p.Out32(0xDFF8,trigger)
    t0=timer.getTime()
    while timer.getTime()<t0+0.005: pass   #wait until 5ms has passed to set all pins to low
    p.Out32(0xDFF8,0) #set trigger back to 0 again
#######################

# Store info about the experiment session
expName = 'BILMEG'  # from the Builder filename that created this script
expInfo = {'participant':' ', 'session': ' '}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('Data'+os.path.sep+'pylog'):
    os.makedirs('Data'+os.path.sep+'pylog') #if this fails (e.g. permissions) we will get error
filename='Data'+os.path.sep+'pylog' + os.path.sep + 'Subj%s_session%s' %(expInfo['participant'],expInfo['session'])
logFile=logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)


# Setup the Window
win = visual.Window(size=(1024, 768), screen=1, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

#present some dead frames to allow setup to occur
for i in range(30):
    win.flip()
#win.setRecordFrameInterval(True) #this has to be turned on manually
win.frameClock.reset() #this should be handled by setRecordFrameInterval, will be as of 1.00.04!

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimuli = sound.Sound('A')
stimuli.setVolume(1)
pauseScr=visual.TextStim(win=win, ori=0, name='pauseScr',
        text='PAUSED',
        font='Arial',
        pos=[0, 0], height=0.1,wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=0.0)
        
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of blocks etc
actualblock1='run-designs/file1_reorder.csv'
actualblock2='run-designs/file2_reorder.csv'
actualblock3='run-designs/file3_reorder.csv'

actualblocklist=[actualblock1,actualblock2,actualblock3]

# ##### Define EEG/MEG trigger codes
ZeroCode=0 #start code (system zeroing is built into the sendEEGTrig function)
PauseCode = 255 #for pausing recording
BoundaryCode=254 #mark boundary events
VideoCode=253 #whenever subject sees a new kind of animal on the screen
    
#CondCode=[] #this depends on the stimulus category: three digits: 
# first: ba (1); da(2)
# second: elizabeth(1); sara(2)
# third: standard (1), big (2), small deviant (3)

stimuluslist = actualblocklist[int(expInfo['session'])-1]
eventList=np.loadtxt(stimuluslist,dtype='str', delimiter=',', skiprows=1)

#make it fixed with 320
#create randomized array of timing jitter values
if(int(expInfo['session'])<3):
    jitterArr=np.zeros((1500,1),dtype='float')
else:
    jitterArr=np.zeros((1000,1),dtype='float')
for i in range(1500):
    jitterArr[i] = randint(320,321)/1000 # jittering is 320
    
#create currentblockarray
currentblockarray = []
for i in range (len(eventList)):
    currentblockarray.append({'cond': eventList[i,0], 'sound': eventList[i,1], 'speaker': eventList[i,2], 'file': eventList[i,3], 'eventCode': eventList[i,4], 'order': eventList[i,5], 'jitterDur': jitterArr[i], 'csvfile': stimuluslist })

# Open file and write header for behavioral data output
    datFile=open('Data'+os.path.sep+'subj%s_Block%s.txt'%(expInfo['participant'],expInfo['session']),'w')
    datFile.write('Subject\tRun\tOrder\tCond\tSound\tSpeaker\tFile\tEventCode\tJitterDur\tcsvfile\n')

# Build stimuli components for instructions
instruct=visual.TextStim(win=win, ori=0, name='instruct',
        text='Press Enter to Start!',
        font='Arial',
        pos=[0, -0.25], height=0.080,wrapWidth=1.7,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)

    #Display instructions
instruct.draw()
win.flip()
core.wait(0.005)
event.waitKeys(keyList=['return','+'])
#sendEEGTrig(ZeroCode)
core.wait(0.005)
#sendEEGTrig(BoundaryCode)

# MMN is the actualblock
MMN= data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=currentblockarray,
    seed=None)
thisTrial = MMN.trialList[0]  # so we can initialise stimuli with some values


for thisTrial in MMN:
    
    currentLoop = MMN
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)

    #------Prepare to start Routine"trial"-------
    # update component parameters for each repeat
    stimuli.setSound('Stimuli'+os.path.sep+'normalized-180'+os.path.sep+'%s_%s'%(thisTrial.sound, thisTrial.speaker)+os.path.sep+'%s%s.wav'%(thisTrial.sound, thisTrial.file))
    triggercounter=0
    trialClock=core.Clock()
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.500000)
    
    # keep track of which components have finished
    pausePress=[]
    resumePress=[]
    pauseKey = event.BuilderKeyResponse() #create an object of type KeyResponse
    pauseKey.status=NOT_STARTED
    resumeKey = event.BuilderKeyResponse() #create an object of type KeyResponse
    resumeKey.status=NOT_STARTED
    respKey1 = event.BuilderKeyResponse() #create an object of type KeyResponse
    respKey1.status=NOT_STARTED
    trialComponents = []
    trialComponents.append(stimuli)
    trialComponents.append(pauseScr)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        #*pauseKey* updates
        if t>=0 and pauseKey.status==NOT_STARTED:
            #keep track of start time/frame for later
            pauseKey.tStart=t#underestimates by a little under one frame
            pauseKey.frameNStart=frameN#exact frame index
            pauseKey.status=STARTED
            #keyboard checking is just starting
            event.clearEvents()
        elif pauseKey.status==STARTED and t>=500:
            pauseKey.status=FINISHED
        if pauseKey.status==STARTED:#only update if being drawn
            pausePress = event.getKeys(keyList=['p'])
            if len(pausePress)>0:
                sendEEGTrig(BoundaryCode)#mark boundary and pause EEG recording
                core.wait(0.005)
                p.Out32(0x378,PauseCode)
     
     #*resumeKey* updates
        if resumeKey.status==NOT_STARTED and t>=500:
            resumeKey.status=FINISHED
        elif resumeKey.status==NOT_STARTED and len(pausePress)>0:
            #keep track of start time/frame for later
            resumeKey.tStart=t#underestimates by a little under one frame
            resumeKey.frameNStart=frameN#exact frame index
            resumeKey.status=STARTED
            #keyboard checking is just starting
            event.clearEvents()
        if resumeKey.status==STARTED:#only update if being drawn
            resumePress = event.getKeys(keyList=['r'])
            if len(resumePress)>0:#at least one key was pressed
                #abort routine on response
                p.Out32(0x378,ZeroCode)
                core.wait(0.005)
                sendEEGTrig(BoundaryCode) #start recording EEG again and mark boundary
                continueRoutine=False
                
     #*pauseScr* updates
        if pauseScr.status==NOT_STARTED and t>=(thisTrial.jitterDur + 0.4):
                pauseScr.status=FINISHED
        elif pauseScr.status==NOT_STARTED and len(pausePress)>0:
            #keep track of start time/frame for later
            pauseScr.tStart=t#underestimates by a little under one frame
            pauseScr.frameNStart=frameN#exact frame index
            pauseScr.setAutoDraw(True)
        elif pauseScr.status==STARTED and len(resumePress)>0:
            pauseScr.setAutoDraw(False)
            
     #*respKey1* updates
        if respKey1.status==NOT_STARTED and t >=0:
            respKey1.status=STARTED
            respKey1.clock.reset()
            event.clearEvents()
        if respKey1.status==STARTED and t < (thisTrial.jitterDur+0.4):
            theseKeys = event.getKeys(keyList=['1','2','3','4']) # if in EEG using 'space'
            if len(theseKeys)>0:
                respKey1.keys=theseKeys[-1]
                respKey1.rt.append(respKey1.clock.getTime())
                sendEEGTrig(VideoCode)
        if respKey1.status==STARTED and t>=(thisTrial.jitterDur + 0.4):
            respKey1.status=STOPPED
                    
     # start/stop stimuli
        if t > 0 and stimuli.status == NOT_STARTED:
            # keep track of start time/frame for later
            stimuli.tStart = t  # underestimates by a little under one frame
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.play()  # start the sound (it finishes automatically)
        elif stimuli.status == STARTED and t >= (thisTrial.jitterDur + 0.4):
            stimuli.stop()  # stop the sound (if longer than duration)
        elif stimuli.status==STARTED and len(pausePress)>0:
            stimuli.stop()
            stimuli.status=FINISHED
        if t >= 0.02 and triggercounter == 0:
             #send EEG/MEG trigger:
            triggercounter = triggercounter + 1
            sendEEGTrig(int(thisTrial.eventCode))
     
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            #routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            sendEEGTrig(BoundaryCode)
            core.wait(0.005)
            p.Out32(0x378,PauseCode)
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
 #completed 1 repeats of 'block1'
# push to dat File
    datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(expInfo['participant'],expInfo['session'],MMN.thisTrialN+1,thisTrial.cond,thisTrial.sound,thisTrial.speaker,thisTrial.file,thisTrial.eventCode,thisTrial.jitterDur,thisTrial.csvfile))
#completed 1 repeats of 'trials' loop

datFile.close()


# Shutting down:
win.close()
core.quit()
