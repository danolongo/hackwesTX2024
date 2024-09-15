from CellClass import Cell
import math

def fill_cell_array(rows, cols, cell_array):
    n = 0
    for i in range(rows):
        inner = []
        for j in range(cols):
            inner.append(Cell(n))
            n += 1
        cell_array.append(inner)




def fill_cell_array_neighbors(rows, cols, cell_array, diagonal = False):
    for i in range(rows):
        for j in range(cols):
            if i > 0:
                cell_array[i][j].add_neighbor(cell_array[i - 1][j])
            if j > 0:
                cell_array[i][j].add_neighbor(cell_array[i][j - 1])
            if j < len(cell_array) - 1:
                cell_array[i][j].add_neighbor(cell_array[i][j + 1])
            if i < len(cell_array) - 1:
                cell_array[i][j].add_neighbor(cell_array[i + 1][j])
    if diagonal == True:
        for i in range(rows):
            for j in range(cols):
                if i > 0 and j > 0:
                    cell_array[i][j].add_neighbor(cell_array[i - 1][j - 1])
                if i > 0 and j < len(cell_array) - 1:
                    cell_array[i][j].add_neighbor(cell_array[i - 1][j + 1])
                if i < len(cell_array) - 1 and j > 0:
                    cell_array[i][j].add_neighbor(cell_array[i + 1][j - 1])
                if i < len(cell_array) - 1 and j < len(cell_array) - 1:
                    cell_array[i][j].add_neighbor(cell_array[i + 1][j + 1])

def first_quarter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    mid_row = math.ceil(rows / 2)
    mid_col = math.ceil(cols / 2)

    first_quarter_value = 0

    for i in range(mid_row - 1):
        for j in range(mid_col - 1):
            if matrix[i][j].state in {2, 3, 4}:
                first_quarter_value += 1

    return first_quarter_value

def second_quarter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    mid_row = math.ceil(rows / 2)
    mid_col = math.ceil(cols / 2)

    second_quarter_value = 0

    for i in range(mid_row - 1):
        for j in range(mid_col, cols):
            if matrix[i][j].state in {2, 3, 4}:
                second_quarter_value += 1

    return second_quarter_value

def third_quarter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    mid_row = math.ceil(rows / 2)
    mid_col = math.ceil(cols / 2)

    third_quarter_value = 0

    for i in range(mid_row, rows):
        for j in range(mid_col - 1):
            if matrix[i][j].state in {2, 3, 4}:
                third_quarter_value += 1

    return third_quarter_value

def fourth_quarter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    mid_row = math.ceil(rows / 2)
    mid_col = math.ceil(cols / 2)

    fourth_quarter_value = 0

    for i in range(mid_row, rows):
        for j in range(mid_col, cols):
            if matrix[i][j].state in {2, 3, 4}:
                fourth_quarter_value += 1

    return fourth_quarter_value