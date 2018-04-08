# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:10:26 2016

@author: ysa
"""

import random
import itertools
import pandas as pd

perm_list_1 = list(itertools.permutations(['1A.wav', '1B.wav', '1C.wav']))
perm_list_2 = list(itertools.permutations(['2A.wav', '2B.wav', '2C.wav']))
perm_list_3 = list(itertools.permutations(['3A.wav', '3B.wav', '3C.wav']))
perm_list_4 = list(itertools.permutations(['4A.wav', '4B.wav', '4C.wav']))

permutations = [perm_list_1, perm_list_2, perm_list_3, perm_list_4]

sequences = [[permutations[0][0], permutations[1][0], permutations[2][0], permutations[3][0]],
             [permutations[0][3], permutations[1][3], permutations[2][3], permutations[3][3]],
             [permutations[0][4], permutations[1][4], permutations[2][4], permutations[3][4]]]


print '''

+++++++++++Generating sequence of triples for block 1++++++++++++


'''
def block_1_generator():
    block_list = []
    triplets = []
    for j in sequences:
        for i in range(4):
            triplets.append(' '.join(j[i]))
    seq = [triplets[0], triplets[1], triplets[2], triplets[3]]       
    while len(block_list) != 96:
        block_list.extend(random.sample(seq, 4))
    for x in range(1, len(block_list)):
        while 1:
            if block_list[x] == block_list[x-1]:
                y = block_list.pop(x)
                if y == block_list[-1] and y != block_list[0]:
                    block_list.insert(0,y)
                elif y == block_list[-1] and y == block_list[0]:
                    block_list.insert(-3,y)
                else:    
                    block_list.append(y)
            else:
                break
    sequence_counts = {seq[0]:0, seq[1]:0, seq[2]:0, seq[3]:0}
    for i in block_list:
        for k,v in sequence_counts.items():
            if k == i:
                v += 1
                sequence_counts[k] = v  
                
    print block_list   
        
    print '''
    
    counts for each sequence: 
    ''', sequence_counts
    

#block_1_generator()

### append each image 24 times
### shuffle the big list
### randomly generate groups of 3

print '''

+++++++++++Generating sequence of triples for block 2++++++++++++

'''

def block_2_generator():
    
    aliens = ['1A.wav', '1B.wav', '1C.wav',
              '2A.wav', '2B.wav', '2C.wav',
              '3A.wav', '3B.wav', '3C.wav',
              '4A.wav', '4B.wav', '4C.wav']
        
    block_2_images = [i for x in range(24*2) for i in aliens]
    random.shuffle(block_2_images)
    triplets = []
    a = 1
    while a == 1:
        x = 0
        for i in range(96*2):
            triplets.append(' '.join(block_2_images[x:x+3]))
            x += 3
        occurances_of_triplets = []
        for x in triplets:
            occurances_of_triplets.append(triplets.count(x))
        for i in range(3,5):
            if i not in occurances_of_triplets:
                a = 2
    print '\n', 'The number of times a particular triplet appears in the random sequence: ', occurances_of_triplets     
    return triplets


second_random_block = block_2_generator()

second_rand_col = []
for i in range(len(second_random_block)):
    triplet = second_random_block[i]
    split_trip = triplet.split(" ")
    second_rand_col.extend(split_trip)

d = pd.read_csv('R_fam_seq_1.csv')
rand_col = d.soundFile

soundFile1 = []
soundFile2 = []
soundFile3 = []
soundFile4 = []
soundFile5 = []
soundFile6 = []
corrAns = []
x = -1
y = -1
for j in range(16):
    x += 1
    soundFile1.append(rand_col[x])
    x += 1
    soundFile2.append(rand_col[x])
    x += 1
    soundFile3.append(rand_col[x])
    y += 1
    soundFile4.append(second_rand_col[y])
    y += 1
    soundFile5.append(second_rand_col[y])
    y += 1
    soundFile6.append(second_rand_col[y])
    corrAns.append('left')

for k in range(16):
    y += 1
    soundFile1.append(second_rand_col[y])
    y += 1
    soundFile2.append(second_rand_col[y])
    y += 1
    soundFile3.append(second_rand_col[y])
    x += 1
    soundFile4.append(rand_col[x])
    x += 1
    soundFile5.append(rand_col[x])
    x += 1
    soundFile6.append(rand_col[x])
    corrAns.append('right')

cols = {"soundFile1": soundFile1, "soundFile2": soundFile2, "soundFile3": soundFile3, \
        "soundFile4": soundFile4, "soundFile5": soundFile5, "soundFile6": soundFile6, \
        "corrAns": corrAns}

new_rand_test = pd.DataFrame(cols, columns = ['soundFile1', 'soundFile2', 'soundFile3', 'soundFile4', 'soundFile5', 'soundFile6', 'corrAns'])
new_rand_test.to_csv('R_forced_test_1.csv')





