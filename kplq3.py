import pandas as pd
import operator
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np
f = pd.read_csv('~/Downloads/data.csv')
distmod = f['Column 9'].values
ra = f['Column 2'].values
dec = f['Column 3'].values
Predshift = f['Column 7'].values
Sredshift = f['Column 6'].values
color = f['Column 10'].values
id = f['Column 1'].values
dct={}
l=[]
for i in range(len(color)):
    dct[id[i]]=color[i]
i=0
for w in sorted(dct, key=dct.get, reverse=True):
    l.append([])
    l[i].append(w)
    l[i].append(dct[w])
    i+=1
#1st index is id 2nd is the color index
#dimness directly proportional to color index
print(l[0])
print(l[3])
print(l[6])
print(l[8])
print(l[11])

# for i,id in id:
#     t = []
# orderuniq = np.unique(order)
# for i in range(0,5):
#     print(id[order.index(orderuniq[i])])
