# Lottery number generator
# 6 non-repeating numbers saved to a Text file

import random
list=[]
f = open("experiments/Lottery-output.txt", "a")
for i in range(6):
    randList = random.sample(range(1,59),k=6)
    if randList not in list: list.append(randList)
print("{} {} {} {} {} {}".format(*randList), file=f)
f.close()