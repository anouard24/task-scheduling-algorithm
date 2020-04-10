"""
Module provides functions to solve the task scheduling problem
in naive method (Brute force search)
Time complexity: O(N!)
Space complexity: O(N)
"""

from itertools import permutations


def penalty_of_tasks(pwd, tasks):
    """
    Function to calculate cost of a given order of task
    params:
        pwd: multi-dimensional list [P, W, D] that contain:
            - P Execution time
            - W Weight penalty
            - D Date limit
        tasks: task indices
    """

    execution_time, weight_penalty, date_limit = pwd

    sum_cost = cost = 0

    for task in tasks:
        cost += execution_time[task]
        sum_cost += max(0, cost - date_limit[task]) * weight_penalty[task]

    return sum_cost


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
