"""
Module provides functions to solve the task scheduling problem
using dynamic programming approach
Time complexity: O(N*(2^N))
"""

from itertools import combinations


def dynamique(p, w, d):
    """
    Function that return one of best possible ordred tasks
    Space complexity: O(N)
    """
    n = len(p)
    indices = tuple(range(n))
    dictionary = temp_dictionary = {}
    dictionary[()] = (0, [], 0)
    for n_i in range(1, n + 1):
        for current_tasks in combinations(indices, n_i):
            min_penalty = float("inf")
            best_sequence = []
            cost = 0
            for k, r in enumerate(combinations(current_tasks, n_i - 1)):
                j = current_tasks[n_i - k - 1]
                fa, fr, cost = dictionary.get(r, None)
                cost += p[j]
                ff = fa + max(0, cost - d[j]) * w[j]
                if ff < min_penalty:
                    min_penalty = ff
                    best_sequence = fr + [j]
                    if ff == 0:
                        break
            temp_dictionary[current_tasks] = (min_penalty, best_sequence, cost)
        dictionary = temp_dictionary
        temp_dictionary = dict()

    return dictionary.get(indices, None)[:2]


def dynamique_all(p, w, d):
    """
    Function that return all possible best ordered tasks
    Space complexity: O(N!)
    """
    n = len(p)
    indices = tuple(range(n))
    dictionary = temp_dictionary = {}
    dictionary[()] = (0, [[]], 0)

    for n_i in range(1, n + 1):
        for current_tasks in combinations(indices, n_i):
            min_penalty = float("inf")
            all_sol = []
            cost = 0
            for k, r in enumerate(combinations(current_tasks, n_i - 1)):
                j = current_tasks[n_i - k - 1]
                fa, fr, cost = dictionary.get(r, None)
                cost += p[j]
                ff = fa + max(0, cost - d[j]) * w[j]
                if ff <= min_penalty:
                    if ff < min_penalty:
                        all_sol = []
                        min_penalty = ff
                    for old_sol in fr:
                        all_sol.append(old_sol + [j])
            temp_dictionary[current_tasks] = (min_penalty, all_sol, cost)
        dictionary = temp_dictionary
        temp_dictionary = dict()

    return dictionary.get(indices, None)[:2]
