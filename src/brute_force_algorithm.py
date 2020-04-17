"""
Module provides functions to solve the task scheduling problem
in naive method (Brute force search)
Time complexity: O(N!)
Space complexity: O(N)
"""

from itertools import permutations

from func import penalty_of_tasks


def resolve_brute_force(pwd):
    """
    Function to generate and test all possible permutations of tasks
    and return the last best solution with the minimum possible penalty
    params:
        pwd: multi-dimensional list [P, W, D] that contain:
            - P Execution time
            - W Weight penalty
            - D Date limit
    """
    tasks_number = len(pwd[0])
    indexes = range(tasks_number)

    best_order_tasks = []
    min_penalty = float("inf")

    for tasks in permutations(indexes):
        current_penalty = penalty_of_tasks(pwd, list(tasks))
        if current_penalty < min_penalty:
            min_penalty = current_penalty
            best_order_tasks = list(tasks)

    return best_order_tasks, min_penalty
