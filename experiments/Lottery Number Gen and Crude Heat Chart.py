# Lottery number generator
# 6 non-repeating numbers and crude Heat Chart
import pandas as pd
import seaborn as sb
import matplotlib.pylab as mp
import random
for o in range(10):
    list=[]
    f = open("Lottery-output.txt", "a")
    for i in range(6):
        randList = random.sample(range(1,59),k=6)
        if randList not in list: list.append(randList)
    print("{} {} {} {} {} {}".format(*randList), file=f)
    f.close()
# Open file again for Heatmap
data_set = pd.read_csv("Lottery-output.txt", sep=" ")
#dataplot = sb.heatmap(data_set.corr(), cmap="YlGnBu", annot=True)
corr = data_set.corr()
ax = sb.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sb.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);

mp.title( "2-D Heat Map" ) 
mp.show() 