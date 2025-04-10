import numpy as np
from conv import Conv3x3
from maxpool import MaxPool2
from softmax import Softmax
import tensorflow as tf

# The mnist package takes care of handling the MNIST dataset for us!
# Learn more at https://github.com/datapythonista/mnist
# We only use the first 1k testing examples (out of 10k total) in the interest of time.
# Feel free to change this if you want.

mnist = tf.keras.datasets.mnist.load_data()
(test_images, test_labels), (_, _) = mnist

conv = Conv3x3(8, filters=np.load("./Train/filters.npy"))  # 28x28x1 -> 26x26x8
pool = MaxPool2()  # 26x26x8 -> 13x13x8
softmax = Softmax(
    13 * 13 * 8,
    10,
    weights=np.load("./Train/weights.npy"),
    biases=np.load("./Train/biases.npy"),
)  # 13x13x8 -> 10


def forward(image, label):
    """
    Completes a forward pass of the CNN and calculates the accuracy and
    cross-entropy loss.
    - image is a 2d numpy array
    - label is a digit
    """
    # We transform the image from [0, 255] to [-0.5, 0.5] to make it easier
    # to work with. This is standard practice.
    out = conv.forward((image / 255) - 0.5)
    out = pool.forward(out)
    out = softmax.forward(out)

    # Calculate cross-entropy loss and accuracy. np.log() is the natural log.
    loss = -np.log(out[label])
    acc = 1 if np.argmax(out) == label else 0

    return out, loss, acc


print("MNIST CNN initialized!")

loss = 0
num_correct = 0
for i, (im, label) in enumerate(zip(test_images, test_labels)):
    # Do a forward pass.
    _, l, acc = forward(im, label)
    loss += l
    num_correct += acc

    # Print stats every 100 steps.
    if i % 100 == 99:
        print(
            "[Step %d] Past 100 steps: Average Loss %.3f | Accuracy: %d%%"
            % (i + 1, loss / 100, num_correct)
        )
        print("Max Value", conv.max_value)
        print("Min Value", conv.min_value)
        print("Max Value: Filters", np.max(conv.filters))
        print("Min Value: Filters", np.min(conv.filters))
        print("Max Value: weights", np.max(softmax.weights))
        print("Min Value: biases", np.min(softmax.biases))
        loss = 0
        num_correct = 0
