import pandas as pd
import numpy as np

import networkx as nx

import matplotlib.pyplot as plt

import sys
import warnings
warnings.filterwarnings('ignore')

print('Python Version : '+sys.version)
print('NetworkX version : '+nx.__version__)

#below

df = pd.read_csv('https://github.com/sunny2309/datasets/moreno_innovation/out.moreno_innovation_innovation', sep=' ', skiprows=2, header=None)
df.columns = ['doctor1', 'doctor2']
df.head()

undirected_G = nx.Graph()

for idx in df.index:
    undirected_G.add_edge(df.loc[idx]['doctor1'], df.loc[idx]['doctor2'])

list(undirected_G.nodes(data=True))[:5]
