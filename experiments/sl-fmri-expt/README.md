# BLAST
## Brain and Language Acquisition Study

### This file overviews the task design and evolution of the BLAST project.

#### Versions info

<b>four_task_fmri</b>:	this experiment has 4 tasks: VSL, SSL, TSL, and LSL. Each task is located in their corresponding folder. VSL and LSL takes about half an hour each while SSL and TSL takes about 20 minutes each. Each task include structured blocks and random blocks of the same type of stimuli.<br/>
<b>dec2017_fmri</b>:	this experiment has 2 tasks: auditory and visual. Auditory is the combination of SSL and TSL, visual is the combination of TSL and SSL. There are 6 runs in each task.<br/>
<b>jan2018_fmri</b>:	this experiment has 2 tasks: auditory and visual. There are 6 runs in each task. However, each mini-block of structured and random is made longer now. So the total number of mini blocks is reduced and the length of each mini block increased.<br/>
<b>shortened_fmri -> scanner stim	</b>:	this experiment has 2 tasks: auditory and visual. There are 4 runs in each task. The exposure phase for visual has been reduced by half. The number of questions in the 2AFC is also reduced by half (16 questions).<br/>
<b>shortened_fmri -> scanner_stim_without_test	</b>:	this experiment has 2 tasks: auditory and visual. There are 4 runs in each task. The exposure phase for visual has been reduced by half. There is no test phase in this experiment.<br/>
<b>shortened_fmri -> test_session	</b>:	This includes the 2AFC tasks for the 4 experiments, in random order. Each task has 32 questions.<br/>
<b>visual_inter</b>:  a separate project that looks into whether learning performance decrease when the intervening random sequences contain the same type of stimuli (e.g. both visual-nonlinguistic) compared to the cases when the intervening random sequences contain a different type of stimuli from the structured sequence (e.g. the random is visual-linguistic and the structured is visual/nonlinguistic). This experiment has 4 tasks: letter-letter, letter-alien, alien-alien, alien-letter. Each task is followed by 32 2AFC questions.

#### How to run the experiment:

Download the whole folder of the task that needs to be run. Open the .py file with PsychoPy and enter the parameters as instructed in the .py file.

## Task Design
The general overall task design of BLAST is an investigation into the interaction between Modality and Domain.

		                  Domain
                      Linguistic    Non-Linguistic
    Modality Auditory Speech (SSL)	Tone (TSL)
             Visual   Letter (LSL)	Image (VSL)

Within each condition (SSL, LSL, TSL, VSL), stimuli were presented in both a "structured" manner (contains statistical regularities) and presented at random (no statistical regularities) in different blocks. The structured condition contained "triplets":

  - The structured mini-blocks were composed of stimuli of the same type, the presentation order of which followed an embedded pattern of four unique triplets, so that the transitional probability within a triplet was 1 and between triplets was 0.25.

  - Each structured mini-block contained four (VSL) or eight (ASL) repetitions of each of the four triplets.

  - In contrast with the structured blocks, the random blocks contained 12 unique images/sounds different from the structured blocks, ordered pseudo-randomly, so that there were no combinations of three stimulus that were repeated more than once.

  - The transitional probability between stimuli in the random blocks was 0.083.

### Stimuli
#### Visual Statisical Learning (VSL)
Twelve standalone alien cartoon images (Image) and twelve letter images (Letter) showing the same alien holding up twelve signs with capital letters written on them were constructed by a professional illustrator. No letter triplet contained any words, common acronyms, or initialisms.

#### Auditory Statistical Learning (ASL)
The auditory stimuli were constructed of twelve English syllables (pi,pu,pa,ti,tu.ta,di,du,da,bi,bu,ba) and twelve musical tones (F,G,D,G#,C#,B,C,F#,D#,E,A,A#).

### Design
- Images were ordered in four 4.77-minute (VSL)/4.42-minute (ASL) streams, with each stream comprised of 3 structured and 3 random mini-blocks randomly ordered (randomization described below), and a resting block between two subsequent mini-blocks (total of 6 blank/silent blocks).
- Visual stimuli SOA = 1000 msec
- Auditory stimuli SOA = 480 msec
- 96 triplets were presented per run in ASL and 48 triplets per run for VSL
- A total of 144 structured, 144 random, and 30 blank items were presented in one run of VSL / 288 structured, 288 random, and 72 blank items were presented in one run of ASL.

### Procedure
- Participants watched/listened to the two continuous streams of stimuli described above, while performing a target detection task.
- While viewing/listening the stream of stimuli, participants tracked a target stimulus, and were instructed to press a response button when they saw/heard the target.  
- Within each task, the participant tracked one linguistic target and one non-linguistic target. The targets are also the third stimulus in one of the triplets of the corresponding domain. Targets (4 options for each of VSL, LSL, and SSL. but 2 options for TSL (see note)) are randomly assigned to each individual participants.
- At the beginning of each mini-block, the participant was reminded of the target.
- Response time was recorded.

#### Pseudo-randomization
- The order of tasks (ASL versus VSL) was pseudo-randomized across participants and can be found on the participant checklist
- Within each task, there are four runs. Within each run are 3 random and 3 structured mini-blocks, along with resting mini-blocks. These are randomized within and across blocks. The order of randomization is determined by Psychopy selecting 1 of 6 possible orders for each block (e.g. for VSL run 1: visual_run1_1 versus visual_run1_4). These orders are stored in the experiment folder:

**AUDITORY**:/data/projects/blast/experiment/fmri_task/psychopy_files/shortened_fmri/scanner_stim_without_test_adult_ver/auditory/auditory_runN_N.xlsx>
**VISUAL**:/data/projects/blast/experiment/fmri_task/psychopy_files/shortened_fmri/scanner_stim_without_test_adult_ver/visual/visual_runN_N.xlsx

- In Runs 1 & 2, Tone & Letter conditions were always random while Speech & Image were always structured
- In Runs 3 & 4, Tone & Letter conditions were always structured while Speech & Image were always random
