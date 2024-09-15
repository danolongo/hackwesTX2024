import numpy as np
import math

neurons_right = 15000000
neurons_left = 10
neurons_up = 8
neurons_down = 4
active_neighbors = 2
columns = 2


input = np.squeeze(np.asarray([[neurons_right],[neurons_left],[neurons_up],[neurons_down]]))

output = np.array([1,2,3,4])

#Assign Weights 1 to 100 (Prioritizing left and right quadrants to resemble left and right brain hemispheres)
weights = np.squeeze(np.asarray([[4],[9],[3],[8]]))

#Add bias,
# A cluster of 6 nodes or larger is consider a "big cluster" reason why any input 6 or bigger would be reinforced
bias = 6

#Activation function
def sigmoid_func(x):
    return 1/(1 + np.exp(-x))

def der(x):
    return sigmoid_func(x) * (1- sigmoid_func(x))

#Updating weights
for epochs in range(10000):
    input_arr = input

    weighted_sum = np.dot(input_arr, weights) + bias


    error = weighted_sum  - output
    total_error = np.square(np.subtract(weighted_sum,output)).mean()
    #print total error

    first_der = error
    second_der = der(weighted_sum)
    derivative = first_der * second_der

    t_input = input.T
    final_derivative = np.dot(t_input, derivative)

    #Update weights
    weights = weights - 0.05 * final_derivative

    #update bias
    for i in derivative:
        bias = bias -0.05 * i


#Results
res =  (weights + bias)/10


print(res)

