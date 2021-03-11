#import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
fig, ax = plt.subplots(figsize=(12,10))

sc = ax.scatter(x,y,s=z*3, c=z,cmap=cm, linewidth=0.2, alpha=0.5)
#test
for x, y in enumerate(mov.Numbers):
    plt.text(x = y,
    y = y-150,
    s = '{:.0f}'.format(y),
    color = 'purple')
#test end
ax.grid()
fig.colorbar(sc)

ax.set_xlabel('Number Selected (what number)', fontsize=14)
ax.set_ylabel('Occurences of Number (how often)', fontsize=14)

plt.show()
