import matplotlib.pyplot as plt
import numpy as np

R = 0.2
w = 26000.0/216
v = 130/3.6

def x(t):
    global R
    global w
    global v
    return R*np.sin(w*t) + v * t

def y(t):
    global R
    global w
    global v
    return R*np.cos(w*t) + 0.3


t = np.linspace(0,0.2,1001)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect(aspect=2)


plt.plot(x(t),y(t))
plt.ylim(0, 0.6)
plt.xlim(0, 7)
plt.xlabel("Strecke $[m]$")
plt.ylabel("Höhe über der Straße $[m]$")
plt.show()
