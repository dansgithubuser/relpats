import collections

class DefaultLict:
	def __init__(self): self.list=[]
	
	def __getitem__(self, index):
		for item in self.list:
			if item[0]==index:
				return item[1]
		self.list.append((index, []))
		return self.list[-1][1]
	
	def __setitem__(self, index, value):
		for i in range(len(self.list)):
			if self.list[i][0]==index:
				self.list[i][1]=value
				return
		self.list.append((index, value))
		
	def __len__(self): return len(self.list)

def repetition(sequence):
	def index(
		sequence,
		symbol_transform=lambda i, sequence: sequence[i],
		index_transform=lambda i, sequence: i
	):
		result=DefaultLict()
		for i in range(len(sequence)):
			result[[symbol_transform(i, sequence)]].append(index_transform(i, sequence))
		return result
	def extend(repetitions, sequence):
		result=DefaultLict()
		for symbol, indices in repetitions.list:
			nexts=[(sequence[i+1], i+1) for i in indices if i+1<len(sequence)]
			nexts_index=index(
				nexts,
				lambda i, sequence: sequence[i][0],
				lambda i, sequence: sequence[i][1]
			)
			for next_symbol, next_indices in nexts_index.list:
				if len(next_indices)>1:
					result[symbol+next_symbol]=next_indices
		return result
	repetitions=index(sequence)
	result=[]
	while True:
		repetitions=extend(repetitions, sequence)
		if len(repetitions)==0: break
		for symbol, indices in repetitions.list:
			result.append((symbol, [i-(len(symbol)-1) for i in indices]))
	return result

def repetition_value(repetitions):
	result=0
	for repetition in repetitions: result+=len(repetition[0])
	return result
