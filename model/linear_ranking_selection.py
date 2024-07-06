import numpy as np


def linear_ranking_selection(population, fitness, num_select, SP=1.5):
    # Step 1: Rank individuals based on fitness (lower fitness is better)
    sorted_indices = np.argsort(
        fitness
    )  # Sort fitness in ascending order for minimization
    ranks = np.empty_like(sorted_indices)
    ranks[sorted_indices] = np.arange(
        len(fitness), 0, -1
    )  # Assign ranks from N to 1,N being the highest rank

    # Step 2: Calculate rank-based fitness
    N = len(fitness)
    rank_fitness = (2 - SP) + 2 * (SP - 1) * (ranks - 1) / (N - 1)

    # Step 3: Apply roulette wheel selection using rank-based fitness
    total_rank_fitness = np.sum(rank_fitness)
    probabilities = rank_fitness / total_rank_fitness
    cumulative_probabilities = np.cumsum(probabilities)

    selected_population = []
    for _ in range(num_select):
        random_num = np.random.random()
        for i, cum_prob in enumerate(cumulative_probabilities):
            if random_num <= cum_prob:
                selected_population.append(population[i])
                break

    return selected_population
