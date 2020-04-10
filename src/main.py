# -*- coding: utf-8 -*-


from func import *
from dynamique import *


def main(pwd=None, n=-1):
    if n > 0:
        pwd = generatePWD_simple(n)

    p, w, d = pwd
    pmd, ood = dynamique(p, w, d)

    return pwd, pmd, ood


if __name__ == "__main__":

    np = 1
    generer = int(input("Voulez generer un fichier (Enrer 1) ou tapez le nom d'un fichier (Entrer 2) : "))
    if generer == 1:
        ng = int(input("Donner le nombre des taches n : "))

        nom_ficher = generate_file_pwd(ng, np)
        print("Le Probleme est dans le fichier", nom_ficher)
    else:
        nom_ficher = input("Entrer le nom du fichier : ")
    pwds, file_out = scan(nom_ficher)
    print("La solution sera dans le fichier", end=" ")
    resultats = map(main, pwds)

    write_to_file(file_out, resultats)
