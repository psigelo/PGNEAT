import numpy as np
import random


class SigmoidNeuron:
    def __init__(
            self, amountOfNeurons=None, sigmoidConstantMin=3.0,
            sigmoidConstantMax=5.2, biasMin=0.0, biasMax=0.0, cloneFrom=None,
            sigmoidConstantMutationRate=0.2, biasMutationRate=0.2
    ):
        self.id = random.getrandbits(128)
        self.output = None
        if(cloneFrom is None):
            self.amountOfNeurons = amountOfNeurons
            self.sigmoidConstantMax = sigmoidConstantMax
            self.sigmoidConstantMin = sigmoidConstantMin
            self.sigmoidConstantMutationRate = sigmoidConstantMutationRate
            self.biasMutationRate = biasMutationRate
            self.biasMax = biasMax
            self.biasMin = biasMin
            self.sigmoidConstantVect = \
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
            self.sigmoidConstantVect = cloneFrom.sigmoidConstantVect.copy()
            self.bias = cloneFrom.bias.copy()

    def MightMutate(self):
        pass

    def Spread(self):
        pass

    def TopologyMutate(self):
        pass

    def GetOutput(self):
        return self.output

    def SumIncomingVoltage(self, incomingVoltage):
        pass
