# Lottery number generator
# 6 non-repeating numbers
import matplotlib.pyplot as plt
import csv
import numpy as np
#import pandas as pd
import re, collections
import random
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
# Open tet file and generate 6 non-repeating numbers 10 times
for o in range(10):
    list=[]
    f = open("Lottery-output.txt", "a")
    for i in range(6):
        randList = random.sample(range(1,59),k=6)
        if randList not in list: list.append(randList)
    print("{} {} {} {} {} {}".format(*randList), file=f)
    f.close()
# Re-open file to do Occurance count, adding count number to first column, then number, then occurences

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

