# Euromillions number generator
# 5 + 2 non-repeating numbers

import random
list=[]
f = open("experiments/Euromill-output.txt", "a")
for i in range(7):
    randList = random.sample(range(1,50),k=5) + ["+", random.choice(range(12))+1] + ["&", random.choice(range(12))+1]
    if randList not in list: list.append(randList)
print("Numbers {} {} {} {} {} {} {} {} {}".format(*randList), file=f)

f.close()