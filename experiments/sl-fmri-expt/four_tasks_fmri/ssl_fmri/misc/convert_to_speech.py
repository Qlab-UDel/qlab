import pandas as pd
d = pd.read_csv('asl_R_fam_seq_1.csv')

sound_to_speech_dict = {"1A.wav": "di.wav", "1B.wav": "ba.wav", "1C.wav": "pu.wav",\
                        "2A.wav": "bu.wav", "2B.wav": "pa.wav", "2C.wav": "da.wav",\
                        "3A.wav": "pi.wav", "3B.wav": "tu.wav", "3C.wav": "bi.wav",\
                        "4A.wav": "ta.wav", "4B.wav": "ti.wav", "4C.wav": "du.wav"}

new_sound_to_speech_dict = {"3B.wav": "pa.wav", "1C.wav": "bi.wav", "4A.wav": "ku.wav",\
                            "4B.wav": "go.wav", "2C.wav": "la.wav", "3A.wav": "tu.wav",\
                            "2B.wav": "da.wav", "4C.wav": "ro.wav", "1A.wav": "pi.wav",\
                            "1B.wav": "ti.wav", "3C.wav": "bu.wav", "2A.wav": "do.wav"}

vsl_to_speech_1 = {"Alien1.BMP": "di.wav", "Alien2.BMP": "ba.wav", "Alien3.BMP": "pu.wav",\
                   "Alien4.BMP": "bu.wav", "Alien5.BMP": "pa.wav", "Alien6.BMP": "da.wav",\
                   "Alien7.BMP": "pi.wav", "Alien8.BMP": "tu.wav", "Alien9.BMP": "bi.wav",\
                   "Alien10.BMP": "ta.wav", "Alien11.BMP": "ti.wav", "Alien12.BMP": "du.wav",\
                   1: "left", 2: "right"}

vsl_to_speech_2 = {"Alien1.BMP": "pa.wav", "Alien2.BMP": "bi.wav", "Alien3.BMP": "ku.wav",\
                   "Alien4.BMP": "go.wav", "Alien5.BMP": "la.wav", "Alien6.BMP": "tu.wav",\
                   "Alien7.BMP": "da.wav", "Alien8.BMP": "ro.wav", "Alien9.BMP": "pi.wav",\
                   "Alien10.BMP": "ti.wav", "Alien11.BMP": "bu.wav", "Alien12.BMP": "do.wav",\
                   1: "left", 2: "right"}

##sound_list = d.soundFile
##
##new_sound_list = []
##for i in sound_list:
##    new_sound_list.append(sound_to_speech_dict[i])
##
##cols = {"soundFile": new_sound_list}
##
##new_d = pd.DataFrame(cols, columns = ['soundFile'])
##
##new_d.to_csv('speech_soundFileList1.csv')


sound_list = d.soundFile

new_sound_list = []
for i in sound_list:
    new_sound_list.append(new_sound_to_speech_dict[i])

cols = {"soundFile": new_sound_list}

new_d = pd.DataFrame(cols, columns = ['soundFile'])

new_d.to_csv('R_fam_seq_2.csv')




##soundFile1 = d.soundFile1
##soundFile2 = d.soundFile2
##soundFile3 = d.soundFile3
##soundFile4 = d.soundFile4
##soundFile5 = d.soundFile5
##soundFile6 = d.soundFile6
##corrAns = d.corrAns
##
##sound1 = []
##for i in soundFile1:
##    sound1.append(new_sound_to_speech_dict[i])
##
##sound2 = []
##for i in soundFile2:
##    sound2.append(new_sound_to_speech_dict[i])
##
##sound3 = []
##for i in soundFile3:
##    sound3.append(new_sound_to_speech_dict[i])
##
##sound4 = []
##for i in soundFile4:
##    sound4.append(new_sound_to_speech_dict[i])
##
##sound5 = []
##for i in soundFile5:
##    sound5.append(new_sound_to_speech_dict[i])
##
##sound6 = []
##for i in soundFile6:
##    sound6.append(new_sound_to_speech_dict[i])
##
##cols = {"soundFile1": sound1, "soundFile2": sound2, "soundFile3": sound3, \
##        "soundFile4": sound4, "soundFile5": sound5, "soundFile6": sound6, \
##        "corrAns": corrAns}
##
##new_d = pd.DataFrame(cols, columns = ['soundFile1', 'soundFile2', 'soundFile3', 'soundFile4', 'soundFile5', 'soundFile6', 'corrAns'])
##
##new_d.to_csv('speech_forced_test_1.csv')

##sound_list = d.soundFile
##
##new_sound_list = []
##for i in sound_list:
##    new_sound_list.append(new_sound_to_speech_dict[i])
##
##cols = {"soundFile": new_sound_list}
##
##new_d = pd.DataFrame(cols, columns = ['soundFile'])
##
##new_d.to_csv('speech_soundFileList2.csv')


##image1 = d.image1
##image2 = d.image2
##image3 = d.image3
##image4 = d.image4
##image5 = d.image5
##image6 = d.image6
##corrAns = d.corrAns
##
##sound1 = []
##for i in image1:
##    sound1.append(vsl_to_speech_2[i])
##
##sound2 = []
##for i in image2:
##    sound2.append(vsl_to_speech_2[i])
##
##sound3 = []
##for i in image3:
##    sound3.append(vsl_to_speech_2[i])
##
##sound4 = []
##for i in image4:
##    sound4.append(vsl_to_speech_2[i])
##
##sound5 = []
##for i in image5:
##    sound5.append(vsl_to_speech_2[i])
##
##sound6 = []
##for i in image6:
##    sound6.append(vsl_to_speech_2[i])
##
##new_corr = []
##for i in corrAns:
##    new_corr.append(vsl_to_speech_2[i])
##
##cols = {"soundFile1": sound1, "soundFile2": sound2, "soundFile3": sound3, \
##        "soundFile4": sound4, "soundFile5": sound5, "soundFile6": sound6, \
##        "corrAns": new_corr}
##
##new_d = pd.DataFrame(cols, columns = ['soundFile1', 'soundFile2', 'soundFile3', 'soundFile4', 'soundFile5', 'soundFile6', 'corrAns'])
##
##new_d.to_csv('R_forced_test_2.csv')
