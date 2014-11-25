import collections

def repetition(sequence):
	def index(
		sequence,
		symbol_transform=lambda i, sequence: sequence[i],
		index_transform=lambda i, sequence: i
	):
		result=collections.defaultdict(list)
		for i in range(len(sequence)):
			result[symbol_transform(i, sequence)].append(index_transform(i, sequence))
		return result
	def extend(repetitions, sequence):
		result=collections.defaultdict(list)
		for symbol, indices in repetitions.items():
			nexts=[(sequence[i+1], i+1) for i in indices if i+1<len(sequence)]
			nexts_index=index(
				nexts,
				lambda i, sequence: sequence[i][0],
				lambda i, sequence: sequence[i][1]
			)
			for next_symbol, next_indices in nexts_index.items():
				if len(next_indices)>1:
					result[symbol+next_symbol]=next_indices
		return result
	repetitions=index(sequence)
	result=[]
	while True:
		repetitions=extend(repetitions, sequence)
		if len(repetitions)==0: break
		new_results={}
		for symbol, indices in repetitions.items():
			new_results[symbol]=[i-(len(symbol)-1) for i in indices]
		result.append(new_results)
	return result

def repetition_value(repetitions):
	result=0
	for repetition in repetitions:
		for symbol in repetition:
			result+=len(symbol)
	return result
