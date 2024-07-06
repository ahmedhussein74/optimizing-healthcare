def compute_term2(x, Iijt):
    N, T = x.shape
    term2 = 0
    for i in range(N):
        for j in range(N):
            for t in range(T):
                term2 += Iijt[i, j, t] * x[i, t] * x[j, t]
    return term2
