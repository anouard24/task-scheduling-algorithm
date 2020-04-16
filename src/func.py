import random
import time


def generatePWD(n):
    """	GENERER P,W,D general
        """
    p, w, d = [], [], []
    for i in range(n):
        p.append(random.randint(1, 100))
        w.append(random.randint(1, 10))
    Ep = sum(p)
    for i in range(n):
        d.append(random.randint(max(p[i], int(0.2 * Ep)), max(int(0.6 * Ep), p[i])))
    return p, w, d


# ---------------------- FILE SCAN FUNCTIONS -------------------------------


def scan(f='problem_in.txt', sep='\n'):
    def list_from_str(string: str):
        return [int(c) for c in string.split(';')]

    file = open(f, 'r')

    lines = file.read().split(sep)
    for i in range(len(lines)):
        lines[i] = lines[i].strip().replace(' ', '')

    n = 1
    i = 0
    if lines[0].isdigit():
        n = int(lines[0])
        i = 1

    pwds = []
    for _ in range(n):
        pwds.append([])

    for ip in range(n):
        ii = i
        while i - 3 < ii:
            if ";" in lines[i]:
                pwds[ip].append(list_from_str(lines[i]))
                i += 1

    file.close()

    i = f.rindex(".")
    file_out = f[:i] + "_solution.txt"
    return pwds, file_out


def generate_file_pwd(n=10, number_pwd=1):
    nom_du_fichier = "problems__" + time.strftime("%Y_%b_%d__%H_%M_%S", time.gmtime()) + ".txt"
    fichier_cree = open(nom_du_fichier, "w")
    fichier_cree.write(str(number_pwd) + "\n")
    for i in range(number_pwd):
        pwd = generatePWD(n)
        for tab in pwd:
            fichier_cree.write(";".join(str(x) for x in tab) + "\n")
        fichier_cree.write("\n")
    fichier_cree.close()
    return nom_du_fichier


def write_to_file(file_out, resultats):
    ht = open(file_out, 'w')
    for i, (pwd, pmd, ood) in enumerate(resultats):
        p, w, d = pwd
        ht.write("Probleme numero " + str(i + 1) + "\n")
        ht.write("p = " + str(p) + "\n")
        ht.write("w = " + str(w) + "\n")
        ht.write("d = " + str(d) + "\n\n")
        ht.write("Ordon_optimal    = " + str(ood) + "\n")
        ht.write("penalite_minimal = " + str(pmd) + "\n")
        ht.write("-" * 80 + "\n\n")

    ht.close()
