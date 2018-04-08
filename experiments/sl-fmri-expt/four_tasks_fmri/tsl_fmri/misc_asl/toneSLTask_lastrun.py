#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Thu May 26 18:26:34 2016
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
expName = 'toneSLTask'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/wendytsai/Desktop/tone_structured_052616/toneSLTask.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "headphones"
headphonesClock = core.Clock()
text_40 = visual.TextStim(win=win, ori=0, name='text_40',
    text="We'll be listening to some sounds today, so before we start, please plug in headphones and make sure your volume isn't too loud or too quiet. Press space when you're ready!",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_23 = sound.Sound('instr_23.wav', secs=-1)
sound_23.setVolume(1)

# Initialize components for Routine "start"
startClock = core.Clock()
startText = visual.TextStim(win=win, ori=0, name='startText',
    text='Press the spacebar to begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_24 = sound.Sound('instr_1.wav', secs=-1)
sound_24.setVolume(1)

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text="Hi! We're going to listen to some alien folk music today.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_25 = sound.Sound('instr_2.wav', secs=-1)
sound_25.setVolume(1)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instr2Text = visual.TextStim(win=win, ori=0, name='instr2Text',
    text='This is Klaptoo!',    font='Arial',
    pos=[-.3, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_10 = visual.ImageStim(win=win, name='image_10',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_26 = sound.Sound('instr_3.wav', secs=-1)
sound_26.setVolume(1)

# Initialize components for Routine "instr3_2"
instr3_2Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text="Klaptoo is from Planet A.\nWe're going to listen to some\nfolk music from Klaptoo's \nplanet!",    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_11 = visual.ImageStim(win=win, name='image_11',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_27 = sound.Sound('instr_4.wav', secs=-1)
sound_27.setVolume(1)

# Initialize components for Routine "instr3_3"
instr3_3Clock = core.Clock()
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='Klaptoo is going to play\nhis favorite note for you \nnow. Listen carefully!',    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_13 = visual.ImageStim(win=win, name='image_13',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_28 = sound.Sound('instr_5.wav', secs=-1)
sound_28.setVolume(1)

# Initialize components for Routine "target_tone"
target_toneClock = core.Clock()
sound_12 = sound.Sound('T1C-M62.wav', secs=-1)
sound_12.setVolume(1)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='Press space to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instr3_4"
instr3_4Clock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text="When you hear Klaptoo play\nhis favorite note, press\nthe space bar as soon as you\ncan. Let's practice!",    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_14 = visual.ImageStim(win=win, name='image_14',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_29 = sound.Sound('instr_6.wav', secs=-1)
sound_29.setVolume(1)

# Initialize components for Routine "target_tone_2"
target_tone_2Clock = core.Clock()
sound_13 = sound.Sound('T1C-M62.wav', secs=-1)
sound_13.setVolume(1)
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='Press space!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instr3_6"
instr3_6Clock = core.Clock()
text_41 = visual.TextStim(win=win, ori=0, name='text_41',
    text='Good job! Now Klaptoo is \ngoing to play six notes in\na row. Press space when you\nhear his favorite note!',    font='Arial',
    pos=[-.4,.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_31 = visual.ImageStim(win=win, name='image_31',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_45 = sound.Sound('instr_24.wav', secs=-1)
sound_45.setVolume(1)

# Initialize components for Routine "six_tones_1"
six_tones_1Clock = core.Clock()
sound_43 = sound.Sound('A', secs=-1)
sound_43.setVolume(1)
image_32 = visual.ImageStim(win=win, name='image_32',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr3_7"
instr3_7Clock = core.Clock()
text_42 = visual.TextStim(win=win, ori=0, name='text_42',
    text="Did you hear it? The fourth\nnote was Klaptoo's favorite\nnote! Let's listen again...",    font='Arial',
    pos=[-.4,.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_33 = visual.ImageStim(win=win, name='image_33',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_46 = sound.Sound('instr_25.wav', secs=-1)
sound_46.setVolume(1)

# Initialize components for Routine "six_tones_1"
six_tones_1Clock = core.Clock()
sound_43 = sound.Sound('A', secs=-1)
sound_43.setVolume(1)
image_32 = visual.ImageStim(win=win, name='image_32',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr3_5"
instr3_5Clock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text="Good job! Now, Klaptoo is going\nto play us a song. Listen carefully\nand press the space bar whenever \nyou hear his favorite note. \nLet's start!",    font='Arial',
    pos=[-.4, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_15 = visual.ImageStim(win=win, name='image_15',
    image='AlienTrumpet.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_30 = sound.Sound('instr_7.wav', secs=-1)
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
    text="One of these aliens is going \nto play music from Klaptoo's \nplanet, and the other will not. \n\nListen to both songs, and press \nthe left arrow if the first song \nis the same as the music that \nKlaptoo made, and the right arrow \nif the second song is the same. ",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_33 = sound.Sound('instr_10.wav', secs=-1)
sound_33.setVolume(1)

# Initialize components for Routine "start"
startClock = core.Clock()
startText = visual.TextStim(win=win, ori=0, name='startText',
    text='Press the spacebar to begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_24 = sound.Sound('instr_1.wav', secs=-1)
sound_24.setVolume(1)

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
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
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
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
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
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
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
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
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
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
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
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
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
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
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
    text="Which song is like Klaptoo's? \nPress left for first and right for second.",    font='Arial',
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

# Initialize components for Routine "instr7"
instr7Clock = core.Clock()
text_21 = visual.TextStim(win=win, ori=0, name='text_21',
    text="Great job! Now we're going to start a new game.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_34 = sound.Sound('instr_12.wav', secs=-1)
sound_34.setVolume(1)

# Initialize components for Routine "instr8"
instr8Clock = core.Clock()
text_22 = visual.TextStim(win=win, ori=0, name='text_22',
    text='Meet Meeple, an alien \nfrom Planet B!',    font='Arial',
    pos=[-.5, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_16 = visual.ImageStim(win=win, name='image_16',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[0.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_35 = sound.Sound('instr_13.wav', secs=-1)
sound_35.setVolume(1)

# Initialize components for Routine "instr9"
instr9Clock = core.Clock()
text_23 = visual.TextStim(win=win, ori=0, name='text_23',
    text='Meeple is going \nto play some \nfolk music from \nher planet. ',    font='Arial',
    pos=[-.5, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_17 = visual.ImageStim(win=win, name='image_17',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_36 = sound.Sound('instr_14.wav', secs=-1)
sound_36.setVolume(1)

# Initialize components for Routine "instr10"
instr10Clock = core.Clock()
text_24 = visual.TextStim(win=win, ori=0, name='text_24',
    text='Meeple is going\nto play her \nfavorite note \nfor you now. \nListen carefully!',    font='Arial',
    pos=[-.5, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_18 = visual.ImageStim(win=win, name='image_18',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[.4,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_37 = sound.Sound('instr_15.wav', secs=-1)
sound_37.setVolume(1)

# Initialize components for Routine "target_tone_3"
target_tone_3Clock = core.Clock()
sound_14 = sound.Sound('T2C-M71.wav', secs=-1)
sound_14.setVolume(1)
text_25 = visual.TextStim(win=win, ori=0, name='text_25',
    text='Press space to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instr11"
instr11Clock = core.Clock()
text_26 = visual.TextStim(win=win, ori=0, name='text_26',
    text="When you hear \nMeeple play her\nfavorite note, \npress the space \nbar as soon as \nyou can. Let's \npractice!",    font='Arial',
    pos=[-.5, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_19 = visual.ImageStim(win=win, name='image_19',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[0.4,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_38 = sound.Sound('instr_16.wav', secs=-1)
sound_38.setVolume(1)

# Initialize components for Routine "target_tone_4"
target_tone_4Clock = core.Clock()
sound_15 = sound.Sound('T2C-M71.wav', secs=-1)
sound_15.setVolume(1)
text_27 = visual.TextStim(win=win, ori=0, name='text_27',
    text='Press space!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instr11_1"
instr11_1Clock = core.Clock()
text_43 = visual.TextStim(win=win, ori=0, name='text_43',
    text='Good job! Now Meeple is \ngoing to play six notes \nin a row. Press space \nwhen you hear her \nfavorite note!',    font='Arial',
    pos=[-.5,.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_34 = visual.ImageStim(win=win, name='image_34',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[0.4,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_47 = sound.Sound('instr_26.wav', secs=-1)
sound_47.setVolume(1)

# Initialize components for Routine "six_tones_2"
six_tones_2Clock = core.Clock()
sound_44 = sound.Sound('A', secs=-1)
sound_44.setVolume(1)
image_35 = visual.ImageStim(win=win, name='image_35',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr11_2"
instr11_2Clock = core.Clock()
text_44 = visual.TextStim(win=win, ori=0, name='text_44',
    text="Did you hear it? The \nfourth note was Meeple's \nfavorite note! Let's \nlisten again...",    font='Arial',
    pos=[-.5,.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_36 = visual.ImageStim(win=win, name='image_36',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[0.4,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_48 = sound.Sound('instr_27.wav', secs=-1)
sound_48.setVolume(1)

# Initialize components for Routine "six_tones_2"
six_tones_2Clock = core.Clock()
sound_44 = sound.Sound('A', secs=-1)
sound_44.setVolume(1)
image_35 = visual.ImageStim(win=win, name='image_35',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instr12"
instr12Clock = core.Clock()
text_28 = visual.TextStim(win=win, ori=0, name='text_28',
    text="Good job! Now, \nMeeple is going\nto play us a song. \nListen carefully\nand press the space \nbar whenever you\nhear her favorite \nnote. Let's start!",    font='Arial',
    pos=[-.5, .4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_20 = visual.ImageStim(win=win, name='image_20',
    image='AlienViolin.png', mask=None,
    ori=0, pos=[0.4, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_39 = sound.Sound('instr_17.wav', secs=-1)
sound_39.setVolume(1)

# Initialize components for Routine "trial_4"
trial_4Clock = core.Clock()
sound_16 = sound.Sound('A', secs=-1)
sound_16.setVolume(1)
image_21 = visual.ImageStim(win=win, name='image_21',
    image='AlienViolin.png', mask=None,
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

# Initialize components for Routine "instr13"
instr13Clock = core.Clock()
text_29 = visual.TextStim(win=win, ori=0, name='text_29',
    text='Now look at these two aliens:',    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
image_22 = visual.ImageStim(win=win, name='image_22',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -0.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_40 = sound.Sound('instr_9.wav', secs=-1)
sound_40.setVolume(1)

# Initialize components for Routine "instr14"
instr14Clock = core.Clock()
text_30 = visual.TextStim(win=win, ori=0, name='text_30',
    text="One of these aliens is going \nto play music from Meeple's \nplanet, and the other will not. \n\nListen to both songs, and press \nthe left arrow if the first song \nis the same as the music that \nMeeple made, and the right arrow \nif the second song is the same. ",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_41 = sound.Sound('instr_20.wav', secs=-1)
sound_41.setVolume(1)

# Initialize components for Routine "start"
startClock = core.Clock()
startText = visual.TextStim(win=win, ori=0, name='startText',
    text='Press the spacebar to begin.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
sound_24 = sound.Sound('instr_1.wav', secs=-1)
sound_24.setVolume(1)

# Initialize components for Routine "test7"
test7Clock = core.Clock()
sound_17 = sound.Sound('A', secs=-1)
sound_17.setVolume(1)
image_23 = visual.ImageStim(win=win, name='image_23',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_31 = visual.TextStim(win=win, ori=0, name='text_31',
    text="Which song is like Meeple's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test8"
test8Clock = core.Clock()
sound_18 = sound.Sound('A', secs=-1)
sound_18.setVolume(1)
text_32 = visual.TextStim(win=win, ori=0, name='text_32',
    text="Which song is like Meeple's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_24 = visual.ImageStim(win=win, name='image_24',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "test9"
test9Clock = core.Clock()
sound_19 = sound.Sound('A', secs=-1)
sound_19.setVolume(1)
image_25 = visual.ImageStim(win=win, name='image_25',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_33 = visual.TextStim(win=win, ori=0, name='text_33',
    text="Which song is like Meeple's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "triplet_pause_2"
triplet_pause_2Clock = core.Clock()
image_26 = visual.ImageStim(win=win, name='image_26',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_34 = visual.TextStim(win=win, ori=0, name='text_34',
    text="Which song is like Meeple's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "test10"
test10Clock = core.Clock()
sound_20 = sound.Sound('A', secs=-1)
sound_20.setVolume(1)
text_35 = visual.TextStim(win=win, ori=0, name='text_35',
    text="Which song is like Meeple's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_27 = visual.ImageStim(win=win, name='image_27',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "test11"
test11Clock = core.Clock()
sound_21 = sound.Sound('A', secs=-1)
sound_21.setVolume(1)
text_36 = visual.TextStim(win=win, ori=0, name='text_36',
    text="Which song is like Meeple's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_28 = visual.ImageStim(win=win, name='image_28',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "test12"
test12Clock = core.Clock()
sound_22 = sound.Sound('A', secs=-1)
sound_22.setVolume(1)
image_29 = visual.ImageStim(win=win, name='image_29',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_37 = visual.TextStim(win=win, ori=0, name='text_37',
    text="Which song is like Meeple's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "question_2"
question_2Clock = core.Clock()
image_30 = visual.ImageStim(win=win, name='image_30',
    image='2AFCAliens_2.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_38 = visual.TextStim(win=win, ori=0, name='text_38',
    text="Which song is like Meeple's? \nPress left for first and right for second.",    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "five_s_gap_2"
five_s_gap_2Clock = core.Clock()
text_39 = visual.TextStim(win=win, ori=0, name='text_39',
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

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "headphones"-------
t = 0
headphonesClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_26 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_26.status = NOT_STARTED
# keep track of which components have finished
headphonesComponents = []
headphonesComponents.append(text_40)
headphonesComponents.append(key_resp_26)
headphonesComponents.append(sound_23)
for thisComponent in headphonesComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "headphones"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = headphonesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_40* updates
    if t >= 0.0 and text_40.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_40.tStart = t  # underestimates by a little under one frame
        text_40.frameNStart = frameN  # exact frame index
        text_40.setAutoDraw(True)
    
    # *key_resp_26* updates
    if t >= 0.0 and key_resp_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_26.tStart = t  # underestimates by a little under one frame
        key_resp_26.frameNStart = frameN  # exact frame index
        key_resp_26.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_26.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_23
    if t >= 0.0 and sound_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_23.tStart = t  # underestimates by a little under one frame
        sound_23.frameNStart = frameN  # exact frame index
        sound_23.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in headphonesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "headphones"-------
for thisComponent in headphonesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_23.stop() #ensure sound has stopped at end of routine
# the Routine "headphones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
startKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
startKey.status = NOT_STARTED
# keep track of which components have finished
startComponents = []
startComponents.append(startText)
startComponents.append(startKey)
startComponents.append(sound_24)
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
    
    # *startText* updates
    if t >= 0.0 and startText.status == NOT_STARTED:
        # keep track of start time/frame for later
        startText.tStart = t  # underestimates by a little under one frame
        startText.frameNStart = frameN  # exact frame index
        startText.setAutoDraw(True)
    
    # *startKey* updates
    if t >= 0.0 and startKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        startKey.tStart = t  # underestimates by a little under one frame
        startKey.frameNStart = frameN  # exact frame index
        startKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if startKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_24
    if t >= 0.0 and sound_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_24.tStart = t  # underestimates by a little under one frame
        sound_24.frameNStart = frameN  # exact frame index
        sound_24.play()  # start the sound (it finishes automatically)
    
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
sound_24.stop() #ensure sound has stopped at end of routine
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instr1Components = []
instr1Components.append(instrText)
instr1Components.append(key_resp_2)
instr1Components.append(sound_25)
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
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_25
    if t >= 0.0 and sound_25.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_25.tStart = t  # underestimates by a little under one frame
        sound_25.frameNStart = frameN  # exact frame index
        sound_25.play()  # start the sound (it finishes automatically)
    
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
sound_25.stop() #ensure sound has stopped at end of routine
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr2"-------
t = 0
instr2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instr2Key = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr2Key.status = NOT_STARTED
# keep track of which components have finished
instr2Components = []
instr2Components.append(instr2Text)
instr2Components.append(instr2Key)
instr2Components.append(image_10)
instr2Components.append(sound_26)
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
    
    # *instr2Text* updates
    if t >= 0.0 and instr2Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2Text.tStart = t  # underestimates by a little under one frame
        instr2Text.frameNStart = frameN  # exact frame index
        instr2Text.setAutoDraw(True)
    
    # *instr2Key* updates
    if t >= 0.0 and instr2Key.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2Key.tStart = t  # underestimates by a little under one frame
        instr2Key.frameNStart = frameN  # exact frame index
        instr2Key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instr2Key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_10* updates
    if t >= 0.0 and image_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_10.tStart = t  # underestimates by a little under one frame
        image_10.frameNStart = frameN  # exact frame index
        image_10.setAutoDraw(True)
    # start/stop sound_26
    if t >= 0.0 and sound_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_26.tStart = t  # underestimates by a little under one frame
        sound_26.frameNStart = frameN  # exact frame index
        sound_26.play()  # start the sound (it finishes automatically)
    
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
sound_26.stop() #ensure sound has stopped at end of routine
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr3_2"-------
t = 0
instr3_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
instr3_2Components = []
instr3_2Components.append(text)
instr3_2Components.append(key_resp_3)
instr3_2Components.append(image_11)
instr3_2Components.append(sound_27)
for thisComponent in instr3_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_11* updates
    if t >= 0.0 and image_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_11.tStart = t  # underestimates by a little under one frame
        image_11.frameNStart = frameN  # exact frame index
        image_11.setAutoDraw(True)
    # start/stop sound_27
    if t >= 0.0 and sound_27.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_27.tStart = t  # underestimates by a little under one frame
        sound_27.frameNStart = frameN  # exact frame index
        sound_27.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_2"-------
for thisComponent in instr3_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_27.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr3_3"-------
t = 0
instr3_3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_9.status = NOT_STARTED
# keep track of which components have finished
instr3_3Components = []
instr3_3Components.append(text_7)
instr3_3Components.append(key_resp_9)
instr3_3Components.append(image_13)
instr3_3Components.append(sound_28)
for thisComponent in instr3_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # underestimates by a little under one frame
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # underestimates by a little under one frame
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_13* updates
    if t >= 0.0 and image_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_13.tStart = t  # underestimates by a little under one frame
        image_13.frameNStart = frameN  # exact frame index
        image_13.setAutoDraw(True)
    # start/stop sound_28
    if t >= 0.0 and sound_28.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_28.tStart = t  # underestimates by a little under one frame
        sound_28.frameNStart = frameN  # exact frame index
        sound_28.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_3"-------
for thisComponent in instr3_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_28.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_3" was not non-slip safe, so reset the non-slip timer
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
        theseKeys = event.getKeys(keyList=['space'])
        
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

#------Prepare to start Routine "instr3_4"-------
t = 0
instr3_4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_10.status = NOT_STARTED
# keep track of which components have finished
instr3_4Components = []
instr3_4Components.append(text_8)
instr3_4Components.append(image_14)
instr3_4Components.append(key_resp_10)
instr3_4Components.append(sound_29)
for thisComponent in instr3_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3_4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3_4Clock.getTime()
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_29
    if t >= 0.0 and sound_29.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_29.tStart = t  # underestimates by a little under one frame
        sound_29.frameNStart = frameN  # exact frame index
        sound_29.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr3_4"-------
for thisComponent in instr3_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_29.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "target_tone_2"-------
t = 0
target_tone_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_11.status = NOT_STARTED
# keep track of which components have finished
target_tone_2Components = []
target_tone_2Components.append(sound_13)
target_tone_2Components.append(key_resp_11)
target_tone_2Components.append(text_9)
for thisComponent in target_tone_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_tone_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_tone_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_13
    if t >= 0.0 and sound_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_13.tStart = t  # underestimates by a little under one frame
        sound_13.frameNStart = frameN  # exact frame index
        sound_13.play()  # start the sound (it finishes automatically)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t  # underestimates by a little under one frame
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # underestimates by a little under one frame
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_tone_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_tone_2"-------
for thisComponent in target_tone_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_13.stop() #ensure sound has stopped at end of routine
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
   key_resp_11.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "target_tone_2" was not non-slip safe, so reset the non-slip timer
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
instr3_6Components.append(sound_45)
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_45
    if t >= 0.0 and sound_45.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_45.tStart = t  # underestimates by a little under one frame
        sound_45.frameNStart = frameN  # exact frame index
        sound_45.play()  # start the sound (it finishes automatically)
    
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
sound_45.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials_1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('six_tones_1C.xlsx'),
    seed=None, name='practice_trials_1')
thisExp.addLoop(practice_trials_1)  # add the loop to the experiment
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_43.setSound(soundFile, secs=0.36)
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
        if sound_43.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_43.stop()  # stop the sound (if longer than duration)
        
        # *image_32* updates
        if t >= 0.0 and image_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_32.tStart = t  # underestimates by a little under one frame
            image_32.frameNStart = frameN  # exact frame index
            image_32.setAutoDraw(True)
        if image_32.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
        if practice_trial_1.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_trial_1.status = STOPPED
        if practice_trial_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
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
    # store data for practice_trials_1 (TrialHandler)
    practice_trials_1.addData('practice_trial_1.keys',practice_trial_1.keys)
    if practice_trial_1.keys != None:  # we had a response
        practice_trials_1.addData('practice_trial_1.rt', practice_trial_1.rt)
    thisExp.nextEntry()
    
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
instr3_7Components.append(sound_46)
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
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_46
    if t >= 0.0 and sound_46.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_46.tStart = t  # underestimates by a little under one frame
        sound_46.frameNStart = frameN  # exact frame index
        sound_46.play()  # start the sound (it finishes automatically)
    
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
sound_46.stop() #ensure sound has stopped at end of routine
# the Routine "instr3_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('six_tones_1C.xlsx'),
    seed=None, name='practice_trials_2')
thisExp.addLoop(practice_trials_2)  # add the loop to the experiment
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_43.setSound(soundFile, secs=0.36)
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
        if sound_43.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_43.stop()  # stop the sound (if longer than duration)
        
        # *image_32* updates
        if t >= 0.0 and image_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_32.tStart = t  # underestimates by a little under one frame
            image_32.frameNStart = frameN  # exact frame index
            image_32.setAutoDraw(True)
        if image_32.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
        if practice_trial_1.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            practice_trial_1.status = STOPPED
        if practice_trial_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
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
    thisExp.nextEntry()
    
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
        theseKeys = event.getKeys(keyList=['space'])
        
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
    trialList=data.importConditions('soundFileList1.xlsx'),
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    tone.setSound(soundFile, secs=0.36)
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
        if tone.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            tone.stop()  # stop the sound (if longer than duration)
        
        # *alien* updates
        if t >= 0.0 and alien.status == NOT_STARTED:
            # keep track of start time/frame for later
            alien.tStart = t  # underestimates by a little under one frame
            alien.frameNStart = frameN  # exact frame index
            alien.setAutoDraw(True)
        if alien.status == STARTED and t >= (0.0 + (.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
        if target_tone_key_resp.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
        theseKeys = event.getKeys(keyList=['space'])
        
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
        theseKeys = event.getKeys(keyList=['space'])
        
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

#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
startKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
startKey.status = NOT_STARTED
# keep track of which components have finished
startComponents = []
startComponents.append(startText)
startComponents.append(startKey)
startComponents.append(sound_24)
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
    
    # *startText* updates
    if t >= 0.0 and startText.status == NOT_STARTED:
        # keep track of start time/frame for later
        startText.tStart = t  # underestimates by a little under one frame
        startText.frameNStart = frameN  # exact frame index
        startText.setAutoDraw(True)
    
    # *startKey* updates
    if t >= 0.0 and startKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        startKey.tStart = t  # underestimates by a little under one frame
        startKey.frameNStart = frameN  # exact frame index
        startKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if startKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_24
    if t >= 0.0 and sound_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_24.tStart = t  # underestimates by a little under one frame
        sound_24.frameNStart = frameN  # exact frame index
        sound_24.play()  # start the sound (it finishes automatically)
    
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
sound_24.stop() #ensure sound has stopped at end of routine
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
twoAFC_1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('twoAFC_1.xlsx'),
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_1.setSound(soundFile1, secs=.36)
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
        if sound_1.status == STARTED and t >= (0 + (.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        if image_2.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_2.setAutoDraw(False)
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t  # underestimates by a little under one frame
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        if text_13.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_7.setSound(soundFile2, secs=0.36)
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
        if sound_7.status == STARTED and t >= (0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_7.stop()  # stop the sound (if longer than duration)
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        if image_3.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_3.setAutoDraw(False)
        
        # *text_14* updates
        if t >= 0.0 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t  # underestimates by a little under one frame
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        if text_14.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_8.setSound(soundFile3, secs=.36)
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
        if sound_8.status == STARTED and t >= (0 + (.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_8.stop()  # stop the sound (if longer than duration)
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t  # underestimates by a little under one frame
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        if image_4.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_4.setAutoDraw(False)
        
        # *text_15* updates
        if t >= 0.0 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t  # underestimates by a little under one frame
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        if text_15.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    routineTimer.add(0.750000)
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
        if image_5.status == STARTED and t >= (0.0 + (0.75-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_5.setAutoDraw(False)
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t  # underestimates by a little under one frame
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        if text_16.status == STARTED and t >= (0.0 + (0.75-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_16.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.75)
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_9.setSound(soundFile4, secs=.36)
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
        if sound_9.status == STARTED and t >= (0 + (.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_9.stop()  # stop the sound (if longer than duration)
        
        # *image_6* updates
        if t >= 0.0 and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_6.tStart = t  # underestimates by a little under one frame
            image_6.frameNStart = frameN  # exact frame index
            image_6.setAutoDraw(True)
        if image_6.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_6.setAutoDraw(False)
        
        # *text_17* updates
        if t >= 0.0 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t  # underestimates by a little under one frame
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        if text_17.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_10.setSound(soundFile5, secs=.36)
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
        if sound_10.status == STARTED and t >= (0 + (.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_10.stop()  # stop the sound (if longer than duration)
        
        # *image_7* updates
        if t >= 0.0 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t  # underestimates by a little under one frame
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        if image_7.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_7.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 0.0 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t  # underestimates by a little under one frame
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        if text_18.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_11.setSound(soundFile6, secs=.36)
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
        if sound_11.status == STARTED and t >= (0 + (.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_11.stop()  # stop the sound (if longer than duration)
        
        # *image_8* updates
        if t >= 0.0 and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t  # underestimates by a little under one frame
            image_8.frameNStart = frameN  # exact frame index
            image_8.setAutoDraw(True)
        if image_8.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_8.setAutoDraw(False)
        
        # *text_19* updates
        if t >= 0.0 and text_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_19.tStart = t  # underestimates by a little under one frame
            text_19.frameNStart = frameN  # exact frame index
            text_19.setAutoDraw(True)
        if text_19.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
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
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
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
    routineTimer.add(2.500000)
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
        if text_4.status == STARTED and t >= (0.0 + (2.5-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    
# completed 1 repeats of 'twoAFC_1'


#------Prepare to start Routine "instr7"-------
t = 0
instr7Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_14 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_14.status = NOT_STARTED
# keep track of which components have finished
instr7Components = []
instr7Components.append(text_21)
instr7Components.append(key_resp_14)
instr7Components.append(sound_34)
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
    
    # *text_21* updates
    if t >= 0.0 and text_21.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_21.tStart = t  # underestimates by a little under one frame
        text_21.frameNStart = frameN  # exact frame index
        text_21.setAutoDraw(True)
    
    # *key_resp_14* updates
    if t >= 0.0 and key_resp_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_14.tStart = t  # underestimates by a little under one frame
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_14.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_34
    if t >= 0.0 and sound_34.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_34.tStart = t  # underestimates by a little under one frame
        sound_34.frameNStart = frameN  # exact frame index
        sound_34.play()  # start the sound (it finishes automatically)
    
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
sound_34.stop() #ensure sound has stopped at end of routine
# the Routine "instr7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr8"-------
t = 0
instr8Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_16 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_16.status = NOT_STARTED
# keep track of which components have finished
instr8Components = []
instr8Components.append(text_22)
instr8Components.append(key_resp_16)
instr8Components.append(image_16)
instr8Components.append(sound_35)
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
    
    # *text_22* updates
    if t >= 0.0 and text_22.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_22.tStart = t  # underestimates by a little under one frame
        text_22.frameNStart = frameN  # exact frame index
        text_22.setAutoDraw(True)
    
    # *key_resp_16* updates
    if t >= 0.0 and key_resp_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_16.tStart = t  # underestimates by a little under one frame
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_16.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_16* updates
    if t >= 0.0 and image_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_16.tStart = t  # underestimates by a little under one frame
        image_16.frameNStart = frameN  # exact frame index
        image_16.setAutoDraw(True)
    # start/stop sound_35
    if t >= 0.0 and sound_35.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_35.tStart = t  # underestimates by a little under one frame
        sound_35.frameNStart = frameN  # exact frame index
        sound_35.play()  # start the sound (it finishes automatically)
    
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
sound_35.stop() #ensure sound has stopped at end of routine
# the Routine "instr8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr9"-------
t = 0
instr9Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_17 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_17.status = NOT_STARTED
# keep track of which components have finished
instr9Components = []
instr9Components.append(text_23)
instr9Components.append(key_resp_17)
instr9Components.append(image_17)
instr9Components.append(sound_36)
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
    
    # *text_23* updates
    if t >= 0.0 and text_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_23.tStart = t  # underestimates by a little under one frame
        text_23.frameNStart = frameN  # exact frame index
        text_23.setAutoDraw(True)
    
    # *key_resp_17* updates
    if t >= 0.0 and key_resp_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_17.tStart = t  # underestimates by a little under one frame
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_17.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_17* updates
    if t >= 0.0 and image_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_17.tStart = t  # underestimates by a little under one frame
        image_17.frameNStart = frameN  # exact frame index
        image_17.setAutoDraw(True)
    # start/stop sound_36
    if t >= 0.0 and sound_36.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_36.tStart = t  # underestimates by a little under one frame
        sound_36.frameNStart = frameN  # exact frame index
        sound_36.play()  # start the sound (it finishes automatically)
    
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
sound_36.stop() #ensure sound has stopped at end of routine
# the Routine "instr9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr10"-------
t = 0
instr10Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_18 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_18.status = NOT_STARTED
# keep track of which components have finished
instr10Components = []
instr10Components.append(text_24)
instr10Components.append(image_18)
instr10Components.append(key_resp_18)
instr10Components.append(sound_37)
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
    
    # *text_24* updates
    if t >= 0.0 and text_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_24.tStart = t  # underestimates by a little under one frame
        text_24.frameNStart = frameN  # exact frame index
        text_24.setAutoDraw(True)
    
    # *image_18* updates
    if t >= 0.0 and image_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_18.tStart = t  # underestimates by a little under one frame
        image_18.frameNStart = frameN  # exact frame index
        image_18.setAutoDraw(True)
    
    # *key_resp_18* updates
    if t >= 0.0 and key_resp_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_18.tStart = t  # underestimates by a little under one frame
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_18.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_37
    if t >= 0.0 and sound_37.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_37.tStart = t  # underestimates by a little under one frame
        sound_37.frameNStart = frameN  # exact frame index
        sound_37.play()  # start the sound (it finishes automatically)
    
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
sound_37.stop() #ensure sound has stopped at end of routine
# the Routine "instr10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "target_tone_3"-------
t = 0
target_tone_3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_19 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_19.status = NOT_STARTED
# keep track of which components have finished
target_tone_3Components = []
target_tone_3Components.append(sound_14)
target_tone_3Components.append(key_resp_19)
target_tone_3Components.append(text_25)
for thisComponent in target_tone_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_tone_3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_tone_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_14
    if t >= 0.0 and sound_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_14.tStart = t  # underestimates by a little under one frame
        sound_14.frameNStart = frameN  # exact frame index
        sound_14.play()  # start the sound (it finishes automatically)
    
    # *key_resp_19* updates
    if t >= 0.0 and key_resp_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_19.tStart = t  # underestimates by a little under one frame
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_19.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_19.keys = theseKeys[-1]  # just the last key pressed
            key_resp_19.rt = key_resp_19.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_25* updates
    if t >= 0.0 and text_25.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_25.tStart = t  # underestimates by a little under one frame
        text_25.frameNStart = frameN  # exact frame index
        text_25.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_tone_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_tone_3"-------
for thisComponent in target_tone_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_14.stop() #ensure sound has stopped at end of routine
# check responses
if key_resp_19.keys in ['', [], None]:  # No response was made
   key_resp_19.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_19.keys',key_resp_19.keys)
if key_resp_19.keys != None:  # we had a response
    thisExp.addData('key_resp_19.rt', key_resp_19.rt)
thisExp.nextEntry()
# the Routine "target_tone_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr11"-------
t = 0
instr11Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_20 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_20.status = NOT_STARTED
# keep track of which components have finished
instr11Components = []
instr11Components.append(text_26)
instr11Components.append(key_resp_20)
instr11Components.append(image_19)
instr11Components.append(sound_38)
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
    
    # *text_26* updates
    if t >= 0.0 and text_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_26.tStart = t  # underestimates by a little under one frame
        text_26.frameNStart = frameN  # exact frame index
        text_26.setAutoDraw(True)
    
    # *key_resp_20* updates
    if t >= 0.0 and key_resp_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_20.tStart = t  # underestimates by a little under one frame
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_20.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_19* updates
    if t >= 0.0 and image_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_19.tStart = t  # underestimates by a little under one frame
        image_19.frameNStart = frameN  # exact frame index
        image_19.setAutoDraw(True)
    # start/stop sound_38
    if t >= 0.0 and sound_38.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_38.tStart = t  # underestimates by a little under one frame
        sound_38.frameNStart = frameN  # exact frame index
        sound_38.play()  # start the sound (it finishes automatically)
    
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
sound_38.stop() #ensure sound has stopped at end of routine
# the Routine "instr11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "target_tone_4"-------
t = 0
target_tone_4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_21 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_21.status = NOT_STARTED
# keep track of which components have finished
target_tone_4Components = []
target_tone_4Components.append(sound_15)
target_tone_4Components.append(key_resp_21)
target_tone_4Components.append(text_27)
for thisComponent in target_tone_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "target_tone_4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = target_tone_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_15
    if t >= 0.0 and sound_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_15.tStart = t  # underestimates by a little under one frame
        sound_15.frameNStart = frameN  # exact frame index
        sound_15.play()  # start the sound (it finishes automatically)
    
    # *key_resp_21* updates
    if t >= 0.0 and key_resp_21.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_21.tStart = t  # underestimates by a little under one frame
        key_resp_21.frameNStart = frameN  # exact frame index
        key_resp_21.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_21.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text_27* updates
    if t >= 0.0 and text_27.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_27.tStart = t  # underestimates by a little under one frame
        text_27.frameNStart = frameN  # exact frame index
        text_27.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in target_tone_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "target_tone_4"-------
for thisComponent in target_tone_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_15.stop() #ensure sound has stopped at end of routine
# the Routine "target_tone_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr11_1"-------
t = 0
instr11_1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_29 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_29.status = NOT_STARTED
# keep track of which components have finished
instr11_1Components = []
instr11_1Components.append(text_43)
instr11_1Components.append(image_34)
instr11_1Components.append(key_resp_29)
instr11_1Components.append(sound_47)
for thisComponent in instr11_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr11_1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr11_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_43* updates
    if t >= 0.0 and text_43.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_43.tStart = t  # underestimates by a little under one frame
        text_43.frameNStart = frameN  # exact frame index
        text_43.setAutoDraw(True)
    
    # *image_34* updates
    if t >= 0.0 and image_34.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_34.tStart = t  # underestimates by a little under one frame
        image_34.frameNStart = frameN  # exact frame index
        image_34.setAutoDraw(True)
    
    # *key_resp_29* updates
    if t >= 0.0 and key_resp_29.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_29.tStart = t  # underestimates by a little under one frame
        key_resp_29.frameNStart = frameN  # exact frame index
        key_resp_29.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_29.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_47
    if t >= 0.0 and sound_47.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_47.tStart = t  # underestimates by a little under one frame
        sound_47.frameNStart = frameN  # exact frame index
        sound_47.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr11_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr11_1"-------
for thisComponent in instr11_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_47.stop() #ensure sound has stopped at end of routine
# the Routine "instr11_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('six_tones_2C.xlsx'),
    seed=None, name='practice_trials_3')
thisExp.addLoop(practice_trials_3)  # add the loop to the experiment
thisPractice_trial_3 = practice_trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_trial_3.rgb)
if thisPractice_trial_3 != None:
    for paramName in thisPractice_trial_3.keys():
        exec(paramName + '= thisPractice_trial_3.' + paramName)

for thisPractice_trial_3 in practice_trials_3:
    currentLoop = practice_trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial_3.rgb)
    if thisPractice_trial_3 != None:
        for paramName in thisPractice_trial_3.keys():
            exec(paramName + '= thisPractice_trial_3.' + paramName)
    
    #------Prepare to start Routine "six_tones_2"-------
    t = 0
    six_tones_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_44.setSound(soundFile, secs=0.36)
    key_resp_30 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_30.status = NOT_STARTED
    # keep track of which components have finished
    six_tones_2Components = []
    six_tones_2Components.append(sound_44)
    six_tones_2Components.append(image_35)
    six_tones_2Components.append(key_resp_30)
    for thisComponent in six_tones_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "six_tones_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = six_tones_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_44
        if t >= 0.0 and sound_44.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_44.tStart = t  # underestimates by a little under one frame
            sound_44.frameNStart = frameN  # exact frame index
            sound_44.play()  # start the sound (it finishes automatically)
        if sound_44.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_44.stop()  # stop the sound (if longer than duration)
        
        # *image_35* updates
        if t >= 0.0 and image_35.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_35.tStart = t  # underestimates by a little under one frame
            image_35.frameNStart = frameN  # exact frame index
            image_35.setAutoDraw(True)
        if image_35.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_35.setAutoDraw(False)
        
        # *key_resp_30* updates
        if t >= 0.0 and key_resp_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_30.tStart = t  # underestimates by a little under one frame
            key_resp_30.frameNStart = frameN  # exact frame index
            key_resp_30.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_30.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_30.status = STOPPED
        if key_resp_30.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_30.keys = theseKeys[-1]  # just the last key pressed
                key_resp_30.rt = key_resp_30.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in six_tones_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "six_tones_2"-------
    for thisComponent in six_tones_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_44.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_30.keys in ['', [], None]:  # No response was made
       key_resp_30.keys=None
    # store data for practice_trials_3 (TrialHandler)
    practice_trials_3.addData('key_resp_30.keys',key_resp_30.keys)
    if key_resp_30.keys != None:  # we had a response
        practice_trials_3.addData('key_resp_30.rt', key_resp_30.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials_3'


#------Prepare to start Routine "instr11_2"-------
t = 0
instr11_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_31 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_31.status = NOT_STARTED
# keep track of which components have finished
instr11_2Components = []
instr11_2Components.append(text_44)
instr11_2Components.append(image_36)
instr11_2Components.append(key_resp_31)
instr11_2Components.append(sound_48)
for thisComponent in instr11_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr11_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr11_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_44* updates
    if t >= 0.0 and text_44.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_44.tStart = t  # underestimates by a little under one frame
        text_44.frameNStart = frameN  # exact frame index
        text_44.setAutoDraw(True)
    
    # *image_36* updates
    if t >= 0.0 and image_36.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_36.tStart = t  # underestimates by a little under one frame
        image_36.frameNStart = frameN  # exact frame index
        image_36.setAutoDraw(True)
    
    # *key_resp_31* updates
    if t >= 0.0 and key_resp_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_31.tStart = t  # underestimates by a little under one frame
        key_resp_31.frameNStart = frameN  # exact frame index
        key_resp_31.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_31.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_48
    if t >= 0.0 and sound_48.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_48.tStart = t  # underestimates by a little under one frame
        sound_48.frameNStart = frameN  # exact frame index
        sound_48.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr11_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr11_2"-------
for thisComponent in instr11_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_48.stop() #ensure sound has stopped at end of routine
# the Routine "instr11_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('six_tones_2C.xlsx'),
    seed=None, name='practice_trials_4')
thisExp.addLoop(practice_trials_4)  # add the loop to the experiment
thisPractice_trial_4 = practice_trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_trial_4.rgb)
if thisPractice_trial_4 != None:
    for paramName in thisPractice_trial_4.keys():
        exec(paramName + '= thisPractice_trial_4.' + paramName)

for thisPractice_trial_4 in practice_trials_4:
    currentLoop = practice_trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial_4.rgb)
    if thisPractice_trial_4 != None:
        for paramName in thisPractice_trial_4.keys():
            exec(paramName + '= thisPractice_trial_4.' + paramName)
    
    #------Prepare to start Routine "six_tones_2"-------
    t = 0
    six_tones_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_44.setSound(soundFile, secs=0.36)
    key_resp_30 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_30.status = NOT_STARTED
    # keep track of which components have finished
    six_tones_2Components = []
    six_tones_2Components.append(sound_44)
    six_tones_2Components.append(image_35)
    six_tones_2Components.append(key_resp_30)
    for thisComponent in six_tones_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "six_tones_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = six_tones_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_44
        if t >= 0.0 and sound_44.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_44.tStart = t  # underestimates by a little under one frame
            sound_44.frameNStart = frameN  # exact frame index
            sound_44.play()  # start the sound (it finishes automatically)
        if sound_44.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_44.stop()  # stop the sound (if longer than duration)
        
        # *image_35* updates
        if t >= 0.0 and image_35.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_35.tStart = t  # underestimates by a little under one frame
            image_35.frameNStart = frameN  # exact frame index
            image_35.setAutoDraw(True)
        if image_35.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_35.setAutoDraw(False)
        
        # *key_resp_30* updates
        if t >= 0.0 and key_resp_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_30.tStart = t  # underestimates by a little under one frame
            key_resp_30.frameNStart = frameN  # exact frame index
            key_resp_30.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_30.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_30.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_30.status = STOPPED
        if key_resp_30.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_30.keys = theseKeys[-1]  # just the last key pressed
                key_resp_30.rt = key_resp_30.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in six_tones_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "six_tones_2"-------
    for thisComponent in six_tones_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_44.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_30.keys in ['', [], None]:  # No response was made
       key_resp_30.keys=None
    # store data for practice_trials_4 (TrialHandler)
    practice_trials_4.addData('key_resp_30.keys',key_resp_30.keys)
    if key_resp_30.keys != None:  # we had a response
        practice_trials_4.addData('key_resp_30.rt', key_resp_30.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials_4'


#------Prepare to start Routine "instr12"-------
t = 0
instr12Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_22 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_22.status = NOT_STARTED
# keep track of which components have finished
instr12Components = []
instr12Components.append(text_28)
instr12Components.append(key_resp_22)
instr12Components.append(image_20)
instr12Components.append(sound_39)
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
    
    # *text_28* updates
    if t >= 0.0 and text_28.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_28.tStart = t  # underestimates by a little under one frame
        text_28.frameNStart = frameN  # exact frame index
        text_28.setAutoDraw(True)
    
    # *key_resp_22* updates
    if t >= 0.0 and key_resp_22.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_22.tStart = t  # underestimates by a little under one frame
        key_resp_22.frameNStart = frameN  # exact frame index
        key_resp_22.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_22.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_20* updates
    if t >= 0.0 and image_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_20.tStart = t  # underestimates by a little under one frame
        image_20.frameNStart = frameN  # exact frame index
        image_20.setAutoDraw(True)
    # start/stop sound_39
    if t >= 0.0 and sound_39.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_39.tStart = t  # underestimates by a little under one frame
        sound_39.frameNStart = frameN  # exact frame index
        sound_39.play()  # start the sound (it finishes automatically)
    
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
sound_39.stop() #ensure sound has stopped at end of routine
# the Routine "instr12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('soundFileList2.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "trial_4"-------
    t = 0
    trial_4Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_16.setSound(soundFile, secs=0.36)
    target_tone_key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    target_tone_key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    trial_4Components = []
    trial_4Components.append(sound_16)
    trial_4Components.append(image_21)
    trial_4Components.append(target_tone_key_resp_2)
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_4"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_16
        if t >= 0.0 and sound_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_16.tStart = t  # underestimates by a little under one frame
            sound_16.frameNStart = frameN  # exact frame index
            sound_16.play()  # start the sound (it finishes automatically)
        if sound_16.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_16.stop()  # stop the sound (if longer than duration)
        
        # *image_21* updates
        if t >= 0.0 and image_21.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_21.tStart = t  # underestimates by a little under one frame
            image_21.frameNStart = frameN  # exact frame index
            image_21.setAutoDraw(True)
        if image_21.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_21.setAutoDraw(False)
        
        # *target_tone_key_resp_2* updates
        if t >= 0.0 and target_tone_key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            target_tone_key_resp_2.tStart = t  # underestimates by a little under one frame
            target_tone_key_resp_2.frameNStart = frameN  # exact frame index
            target_tone_key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(target_tone_key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if target_tone_key_resp_2.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            target_tone_key_resp_2.status = STOPPED
        if target_tone_key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                target_tone_key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                target_tone_key_resp_2.rt = target_tone_key_resp_2.clock.getTime()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_4"-------
    for thisComponent in trial_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_16.stop() #ensure sound has stopped at end of routine
    # check responses
    if target_tone_key_resp_2.keys in ['', [], None]:  # No response was made
       target_tone_key_resp_2.keys=None
    # store data for trials_2 (TrialHandler)
    trials_2.addData('target_tone_key_resp_2.keys',target_tone_key_resp_2.keys)
    if target_tone_key_resp_2.keys != None:  # we had a response
        trials_2.addData('target_tone_key_resp_2.rt', target_tone_key_resp_2.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


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

#------Prepare to start Routine "instr13"-------
t = 0
instr13Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_23 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_23.status = NOT_STARTED
# keep track of which components have finished
instr13Components = []
instr13Components.append(text_29)
instr13Components.append(key_resp_23)
instr13Components.append(image_22)
instr13Components.append(sound_40)
for thisComponent in instr13Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr13"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr13Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_29* updates
    if t >= 0.0 and text_29.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_29.tStart = t  # underestimates by a little under one frame
        text_29.frameNStart = frameN  # exact frame index
        text_29.setAutoDraw(True)
    
    # *key_resp_23* updates
    if t >= 0.0 and key_resp_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_23.tStart = t  # underestimates by a little under one frame
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_23.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *image_22* updates
    if t >= 0.0 and image_22.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_22.tStart = t  # underestimates by a little under one frame
        image_22.frameNStart = frameN  # exact frame index
        image_22.setAutoDraw(True)
    # start/stop sound_40
    if t >= 0.0 and sound_40.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_40.tStart = t  # underestimates by a little under one frame
        sound_40.frameNStart = frameN  # exact frame index
        sound_40.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr13Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr13"-------
for thisComponent in instr13Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_40.stop() #ensure sound has stopped at end of routine
# the Routine "instr13" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instr14"-------
t = 0
instr14Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_24 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_24.status = NOT_STARTED
# keep track of which components have finished
instr14Components = []
instr14Components.append(text_30)
instr14Components.append(key_resp_24)
instr14Components.append(sound_41)
for thisComponent in instr14Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr14"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr14Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if t >= 0.0 and text_30.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_30.tStart = t  # underestimates by a little under one frame
        text_30.frameNStart = frameN  # exact frame index
        text_30.setAutoDraw(True)
    
    # *key_resp_24* updates
    if t >= 0.0 and key_resp_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_24.tStart = t  # underestimates by a little under one frame
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_24.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_41
    if t >= 0.0 and sound_41.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_41.tStart = t  # underestimates by a little under one frame
        sound_41.frameNStart = frameN  # exact frame index
        sound_41.play()  # start the sound (it finishes automatically)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr14Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr14"-------
for thisComponent in instr14Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_41.stop() #ensure sound has stopped at end of routine
# the Routine "instr14" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
startKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
startKey.status = NOT_STARTED
# keep track of which components have finished
startComponents = []
startComponents.append(startText)
startComponents.append(startKey)
startComponents.append(sound_24)
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
    
    # *startText* updates
    if t >= 0.0 and startText.status == NOT_STARTED:
        # keep track of start time/frame for later
        startText.tStart = t  # underestimates by a little under one frame
        startText.frameNStart = frameN  # exact frame index
        startText.setAutoDraw(True)
    
    # *startKey* updates
    if t >= 0.0 and startKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        startKey.tStart = t  # underestimates by a little under one frame
        startKey.frameNStart = frameN  # exact frame index
        startKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if startKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_24
    if t >= 0.0 and sound_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_24.tStart = t  # underestimates by a little under one frame
        sound_24.frameNStart = frameN  # exact frame index
        sound_24.play()  # start the sound (it finishes automatically)
    
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
sound_24.stop() #ensure sound has stopped at end of routine
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
twoAFC_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('twoAFC_2.xlsx'),
    seed=None, name='twoAFC_2')
thisExp.addLoop(twoAFC_2)  # add the loop to the experiment
thisTwoAFC_2 = twoAFC_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTwoAFC_2.rgb)
if thisTwoAFC_2 != None:
    for paramName in thisTwoAFC_2.keys():
        exec(paramName + '= thisTwoAFC_2.' + paramName)

for thisTwoAFC_2 in twoAFC_2:
    currentLoop = twoAFC_2
    # abbreviate parameter names if possible (e.g. rgb = thisTwoAFC_2.rgb)
    if thisTwoAFC_2 != None:
        for paramName in thisTwoAFC_2.keys():
            exec(paramName + '= thisTwoAFC_2.' + paramName)
    
    #------Prepare to start Routine "test7"-------
    t = 0
    test7Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_17.setSound(soundFile1, secs=0.36)
    # keep track of which components have finished
    test7Components = []
    test7Components.append(sound_17)
    test7Components.append(image_23)
    test7Components.append(text_31)
    for thisComponent in test7Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test7"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test7Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_17
        if t >= 0.0 and sound_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_17.tStart = t  # underestimates by a little under one frame
            sound_17.frameNStart = frameN  # exact frame index
            sound_17.play()  # start the sound (it finishes automatically)
        if sound_17.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_17.stop()  # stop the sound (if longer than duration)
        
        # *image_23* updates
        if t >= 0.0 and image_23.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_23.tStart = t  # underestimates by a little under one frame
            image_23.frameNStart = frameN  # exact frame index
            image_23.setAutoDraw(True)
        if image_23.status == STARTED and t >= (0.0 + (.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_23.setAutoDraw(False)
        
        # *text_31* updates
        if t >= 0.0 and text_31.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_31.tStart = t  # underestimates by a little under one frame
            text_31.frameNStart = frameN  # exact frame index
            text_31.setAutoDraw(True)
        if text_31.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_31.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test7"-------
    for thisComponent in test7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_17.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test8"-------
    t = 0
    test8Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_18.setSound(soundFile2, secs=0.36)
    # keep track of which components have finished
    test8Components = []
    test8Components.append(sound_18)
    test8Components.append(text_32)
    test8Components.append(image_24)
    for thisComponent in test8Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test8"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test8Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_18
        if t >= 0.0 and sound_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_18.tStart = t  # underestimates by a little under one frame
            sound_18.frameNStart = frameN  # exact frame index
            sound_18.play()  # start the sound (it finishes automatically)
        if sound_18.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_18.stop()  # stop the sound (if longer than duration)
        
        # *text_32* updates
        if t >= 0.0 and text_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_32.tStart = t  # underestimates by a little under one frame
            text_32.frameNStart = frameN  # exact frame index
            text_32.setAutoDraw(True)
        if text_32.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_32.setAutoDraw(False)
        
        # *image_24* updates
        if t >= 0.0 and image_24.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_24.tStart = t  # underestimates by a little under one frame
            image_24.frameNStart = frameN  # exact frame index
            image_24.setAutoDraw(True)
        if image_24.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_24.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test8"-------
    for thisComponent in test8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_18.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test9"-------
    t = 0
    test9Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_19.setSound(soundFile3, secs=0.36)
    # keep track of which components have finished
    test9Components = []
    test9Components.append(sound_19)
    test9Components.append(image_25)
    test9Components.append(text_33)
    for thisComponent in test9Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test9"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test9Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_19
        if t >= 0.0 and sound_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_19.tStart = t  # underestimates by a little under one frame
            sound_19.frameNStart = frameN  # exact frame index
            sound_19.play()  # start the sound (it finishes automatically)
        if sound_19.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_19.stop()  # stop the sound (if longer than duration)
        
        # *image_25* updates
        if t >= 0.0 and image_25.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_25.tStart = t  # underestimates by a little under one frame
            image_25.frameNStart = frameN  # exact frame index
            image_25.setAutoDraw(True)
        if image_25.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_25.setAutoDraw(False)
        
        # *text_33* updates
        if t >= 0.0 and text_33.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_33.tStart = t  # underestimates by a little under one frame
            text_33.frameNStart = frameN  # exact frame index
            text_33.setAutoDraw(True)
        if text_33.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_33.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test9"-------
    for thisComponent in test9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_19.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "triplet_pause_2"-------
    t = 0
    triplet_pause_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    triplet_pause_2Components = []
    triplet_pause_2Components.append(image_26)
    triplet_pause_2Components.append(text_34)
    for thisComponent in triplet_pause_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "triplet_pause_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = triplet_pause_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_26* updates
        if t >= 0.0 and image_26.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_26.tStart = t  # underestimates by a little under one frame
            image_26.frameNStart = frameN  # exact frame index
            image_26.setAutoDraw(True)
        if image_26.status == STARTED and t >= (0.0 + (0.75-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_26.setAutoDraw(False)
        
        # *text_34* updates
        if t >= 0.0 and text_34.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_34.tStart = t  # underestimates by a little under one frame
            text_34.frameNStart = frameN  # exact frame index
            text_34.setAutoDraw(True)
        if text_34.status == STARTED and t >= (0.0 + (0.75-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_34.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in triplet_pause_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "triplet_pause_2"-------
    for thisComponent in triplet_pause_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "test10"-------
    t = 0
    test10Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_20.setSound(soundFile4, secs=0.36)
    # keep track of which components have finished
    test10Components = []
    test10Components.append(sound_20)
    test10Components.append(text_35)
    test10Components.append(image_27)
    for thisComponent in test10Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test10"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test10Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_20
        if t >= 0.0 and sound_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_20.tStart = t  # underestimates by a little under one frame
            sound_20.frameNStart = frameN  # exact frame index
            sound_20.play()  # start the sound (it finishes automatically)
        if sound_20.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_20.stop()  # stop the sound (if longer than duration)
        
        # *text_35* updates
        if t >= 0.0 and text_35.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_35.tStart = t  # underestimates by a little under one frame
            text_35.frameNStart = frameN  # exact frame index
            text_35.setAutoDraw(True)
        if text_35.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_35.setAutoDraw(False)
        
        # *image_27* updates
        if t >= 0.0 and image_27.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_27.tStart = t  # underestimates by a little under one frame
            image_27.frameNStart = frameN  # exact frame index
            image_27.setAutoDraw(True)
        if image_27.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_27.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test10"-------
    for thisComponent in test10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_20.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test11"-------
    t = 0
    test11Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_21.setSound(soundFile5, secs=0.36)
    # keep track of which components have finished
    test11Components = []
    test11Components.append(sound_21)
    test11Components.append(text_36)
    test11Components.append(image_28)
    for thisComponent in test11Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test11"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test11Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_21
        if t >= 0.0 and sound_21.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_21.tStart = t  # underestimates by a little under one frame
            sound_21.frameNStart = frameN  # exact frame index
            sound_21.play()  # start the sound (it finishes automatically)
        if sound_21.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_21.stop()  # stop the sound (if longer than duration)
        
        # *text_36* updates
        if t >= 0.0 and text_36.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_36.tStart = t  # underestimates by a little under one frame
            text_36.frameNStart = frameN  # exact frame index
            text_36.setAutoDraw(True)
        if text_36.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_36.setAutoDraw(False)
        
        # *image_28* updates
        if t >= 0.0 and image_28.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_28.tStart = t  # underestimates by a little under one frame
            image_28.frameNStart = frameN  # exact frame index
            image_28.setAutoDraw(True)
        if image_28.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_28.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test11Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test11"-------
    for thisComponent in test11Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_21.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "test12"-------
    t = 0
    test12Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.360000)
    # update component parameters for each repeat
    sound_22.setSound(soundFile6, secs=0.36)
    # keep track of which components have finished
    test12Components = []
    test12Components.append(sound_22)
    test12Components.append(image_29)
    test12Components.append(text_37)
    for thisComponent in test12Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test12"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test12Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_22
        if t >= 0.0 and sound_22.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_22.tStart = t  # underestimates by a little under one frame
            sound_22.frameNStart = frameN  # exact frame index
            sound_22.play()  # start the sound (it finishes automatically)
        if sound_22.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_22.stop()  # stop the sound (if longer than duration)
        
        # *image_29* updates
        if t >= 0.0 and image_29.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_29.tStart = t  # underestimates by a little under one frame
            image_29.frameNStart = frameN  # exact frame index
            image_29.setAutoDraw(True)
        if image_29.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_29.setAutoDraw(False)
        
        # *text_37* updates
        if t >= 0.0 and text_37.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_37.tStart = t  # underestimates by a little under one frame
            text_37.frameNStart = frameN  # exact frame index
            text_37.setAutoDraw(True)
        if text_37.status == STARTED and t >= (0.0 + (0.36-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_37.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test12Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test12"-------
    for thisComponent in test12Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_22.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "question_2"-------
    t = 0
    question_2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_25 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_25.status = NOT_STARTED
    # keep track of which components have finished
    question_2Components = []
    question_2Components.append(key_resp_25)
    question_2Components.append(image_30)
    question_2Components.append(text_38)
    for thisComponent in question_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "question_2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = question_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_25* updates
        if t >= 0.0 and key_resp_25.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_25.tStart = t  # underestimates by a little under one frame
            key_resp_25.frameNStart = frameN  # exact frame index
            key_resp_25.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_25.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_25.keys = theseKeys[-1]  # just the last key pressed
                key_resp_25.rt = key_resp_25.clock.getTime()
                # was this 'correct'?
                if (key_resp_25.keys == str(corrAns)) or (key_resp_25.keys == corrAns):
                    key_resp_25.corr = 1
                else:
                    key_resp_25.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image_30* updates
        if t >= 0.0 and image_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_30.tStart = t  # underestimates by a little under one frame
            image_30.frameNStart = frameN  # exact frame index
            image_30.setAutoDraw(True)
        
        # *text_38* updates
        if t >= 0.0 and text_38.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_38.tStart = t  # underestimates by a little under one frame
            text_38.frameNStart = frameN  # exact frame index
            text_38.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "question_2"-------
    for thisComponent in question_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_25.keys in ['', [], None]:  # No response was made
       key_resp_25.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_25.corr = 1  # correct non-response
       else: key_resp_25.corr = 0  # failed to respond (incorrectly)
    # store data for twoAFC_2 (TrialHandler)
    twoAFC_2.addData('key_resp_25.keys',key_resp_25.keys)
    twoAFC_2.addData('key_resp_25.corr', key_resp_25.corr)
    if key_resp_25.keys != None:  # we had a response
        twoAFC_2.addData('key_resp_25.rt', key_resp_25.rt)
    # the Routine "question_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "five_s_gap_2"-------
    t = 0
    five_s_gap_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    five_s_gap_2Components = []
    five_s_gap_2Components.append(text_39)
    for thisComponent in five_s_gap_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "five_s_gap_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = five_s_gap_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_39* updates
        if t >= 0.0 and text_39.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_39.tStart = t  # underestimates by a little under one frame
            text_39.frameNStart = frameN  # exact frame index
            text_39.setAutoDraw(True)
        if text_39.status == STARTED and t >= (0.0 + (2.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_39.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in five_s_gap_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "five_s_gap_2"-------
    for thisComponent in five_s_gap_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'twoAFC_2'


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
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
