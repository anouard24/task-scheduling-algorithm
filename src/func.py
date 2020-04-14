import random
import time


def generatePWD_simple(n):
    """	GENERER P,W,D du professeur
        """
    p, w, d = [], [], []
    for i in range(n):
        p.append(random.randint(1, 100))
        w.append(random.randint(1, 10))
    Ep = sum(p)
    for i in range(n):
        d.append(random.randint(int(0.2 * Ep), int(0.6 * Ep)))
    return p, w, d


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


def generatePWD_nozero(n):
    """	GENERER P,W,D avec les pire des cas
        """
    p, w, d = [], [], []
    for i in range(n):
        p.append(random.randint(2, 100))
        w.append(random.randint(1, 10))
    for i in range(n):
        d.append(random.randint(1, p[i] - 1))
    return p, w, d


def generatePWD_zeros(n):
    """	GENERER P,W,D avec des cas en moyenne
        """
    p, w, d = [], [], []
    for i in range(n):
        p.append(random.randint(1, 100))
        w.append(random.randint(1, 10))
    Ep = sum(p)
    for i in range(n):
        d.append(random.randint(int(2 * p[i]), max(2 * p[i], Ep)))
    return p, w, d


def generatePWD_best_cases(n):
    """	GENERER P,W,D avec des bon cas <=> penalite minimal = 0
        """
    p, w, d = [], [], []
    for i in range(n):
        p.append(random.randint(1, 100))
        w.append(random.randint(1, 10))
    Ep = sum(p)
    for i in range(n):
        d.append(Ep + p[i])
    return p, w, d


# ---------------------- FILE SCAN FUNCTIONS -------------------------------
def supespace(s):
    return s.replace(" ", "").replace("\t", "")


def listFromStr(string):
    return [int(c) for c in string.split(';')]


def scan(f="pwdin.txt", dir=".", sep="\n"):
    fin = open(f, "r")
    donnee = fin.read()
    lignes = donnee.split(sep)
    lignes = [s for s in map(supespace, lignes) if s != ""]
    for i in range(len(lignes)):
        lignes[i].replace("\r", "")

    nx = 1
    if lignes[0].isdigit():
        n = int(lignes[0])
        nx = 2

    pwds = []
    for k in range(n):
        pwds.append([])
    ip = 0
    i = 0 + 1 * (nx > 1)
    while i - 2 < len(lignes) and ip < n:
        if ";" in lignes[i]:
            pwds[ip].append(listFromStr(lignes[i]))
        if ";" in lignes[i + 1]:
            pwds[ip].append(listFromStr(lignes[i + 1]))
        if ";" in lignes[i + 2]:
            pwds[ip].append(listFromStr(lignes[i + 2]))
        ip += 1
        i += 3
    fin.close()

    i = len(f) - f[::-1].index(".")
    file_out = f[:i - 1] + "_solution.txt"
    return pwds, file_out


def generate_file_pwd(n=10, number_pwd=1):
    nom_du_fichier = "problems__" + time.strftime("%Y_%b_%d__%H_%M_%S", time.gmtime()) + ".txt"
    fichier_cree = open(nom_du_fichier, "w")
    fichier_cree.write(str(number_pwd) + "\n")
    for i in range(number_pwd):
        pwd = generatePWD_simple(n)
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
