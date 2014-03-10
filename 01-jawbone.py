import pandas as pd
import numpy
# import matplotlib as plt
# plt.use('TkAgg') 
# import pylab
# pylab.show()

from pylab import *

up2013  = '/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/2013.csv'
up2014  = '/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/2014.csv'
we2013  = '/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/weather2013.csv'
we2014  = '/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/weather2014.csv'

up20132014mw = '/Users/danielmsheehan/Dropbox/GIS/Data/Monitoring/JawboneUp/20132014mw.csv'

dfu13 = pd.read_csv(up2013)
dfw13 = pd.read_csv(we2013)
dfu13['date_join'] = dfu13['DATE']
dfw13['date_join'] = dfw13['date']
dfu13['date_join'].apply(int)
dfw13['date_join'].apply(int)

dfu14 = pd.read_csv(up2014)
dfw14 = pd.read_csv(we2014)
dfu14['date_join'] = dfu14['DATE']
dfw14['date_join'] = dfw14['date']
dfu14['date_join'].apply(int)
dfw14['date_join'].apply(int)


pieces = [dfu13, dfu14]
dfu1314 = pd.concat(pieces)
pieces = [dfw13, dfw14]
dfw1314 = pd.concat(pieces)

mdf13 = dfu1314.merge(dfw1314, on='date_join', how='inner',sort=False)
mdf13 = mdf13.fillna(0)
mdf13.to_csv(up20132014mw, index=False)

x = mdf13.m_steps
y = mdf13.tempmean
z = mdf13.tempmax
w = mdf13.tempmin

coefficients = numpy.polyfit(x, y, 1)
polynomial = numpy.poly1d(coefficients)
ys = polynomial(x)
print coefficients
print polynomial

plot(x, y, 'o')
plot(x, ys)

coefficients = numpy.polyfit(x, z, 1)
polynomial = numpy.poly1d(coefficients)
ys = polynomial(x)
print coefficients
print polynomial

plot(x, z, 'o')
plot(x, ys)

coefficients = numpy.polyfit(x, w, 1)
polynomial = numpy.poly1d(coefficients)
ys = polynomial(x)
print coefficients
print polynomial

plot(x, w, 'o')
plot(x, ys)

scatter(x,y)


grid(True)
xlabel('steps')
ylabel('temp-nyc')
show()
