import numpy as np


def generate_binary_matrix(rows, cols, seed=None):
    """
    Generates a binary matrix with random 0s and 1s.
    Args:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.
        seed (int, optional): Seed for the random number generator.
    Returns:
        numpy.ndarray: A binary matrix of shape (rows, cols) with random 0s and 1s.
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(2, size=(rows, cols))
