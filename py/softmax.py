import numpy as np


class Softmax:
    def __init__(self, input_len, nodes, weights=None, biases=None):
        """
        Initializes the softmax layer.
        input_len: Number of inputs (flattened size of input feature map)
        nodes: Number of output nodes (classes)
        """
        if weights == None or biases == None:
            # Initialize weights with small values (to be replaced with trained model values)
            self.weights = np.random.randn(input_len, nodes) / input_len
            self.biases = np.zeros(nodes)

    def flatten_input(self, input):
        """
        Flattens a 3D input (e.g., feature map from CNN) into a 1D vector.
        Uses explicit loops instead of NumPy functions for easier RTL translation.
        """
        h, w, c = input.shape  # Height, Width, Channels
        flatten = np.zeros(h * w * c)  # Preallocate flattened array
        index = 0

        for i in range(h):
            for j in range(w):
                for k in range(c):
                    flatten[index] = input[i, j, k]
                    index += 1

        return flatten

    def forward(self, input):
        """
        Performs a forward pass of the softmax layer using the given input.
        Computes the weighted sum, applies softmax function, and returns probabilities.
        """
        flatten = self.flatten_input(input)  # Manually flatten input

        input_len, nodes = self.weights.shape
        totals = np.zeros(nodes)  # Preallocate totals array

        # Multiply-Accumulate (MAC) operation: totals = flatten @ weights + biases
        for j in range(nodes):  # Iterate over each output node
            acc = 0  # Initialize accumulator for MAC operation
            for i in range(input_len):  # Iterate over input features
                acc += flatten[i] * self.weights[i, j]  # MAC operation
            totals[j] = acc + self.biases[j]  # Add bias

        # Softmax activation: exp(x) / sum(exp(x))
        exp_values = np.zeros(nodes)  # Preallocate exponent array
        sum_exp = 0  # Sum of all exponent values

        for j in range(nodes):
            exp_values[j] = np.exp(totals[j])  # Compute exponent
            sum_exp += exp_values[j]  # Sum for normalization

        output = np.zeros(nodes)  # Preallocate output probabilities
        for j in range(nodes):
            output[j] = exp_values[j] / sum_exp  # Normalize to get probability

        return output
