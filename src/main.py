# -*- coding: utf-8 -*-

from multiprocessing import Process,Pool

from func import *
from dynamique import *
import time



def main(pwd=[[],[],[]],n=-1):

	if n>0:
		pwd = generatePWD_simple(n)
		# pwd = generatePWD_nozero(n)
	
	# p = [45, 57, 28, 71, 99, 5, 16]
	# w = [6, 5, 9, 5, 9, 10, 8]
	# d = [188, 177, 96, 104, 100, 132, 167]
	
	# pwd = p,w,d

	n = len(pwd[0])
	
	# printPWD(pwd)
	p,w,d = pwd

	# print "p =",p
	# print "w =",w
	# print "d =",d

	start_time = time.time()
	# (pmd,ood),dico = resolve_dyna_it_all(pwd)
	(pmd,ood) = dynamique(p,w,d)
	end_time = time.time()
	# print "Ordon.optimal    : {}\npenalite minimal : {}\n".format(ood,pmd)
	# print "%d taches : Temps d execution : %s secondes --- dp method" % (n,(end_time - start_time))


	# start_time = time.time()
	# (pmd,ood),list_dico = resolve_dyna_it_all((p,w,d))
	# # (pm,oo) = resolve_dyna_it_all((p,w,d))
	# end_time = time.time()
	# print "Ordon.optimal    : {}\npenalite minimal : {}\n".format(ood,pmd)

	# print "%d taches : Temps d execution : %s secondes --- n! method" % (n,(time.time() - start_time))
	# letage = []
	# for pnn,oon,cout in list_all_f:
	# 	le = len(oon[0])
	# 	if le not in letage:
	# 		print "Etage numero ",len(oon[0])
	# 		letage.append(le)

	# 	for ooon in oon:
	# 		print "f",tuple(ooon)," = ",
	# 	print pnn

 # -----------------------------------------------------------

	


	# return end_time - start_time
	# return pwd,pmd,ood,dico_all
	return pwd,pmd,ood



# if __name__ == "__main__":
# 	ng = input("Donner le nombre des taches n : ")

# 	main(n=ng)
	# pwds,file_out = scan()
	# s = []

	# pl = Pool(4)
	# s = pl.map(main,pwds)
	# pl.close()
	# pl.join()

	# ht = open(file_out, 'w')
	# for i,(pwd,pmd,ood) in enumerate(s):
	# 	p,w,d = pwd
	# 	ht.write("Probleme numero "+str(i+1))
	# 	ht.write("\np = "+str(p)+"\n")
	# 	ht.write("w = "+str(w)+"\n")
	# 	ht.write("d = "+str(d)+"\n\n")
	# 	ht.write("Ordon_optimal    = "+str(ood)+"\n")
	# 	ht.write("penalite_minimal = "+str(pmd)+"\n")
	# 	ht.write("-"*80+"\n\n")

	# ht.close()



	# pl = Pool(4)
	# start_time = time.time()
	# ss = pl.map(main,scan())
	# pl.close()
	# pl.join()
	# end_time = time.time()



if __name__ == "__main__":
	# np = input("Donner le nombre des problemes : ")
	np = 1
	generer = int(input("Voulez generer un fichier (Enrer 1) ou tapez le nom d'un fichier (Entrer 2) : "))
	if generer == 1:
		ng = int(input("Donner le nombre des taches n : "))

		nom_ficher = generate_file_pwd(ng,np)
		print("Le Probleme est dans le fichier",nom_ficher)
	else:
		nom_ficher = input("Entrer le nom du fichier : ")
	pwds,file_out = scan(nom_ficher)
	print("La solution sera dans le fichier", end=" ")
	resultats = map(main,pwds)


	write_to_file(file_out,resultats)





