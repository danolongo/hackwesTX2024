import numpy as np

class Cell:
    def __init__(self,identity, state):
        self.identity = identity
        self.state = state
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

rows, columns = (8, 8)
cell_array = np.empty((rows, columns), dtype=object)

#Fill array with cells with state 0
n = 0
for i in range(rows):
    for j in range(columns):
        cell_array[i, j] = Cell(n, 0)
        n += 1

#Fill neighbor array in cells
for i in range(rows):
    for j in range(columns):
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

#Print Cell State
for i in range(rows):
    for j in range(columns):
        print(cell_array[i, j].state, end=" ")
    print()

#Print Cell Identity
for i in range(rows):
    for j in range(columns):
        print(cell_array[i, j].identity, end=" ")
    print()

for i in range(rows):
    for j in range(columns):
        print(i, j, "  ", cell_array[i, j].identity, "  ", [x.identity for x in cell_array[i, j].neighbors])