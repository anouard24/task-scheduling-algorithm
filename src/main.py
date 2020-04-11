# -*- coding: utf-8 -*-
"""
Main module that contains driver code to use the algorithm in an interactive mode
"""

from func import generate_file_pwd, scan, write_to_file
from dynamique import dynamique


def main(pwd):
    """
    Function that execute the dynamic algorithm and return the results
    """
    pmd, ood = dynamique(*pwd)

    return pwd, pmd, ood


if __name__ == "__main__":

    ACTION = input("1.Generate a file\n2.Enter file name\n[?] Your choice: ")

    if ACTION == '1':
        NG = int(input("Enter the number of tasks N: "))
        FILE_NAME = generate_file_pwd(NG)
        print("tasks data in file: ", FILE_NAME)
    else:
        FILE_NAME = input("Enter path to file name: ")

    LIST_PWD, FILE_OUT = scan(FILE_NAME)
    print("Solution will be in file: ", FILE_OUT)
    RESULTS = map(main, LIST_PWD)

    write_to_file(FILE_OUT, RESULTS)
