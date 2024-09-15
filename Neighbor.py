import numpy as np

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

    def find_neurons(self):
        neuron_array = []
        for n in range(len(self.neighbors)):
            if self.neighbors[n].state == 3:
                neuron_array.append(self.neighbors[n])
        return neuron_array

    def find_neurons_firing(self):
        neuron_array = []
        for n in range(len(self.neighbors)):
            if self.neighbors[n].state == 4:
                neuron_array.append(self.neighbors[n])
        return neuron_array


rows, cols = (9, 9)
cell_array = np.empty((rows, cols), dtype=object)

#Fill array with cells with state 0
n = 0
for i in range(rows):
    for j in range(cols):
        cell_array[i, j] = Cell(n, 0)
        n += 1

# Define the quadrants (top-left, top-right, bottom-left, bottom-right)
mid_row = rows // 2
mid_col = cols // 2

# Create four separate arrays for each quadrant
top_left_array = cell_array[:mid_row, :mid_col]
top_right_array = cell_array[:mid_row, mid_col:]
bottom_left_array = cell_array[mid_row:, :mid_col]
bottom_right_array = cell_array[mid_row:, mid_col:]

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
print()

for n in range(len(cell_array[0,0].find_transmitters())):
    print(cell_array[0,0].find_transmitters()[n].identity)
print()

print("Top Left Array:")
for row in top_left_array:
    for cell in row:
        print(cell.identity, end=" ")
    print()

print("\nTop Right Array:")
for row in top_right_array:
    for cell in row:
        print(cell.identity, end=" ")
    print()

print("\nBottom Left Array:")
for row in bottom_left_array:
    for cell in row:
        print(cell.identity, end=" ")
    print()

print("\nBottom Right Array:")
for row in bottom_right_array:
    for cell in row:
        print(cell.identity, end=" ")
    print()
