import collections

class Histogram:
	def __init__(self):
		self.total=0
		self.values=collections.defaultdict(int)
	
	def __str__(self):
		result=""
		for pair in self.get_pairs():
			result+="{0:8}: {1:8}    {2:<16.4}\n".format(
				pair[0], pair[1], 1.0*pair[1]/self.total
			)
		return result
	
	def add(self, values):
		self.total+=len(values)
		for value in values: self.values[value]+=1
	
	def matched_frequency_distance(self, other):
		a=[1.0*x[1]/self.total for x in self.get_pairs()]
		b=[1.0*x[1]/other.total for x in other.get_pairs()]
		if len(a)<len(b): a+=[0.0]*(len(b)-len(a))
		if len(b)<len(a): b+=[0.0]*(len(a)-len(b))
		result=0.0
		for i in range(len(a)): result+=abs(a[i]-b[i])
		return result
	
	def get_values(self):
		return sorted(self.values.keys())
	
	def get_pairs(self):
		return reversed(sorted(self.values.items(), key=lambda x: x[1]))
