#!/usr/bin/python

import pandas as pd
import numpy as np
from sklearn.utils.extmath import randomized_svd
import matplotlib.pyplot as plt

class biplotpy:
	'''
	Gabriel Biplots
	'''

	def __init__(self, data,dim,alpha = 1):
		self.data = data
		self.p = self.data.shape[1] #elements
		self.n = self.data.shape[0] #variables
		if isinstance(dim, (int, float)):
			self.dim = dim
		else:
			raise ValueError('not numeric')
		if self.dim>self.p:
			raise ValueError('dim bigger than p')
		if (alpha>=0 and alpha<=1):
			self.alpha = alpha
		else:
			raise ValueError('not between 0 and 1')

	def standardize(self):
		medias = self.data.mean(axis=0)
		desv = self.data.std(axis=0)
		self.data_st = (self.data-medias)/desv
		return self.data_st

	def SVD(self,niter=5,state=None,std=True):
		if std==True:
			self.data = self.standardize()
		self.U, self.Sigma, self.VT = randomized_svd(self.data, n_components=self.dim,n_iter=niter,random_state=state)

	def Inertia(self):
		self.EV = np.power(self.Sigma,2)
		self.Inertia = EV/np.sum(EV) * 100

