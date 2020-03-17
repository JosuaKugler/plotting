import matplotlib.pyplot as plt
import numpy as np
import scipy
import sympy

def f(v, T):
    """
    Funktion, die den Funktionswert an der Stelle x berechnet
    """
    return np.sqrt(np.abs(x))

#x = np.linspace(start, stop, num) num = Anzahl der Werte im Intervall von start bis stop
x = np.linspace(-100,100,2001)
T = 300

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x, f(x, T))

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.show()
