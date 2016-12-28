import numpy as np 


class WeightedSynapse:
	def __init__(self, minWeight=-1.0, maxWeight=1.0, changeWeightRate=0.1, connectivity=None):
		self.connectivity = connectivity
		self.minWeight = minWeight
		self.maxWeight = maxWeight
		self.changeWeightRate = changeWeightRate
		self.weights = np.random.uniform(minWeight, maxWeight, self.connectivity.shape[0])

	def MightMutate(self):
		large = self.weights.shape[0]
		randomWeights = np.random.uniform(self.minWeight, self.maxWeight, large)
		mask = 1-np.random.binomial(1,self.changeWeightRate, large)
		self.weights = self.weights * mask +  randomWeights * (1-mask)

	def Clone(self):
		pass

	def Spread(self):
		pass 

		