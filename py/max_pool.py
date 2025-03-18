import numpy as np


class MaxPool2x2:
    def forward(self, image):
        """
        Performs a forward pass of the maxpool layer using the given input.
        Returns a 3d numpy array with dimensions (h / 2, w / 2, num_filters).
        - input is a 3d numpy array with dimensions (h, w, num_filters)
        """
        height, width, num_filters = image.shape
        new_height = height // 2
        new_width = width // 2
        pool = np.zeros((new_height, new_width, num_filters))

        for i in range(new_height):
            for j in range(new_width):
                region = image[i * 2 : i * 2 + 2, j * 2 : j * 2 + 2]
                pool[i, j] = np.amax(region)

        # gets the max value of every no overlapping 2 by 2 region

        return pool
