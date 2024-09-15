import numpy as np
import math

neurons = 5
possible_paths = 3
active_neighbors = 2
columns = 2

def neuralNetwork(weight1, weight2, bias1, bias2, totalNeurons, possiblePaths, activeNeighbors):
    # Calculate weight and activation formulae
    weightFormula = float(math.sqrt(6 / (totalNeurons + possiblePaths)))
    actFormula = float(1 / (1 + math.exp(-activeNeighbors)))

    # Example input vector (activations from previous layer)
    activationArr = np.array([[0.5], [0.3], [0.8], [0.9]])  # shape (4, 1)

    # Multiply W1 by A and add bias
    intermediate_output = np.dot(weight1, activationArr) + bias1  # shape (6, 1)

    # Multiply W2 by the intermediate output and add the final bias
    output = np.dot(weight2, intermediate_output) + bias2  # shape (4, 1)

    # Multiply the entire result by the final bias factor
    final_bias = 0.9
    output = output * final_bias

    # Print the final output (4x1)
    print("Final Output:")
    print(output)


def create_2d_array(neurons, value=0):
    """
    Create a 2D NumPy array with specified dimensions and an optional initial value.

    Parameters:
    - rows (int): Number of rows in the array.
    - cols (int): Number of columns in the array.
    - value (optional): Value to fill the array with (default is 0). 
                         Can be any scalar value.

    Returns:
    - np.ndarray: A 2D NumPy array with the specified dimensions and value.
    """
    # Create a 2D array with the given dimensions and fill it with the specified value
    array = np.full((rows, col), value)
    return array

# Example usage
rows, cols = 6, 4  # number of rows and columns
initial_value = 5  # value to fill the array with

array = create_2d_array(rows, cols, initial_value)
print("2D Array with dimensions ({}, {}):".format(rows, cols))
print(array)

# Example weights and biases
weight1 = np.array([[0.2, 0.4, 0.1, 0.6],
                    [0.5, 0.7, 0.2, 0.9],
                    [0.3, 0.8, 0.5, 0.2],
                    [0.9, 0.6, 0.4, 0.3],
                    [0.7, 0.5, 0.3, 0.1],
                    [0.4, 0.9, 0.6, 0.5]])  # shape (6, 4)

bias1 = np.array([[0.1], [0.2], [0.3], [0.4], [0.5], [0.6]])

weight2 = np.array([[0.1, 0.3, 0.5, 0.7, 0.9, 0.2],
                    [0.6, 0.8, 0.4, 0.2, 0.5, 0.9],
                    [0.3, 0.1, 0.7, 0.8, 0.2, 0.6],
                    [0.4, 0.5, 0.2, 0.6, 0.7, 0.3]])  # shape (4, 6)

bias2 = np.array([[0.1], [0.2], [0.3], [0.4]])

# Call the function with weights, biases, and other parameters
neuralNetwork(weight1, weight2, bias1, bias2, 10, 3, 4)
