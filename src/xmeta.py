import time
import random
from func import *
import main

def echange(maliste, i, j):
	l = maliste[:]
	l[i], l[j] = l[j], l[i]
	return l

def right_pivot(liste):
	for i in range(1,len(liste)-1):
		yield (liste[:i] + liste[i:][::-1])

def left_pivot(liste):
	for i in range(2,len(liste)):
		yield (liste[:i][::-1] + liste[i:])

def inversion(liste):
	mini = maxi = 0
	while abs(mini-maxi)<2:
		mini = random.randint(1, len(liste) - 2)
		maxi = random.randint(2, len(liste) - 1)
	if mini>maxi:
		mini, maxi = maxi, mini

	l_between = liste[mini:maxi][::-1]
	l_min = liste[0:mini]
	l_max = liste[maxi:]
	l = l_min+l_between+l_max
	assert len(l)==len(liste)
	return l

def inversion_liste(liste):
	tot=[]
	i = 0
	while i < len(liste)-2:
		l = inversion(liste)
		if l not in tot:
			tot.append(l)
			i+=1
	return tot

def swap_op(liste):
	for i in range(len(liste)-1):
		for j in range(i+1,len(liste)):
			yield (echange(liste, i, j))

neighborhood_structures = [right_pivot,inversion_liste,left_pivot,swap_op]

def fonction_objective(pwd,liste):
	p,w,d = pwd
	s = c = 0
	for x in liste:
		c = c + p[x]
		s = s + max(0,c-d[x])*w[x]
	return s


# #####################################################
def shaking(x,k=0):
	liste_x_prime = list(neighborhood_structures[k](x))	# N_k(x)
	index_x_prime = random.randint(0,len(liste_x_prime)-1) # random index
	
	x_prime = liste_x_prime[index_x_prime] # prend la valeur de l'index generer par random
	return x_prime

def reduced_vns(pwd,x=[],time_to_run=0.1): # le temps sera 0.1 second par defaut si on n'a pas entrer le temps
	# Initialization
	# si x est vide <=> [] alors on genere x par random
	if x==[]:
		p,w,d = pwd
		n = len(p) # le nombre des taches
		indices = range(n)
		x = indices
		# initial solution x
		random.shuffle(x)
	
	k_max = len(neighborhood_structures)-1 # tous les structures de voisinage sauf la derniere

	x_value = fonction_objective(pwd,x)
	
	stopping_condition = False
	start_time = time.time() # on prend le temps avant de debuter
	while stopping_condition == False:
		k = 0
		while k != k_max:
			x_prime = shaking(x,k) # generer x_prime appartient a N_k(x)
			x_prime_value = fonction_objective(pwd,x_prime)
			if x_prime_value < x_value:
				x = x_prime
				x_value = x_prime_value
				k = 0
			else:
				k = k + 1

			if time.time() - start_time > time_to_run:
				stopping_condition = True
				break
	return x,x_value

def general_vns(pwd,x=[],time_to_run=0.9,time_to_run_reduced_vns=0.1): # le temps sera 0.9 second par defaut si on n'a pas entrer le temps
	# Initialization
	# si x est vide <=> [] alors on genere x par random
	if x==[]:
		p,w,d = pwd
		n = len(p) # le nombre des taches
		indices = range(n)
		x = indices
		# initial solution x
		random.shuffle(x)
	
	k_max = len(neighborhood_structures) # tous les structures de voisinage
	l_max = len(neighborhood_structures) - 1  # tous les structures de voisinage sauf la derniere

	# improve x by using RVNS <=> reduced_vns()
	x , x_value = reduced_vns(pwd,x,time_to_run_reduced_vns)
	
	stopping_condition = False
	start_time = time.time() # on prend le temps avant de debuter
	while stopping_condition == False:
		k = 0
		while k != k_max and stopping_condition == False:
			x_prime = shaking(x,k) # generer x_prime appartient a N_k(x)
			x_prime_value = fonction_objective(pwd,x_prime)
			# local search by VND
			l = 0
			while l != l_max and stopping_condition == False:
				x_second = []
				x_second_value = float("inf")
				# Exploration of neighborhood
				for current_x_second in neighborhood_structures[l](x_prime):
					current_x_second_value = fonction_objective(pwd,current_x_second)
					if current_x_second_value < x_second_value:
						x_second = current_x_second
						x_second_value = current_x_second_value

					if time.time() - start_time > time_to_run:
						stopping_condition = True
						break
				if x_second_value < x_prime_value:
					x_prime = x_second
					x_prime_value = x_second_value
					l = 0
				else:
					l = l + 1

			if x_prime_value < x_value:
				x = x_prime
				x_value = x_prime_value
				k = 0
			else:
				k = k + 1

	return x,x_value





if __name__=="__main__":

	n = input("Entrer le nombre des taches N : ")
	pwd = generatePWD(n)	

	print("general_vns")
	x = range(n)
	debut = time.time()
	oov,pnv =  general_vns(pwd,x,0.45,0.05)
	fin = time.time()

	if n<=20:
		ret = main.main(pwd)
		res = ret[1:][::-1]
		print(res[0],res[1])
	else:
		pass
		# printPWD(pwd)
	print(oov)
	print(pnv)
	print()
	print(fin - debut)


