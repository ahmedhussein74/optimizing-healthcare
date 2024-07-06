from model.get_best_individual import get_best_individual


def get_final_results(best_individual, best_fitness):
    individual = get_best_individual(best_individual)
    return {"best_fitness": best_fitness, "best_individual": individual}
