import pandas as pd
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
f = pd.read_csv('~/Downloads/data.csv')
distmod = f['Column 9'].values
ra = f['Column 2'].values
dec = f['Column 3'].values
Predshift = f['Column 7'].values
Sredshift = f['Column 6'].values
id = f['Column 1'].values
ratio = []
reqmod = []
insideGal = []
for i,id in enumerate(id):
    if(Predshift[i]!=0):
        ratio.append(1+Predshift[i])
        reqmod.append(distmod[i])
    else:
        insideGal.append(id)
print("Objects inside galaxy:")
print(insideGal)
print("Plot saved as 'plot.png'")
plt.scatter(reqmod,ratio)
plt.savefig("plot.png")
