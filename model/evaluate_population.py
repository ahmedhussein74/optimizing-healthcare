import numpy as np
from model.objective_with_penalties import objective_with_penalties


def evaluate_population(
    population, Wit, Iijt, Cpt, Drt, Ppt, Oi, Up, Si, D_t, Hi, Mipkt, Fij, C_penalty, B
):
    fitness_values = []
    for individual in population:
        x, y, z, o, v = individual
        fitness = objective_with_penalties(
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
        )
        fitness_values.append(fitness)
    return np.array(fitness_values)
