import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('csvfile1.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y, marker='o')

plt.title('Data from the CSV File: Cities and Covid')

plt.xlabel('Date')
plt.ylabel('Expenses')

plt.show()
