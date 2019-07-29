from itertools import permutations


def fonction_objective(pwd,liste):
	p,w,d = pwd
	s = c = 0
	for x in liste:
		c += p[x]
		s += max(0,c-d[x])*w[x]
	return s


def resolve_n_fact(pwdx):
	n = len(pwdx[0])
	indices = range(n)
	l_best = []
	p_best = float("inf")
	for permut in permutations(indices):
		p = fonction_objective(pwdx,list(permut))			
		if p < p_best:
			p_best = p
			l_best = list(permut)
	return l_best,p_best

