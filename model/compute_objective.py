import numpy as np
from model.compute_term2 import compute_term2


def compute_objective(x, y, z, o, v, Wit, Iijt, Cpt, Drt, Ppt, Oi, Up, Si):
    """
    Computes the objective value based on the given decision variables and weights.
    Args:
        x (numpy.ndarray): Staff assignments binary matrix with dimensions (N, T).
        y (numpy.ndarray): Patient scheduling binary matrix with dimensions (P, T).
        z (numpy.ndarray): Resource allocation binary matrix with dimensions (R, T).
        o (numpy.ndarray): Overtime binary vector with length N.
        v (numpy.ndarray): VIP (Staff serving patients) binary matrix with dimensions (N, P).
        W (numpy.ndarray): Staff assignment weights matrix with dimensions (N, T).
        I (numpy.ndarray): Interaction weights between staff members tensor with dimensions (N, N, T).
        C (numpy.ndarray): Patient scheduling weights matrix with dimensions (P, T).
        D (numpy.ndarray): Resource allocation weights matrix with dimensions (R, T).
        P (numpy.ndarray): Penalty weights matrix with dimensions (P, T).
        O (numpy.ndarray): Overtime weights vector with length N.
        U (numpy.ndarray): Not receiving service weights matrix with dimensions (N, P).
        S (numpy.ndarray): Skill level weights matrix with dimensions (N, T).
    Returns:
        float: Objective value.
    """
    N, T = x.shape
    P = y.shape[0]
    # Compute each term of the objective function
    term1 = np.sum(Wit * x)
    term2 = compute_term2(x, Iijt)
    term3 = np.sum(Cpt * y)
    term4 = np.sum(Drt * z)
    term5 = np.sum(Ppt * y)
    term6 = np.sum(Oi * o)
    term7 = np.sum(Up * v)
    term8 = np.sum(Si[:, np.newaxis] * x)

    # Combine all terms to get the objective value
    objective_value = term1 + term2 + term3 + term4 + term5 + term6 + term7 + term8
    return objective_value
