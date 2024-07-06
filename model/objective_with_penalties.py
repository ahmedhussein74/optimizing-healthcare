from model.compute_penalty import compute_penalty
from model.compute_objective import compute_objective
from model.compute_violations import compute_violations


def objective_with_penalties(
    x,
    y,
    z,
    o,
    v,
    Wit,
    Iijt,
    Cpt,
    Drt,
    Ppt,
    Oi,
    Up,
    Si,
    D_t,
    Hi,
    Mipkt,
    B,
    Fij,
    C_penalty,
    k=2,
):

    objective_value = compute_objective(
        x, y, z, o, v, Wit, Iijt, Cpt, Drt, Ppt, Oi, Up, Si
    )

    # Compute violations
    violations = compute_violations(
        x, y, z, o, v, Drt, D_t, Hi, Si, Mipkt, Oi, Wit, B, Fij
    )

    # Compute total penalty
    total_penalty = compute_penalty(violations, C_penalty, k)

    # Penalized fitness function
    penalized_fitness = objective_value + total_penalty

    return penalized_fitness
