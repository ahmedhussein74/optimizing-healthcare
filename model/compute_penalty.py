import numpy as np


def compute_penalty(violations, C, k=2):
    total_penalty = 0
    for i, violation in enumerate(violations):
        total_penalty += C[i] * np.sum(violation**k)
    return total_penalty
