import iris
from datetime import datetime
from iris.analysis.interpolate import circular_time


fname = '/home2/hilboll/Data/albedo/omi/OMLER_0125.nc'
albedo = iris.load_cube(fname)

times = [datetime(2010, i, i) for i in range(1, 13)]
cube_2010 = circular_time(albedo, times)

times = [datetime(2015, i, i) for i in range(1, 13)]
cube_2015 = circular_time(albedo, times)

import matplotlib.pyplot as plt
import iris.plot as iplt


levels = 50
fig = plt.figure()

fig.add_subplot(211)
iplt.contourf(cube_2010[0, 0], levels)
ax = plt.gca()
ax.coastlines('50m')
ax.gridlines()

fig.add_subplot(212)
iplt.contourf(cube_2015[0, 0], levels)
ax = plt.gca()
ax.coastlines('50m')
ax.gridlines()

cube_2010 == cube_2015

