import numpy as np


def generate_binary_vector(size, seed=None):
    """
    Generates a binary vector with random 0s and 1s.
    Args:
        size (int): Length of the vector.
        seed (int, optional): Seed for the random number generator.
    Returns:
        numpy.ndarray: A binary vector of length `size` with random 0s and 1s.
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(2, size=size)
