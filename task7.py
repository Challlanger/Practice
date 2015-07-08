import random
count=
hadsOfSix=0
for throw in range(0, count):
    diceF = random.randint(1,6)
    diceS = random.randint(1,6)
    if diceF == 6 or diceS == 6:
        hadsOfSix += 1
        