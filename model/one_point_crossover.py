import numpy as np


def one_point_crossover(parent1, parent2, crossover_rate):
    """
    Performs one-point crossover on pairs of parents to generate offspring.
    Args:
        parent1 (tuple): First parent, containing vectors and matrices.
        parent2 (tuple): Second parent, containing vectors and matrices.
        crossover_rate (float): Probability of performing crossover.
    Returns:
        tuple: Two offspring generated from the parents.
    """
    offspring1, offspring2 = [], []

    for var1, var2 in zip(parent1, parent2):
        if np.random.rand() < crossover_rate:
            if var1.ndim == 1:  # Vector
                crossover_point = np.random.randint(1, len(var1))
                child1 = np.concatenate(
                    (var1[:crossover_point], var2[crossover_point:])
                )
                child2 = np.concatenate(
                    (var2[:crossover_point], var1[crossover_point:])
                )
            else:  # Matrix
                crossover_point = np.random.randint(1, var1.shape[1])
                child1 = np.hstack(
                    (var1[:, :crossover_point], var2[:, crossover_point:])
                )
                child2 = np.hstack(
                    (var2[:, :crossover_point], var1[:, crossover_point:])
                )
        else:
            child1, child2 = var1, var2
        offspring1.append(child1)
        offspring2.append(child2)

    return tuple(offspring1), tuple(offspring2)
