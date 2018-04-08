

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
expName = 'test_session'  # from the Builder filename that created this script
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

#TSL TEST
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

#SSL TEST
# Initialize components for Routine "instr10"
instr10Clock = core.Clock()
instr10_text = visual.TextStim(win=win, ori=0, name='instr10_text',
    text=u"Each of these aliens will say a short phrase. Please try your best to identify which phrase sounds more like Meeple's language. If you don't know the answer, just give your best guess!\n\nPress the green button if the first alien's phrase sounds more like Meeple's language, and press the red button if the second alien's phrase sounds more like Meeple's language.",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr10_sound = sound.Sound(u'ssl_instr10.wav', secs=-1)
instr10_sound.setVolume(1)


# Initialize components for Routine "ssl1"
ssl1Clock = core.Clock()
ssl1_image = visual.ImageStim(win=win, name='ssl1_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ssl1_sound = sound.Sound('A', secs=-1)
ssl1_sound.setVolume(1)
ssl1_text = visual.TextStim(win=win, ori=0, name='ssl1_text',
    text=u"Which phrase is like Meeple's?\nPress the green button for first and red button for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "ssl2"
ssl2Clock = core.Clock()
ssl2_image = visual.ImageStim(win=win, name='ssl2_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ssl2_sound = sound.Sound('A', secs=-1)
ssl2_sound.setVolume(1)
ssl2_text = visual.TextStim(win=win, ori=0, name='ssl2_text',
    text=u"Which phrase is like Meeple's?\nPress the green button for first and red button for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "ssl3"
ssl3Clock = core.Clock()
ssl3_image = visual.ImageStim(win=win, name='ssl3_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ssl3_sound = sound.Sound('A', secs=-1)
ssl3_sound.setVolume(1)
ssl3_text = visual.TextStim(win=win, ori=0, name='ssl3_text',
    text=u"Which phrase is like Meeple's?\nPress the green button for first and red button for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "ssl_triplet_pause"
ssl_triplet_pauseClock = core.Clock()
ssl_triplet_pause_image = visual.ImageStim(win=win, name='ssl_triplet_pause_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ssl_triplet_pause_text = visual.TextStim(win=win, ori=0, name='ssl_triplet_pause_text',
    text=u"Which phrase is like Meeple's?\nPress the green button for first and red button for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ssl4"
ssl4Clock = core.Clock()
ssl4_image = visual.ImageStim(win=win, name='ssl4_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ssl4_sound = sound.Sound('A', secs=-1)
ssl4_sound.setVolume(1)
ssl4_text = visual.TextStim(win=win, ori=0, name='ssl4_text',
    text=u"Which phrase is like Meeple's?\nPress the green button for first and red button for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "ssl5"
ssl5Clock = core.Clock()
ssl5_image = visual.ImageStim(win=win, name='ssl5_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ssl5_sound = sound.Sound('A', secs=-1)
ssl5_sound.setVolume(1)
ssl5_text = visual.TextStim(win=win, ori=0, name='ssl5_text',
    text=u"Which phrase is like Meeple's?\nPress the green button for first and red button for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "ssl6"
ssl6Clock = core.Clock()
ssl6_image = visual.ImageStim(win=win, name='ssl6_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ssl6_sound = sound.Sound('A', secs=-1)
ssl6_sound.setVolume(1)
ssl6_text = visual.TextStim(win=win, ori=0, name='ssl6_text',
    text=u"Which phrase is like Meeple's?\nPress the green button for first and red button for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "ssl_question"
ssl_questionClock = core.Clock()
ssl_question_image = visual.ImageStim(win=win, name='ssl_question_image',
    image=u'2AFCAliens.png', mask=None,
    ori=0, pos=[0, -.1], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ssl_question_text = visual.TextStim(win=win, ori=0, name='ssl_question_text',
    text=u"Which phrase is like Meeple's?\nPress the green button for first and red button for second.",    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "ssl_gap"
ssl_gapClock = core.Clock()
ssl_gap_text = visual.TextStim(win=win, ori=0, name='ssl_gap_text',
    text=u'Please wait...',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0)


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
    
    
#VSL test

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

testList = ['v','l','s','t']
random.shuffle(testList)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

for fileName in testList:
    if (fileName == 'v'):
        
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
            trialList=data.importConditions(u'vsl_forced_test.xlsx'),
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
            
    if (fileName == 'l'):
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
            trialList=data.importConditions(u'lsl_forced_test.xlsx'),
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
        
    if (fileName == 's'):
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
                theseKeys = event.getKeys(keyList=['num_add', '+', 'num_5', '5'])
                
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
        
        
        
        # set up handler to look after randomisation of conditions etc
        ssl_block = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'ssl_forced_test.xlsx' ),
            seed=None, name='ssl_block')
        thisExp.addLoop(ssl_block)  # add the loop to the experiment
        thisTest_trial = ssl_block.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTest_trial.rgb)
        if thisTest_trial != None:
            for paramName in thisTest_trial.keys():
                exec(paramName + '= thisTest_trial.' + paramName)
        
        for thisTest_trial in ssl_block:
            currentLoop = ssl_block
            # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
            if thisTest_trial != None:
                for paramName in thisTest_trial.keys():
                    exec(paramName + '= thisTest_trial.' + paramName)
            
            #------Prepare to start Routine "ssl1"-------
            t = 0
            ssl1Clock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.480000)
            # update component parameters for each repeat
            ssl1_sound.setSound(ssl1, secs=0.46)
            # keep track of which components have finished
            ssl1Components = []
            ssl1Components.append(ssl1_image)
            ssl1Components.append(ssl1_sound)
            ssl1Components.append(ssl1_text)
            for thisComponent in ssl1Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl1"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ssl1Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl1_image* updates
                if t >= 0.0 and ssl1_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl1_image.tStart = t  # underestimates by a little under one frame
                    ssl1_image.frameNStart = frameN  # exact frame index
                    ssl1_image.setAutoDraw(True)
                if ssl1_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl1_image.setAutoDraw(False)
                # start/stop ssl1_sound
                if t >= 0.0 and ssl1_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl1_sound.tStart = t  # underestimates by a little under one frame
                    ssl1_sound.frameNStart = frameN  # exact frame index
                    ssl1_sound.play()  # start the sound (it finishes automatically)
                if ssl1_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl1_sound.stop()  # stop the sound (if longer than duration)
                
                # *ssl1_text* updates
                if t >= 0.0 and ssl1_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl1_text.tStart = t  # underestimates by a little under one frame
                    ssl1_text.frameNStart = frameN  # exact frame index
                    ssl1_text.setAutoDraw(True)
                if ssl1_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl1_text.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl1"-------
            for thisComponent in ssl1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ssl1_sound.stop() #ensure sound has stopped at end of routine
            
            #------Prepare to start Routine "ssl2"-------
            t = 0
            ssl2Clock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.480000)
            # update component parameters for each repeat
            ssl2_sound.setSound(ssl2, secs=0.46)
            # keep track of which components have finished
            ssl2Components = []
            ssl2Components.append(ssl2_image)
            ssl2Components.append(ssl2_sound)
            ssl2Components.append(ssl2_text)
            for thisComponent in ssl2Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl2"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ssl2Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl2_image* updates
                if t >= 0.0 and ssl2_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl2_image.tStart = t  # underestimates by a little under one frame
                    ssl2_image.frameNStart = frameN  # exact frame index
                    ssl2_image.setAutoDraw(True)
                if ssl2_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl2_image.setAutoDraw(False)
                # start/stop ssl2_sound
                if t >= 0.0 and ssl2_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl2_sound.tStart = t  # underestimates by a little under one frame
                    ssl2_sound.frameNStart = frameN  # exact frame index
                    ssl2_sound.play()  # start the sound (it finishes automatically)
                if ssl2_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl2_sound.stop()  # stop the sound (if longer than duration)
                
                # *ssl2_text* updates
                if t >= 0.0 and ssl2_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl2_text.tStart = t  # underestimates by a little under one frame
                    ssl2_text.frameNStart = frameN  # exact frame index
                    ssl2_text.setAutoDraw(True)
                if ssl2_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl2_text.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl2"-------
            for thisComponent in ssl2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ssl2_sound.stop() #ensure sound has stopped at end of routine
            
            #------Prepare to start Routine "ssl3"-------
            t = 0
            ssl3Clock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.480000)
            # update component parameters for each repeat
            ssl3_sound.setSound(ssl3, secs=0.46)
            # keep track of which components have finished
            ssl3Components = []
            ssl3Components.append(ssl3_image)
            ssl3Components.append(ssl3_sound)
            ssl3Components.append(ssl3_text)
            for thisComponent in ssl3Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl3"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ssl3Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl3_image* updates
                if t >= 0.0 and ssl3_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl3_image.tStart = t  # underestimates by a little under one frame
                    ssl3_image.frameNStart = frameN  # exact frame index
                    ssl3_image.setAutoDraw(True)
                if ssl3_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl3_image.setAutoDraw(False)
                # start/stop ssl3_sound
                if t >= 0.0 and ssl3_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl3_sound.tStart = t  # underestimates by a little under one frame
                    ssl3_sound.frameNStart = frameN  # exact frame index
                    ssl3_sound.play()  # start the sound (it finishes automatically)
                if ssl3_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl3_sound.stop()  # stop the sound (if longer than duration)
                
                # *ssl3_text* updates
                if t >= 0.0 and ssl3_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl3_text.tStart = t  # underestimates by a little under one frame
                    ssl3_text.frameNStart = frameN  # exact frame index
                    ssl3_text.setAutoDraw(True)
                if ssl3_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl3_text.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl3"-------
            for thisComponent in ssl3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ssl3_sound.stop() #ensure sound has stopped at end of routine
            
            #------Prepare to start Routine "ssl_triplet_pause"-------
            t = 0
            ssl_triplet_pauseClock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.750000)
            # update component parameters for each repeat
            # keep track of which components have finished
            ssl_triplet_pauseComponents = []
            ssl_triplet_pauseComponents.append(ssl_triplet_pause_image)
            ssl_triplet_pauseComponents.append(ssl_triplet_pause_text)
            for thisComponent in ssl_triplet_pauseComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl_triplet_pause"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ssl_triplet_pauseClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl_triplet_pause_image* updates
                if t >= 0.0 and ssl_triplet_pause_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl_triplet_pause_image.tStart = t  # underestimates by a little under one frame
                    ssl_triplet_pause_image.frameNStart = frameN  # exact frame index
                    ssl_triplet_pause_image.setAutoDraw(True)
                if ssl_triplet_pause_image.status == STARTED and t >= (0.0 + (0.75-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl_triplet_pause_image.setAutoDraw(False)
                
                # *ssl_triplet_pause_text* updates
                if t >= 0.0 and ssl_triplet_pause_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl_triplet_pause_text.tStart = t  # underestimates by a little under one frame
                    ssl_triplet_pause_text.frameNStart = frameN  # exact frame index
                    ssl_triplet_pause_text.setAutoDraw(True)
                if ssl_triplet_pause_text.status == STARTED and t >= (0.0 + (0.75-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl_triplet_pause_text.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl_triplet_pauseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl_triplet_pause"-------
            for thisComponent in ssl_triplet_pauseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            #------Prepare to start Routine "ssl4"-------
            t = 0
            ssl4Clock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.480000)
            # update component parameters for each repeat
            ssl4_sound.setSound(ssl4, secs=0.46)
            # keep track of which components have finished
            ssl4Components = []
            ssl4Components.append(ssl4_image)
            ssl4Components.append(ssl4_sound)
            ssl4Components.append(ssl4_text)
            for thisComponent in ssl4Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl4"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ssl4Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl4_image* updates
                if t >= 0.0 and ssl4_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl4_image.tStart = t  # underestimates by a little under one frame
                    ssl4_image.frameNStart = frameN  # exact frame index
                    ssl4_image.setAutoDraw(True)
                if ssl4_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl4_image.setAutoDraw(False)
                # start/stop ssl4_sound
                if t >= 0.0 and ssl4_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl4_sound.tStart = t  # underestimates by a little under one frame
                    ssl4_sound.frameNStart = frameN  # exact frame index
                    ssl4_sound.play()  # start the sound (it finishes automatically)
                if ssl4_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl4_sound.stop()  # stop the sound (if longer than duration)
                
                # *ssl4_text* updates
                if t >= 0.0 and ssl4_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl4_text.tStart = t  # underestimates by a little under one frame
                    ssl4_text.frameNStart = frameN  # exact frame index
                    ssl4_text.setAutoDraw(True)
                if ssl4_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl4_text.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl4"-------
            for thisComponent in ssl4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ssl4_sound.stop() #ensure sound has stopped at end of routine
            
            #------Prepare to start Routine "ssl5"-------
            t = 0
            ssl5Clock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.480000)
            # update component parameters for each repeat
            ssl5_sound.setSound(ssl5, secs=0.46)
            # keep track of which components have finished
            ssl5Components = []
            ssl5Components.append(ssl5_image)
            ssl5Components.append(ssl5_sound)
            ssl5Components.append(ssl5_text)
            for thisComponent in ssl5Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl5"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ssl5Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl5_image* updates
                if t >= 0.0 and ssl5_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl5_image.tStart = t  # underestimates by a little under one frame
                    ssl5_image.frameNStart = frameN  # exact frame index
                    ssl5_image.setAutoDraw(True)
                if ssl5_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl5_image.setAutoDraw(False)
                # start/stop ssl5_sound
                if t >= 0.0 and ssl5_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl5_sound.tStart = t  # underestimates by a little under one frame
                    ssl5_sound.frameNStart = frameN  # exact frame index
                    ssl5_sound.play()  # start the sound (it finishes automatically)
                if ssl5_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl5_sound.stop()  # stop the sound (if longer than duration)
                
                # *ssl5_text* updates
                if t >= 0.0 and ssl5_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl5_text.tStart = t  # underestimates by a little under one frame
                    ssl5_text.frameNStart = frameN  # exact frame index
                    ssl5_text.setAutoDraw(True)
                if ssl5_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl5_text.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl5Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl5"-------
            for thisComponent in ssl5Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ssl5_sound.stop() #ensure sound has stopped at end of routine
            
            #------Prepare to start Routine "ssl6"-------
            t = 0
            ssl6Clock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.480000)
            # update component parameters for each repeat
            ssl6_sound.setSound(ssl6, secs=0.46)
            # keep track of which components have finished
            ssl6Components = []
            ssl6Components.append(ssl6_image)
            ssl6Components.append(ssl6_sound)
            ssl6Components.append(ssl6_text)
            for thisComponent in ssl6Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl6"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ssl6Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl6_image* updates
                if t >= 0.0 and ssl6_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl6_image.tStart = t  # underestimates by a little under one frame
                    ssl6_image.frameNStart = frameN  # exact frame index
                    ssl6_image.setAutoDraw(True)
                if ssl6_image.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl6_image.setAutoDraw(False)
                # start/stop ssl6_sound
                if t >= 0.0 and ssl6_sound.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl6_sound.tStart = t  # underestimates by a little under one frame
                    ssl6_sound.frameNStart = frameN  # exact frame index
                    ssl6_sound.play()  # start the sound (it finishes automatically)
                if ssl6_sound.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl6_sound.stop()  # stop the sound (if longer than duration)
                
                # *ssl6_text* updates
                if t >= 0.0 and ssl6_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl6_text.tStart = t  # underestimates by a little under one frame
                    ssl6_text.frameNStart = frameN  # exact frame index
                    ssl6_text.setAutoDraw(True)
                if ssl6_text.status == STARTED and t >= (0.0 + (0.46-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl6_text.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl6Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl6"-------
            for thisComponent in ssl6Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ssl6_sound.stop() #ensure sound has stopped at end of routine
            
            #------Prepare to start Routine "ssl_question"-------
            t = 0
            ssl_questionClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            ssl_question_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            ssl_question_key_resp.status = NOT_STARTED
            # keep track of which components have finished
            ssl_questionComponents = []
            ssl_questionComponents.append(ssl_question_image)
            ssl_questionComponents.append(ssl_question_text)
            ssl_questionComponents.append(ssl_question_key_resp)
            for thisComponent in ssl_questionComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl_question"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = ssl_questionClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl_question_image* updates
                if t >= 0.0 and ssl_question_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl_question_image.tStart = t  # underestimates by a little under one frame
                    ssl_question_image.frameNStart = frameN  # exact frame index
                    ssl_question_image.setAutoDraw(True)
                
                # *ssl_question_text* updates
                if t >= 0.0 and ssl_question_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl_question_text.tStart = t  # underestimates by a little under one frame
                    ssl_question_text.frameNStart = frameN  # exact frame index
                    ssl_question_text.setAutoDraw(True)
                
                # *ssl_question_key_resp* updates
                if t >= 0.0 and ssl_question_key_resp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl_question_key_resp.tStart = t  # underestimates by a little under one frame
                    ssl_question_key_resp.frameNStart = frameN  # exact frame index
                    ssl_question_key_resp.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(ssl_question_key_resp.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if ssl_question_key_resp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['num_add', '+', 'num_1', '1','num_4','num_2','num_3','2','3','4'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        ssl_question_key_resp.keys = theseKeys[-1]  # just the last key pressed
                        ssl_question_key_resp.rt = ssl_question_key_resp.clock.getTime()
                        # was this 'correct'?
                        if (ssl_question_key_resp.keys == str(sslcorrAns)) or (ssl_question_key_resp.keys == sslcorrAns):
                            ssl_question_key_resp.corr = 1
                        else:
                            ssl_question_key_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl_questionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl_question"-------
            for thisComponent in ssl_questionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if ssl_question_key_resp.keys in ['', [], None]:  # No response was made
               ssl_question_key_resp.keys=None
               # was no response the correct answer?!
               if str(sslcorrAns).lower() == 'none': ssl_question_key_resp.corr = 1  # correct non-response
               else: ssl_question_key_resp.corr = 0  # failed to respond (incorrectly)
            # store data for ssl_block (TrialHandler)
            ssl_block.addData('ssl_question_key_resp.keys',ssl_question_key_resp.keys)
            ssl_block.addData('ssl_question_key_resp.corr', ssl_question_key_resp.corr)
            if ssl_question_key_resp.keys != None:  # we had a response
                ssl_block.addData('ssl_question_key_resp.rt', ssl_question_key_resp.rt)
            # the Routine "ssl_question" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            #------Prepare to start Routine "ssl_gap"-------
            t = 0
            ssl_gapClock.reset()  # clock 
            frameN = -1
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            ssl_gapComponents = []
            ssl_gapComponents.append(ssl_gap_text)
            for thisComponent in ssl_gapComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "ssl_gap"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ssl_gapClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssl_gap_text* updates
                if t >= 0.0 and ssl_gap_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ssl_gap_text.tStart = t  # underestimates by a little under one frame
                    ssl_gap_text.frameNStart = frameN  # exact frame index
                    ssl_gap_text.setAutoDraw(True)
                if ssl_gap_text.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ssl_gap_text.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssl_gapComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "ssl_gap"-------
            for thisComponent in ssl_gapComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'test_trials'
    if (fileName == 't'):
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
        tsl_block = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'tsl_forced_test.xlsx'),
            seed=None, name='tsl_block')
        thisExp.addLoop(tsl_block)  # add the loop to the experiment
        thisTwoAFC_1 = tsl_block.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTwoAFC_1.rgb)
        if thisTwoAFC_1 != None:
            for paramName in thisTwoAFC_1.keys():
                exec(paramName + '= thisTwoAFC_1.' + paramName)
        
        for thisTwoAFC_1 in tsl_block:
            currentLoop = tsl_block
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
            sound_1.setSound(tsl1, secs=.46)
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
            sound_7.setSound(tsl2, secs=0.46)
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
            sound_8.setSound(tsl3, secs=.46)
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
            sound_9.setSound(tsl4, secs=.46)
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
            sound_10.setSound(tsl5, secs=.46)
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
            sound_11.setSound(tsl6, secs=.46)
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
                        if (key_resp_6.keys == str(tslcorrAns)) or (key_resp_6.keys == tslcorrAns):
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
               if str(tslcorrAns).lower() == 'none': key_resp_6.corr = 1  # correct non-response
               else: key_resp_6.corr = 0  # failed to respond (incorrectly)
            # store data for twoAFC_1 (TrialHandler)
            tsl_block.addData('tsl.keys',key_resp_6.keys)
            tsl_block.addData('tsl.corr', key_resp_6.corr)
            if key_resp_6.keys != None:  # we had a response
                tsl_block.addData('tsl.rt', key_resp_6.rt)
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
        
        # completed 1 repeats of 'tsl_block'