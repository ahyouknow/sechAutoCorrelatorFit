#!/usr/bin/python3
from scipy.optimize import curve_fit as cf
import numpy as np
from matplotlib import pyplot as plt

def main():
	
	errorY = []
	errorX = []
	c = 3e8								#speed limit of the universe
	N=1000								##this is a number with no units
	xx, data, errorY = np.genfromtxt('take1.csv', delimiter=',', unpack=True, skip_header=1) #lol
	
	datafwhm=20e-12 					#this need to be a TIME in seconds, the pulse length
	dataoffset=20e-3 					## this is a length in meters
	xmax=max(xx)		##this is a length
	xmin=min(xx)
	#xx = np.linspace(xmin, xmax, N) 	##set some variable for plotting x axis
	
	# xx = csv[1:,0]
	# data = csv[1:,1]
	# errorY = csv[1:,2]
	print(xx)
	p0 = [120, dataoffset, datafwhm] 		##fit start is exactly what i made it
	popt, pcov = cf(veryCoolAutoCorrelatorSechFit, xx, data, p0=p0) ## fit fit fit
	print(popt) 						##were we even close?
	graphline = np.linspace(xmin, xmax, N) ##no need for this, but cool
	plt.plot(xx, data, '.')
	plt.plot(graphline, veryCoolAutoCorrelatorSechFit(graphline, *popt))
	plt.show() 							## plot ^^
	
	
def veryCoolAutoCorrelatorSechFit(L, A0, L0, FWHM):
	c = 3e8
	delay=2*(L-L0)/c
	return A0/(np.sinh(2.17196*delay / FWHM)**2) * (2.7196*delay / FWHM * 1/(np.tanh(2.7196 * delay / FWHM)) - 1)
	
if __name__ == '__main__':
	main()