class Cell:
    def __init__(self,identity):
        self.identity = identity
        self.state = 0
        self.neighbors = []
        self.signal = 0
        self.enabled = 0

    def get_state(self):
        return self.state

    def set_state(self, data):
        self.state = data

    def set_signal(self, state):
        self.signal = state

    def set_enabled(self, state):
        self.enabled = state

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def change_signal(self, data):
        self.signal += data

    def change_enabled(self, data):
        self.enabled += data

    def find_enabled_transmitters(self):
        transmitter_array = []
        for n in range(len(self.neighbors)):
            if self.neighbors[n].state == 2 and self.neighbors[n].enabled == 0:
                transmitter_array.append(self.neighbors[n])
        return transmitter_array

    def find_enabled_resting_neurons(self):
        neuron_array = []
        for n in range(len(self.neighbors)):
            if self.neighbors[n].state == 3 and self.neighbors[n].enabled == 0:
                neuron_array.append(self.neighbors[n])
        return neuron_array

