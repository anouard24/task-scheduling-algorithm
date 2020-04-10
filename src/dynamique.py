from itertools import combinations

def dynamique(p,w,d):
	n = len(p)
	indices = tuple(range(n))
	dictionary = temp_dictionary = {}
	dictionary[()] = (0,[],0)
	for n_i in range(1,n+1):
		for current_combin in combinations(indices,n_i):
			min_penalty = float("inf")
			best_sequence = []
			cout = 0
			for k,r in enumerate(combinations(current_combin,n_i-1)):
				j = current_combin[n_i-k-1]
				fa,fr,cout = dictionary.get(r)
				cout += p[j]
				ff = fa + max(0,cout-d[j])*w[j]
				if ff < min_penalty:
					min_penalty = ff
					best_sequence = fr + [j]
					if ff==0:
						break
			temp_dictionary[current_combin] = (min_penalty,best_sequence,cout)
		dictionary = temp_dictionary
		temp_dictionary = dict()

	return dictionary.get(indices)[:2]

def dynamique_all(p,w,d):
	n = len(p)
	indices = tuple(range(n))
	dictionary = temp_dictionary = {}
	dictionary[()] = (0,[[]],0)
	for n_i in range(1,n+1):
		for current_combin in combinations(indices,n_i):
			min_penalty = float("inf")
			best_sequence = []
			cout = 0
			for k,r in enumerate(combinations(current_combin,n_i-1)):
				j = current_combin[n_i-k-1]
				fa,fr,cout = dictionary.get(r)
				cout += p[j]
				ff = fa + max(0,cout-d[j])*w[j]
				if ff <= min_penalty:
					if ff < min_penalty:
						all_sol = []
						min_penalty = ff
						best_sequence = fr + [j]
					for old_sol in fr:
						all_sol.append(old_sol+[j])
			# temp_dictionary[current_combin] = (min_penalty,best_sequence,cout)
			temp_dictionary[current_combin] = (min_penalty,all_sol,cout)
		dictionary = temp_dictionary
		temp_dictionary = dict()

	return dictionary.get(indices)[:2]
