import numpy as np
import random


class SigmoidNeuron:
    def __init__(
            self, amountOfNeurons=None, sigmoidConstantMin=3.0,
            sigmoidConstantMax=5.2, biasMin=0.0, biasMax=0.0, cloneFrom=None,
            sigmoidConstantMutationRate=0.2, biasMutationRate=0.2
    ):
        self.preSynapseAmount = 0
        self.postSynapseAmount = 0
        self.preSynapse = dict()
        self.id = random.getrandbits(128)
        self.output = None
        self.incomingVoltage = np.zeros(1, amountOfNeurons)
        if(cloneFrom is None):
            self.amountOfNeurons = amountOfNeurons
            self.sigmoidConstantMax = sigmoidConstantMax
            self.sigmoidConstantMin = sigmoidConstantMin
            self.sigmoidConstantMutationRate = sigmoidConstantMutationRate
            self.biasMutationRate = biasMutationRate
            self.biasMax = biasMax
            self.biasMin = biasMin
            self.sigmoidConstants = \
                np.random.uniform(
                    self.sigmoidConstantMin, self.sigmoidConstantMax,
                    [1, self.amountOfNeurons]
                )
            self.bias = \
                np.random.uniform(
                    self.biasMin, self.biasMax,
                    [1, self.amountOfNeurons]
                )
        else:
            self.amountOfNeurons = cloneFrom.amountOfNeurons
            self.sigmoidConstantMax = cloneFrom.sigmoidConstantMax
            self.sigmoidConstantMin = cloneFrom.sigmoidConstantMin
            self.sigmoidConstantMutationRate = \
                cloneFrom.sigmoidConstantMutationRate
            self.biasMutationRate = cloneFrom.biasMutationRate
            self.biasMax = cloneFrom.biasMax
            self.biasMin = cloneFrom.biasMin
            self.sigmoidConstants = cloneFrom.sigmoidConstants.copy()
            self.bias = cloneFrom.bias.copy()

    def MightMutate(self):
        mask_sigmoid = 1 - np.random.binomial(
            1, self.sigmoidConstantMutationRate,
            [1, self.amountOfNeurons]
        )
        mask_bias = 1 - np.random.binomial(
            1, self.biasMutationRate,
            [1, self.amountOfNeurons]
        )
        randomSigmoidConstants = np.random.uniform(
            self.sigmoidConstantMin, self.sigmoidConstantMax,
            [1, self.amountOfNeurons]
        )
        randomBias = np.random.uniform(
            self.biasMin, self.biasMax,
            [1, self.amountOfNeurons]
        )
        self.sigmoidConstants = self.sigmoidConstants * mask_sigmoid
        + randomSigmoidConstants * (1 - mask_sigmoid)
        self.bias = self.bias * mask_bias + randomBias * (1 - mask_bias)

    def Spread(self):
        self.output = np.sigmoid(
            self.incomingVoltage *
            self.sigmoidConstants + self.bias
        )

    def TopologyMutate(self):
        pass

    def GetOutput(self):
        return self.output

    def resetIncomingVoltage(self):
        self.incomingVoltage = np.zeros(self.incomingVoltage.shape)

    def SumIncomingVoltage(self, incomingVoltage):
        self.incomingVoltage += incomingVoltage

    def AddPreSynapse(self, preSynapse):
        self.preSynapse.update({self.preSynapseAmount, preSynapse})
        self.preSynapseAmount += 1

    def AddPostSynapse(self, postSynapse):
        self.postSynapse.update({self.postSynapseAmount, postSynapse})
        self.postSynapseAmount += 1
