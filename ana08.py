import matplotlib.pyplot as plt
import numpy as np
import scipy
import sympy


a = 1
b = 1.1

def f1(x, a, b):
    """
    Funktion, die den Funktionswert an der Stelle x berechnet
    """
    #return x**43 - b*x**42 + x**7 - x**6 * a + 84*x - 42 * b - 42 * a
    return (x**42 + 42)/(x-a) + (x**6 + 42)/(x-b)

#x = np.linspace(start, stop, num) num = Anzahl der Werte im Intervall von start bis stop
x = np.linspace(a,b,10001)
#for i in x:
#    if f1(i, a, b) > 0:
#        print("YyYYYYYYYYYYYYYYYYYYYYYYYYYYyesSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x, f1(x, a, b))
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.show()