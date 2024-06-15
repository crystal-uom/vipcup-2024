import numpy as np
from numpy.linalg import svd
from PIL import Image
import math

def get_svd_image(image_path):
    # Open the PNG image
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Convert the image to a NumPy array
    A = np.array(grayscale_image)

    # Remember image size
    n = len(A)

    # Take SVD
    U, S, V = svd(A)

    # Threshold
    N = 4 * n / math.sqrt(3)

    # Initialize blank image
    final_img = np.zeros((n, n))
    
    for i in range(N):
        matrix = S[i]*np.outer(U[:,i],V[i])
        final_img += matrix
    
    return final_img