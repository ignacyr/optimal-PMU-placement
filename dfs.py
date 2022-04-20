import numpy as np


def dfs(adjacency_m):
    num_buses = adjacency_m[:1].size
    x = np.zeros(num_buses)
    in_degree = np.sum(adjacency_m, axis=1)
    for k in range(num_buses):
        index = np.argmax(in_degree)  # zmniejszyć do jednego elementu chyba trzeba
        x[index] = 1
        f = np.dot(adjacency_m, x)
        if ~np.any(f < 1):
            break
        in_degree[index] = 0
        for i in range(num_buses):
            if adjacency_m[index, i] == 0 or in_degree[i] == 0:
                continue
            in_degree[i] = 0
            for j in range(num_buses):
                if adjacency_m[i, j] == 0 or f[j] > 0:
                    continue
            in_degree[i] = in_degree[i] + 1
    placement = np.argwhere(x == 1) + 1
    return placement





