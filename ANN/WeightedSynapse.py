import numpy as np
import random


class WeightedSynapse:
    def __init__(
            self, minWeight=-1.0, maxWeight=1.0, changeWeightRate=0.1,
            connectivityRate=0.8, cloneFrom=None,
            randomTopologyMutationRate=0.5
    ):
        self.id = random.getrandbits(128)
        self.connected = False
        self.output = None
        # Pre synaptic neuron group and post synaptics Neuron groups have
        # to be reconnected every time that a Synapse is created or cloned.
        self.preNeuronGroup = None
        self.postNeuronGroup = None
        if (cloneFrom is None):
            self.minWeight = minWeight
            self.maxWeight = maxWeight
            self.changeWeightRate = changeWeightRate
            self.weights = None  # Is created is connected.
            self.connectivityMask = None
            self.randomTopologyMutationRate = randomTopologyMutationRate
        else:
            self.minWeight = cloneFrom.minWeight
            self.maxWeight = cloneFrom.maxWeight
            self.changeWeightRate = cloneFrom.changeWeightRate
            self.weights = cloneFrom.weights.copy()
            self.randomTopologyMutationRate = \
                cloneFrom.randomTopologyMutationRate
            self.connectivityMask = cloneFrom.connectivityMask

    def MightMutate(self):
        preNeuronLarge = self.preNeuronGroup.NeuronAmount()
        postNeuronLarge = self.postNeuronGroup.NeuronAmount()
        randomWeights = np.random.uniform(
            self.minWeight, self.maxWeight, [preNeuronLarge, postNeuronLarge]
        )
        mask = 1 - np.random.binomial(
            1, self.changeWeightRate, [preNeuronLarge, postNeuronLarge]
        )
        self.weights = self.weights * mask + randomWeights * (1 - mask)
        self.weights = self.weights * self.connectivityMask

    def Connect(self, preNeuronGroup=None,
                postNeuronGroup=None, createNewWeights=True):
        # Connect preNeuronGroup with postNeuronGroup, but some wights have to
        # be 0, connectivityMask have 1 in the weights that can be different
        # than 0, and is 0 where is none a connection.
        self.connected = True
        self.preNeuronGroup = preNeuronGroup
        self.postNeuronGroup = postNeuronGroup
        preNeuronLarge = self.preNeuronGroup.NeuronAmount()
        postNeuronLarge = self.postNeuronGroup.NeuronAmount()
        if(createNewWeights):
            self.weights = np.random.uniform(
                self.minWeight, self.maxWeight,
                [preNeuronLarge, postNeuronLarge]
            )
            self.connectivityMask = 1 - np.random.binomial(
                1, self.connectivityRate,
                [preNeuronLarge, postNeuronLarge]
            )
            self.weights = self.weights * self.connectivityMask

    def Clone(self):
        return WeightedSynapse(cloneFrom=self)

    def Spread(self):
        assert (self.connected), "ERROR::WeightedSynapse::Clone::WeightedS"\
            "ynapse id %d is not connected." % self.id
        self.output = np.matmul(self.preNeuronGroup.GetOutputVector(),
                                self.weights)

    def GetOutput(self):
        return self.output

    def TopologyMutation(self):
        randomTopology = random.rand() < self.randomTopologyMutationRate
        addConnectivity = random.rand() < self.addConnectivityRate
        removeConnectivity = random.rand() < self.removeConnectivityRate
        preNeuronLarge = self.preNeuronGroup.NeuronAmount()
        postNeuronLarge = self.postNeuronGroup.NeuronAmount()

        if (randomTopology or not (removeConnectivity or addConnectivity)):
            self.connectivityMask = 1 - np.random.binomial(
                1, self.connectivityRate,
                [preNeuronLarge, postNeuronLarge]
            )
        elif(addConnectivity):
            pass
        elif(removeConnectivity):
            pass
        else:
            assert (False), "ERROR::WeightedSynapse::TopologyMutation::not"\
                "logical result"
