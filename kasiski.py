def shift(sequence, max):
	result=[]
	for i in range(1, max+1):
		repetitions=0
		for j in range(len(sequence)-i):
			if sequence[j]==sequence[j+i]: repetitions+=1
		result.append((i, repetitions))
	return result
