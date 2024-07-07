import numpy as np
from model.generate_random_matrix import generate_random_matrix


def init_params(
    N, T, P, R, K, M_min, M_max, H_min, H_max, D_min, D_max, F_min, F_max, seed
):

    if seed is not None:
        np.random.seed(seed)

    # Initialize Wit (Weight Variable) - dimensions: N x T
    Wit = np.random.rand(N, T)

    # Initialize Iijt (Interaction Weight Variable) - dimensions: N x N x T
    Iijt = np.random.rand(N, N, T)

    # Initialize Cpt (Cost Variable) - dimensions: P x T
    Cpt = np.random.rand(P, T)

    # Initialize Drt (Cost Variable) - dimensions: R x T
    Drt = np.random.rand(R, T)

    # Initialize Ppt (Penalty Variable) - dimensions: P x T
    Ppt = np.random.rand(P, T)

    # Initialize Oi (Overtime Weight Variable) - dimensions: N
    Oi = np.random.rand(N)

    # Initialize Up (Weight Variable) - dimensions: P
    Up = np.random.rand(P)

    # Initialize Si (Skill Level Variable) - dimensions: N
    Si = np.random.rand(N)

    Mipkt = generate_random_matrix(
        (N, P, K, T), M_min, M_max, seed
    )  # Task matching weights
    Hi = generate_random_matrix((N), H_min, H_max, seed)  # Staff hours
    D_t = generate_random_matrix((T), D_min, D_max, seed)  # Total demand per time slot
    Fij = generate_random_matrix((N, N), F_min, F_max, seed)  # Staff familiarity

    return Wit, Iijt, Cpt, Drt, Ppt, Oi, Up, Si, Mipkt, Hi, D_t, Fij
