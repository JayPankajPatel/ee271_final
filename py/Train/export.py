import numpy as np

a = np.load('weights_fixed.npy')

np.savetxt("weights_fixed.csv", a, delimiter=",")


