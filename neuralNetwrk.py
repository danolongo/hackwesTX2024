import numpy as np
import numpy as np

def main(weight1, weight2, bias1, bias2):
{
    # Example input vector (activations from previous layer)
    activationArr = np.array([[0.5], [0.3], [0.8], [0.9]])  # shape (4, 1)

    # Initial weight matrix (larger, for example, 6x4)
    weight1 = np.array([[0.2, 0.4, 0.1, 0.6],
                   [0.5, 0.7, 0.2, 0.9],
                   [0.3, 0.8, 0.5, 0.2],
                   [0.9, 0.6, 0.4, 0.3],
                   [0.7, 0.5, 0.3, 0.1],
                   [0.4, 0.9, 0.6, 0.5]])  # shape (6, 4)

    # Bias vector for the first layer (6x1)
    bias1 = np.array([[0.1], [0.2], [0.3], [0.4], [0.5], [0.6]])

    # Multiply W1 by A and add bias
    intermediate_output = np.dot(weight1, activationArr) + bias1  # shape (6, 1)

    # Now reduce the intermediate output to a 4x1 output using a final weight matrix (W2)
    weight2 = np.array([[0.1, 0.3, 0.5, 0.7, 0.9, 0.2],
                   [0.6, 0.8, 0.4, 0.2, 0.5, 0.9],
                   [0.3, 0.1, 0.7, 0.8, 0.2, 0.6],
                   [0.4, 0.5, 0.2, 0.6, 0.7, 0.3]])  # shape (4, 6)

    # Bias vector for the final layer (4x1)
    bias2 = np.array([[0.1], [0.2], [0.3], [0.4]])

    # Multiply W2 by the intermediate output and add the final bias
    output = np.dot(weight2, intermediate_output) + bias2  # shape (4, 1)

    # Multiply the entire result by the final bias factor
    final_bias = 0.9
    output = output * final_bias

    # Print the final output (4x1)
    print(output)
}
