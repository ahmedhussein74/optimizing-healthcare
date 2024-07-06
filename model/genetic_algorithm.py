import numpy as np
from model.init_params import init_params
from model.init_population import init_population
from model.bitwise_mutation import bitwise_mutation
from model.one_point_crossover import one_point_crossover
from model.evaluate_population import evaluate_population
from model.linear_ranking_selection import linear_ranking_selection


def genetic_algorithm(
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
    population = init_population(pop_size, N, T, P, R, K, seed)

    Wit, Iijt, Cpt, Drt, Ppt, Oi, Up, Si, Mipkt, Hi, D_t, Fij = init_params(
        N, T, P, R, K, M_min, M_max, H_min, H_max, D_min, D_max, F_min, F_max, seed
    )

    best_fitness_over_time = []
    avg_hist = np.zeros(generations)
    for generation in range(generations):
        fitness = evaluate_population(
            population,
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
            Fij,
            C_penalty,
            B,
        )
        best_fitness_over_time.append(np.min(fitness))
        avg_hist[generation] = np.mean(fitness)

        selected_population = linear_ranking_selection(
            population, fitness, pop_size // 2, SP=1.5
        )

        new_population = []
        for i in range(0, len(selected_population), 2):
            parent1 = selected_population[i]
            parent2 = selected_population[(i + 1) % len(selected_population)]
            offspring1, offspring2 = one_point_crossover(
                parent1, parent2, crossover_rate
            )
            new_population.extend([offspring1, offspring2])

        mutated_population = [
            bitwise_mutation(individual, mutation_rate) for individual in new_population
        ]
        population = mutated_population

    final_fitness = evaluate_population(
        population,
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
        Fij,
        C_penalty,
        B,
    )
    best_individual_index = np.argmin(final_fitness)
    best_individual = population[best_individual_index]
    best_fitness = final_fitness[best_individual_index]

    return best_individual, best_fitness, best_fitness_over_time, avg_hist
