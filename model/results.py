from model.genetic_algorithm import genetic_algorithm


def results(
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
):

    best_individual, best_fitness, best_fitness_over_time, avg_hist = genetic_algorithm(
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

    return best_individual, best_fitness
