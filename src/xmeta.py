import random
import time

from func import generate_pwd, penalty_of_tasks


def swapped(tasks, i, j):
    new_tasks = tasks[:]
    new_tasks[i], new_tasks[j] = new_tasks[j], new_tasks[i]
    return new_tasks


def right_pivot(tasks):
    for i in range(1, len(tasks) - 1):
        yield list(tasks[:i] + tasks[i:][::-1])


def left_pivot(tasks):
    for i in range(2, len(tasks)):
        yield list(tasks[:i][::-1] + tasks[i:])


def inversion(tasks):
    mini = maxi = 0
    while abs(mini - maxi) < 2:
        mini = random.randint(1, len(tasks) - 2)
        maxi = random.randint(2, len(tasks) - 1)

    if mini > maxi:
        mini, maxi = maxi, mini

    tasks_between_reversed = tasks[mini:maxi][::-1]
    l_min = tasks[:mini]
    l_max = tasks[maxi:]

    new_tasks = list(l_min + tasks_between_reversed + l_max)

    assert len(new_tasks) == len(tasks)

    return new_tasks


def inversion_tasks(tasks):
    list_of_tasks = []
    i = 0
    while i < len(tasks) - 2:
        new_tasks = inversion(tasks)
        if new_tasks not in list_of_tasks:
            list_of_tasks.append(new_tasks)
            i += 1
    return list_of_tasks


def swap_op(tasks):
    for i in range(len(tasks) - 1):
        for j in range(i + 1, len(tasks)):
            yield swapped(tasks, i, j)


NEIGHBORHOOD_STRUCTURES = [right_pivot, inversion_tasks, left_pivot, swap_op]


def shaking(tasks, k=0):
    neighborhood_function = NEIGHBORHOOD_STRUCTURES[k]
    tasks_x_prime = list(neighborhood_function(tasks))

    index_x_prime = random.randint(0, len(tasks_x_prime) - 1)

    x_prime = tasks_x_prime[index_x_prime]
    return x_prime


def reduced_vns(pwd, tasks=None, time_to_run=0.1):
    if not tasks:
        tasks_number = len(pwd[0])
        indices = range(tasks_number)
        tasks = indices
        random.shuffle(tasks)  # initial solution

    k_max = len(NEIGHBORHOOD_STRUCTURES) - 1  # all neighborhood structures except the last

    x_min_cost = penalty_of_tasks(pwd, tasks)

    stopping_condition = False
    start_time = time.time()  # take the time before start

    while not stopping_condition:
        k = 0
        while k != k_max:
            x_prime = shaking(tasks, k)  # generate x_prime from the k-th neighborhood structures

            x_prime_cost = penalty_of_tasks(pwd, x_prime)

            if x_prime_cost < x_min_cost:
                tasks = x_prime
                x_min_cost = x_prime_cost
                k = 0
            else:
                k = k + 1

            if time.time() - start_time > time_to_run:
                stopping_condition = True
                break

    return tasks, x_min_cost


def general_vns(pwd, tasks=None, time_to_run=0.9, time_to_run_reduced_vns=0.1):
    if not tasks:
        tasks_number = len(pwd[0])
        indices = range(tasks_number)
        tasks = indices
        random.shuffle(tasks)  # initial solution

    k_max = len(NEIGHBORHOOD_STRUCTURES)  # all neighborhood structures
    l_max = len(NEIGHBORHOOD_STRUCTURES) - 1  # all neighborhood structures except the last

    # improve x by using Reduced VNS <=> reduced_vns()
    tasks, x_cost = reduced_vns(pwd, tasks, time_to_run_reduced_vns)

    stopping_condition = False
    start_time = time.time()  # take the time before start
    while not stopping_condition:
        k = 0
        while k != k_max and stopping_condition is False:
            x_prime = shaking(tasks, k)  # generate x_prime from the k-th neighborhood structures
            x_prime_cost = penalty_of_tasks(pwd, x_prime)
            # local search by VND
            cpt_l = 0
            while cpt_l != l_max and stopping_condition is False:
                x_second = []
                x_second_cost = float("inf")

                # Exploration of neighborhood
                for current_x_second in NEIGHBORHOOD_STRUCTURES[cpt_l](x_prime):

                    current_x_second_value = penalty_of_tasks(pwd, current_x_second)

                    if current_x_second_value < x_second_cost:
                        x_second = current_x_second
                        x_second_cost = current_x_second_value

                    if time.time() - start_time > time_to_run:
                        stopping_condition = True
                        break

                if x_second_cost < x_prime_cost:
                    x_prime = x_second
                    x_prime_cost = x_second_cost
                    cpt_l = 0
                else:
                    cpt_l = cpt_l + 1

            if x_prime_cost < x_cost:
                tasks = x_prime
                x_cost = x_prime_cost
                k = 0
            else:
                k = k + 1

    return tasks, x_cost


if __name__ == "__main__":
    NUMBER_OF_TASKS = int(input("Enter number of tasks N to generate: "))
    PWD = generate_pwd(NUMBER_OF_TASKS)

    print("general_vns")
    TASKS = list(range(NUMBER_OF_TASKS))

    START_TIME = time.time()
    ORDERED_TASKS, MIN_PENALTY = general_vns(PWD, TASKS, 0.45, 0.05)
    END_TIME = time.time()

    print(ORDERED_TASKS)
    print(MIN_PENALTY)
    print()
    print(END_TIME - START_TIME)
