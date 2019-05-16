def chk(ra,dec):
    observing_location = EarthLocation(lat='31.7754', lon='76.9861', height=1044*u.m)

    observing_time = Time('2019-05-15 21:00:00')
    aa = AltAz(location=observing_location, obstime=observing_time)
    coord = SkyCoord(ra,dec)
    z=coord.transform_to(aa)
    return z






from astropy import units as u
import pandas as pd
from astropy.coordinates import EarthLocation,SkyCoord
from astropy.time import Time
from astropy.coordinates import AltAz

def chk(ra,dec):
    observing_location = EarthLocation(lat='31.7754', lon='76.9861', height=1044*u.m)

    observing_time = Time('2019-05-15 21:00:00')
    aa = AltAz(location=observing_location, obstime=observing_time)
    coord = SkyCoord(ra,dec)
    z=coord.transform_to(aa)
    dist=z.alt
    ang=float(dist.to_string(unit=u.degree, decimal=True))
    return ang>0

neo={}
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
    if (chk(d['Column 2']*u.hour,d['Column 3']*u.degree)==True):
        rd[sid]=ang
nr=[]
print(neo)
cnt=0
for w in sorted(rd, key=rd.get):
    nr.append(int(w))
    cnt+=1
near5=nr[1:6]
print(near5)
