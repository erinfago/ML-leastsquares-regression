# Erin Fago
# Machine Learning - Prof. Hu
# HW # 2

#reg.py

'''can read a data file (e.g., syn_train.txt) to train the nth degree polynomial function (n = 1, 2, 3, etc.), and make predictions on the validation set (e.g., syn_validation.txt)'''

import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot
from numpy import *
from numpy.linalg import *
from numpy.matlib import *


def main():
	# name the files given to then use
	train = open(sys.argv[1], "r")
	validation = open(sys.argv[2], "r")
	degree = sys.argv[3]

	#intialize lists that will hold the data from the training and validation files
	xlist = []
	tlist = []
	xlistV = []
	tlistV = []

	#go through file, split at \t and make a list of float point #'s split into 2 lists
	for line in train.readlines():
		vals = line.split('\t')
		xlist.append(float(vals[0]))
		tlist.append(float(vals[1]))


	for vline in validation.readlines():
		vvals = vline.split('\t')
		xlistV.append(float(vvals[0]))
		tlistV.append(float(vvals[1]))

	#from the lists created make matricies to then begin training the nth degree polynomial 
	xData = matrix(xlist).T
	yData = matrix(tlist).T

	#create a matrix from the validation and training data so you can plot
	validX = matrix(xlistV).T
	validY = matrix(tlistV).T

	#Turns on interactive mode
	plot.ion()

	#Creates a subplot
	#Everything after the subplot command refer to that particular subplot
	plot.subplot(111)
	plot.axis([min(xlist), max(xlist), min(tlist), max(tlist)])
	plot.xlabel('x values')
	plot.ylabel('t values')

	#plot training
	plot.plot(xData, yData, 'go', color='blue', markersize=12)

	#plot validation
	plot.plot(validX, validY, 'go', color='green', markersize=6)


	X = ones((len(xData), 1))
	#Creates the x values for plotting the regression curve
	regressionXData = matrix(arange(min(xlist), max(xlist), .2), dtype=float64).T
	regressionX = ones((len(regressionXData), 1))

	# go through and plot up to desired degree
	for i in range(1, int(degree)+1):
		#Add a column to X that corresponds to a polynomial feature of degree i
		#Note that the input values are also recentered to the range [-1, 1]
		X = column_stack((X, power((2*xData - xData.max() - xData.min())/(xData.max() - xData.min()), i)))

    	#Add a corresponding column to regressionX as well
		regressionX = column_stack((regressionX, power((2*regressionXData - xData.max() - xData.min())/(xData.max() - xData.min()), i)))


	#Solve this regression
	w = (X.T * X).I * X.T * yData

	#regression plot
	plot.plot(regressionXData, regressionX*w, color='red', linewidth=2)

	#draw
	plot.draw()


	#calculate mse and print to terminal
	mse = float(1.0/len(xData) * (X*w - yData).T * (X*w - yData))
	
	#prints MSE and degree and function
	print("degree: ", degree)
	print("MSE: ", mse)

	#now print out function by looking at the w matrix
	outputstr = ""
	for j in range(len(w)):
		outputstr += str(float(w[j]))
		if j == 1:
			outputstr += "x"
		elif j > 1:
			outputstr += "x^"
			outputstr += str(j)

		if j != len(w)-1:
			outputstr += " + "

	print("function: ", outputstr)

	#this print statement was here to help with plotting coordinate points
	#print(str(degree) + "," + str(mse))

	input('<press enter>')


	train.close()
	validation.close()

main()