
import numpy as np
import matplotlib.pyplot as plt

#As a path collection

from matplotlib.collections import LineCollection

""" fig, ax = plt.subplots()
r = np.arange(0, .075, 0.00001)
nverts = len(r)
theta = np.array(range(nverts)) * (2*np.pi)/(nverts-1)
theta = 90*np.pi*r
xoffset, yoffset = .5, .5
yy = 1.4*r * np.sin(theta) + yoffset
xx = r * np.cos(theta) + xoffset
spiral = zip(xx,yy)
collection = LineCollection([spiral], colors='k')
ax.add_collection(collection)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1) """

# In polar coordinates

fig, ax = plt.subplots(subplot_kw=dict(polar=True, axisbg='none'), figsize=(.5,.5))
r = np.arange(0, 3.4, 0.01)
theta = 0.1*np.pi*r**2
ax.set_axis_off()
ax.grid(False)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.plot(theta, r, linewidth=2, color='k')

plt.show()