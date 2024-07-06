from model.generate_binary_matrix import generate_binary_matrix
from model.generate_binary_vector import generate_binary_vector


def init_decision_variables(N, T, P, R, K, seed=None):
    """
    Initializes decision variable matrices for a given optimization problem.
    Args:
        N (int): Number of staff members.
        T (int): Number of time slots.
        P (int): Number of patients.
        R (int): Number of resources.
        K (int): Number of taskes.
        seed (int, optional): Seed for the random number generator.
    Returns:
        numpy.ndarray:
            - x: Staff assignments Binary matrix with dimensions(N,T)
            - y: Patient scheduling Binary matrix with dimensions(P,T)
            - z: Resource allocation Binary matrix with dimensions(R,T)
            - o: Overtime (binary vector) with length N
            - v: VIP (Staff serving patients) Binary matrix with dimensions(N,P)
    """
    # Initialize decision variable matrices
    x = generate_binary_matrix(N, T, seed)  # Staff assignments
    y = generate_binary_matrix(P, T, seed)  # Patient scheduling
    z = generate_binary_matrix(R, T, seed)  # Resource allocation
    o = generate_binary_vector(N, seed)  # Overtime
    v = generate_binary_matrix(N, P, seed)  # VIP (Staff serving patients)
    return x, y, z, o, v
