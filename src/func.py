"""
Module that contains useful functions that generate problem's data
or manipulate problems data's files
"""

import random
import time


def generate_pwd(problems_number: int):
    """
    Generate data of a problem P, W, D
    """
    p_time, weight_p, d_limit = [], [], []
    for i in range(problems_number):
        p_time.append(random.randint(1, 100))
        weight_p.append(random.randint(1, 10))
    total_time = sum(p_time)
    for i in range(problems_number):
        min_limit = max(p_time[i], int(0.2 * total_time))
        max_limit = max(int(0.6 * total_time), p_time[i])
        d_limit.append(random.randint(min_limit, max_limit))
    return p_time, weight_p, d_limit


# ---------------------- FILE SCAN FUNCTIONS -------------------------------


def scan(file_name='problem_in.txt', sep='\n'):
    """
    Function that read problem data from file
    """
    def list_from_str(string: str):
        return [int(c) for c in string.split(';')]

    file = open(file_name, 'r')

    lines = file.read().split(sep)
    for i, line in enumerate(lines):
        lines[i] = line.strip().replace(' ', '')

    problems_number = 1
    i = 0
    if lines[0].isdigit():
        problems_number = int(lines[0])
        i = 1

    pwds = []
    for _ in range(problems_number):
        pwds.append([])

    for problem_i in range(problems_number):
        i_minus3 = i
        while i - 3 < i_minus3:
            if ";" in lines[i]:
                pwds[problem_i].append(list_from_str(lines[i]))
                i += 1

    file.close()

    i = file_name.rindex(".")
    file_out = file_name[:i] + "_solution.txt"
    return pwds, file_out


def generate_file_pwd(problems_number=10, number_pwd=1):
    """
    Function that generate problem data and store it in a file
    """
    file_name = "problems__" + time.strftime("%Y_%b_%d__%H_%M_%S", time.gmtime()) + ".txt"
    new_file = open(file_name, "w")
    new_file.write(str(number_pwd) + "\n")
    for _ in range(number_pwd):
        pwd = generate_pwd(problems_number)
        for tab in pwd:
            new_file.write(";".join(str(x) for x in tab) + "\n")
        new_file.write("\n")
    new_file.close()
    return file_name


def write_to_file(file_out: str, results):
    """
    Function that write results in file
    """
    results_file = open(file_out, 'w')
    for i, (pwd, min_cost, ord_tasks) in enumerate(results):
        p_time, weight, d_limit = pwd
        results_file.write("Probleme numero " + str(i + 1) + "\n")
        results_file.write("p = " + str(p_time) + "\n")
        results_file.write("w = " + str(weight) + "\n")
        results_file.write("d = " + str(d_limit) + "\n\n")
        results_file.write("Ordon_optimal    = " + str(ord_tasks) + "\n")
        results_file.write("penalite_minimal = " + str(min_cost) + "\n")
        results_file.write("-" * 80 + "\n\n")

    results_file.close()
