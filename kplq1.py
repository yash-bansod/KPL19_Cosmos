from astropy.coordinates import SkyCoord
from astropy import units as u
import pandas as pd
df=pd.read_csv('data.csv')
rd={}
n=float(input("Star ID:- "))
for i,d in df.iterrows():
    if d['Column 1']==n:
        c=SkyCoord(d['Column 2']*u.degree,d['Column 3']*u.degree,frame='gcrs')
for i,d in df.iterrows():
    c1=SkyCoord(d['Column 2']*u.degree,d['Column 3']*u.degree,frame='gcrs')
    sid=(d['Column 1'])
    dist=c1.separation(c)
    ang=float(dist.to_string(unit=u.hour, decimal=True))
    rd[sid]=ang
nr=[]
cnt=0
print(type(rd[1]))
for w in sorted(rd, key=rd.get):
    nr.append(int(w))
    cnt+=1
near5=nr[1:6]
print("nearest stars ",near5)
