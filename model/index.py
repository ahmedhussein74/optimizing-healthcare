from model.results import results
from model.get_final_results import get_final_results


def GA(
    n, t, p, r, k, b, m_min, m_max, h_min, h_max, d_min, d_max, f_min, f_max, seed2
):
    pop_size = 50
    generations = 100
    mutation_rate = 0.01
    crossover_rate = 0.7
    C_penalty = [0.25, 0.2, 0.15, 0.12, 0.1, 0.08, 0.06, 0.04]

    N = n
    T = t
    P = p
    R = r
    K = k
    B = b
    M_min = m_min
    M_max = m_max
    H_min = h_min
    H_max = h_max
    D_min = d_min
    D_max = d_max
    F_min = f_min
    F_max = f_max
    seed = seed2

    best_individual, best_fitness = results(
        pop_size,
        N,
        T,
        P,
        R,
        K,
        generations,
        crossover_rate,
        mutation_rate,
        seed,
        C_penalty,
        B,
        M_min,
        M_max,
        H_min,
        H_max,
        D_min,
        D_max,
        F_min,
        F_max,
    )

    return get_final_results(best_individual, best_fitness)
