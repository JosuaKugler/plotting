import matplotlib.pyplot as plt
import numpy as np
import sys


nbins = int(sys.argv[1])

lenghts = [15.0,13.0,8.0,9.5, 12.5, 14.5, 12.0, 13.5, 5.0, 8.5, 14.0, 10.5, 16.5, 12.5, 8.0, 10.5, 7.0, 13.5, 11.0, 12.5, 12.5, 15.0, 16.5, 11.0, 16, 9.5, 14.5, 10.5, 9.5, 13.5, 13.5, 14.5, 11.0, 11.0, 12.0, 12.5, 8.5, 14.5, 8.0, 8.5, 5.0, 9.5, 7.5, 4.0, 10.5, 10.5, 14.0, 10.0, 8.5, 9.0]


truelengths = np.array(lenghts)
truelengths += 6.5
truelengths *= 0.01

print(max(truelengths))

def time(x):
	return np.sqrt((2*x)/9.81)

timearray = time(truelengths)
print("standardabweichung", np.std(timearray))
additionaltime = np.random.rand(50)
additionaltime = additionaltime/100
timearray2 = timearray + additionaltime



def createtexcode():
	startlist = [r"\documentclass{article}", r"\usepackage[ngerman]{babel}", r"\usepackage{graphicx}", r"\usepackage[left = 2cm, top = 2cm, bottom = 2cm, right = 2cm]{geometry}", r"\begin{document}", r"\includegraphics{ex1_1.png}\par\noindent"]
	tabularline = r"\begin{tabular}{c"
	numberline = r"Nr:"
	lengthline = r"Länge $[\mathrm{m}]$:"
	timeline = r"Zeit $[\mathrm{s}]$:"
	for i in range(10):
		tabularline+=r"|c"
		numberline+=r"&"+ str(i+1)
		lengthline+=r"&"+ str(round(truelengths[i], 3))
		timeline+=r"&"+str(round(timearray[i], 2))
	tabularline+=r"}"
	numberline+=r"\\"
	lengthline+=r"\\"
	timeline+=r"\\"
	startlist.append(tabularline)
	startlist.append(numberline + r"\hline")
	startlist.append(lengthline)
	startlist.append(timeline)
	startlist.append(r"\end{tabular}\par\vspace*{2mm}\noindent")
	tabularline = r"\begin{tabular}{c"
	numberline = r"Nr:"
	lengthline = r"Länge $[\mathrm{m}]$:"
	timeline = r"Zeit $[\mathrm{s}]$:"
	for i in range(10,20):
		tabularline+=r"|c"
		numberline+=r"&"+ str(i+1)
		lengthline+=r"&"+ str(round(truelengths[i], 3))
		timeline+=r"&"+str(round(timearray[i], 2))
	tabularline+=r"}"
	numberline+=r"\\"
	lengthline+=r"\\"
	timeline+=r"\\"
	startlist.append(tabularline)
	startlist.append(numberline + r"\hline")
	startlist.append(lengthline)
	startlist.append(timeline)
	startlist.append(r"\end{tabular}\par\vspace*{2mm}\noindent")
	tabularline = r"\begin{tabular}{c"
	numberline = r"Nr:"
	lengthline = r"Länge $[\mathrm{m}]$:"
	timeline = r"Zeit $[\mathrm{s}]$:"
	for i in range(20,30):
		tabularline+=r"|c"
		numberline+=r"&"+ str(i+1)
		lengthline+=r"&"+ str(round(truelengths[i], 3))
		timeline+=r"&"+str(round(timearray[i], 2))
	tabularline+=r"}"
	numberline+=r"\\"
	lengthline+=r"\\"
	timeline+=r"\\"
	startlist.append(tabularline)
	startlist.append(numberline + r"\hline")
	startlist.append(lengthline)
	startlist.append(timeline)
	startlist.append(r"\end{tabular}\par\vspace*{2mm}\noindent")
	tabularline = r"\begin{tabular}{c"
	numberline = r"Nr:"
	lengthline = r"Länge $[\mathrm{m}]$:"
	timeline = r"Zeit $[\mathrm{s}]$:"
	for i in range(30,40):
		tabularline+=r"|c"
		numberline+=r"&"+ str(i+1)
		lengthline+=r"&"+ str(round(truelengths[i], 3))
		timeline+=r"&"+str(round(timearray[i], 2))
	tabularline+=r"}"
	numberline+=r"\\"
	lengthline+=r"\\"
	timeline+=r"\\"
	startlist.append(tabularline)
	startlist.append(numberline + r"\hline")
	startlist.append(lengthline)
	startlist.append(timeline)
	startlist.append(r"\end{tabular}\par\vspace*{2mm}\noindent")
	tabularline = r"\begin{tabular}{c"
	numberline = r"Nr:"
	lengthline = r"Länge $[\mathrm{m}]$:"
	timeline = r"Zeit $[\mathrm{s}]$:"
	for i in range(40,50):
		tabularline+=r"|c"
		numberline+=r"&"+ str(i+1)
		lengthline+=r"&"+ str(round(truelengths[i], 3))
		timeline+=r"&"+str(round(timearray[i], 2))
	tabularline+=r"}"
	numberline+=r"\\"
	lengthline+=r"\\"
	timeline+=r"\\"
	startlist.append(tabularline)
	startlist.append(numberline + r"\hline")
	startlist.append(lengthline)
	startlist.append(timeline)
	startlist.append(r"\end{tabular}\par\vspace*{2mm}\noindent")
	lmean = np.mean(truelengths)
	tmean = np.mean(timearray)
	startlist.append(r"Mittelwert der Längen: {} m\\".format(round(lmean, 3)))
	startlist.append(r"Mittelwert der Reaktionszeit: {} s\\".format(round(tmean, 3)))
	startlist.append(r"\end{document}")
	return startlist

liste = createtexcode()
with open("ex1_1.tex", "w") as f:
	for i in liste:
		f.write(i + "\n")

#print(timearray2)

N, bins, patches = plt.hist(timearray,bins = nbins, color = 'grey')

for n, patch in zip(range(nbins), patches):
    if n%2==0:
        patch.set_facecolor('lightgrey')

plt.xlabel('$t$ [s]')
plt.title('ReaktionsZeit $[\mathrm{s}]$ von Rui Yang')
plt.show()



#plt.hist(timearray2, bins = 15, color = "blue")
#plt.xlabel('t [s]')
#plt.title('ReaktionsZeit $[\mathrm{s}]$ von Cathrin Wesener')
#plt.show()
#print(timearray)
#print(np.mean(timearray))
#print(np.std(timearray))
