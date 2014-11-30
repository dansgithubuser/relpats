import math

def prime_factor(n):
	original=n
	result=[]
	for i in range(2, int(math.sqrt(n)+2)):
		while n%i==0:
			result.append(i)
			n/=i
	if n!=1: result.append(n)
	check=1
	for factor in result: check*=factor
	if check!=original: import pdb; pdb.set_trace
	return result
