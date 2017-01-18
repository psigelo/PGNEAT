import numpy as np
import copy

INPUT_NEURON_GROUP_ID = 0
OUTPUT_NEURON_GROUP_ID = 1000  # TODO: get a max number posible
INITIAL_NEURON_GROUP_ID = 1
INPUT_SYNAPSE_GROUP_ID = 0
OUTPUT_SYNAPSE_GROUP_ID = 1000  # TODO: get a max number posible
INITIAL_SYNAPSE_GROUP_ID = 1


class ANN:
    def __init__(
        self, inputAmount=None, outputAmount=None,
        sensorNeuronGroup=None, hiddenNeuronGroup=None,
        outputNeuronGroup=None, inputSynapses=None, hiddenSynapses=None,
        outputSynapses=None, newHiddenNeuronGroupRate=0.1,
        backwardConnections=False, cloneFrom=None
    ):
        self.neuronGroups_dict = dict()
        self.synapses_dict = dict()
        self.synapse_id = 0
        if(cloneFrom is None):
            self.neuronGroupId = INITIAL_NEURON_GROUP_ID
            self.synapseId = INITIAL_NEURON_GROUP_ID
            self.inputAmount = inputAmount
            self.outputAmount = outputAmount
            self.sensorNeuronGroup = copy.deepcopy(sensorNeuronGroup)
            self.hiddenNeuronGroup = copy.deepcopy(hiddenNeuronGroup)
            self.outputNeuronGroup = copy.deepcopy(outputNeuronGroup)
            self.inputSynapses = inputSynapses
            self.hiddenSynapses = hiddenSynapses
            self.outputSynapses = outputSynapses
            self.newHiddenNeuronGroupRate = newHiddenNeuronGroupRate
            self.backwardConnections = backwardConnections
            self.CreateInitialStructure()
        else:
            self.neuronGroupId = cloneFrom.neuronGroupId
            self.self.synapseId = cloneFrom.self.synapseId
            self.sensorNeuronGroup = copy.deepcopy(cloneFrom.sensorNeuronGroup)
            self.hiddenNeuronGroup = copy.deepcopy(cloneFrom.hiddenNeuronGroup)
            self.outputNeuronGroup = copy.deepcopy(cloneFrom.outputNeuronGroup)
            self.inputSynapses = cloneFrom.inputSynapses
            self.hiddenSynapses = cloneFrom.hiddenSynapses
            self.outputSynapses = cloneFrom.outputSynapses
            self.newHiddenNeuronGroupRate = cloneFrom.newHiddenNeuronGroupRate
            self.backwardConnections = cloneFrom.backwardConnections
            self.neuronGroups_dict = copy.deepcopy(cloneFrom.neuronGroups_dict)
            self.synapses_dict = copy.deepcopy(cloneFrom.synapses_dict)

    def Spread(self):
        for ng_id, neuronGroup in self.neuronGroups_dict:
            neuronGroup.Spread()

    def CreateInitialStructure(self):
        # First we create all neurons and latter we connect with synapses
        self.neuronGroups_dict.update(
            {
                'id': INPUT_NEURON_GROUP_ID,
                'NG': self.sensorNeuronGroup.CreateNew()
            }
        )
        self.neuronGroups_dict.update(
            {
                'id': OUTPUT_NEURON_GROUP_ID,
                'NG': self.outputNeuronGroup.CreateNew()
            }
        )
        # Input synapse
        self.synapses_dict.update(
            {'id': INPUT_SYNAPSE_GROUP_ID, 'S': self.inputSynapses.CreateNew()}
        )
        self.synapses_dict[INPUT_SYNAPSE_GROUP_ID].Connect(
            self.neuronGroups_dict[INPUT_NEURON_GROUP_ID]
        )
        # Output synapse
        self.synapses_dict.update(
            {
                'id': OUTPUT_SYNAPSE_GROUP_ID,
                'S': self.outputSynapses.CreateNew()
            }
        )
        self.synapses_dict[OUTPUT_SYNAPSE_GROUP_ID].Connect(
            self.neuronGroups_dict[OUTPUT_NEURON_GROUP_ID]
        )
        # 1rst Hidden synapse.
        new_synapse_id = self.synapse_id
        self.synapse_id += 1
        self.synapses_dict.update(
            {'id': new_synapse_id, 'S': self.inputSynapses.CreateNew()}
        )
        self.synapses_dict[new_synapse_id].Connect(
            self.neuronGroups_dict[INPUT_NEURON_GROUP_ID],
            self.neuronGroups_dict[OUTPUT_NEURON_GROUP_ID]
        )

    def SetInputsInSensorGroup(self, inputs):
        self.synapses_dict[INPUT_SYNAPSE_GROUP_ID].SetInputs(inputs)

    def GetOutput(self):
        return self.synapses_dict[OUTPUT_SYNAPSE_GROUP_ID].GetOutput()
