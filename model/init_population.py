from model.init_decision_variables import init_decision_variables


def init_population(pop_size, N, T, P, R, K, seed=None):
    population = []
    for _ in range(pop_size):
        x, y, z, o, v = init_decision_variables(N, T, P, R, K, seed)
        population.append((x, y, z, o, v))
    return population
