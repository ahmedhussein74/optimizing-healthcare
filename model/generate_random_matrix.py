import numpy as np


def generate_random_matrix(shape, low, high, seed=None):
    """
    Generates a random matrix with integer values within the specified range.
    Args:
        shape (tuple): The shape of the matrix (rows, columns).
        low (int): The lower bound (inclusive) for random values.
        high (int): The upper bound (inclusive) for random values.
        seed (int, optional): Seed for the random number generator.
    Returns:
        numpy.ndarray: A matrix of random integers within the specified range.
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(low, high + 1, size=shape)
