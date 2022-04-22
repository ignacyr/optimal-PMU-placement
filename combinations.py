import math
import numpy as np
import matplotlib.pyplot as plt


def factorial(n):
    return n*factorial(n-1) if n > 1 else 1


def calc_poss(n):
    possibilities = 0
    for k in range(n+1):
        possibilities = possibilities + math.factorial(n+1) / (math.factorial(n+1 - (k+1)) * math.factorial(k+1))
    return possibilities


def calc_poss_in_range(max_n):
    poss_in_range = np.zeros(max_n, dtype='object')
    for n in range(max_n):
        poss_in_range[n] = calc_poss(n)
    return poss_in_range


def main():
    max_nodes = 200

    # possibilities = np.zeros(nodes, dtype='object')

    possibilities_in_range = calc_poss_in_range(max_nodes)

    print(possibilities_in_range)

    plt.plot(possibilities_in_range)
    plt.show()

    # x = calc_poss(1000)
    # print(x)


if __name__ == '__main__':
    main()
