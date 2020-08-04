"""
The knapsack problem or rucksack problem is a problem in combinatorial optimization: Given a set of items,
each with a weight and a value, determine the number of each item to include in a collection so that the total
weight is less than or equal to a given limit and the total value is as large as possible. It derives its name
from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most
valuable items.
"""


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def knapsack_solver(values, weights, n, capacity):
    @memoize
    def solver(rem_capacity, i=0):
        if i == n or rem_capacity - weights[i] < 0:
            return 0

        possibility1 = solver(rem_capacity, i + 1)
        possibility2 = values[i] + solver(rem_capacity - weights[i], i + 1)

        if possibility1 > possibility2:
            return possibility1
        else:
            return possibility2

    return solver(capacity)


if __name__ == "__main__":
    values = [2, 3, 5, 1, 5]
    weights = [4, 2, 6, 1, 2]
    capacity = 10
    n = len(values)

    optimal_items = knapsack_solver(values, weights, n, capacity)
    print(optimal_items)
