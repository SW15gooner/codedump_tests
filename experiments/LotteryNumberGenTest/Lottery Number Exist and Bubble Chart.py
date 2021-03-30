# Lottery number generator
# 6 non-repeating numbers, saved to two text files. One with Generated numbers and the other with the number of occurences
# Plus Bubble Graph showing prevelance of each number
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import seaborn as sns
#from pylab import *
#from scipy import *
import re, collections
import random
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")

# open file to do Occurance count, adding count number to first column, then number, then occurences

with open("Lottery-output.txt", 'r') as fh:
    r = 0
    # setting space as a common delimiter
    contents = re.sub(r':|\n', ' ', fh.read()).split()
    counts = collections.Counter(contents)

# Zero old Counts file for a new count, and add headers
open("Lottery-counts.txt", 'w').close()
a = open("Lottery-counts.txt", 'w')
print("Sequence,Numbers,Occurences", file=a)
a.close() # Close to fix headers and not get overwritten by next

# iterating through `number` counts
for a in counts:
    s = open("Lottery-counts.txt", "a")
    r = r+1
    print(r, ',', a, ',' ,counts[a], file=s)
    s.close() # Close to complete 58 lines

# Plot

sns.set(style="ticks")
# sns.set(style="whitegrid")
mov = pd.read_csv("Lottery-counts.txt")

x=mov.Sequence
#delete ol Numbers to make it spread 'up' with occurence as well as size of Bubble
#y=mov.Numbers
#Make them grow 'upwards' too with new Y
y=mov.Occurences
z=mov.Occurences

cm = plt.cm.get_cmap('coolwarm')
fig, ax = plt.subplots(figsize=(10,8))

sc = ax.scatter(x,y,s=z*3, c=z,cmap=cm, linewidth=0.2, alpha=0.5)
ax.grid()
fig.colorbar(sc)

ax.set_title('Frequency of automatically random generated Lottery Numbers', fontsize=18)
ax.set_xlabel('Number Selected (what number)', fontsize=14)
ax.set_ylabel('Occurences of Number (how often)', fontsize=14)

plt.show()