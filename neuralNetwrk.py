import numpy as np
import math
import random

# Define parameters
neurons = 5
possible_paths = 3
active_neighbors = 2
columns = 4  # Adjusted to match activationArr dimensions

# Bias numbers (adjusted to match neuron count)
bias1 = np.array([[6], [8], [9], [7], [5]])  # shape (5, 1)
bias2 = np.array([[8], [6], [5], [7]])  # shape (4, 1)

def neuralNetwork(bias1, bias2, totalNeurons, possiblePaths, activeNeighbors):
    # Calculate weight and activation formulae
    weightFormula = float(math.sqrt(6 / (random.choice(range(possiblePaths, totalNeurons)))))
    actFormula = float(1 / (1 + math.exp(-activeNeighbors)))

    # Create weight1 matrix (adjusted to match input dimensions)
    w1 = np.zeros((totalNeurons, columns))  # shape (5, 4)
    for i in range(totalNeurons):
        for j in range(columns):
            w1[i, j] = weightFormula

    # Create weight2 matrix (adjusted dimensions)
    w2 = np.zeros((columns, totalNeurons))  # shape (4, 5)
    for i in range(columns):
        for j in range(totalNeurons):
            w2[i, j] = weightFormula

    #print("Weight 1:")
    #print(w1)
    #print("Weight 2:")
    #print(w2)

    # Example input vector (activations from previous layer)
    activationArr = np.array(neurons, 1, value=actFormula)

    # Multiply W1 by A and add bias
    intermediate_output = np.dot(w1, activationArr) + bias1

    # Multiply W2 by the intermediate output and add the final bias
    output = np.dot(w2, intermediate_output) + bias2
    # Multiply the entire result by the final bias factor
    final_bias = 0.9
    output = output * final_bias

    # Print the final output (4x1)
    print("Final Output:")
    print(output)

# Call the function with weights, biases, and other parameters
neuralNetwork(bias1, bias2, neurons, possible_paths, active_neighbors)

