def get_best_individual(best_individual):
    x, y, z, o, v = best_individual
    return {
        "x": x.tolist(),
        "y": y.tolist(),
        "z": z.tolist(),
        "o": o.tolist(),
        "v": v.tolist(),
    }
