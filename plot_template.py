import matplotlib.pyplot as plt
import numpy as np
import scipy
import sympy

def f1(x):
    """
    Funktion, die den Funktionswert an der Stelle x berechnet
    """
    return np.sin(x)

#x = np.linspace(start, stop, num) num = Anzahl der Werte im Intervall von start bis stop
x = np.linspace(0,100,1001)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x, f1(x))

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.show()
