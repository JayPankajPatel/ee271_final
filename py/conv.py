"""
 We are using the MNIST handwritten number set where the data is greyscale
 black is 0 and white is 255 in our images. 
 use this as a reference
 https://victorzhou.com/blog/intro-to-cnns-part-1/
 our network is small so a 2d array is good enough, the link above goes
 into more detail. The code here is implemented so it is easier to read
 when converted this model to FPGA

"""

import numpy as np


class Conv3x3:
    def __init__(self, num_filters, filters):
        self.num_filters = num_filters
        self.filters = filters  

    def extract_regions(self, image):
        """
        Extracts all possible 3x3 image regions (valid padding).
        Returns a list of tuples (region, row, col).
        - image is a 2D numpy array.
        """
        h, w = image.shape
        regions = []

        for i in range(h - 2):
            for j in range(w - 2):
                im_region = image[i : i + 3, j : j + 3]  # Extract 3x3 region
                regions.append((im_region, i, j))  # Store tuple (region, row, col)

        return regions

    def forward(self, input):
        """
        Performs a forward pass of the conv layer using the given input.
        Returns a 3D numpy array with dimensions (h, w, num_filters).
        - input is a 2D numpy array.
        """
        h, w = input.shape
        output = np.zeros((h - 2, w - 2, self.num_filters))  # Output feature map

        # Extract all 3x3 regions manually
        regions = self.extract_regions(input)

        # Convolution operation
        for region, i, j in regions:
            for f in range(self.num_filters):  # Loop over filters
                sum_value = 0  # MAC accumulation
                for ki in range(3):  # Kernel height
                    for kj in range(3):  # Kernel width
                        sum_value += (
                            region[ki, kj] * self.filters[f, ki, kj]
                        )  # MAC operation

                output[i, j, f] = sum_value  # Store result in output map

        return output


if __name__ == "__main__":
    # Example usage
    image = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    conv = Conv3x3(num_filters=1)
    output = conv.forward(image)

    print(output)  # Outputs the manually computed convolution result
