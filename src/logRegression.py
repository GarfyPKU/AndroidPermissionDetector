#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Logistic Regression

from numpy import *
import random, warnings
import matplotlib.pyplot as plt


# if you do not have matplotlib and do not want to use gui,
# you can comment out "import matpllotlib" and _gui() method.
def _gui(numIter, weightsMatrix):
	weightsList = weightsMatrix.tolist()
	plt.figure()
	for i in range(5):
		plt.subplot(2, 3, i)
		plt.plot(range(numIter),weightsList[i])
	plt.show()


def sigmoid(inX):
	return 1.0/(1+exp(-inX))

def smoothStocGradAscent(dataMatrix, classLabels, numIter, alphaLen, gui):
	warnings.filterwarnings("ignore")
	weightsMatrix = empty((5,numIter))
	m, n = shape(dataMatrix)
	weights = ones((n, 1))
	for j in range(numIter):
		dataIndex = range(m)
		for i in range(m):
			alpha = 4/(1.0+j+i)+alphaLen
			randIndex = int(random.uniform(0,len(dataIndex)))
			h = sigmoid(sum(dataMatrix[randIndex]*weights))
			error = classLabels[randIndex] - h
			weights = weights + alpha * error * dataMatrix[randIndex].transpose()
			del(dataIndex[randIndex])
		weightsMatrix[:, j] = weights.transpose()

	if gui:
		_gui(numIter, weightsMatrix)
	return weights

