import random

blockList = ['1','2','3','4','5','6']
random.shuffle(blockList)
print(blockList)

for fileName in blockList:
    if int(fileName)%2==0:
        print('a_%s'%(str(fileName)))
    elif int(fileName)%2!=0:
        print(fileName)
    