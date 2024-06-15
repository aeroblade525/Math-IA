import random
import numpy as np

# weighting of the substats
CR = 3
CD = 3
EM = 4
ER = 4
pATK = 4
pDEF = 4
pHP = 4
bATK = 6
bDEF = 6
bHP = 6
sample = 0
numberOfCRnCD = 0
numberOfCR = 0
numberOfCD = 0
numberOfCRoCD = 0
substats = [CR, CD, EM, ER, pATK, bATK, bDEF, bHP, pDEF, pHP]
# total weighting of all the substats
totalweight = [sum(substats)]
# wieghting of the substats in percentage
weighting = [3/totalweight[0], 3/totalweight[0], 4/totalweight[0], 4/totalweight[0], 4/totalweight[0], 6/totalweight[0], 6/totalweight[0], 6/totalweight[0], 4/totalweight[0], 4/totalweight[0]]
artifactSubStats = ["CR", "CD", "ER", "EM", "ATKpercentage", "baseHP", "baseDEF", "baseATK", "DEFpercentage", "HPpercentage"]
# asking which artifact they are using
artifactChoice = input("What artifact piece are you using")

# if the artifact is a plume or flower we remove the substats that it affects changing the weighting
if artifactChoice == "plume" or artifactChoice == "flower":
    artifactSubStats.pop(5)
    substats.pop(5)
    x = sum(substats)
    totalweight[0] = int(x)
    weighting = weighting = [3/totalweight[0], 3/totalweight[0], 4/totalweight[0], 4/totalweight[0], 4/totalweight[0], 6/totalweight[0], 6/totalweight[0], 6/totalweight[0], 4/totalweight[0], 4/totalweight[0]]
    weighting.pop(5)

# if the artifact is a cirlet goblet or sands we remove the substats that it affects chanigng the weighting
if artifactChoice == "cirlet" or artifactChoice == "goblet" or artifactChoice == "sands":
    mainstat = input("What mainstat is it?")
    removeWeight = artifactSubStats.index(mainstat)
    artifactSubStats.remove(mainstat)
    substats.pop(removeWeight)
    x = sum(substats)
    totalweight[0] = int(x)
    weighting = weighting = [3/totalweight[0], 3/totalweight[0], 4/totalweight[0], 4/totalweight[0], 4/totalweight[0], 6/totalweight[0], 6/totalweight[0], 6/totalweight[0], 4/totalweight[0], 4/totalweight[0]]
    weighting.pop(removeWeight)

# sampling 10 million artifacts and using large number theorum
while sample < 10000:
    sample_list = np.random.choice(artifactSubStats,size=4,replace=False, p=weighting)
    print(sample_list)
    sample += 1
    if "CR" in sample_list and "CD" in sample_list:
            numberOfCRnCD += 1
    if "CR" in sample_list:
        numberOfCR += 1
    if "CD" in sample_list:
        numberOfCD += 1
    if "CR" in sample_list or "CD" in sample_list:
        numberOfCRoCD += 1

# print the results of the samlping
print(numberOfCRnCD)
print(numberOfCR)
print(numberOfCD)
print(numberOfCRoCD)
print(numberOfCRnCD/sample)
print(numberOfCD/sample)
print(numberOfCR/sample)
print(numberOfCRoCD/sample)
