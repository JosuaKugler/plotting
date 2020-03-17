import matplotlib.pyplot as plt
import numpy as np
import scipy
import sympy

def f1(x):
    """
    Funktion, die den Funktionswert an der Stelle x berechnet
    """
    return 1/(np.sqrt(1-x))


def f2(x):
    """
    Funktion, die den Funktionswert an der Stelle x berechnet
    """
    return 1 + 0.5*x + 3/8*x**2



#x = np.linspace(start, stop, num) num = Anzahl der Werte im Intervall von start bis stop
x = np.linspace(0,0.2,100)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x, f1(x))
plt.plot(x, f2(x))

plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.show()
