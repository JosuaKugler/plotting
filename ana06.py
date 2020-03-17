import matplotlib.pyplot as plt
import numpy as np
import scipy
import sympy
import math

def f1(n):
    """
    Funktion, die den Funktionswert an der Stelle x berechnet
    """
    return n**n



def computereihebis(n, x):
    reihe = []
    for i in range(n):
        if i== 0:
            reihe.append(0)
        else:
            if i % 2 == 0:
                this = i**2 * math.pi**i * (x-42)**i
            else:
                this = -i*4**i*(x-42)**i
            reihe.append(reihe[-1] + this)
    return reihe

#x = np.linspace(start, stop, num) num = Anzahl der Werte im Intervall von start bis stop
xmax = 200
x = np.linspace(0,xmax, xmax+1)

fig = plt.figure()
ax = fig.add_subplot(111)
#plt.plot(x, f1(x))
x_value = 42.24
liste = computereihebis(xmax + 1, x_value)
plt.plot(x, liste)

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.show()
