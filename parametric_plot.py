from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

#variables
a = 1
omega = 2*np.pi

# Prepare arrays x, y, z
t = np.linspace(0, 5, 1000)

x = np.exp(-a * t) * np.cos(omega * t)
y = np.exp(-a * t) * np.sin(omega * t)
z = 0*t


ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()