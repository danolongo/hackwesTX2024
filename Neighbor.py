 as np

class Cell:
    def __init__(self,identity, state):
        self.identity = identity
        self.state = state
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def set_state(self, data):
        self.state = data

    def find_transmitters(self):
        transmitter_array = []
        for n in range(len(self.neighbors)):
            if self.neighbors[n].state == 2:
                transmitter_array.append(self.neighbors[n])
        return transmitter_array

    def find_neuron(self):
        neuron_array = []
        for n in range(len(self.neighbors)):
            if self.neighbors[n].state == 3:
                neuron_array.append(self.neighbors[n])
        return neuron_array


rows, cols = (8, 8)
cell_array = np.empty((rows, cols), dtype=object)

#Fill array with cells with state 0
n = 0
for i in range(rows):
    for j in range(cols):
        cell_array[i, j] = Cell(n, 0)
        n += 1

#Fill neighbor array in cells
for i in range(rows):
    for j in range(cols):
        if i > 0 and j > 0:
            cell_array[i, j].add_neighbor(cell_array[i - 1, j - 1])
        if i > 0:
            cell_array[i, j].add_neighbor(cell_array[i - 1, j])
        if i > 0 and j < len(cell_array) - 1:
            cell_array[i, j].add_neighbor(cell_array[i - 1, j + 1])
        if j > 0:
            cell_array[i, j].add_neighbor(cell_array[i, j - 1])
        if j < len(cell_array) - 1:
            cell_array[i, j].add_neighbor(cell_array[i, j + 1])
        if i < len(cell_array) - 1 and j > 0:
            cell_array[i, j].add_neighbor(cell_array[i + 1, j - 1])
        if i < len(cell_array) - 1:
            cell_array[i, j].add_neighbor(cell_array[i + 1, j])
        if i < len(cell_array) - 1 and j < len(cell_array) - 1:
            cell_array[i, j].add_neighbor(cell_array[i + 1, j + 1])

cell_array[0,1].set_state(2)
cell_array[1,0].set_state(0)
cell_array[1,1].set_state(2)

#Print Cell State
for i in range(rows):
    for j in range(cols):
        print(cell_array[i, j].state, end=" ")
    print()

print()

#Print Cell Identity
for i in range(rows):
    for j in range(cols):
        print(cell_array[i, j].identity, end=" ")
    print()

print()

for i in range(rows):
    for j in range(cols):
        print(i, j, "  ", cell_array[i, j].identity, "  ", [x.identity for x in cell_array[i, j].neighbors])

for n in range(len(cell_array[0,0].find_transmitters())):
    print(cell_array[0,0].find_transmitters()[n].identity)
