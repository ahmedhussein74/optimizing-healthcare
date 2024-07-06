import numpy as np


def bitwise_mutation(individual, mutation_rate):
    """
    Performs bitwise mutation on the decision variables of an individual.
    Args:
        individual (tuple): Individual containing decision variable vectors and matrices.
        mutation_rate (float): Probability of flipping each bit.
    Returns:
        tuple: Mutated individual.
    """
    mutated_individual = []

    for var in individual:
        var_copy = np.copy(var)  # Create a copy to avoid modifying the original
        if var.ndim == 1:  # Vector
            for i in range(len(var_copy)):
                if np.random.rand() < mutation_rate:
                    var_copy[i] = 1 - var_copy[i]  # Flip bit
        else:  # Matrix
            for i in range(var_copy.shape[0]):
                for j in range(var_copy.shape[1]):
                    if np.random.rand() < mutation_rate:
                        var_copy[i, j] = 1 - var_copy[i, j]  # Flip bit
        mutated_individual.append(var_copy)

    return tuple(mutated_individual)
