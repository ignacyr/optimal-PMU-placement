# Run this script if you want to calculate number of possible combinations of PMU placement in the power system.
import math
import numpy as np
import matplotlib.pyplot as plt


# Calculate number of combinations of PMU placement in the power system (n - number of buses)
def calc_combs(n):
    combinations = 0
    for k in range(n+1):
        combinations = combinations + math.factorial(n+1) / (math.factorial(n+1 - (k+1)) * math.factorial(k+1))
    return combinations


# Calculate number of combinations of PMU placement in range from 1 to max_n buses
def calc_combs_in_range(max_n):
    combs_in_range = np.zeros(max_n, dtype='object')
    for n in range(max_n):
        combs_in_range[n] = calc_combs(n)
    return combs_in_range  # return array of possible combinations for from 1 to max_n buses


def main():
    max_buses = 50

    combinations_in_range = calc_combs_in_range(max_buses)

    print(combinations_in_range)

    plt.plot(combinations_in_range)
    plt.show()

    # x = calc_poss(1000)
    # print(x)


if __name__ == '__main__':
    main()
