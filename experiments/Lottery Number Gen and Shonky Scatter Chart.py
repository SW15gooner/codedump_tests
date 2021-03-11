# Lottery number generator
# 6 non-repeating numbers
# and a shoddy looking Scatter graph
import csv
import matplotlib.pyplot as plt
import random
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
x = []
y = []
for o in range(10):
    list=[]
    f = open("experiments/Lottery-output.txt", "a")
    for i in range(6):
        randList = random.sample(range(1,59),k=6)
        if randList not in list: list.append(randList)
    print("{} {} {} {} {} {}".format(*randList), file=f)
    f.close()

    with open('experiments/Lottery-output.txt', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))


plt.plot(x,y, marker='o')

plt.title('Occurances of numbers')

plt.xlabel('1-59')
plt.ylabel('1-59')

plt.show()