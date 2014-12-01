import sys
sys.path.append("analysis")

#=====Analyzers=====#
analyzers=[]

class Analyzer:
	def name(self): raise NotImplementedError
	def setup(self): raise NotImplementedError
	def analyze(self, cipher): raise NotImplementedError

class FrequencyAnalyzer(Analyzer):
	def name(self): return "frequency analysis"
	
	def setup(self):
		import histogram, glob
		self.corpus=histogram.Histogram()
		for file_name in glob.glob("books/*.txt"):
			with open(file_name) as file:
				self.corpus.add(file.read())
				
	def analyze(self, cipher):
		import histogram
		x=histogram.Histogram()
		x.add(cipher)
		print self.corpus.matched_frequency_distance(x)
		return x

analyzers.append(FrequencyAnalyzer())

class SequenceAnalyzer(Analyzer):
	def name(self): return "sequence analysis"
	
	def setup(self): pass
	
	def analyze(self, cipher):
		import sequence
		x=sequence.repetition(cipher)
		print sequence.repetition_value(x)
		return x
		
analyzers.append(SequenceAnalyzer())

class KasiskiAnalyzer(Analyzer):
	def name(self): return "kasiski analysis"
	
	def setup(self): pass
	
	def analyze(self, cipher):
		import kasiski
		x=kasiski.shift(cipher, 16)
		print x
		return x

analyzers.append(KasiskiAnalyzer())
		
#=====ciphers=====#
ciphers=[]
with open("input.txt") as file: words=file.read().split()

#-----noise-----#
import random
ciphers.append(("noise", [random.randint(0, 255) for x in range(len(words))]))
ciphers.append(("noise*2", [random.randint(0, 255) for x in range(len(words)*2)]))

#-----vigenere-----#
plain=[int(x[2:4], 16)^0b1011 for x in words]
keyword="relpats_eht"
cipher=[]
for i in range(len(plain)): cipher.append(plain[i]^ord(keyword[i%len(keyword)]))
ciphers.append(("vigenere", cipher))

#-----transforms-----#
transforms=[
	("r", lambda x: [int(x[0:2], 16)]),
	("g", lambda x: [int(x[2:4], 16)]),
	("b", lambda x: [int(x[4:6], 16)]),
	("r^g", lambda x: [int(x[0:2], 16)^int(x[2:4], 16)]),
	("r^b", lambda x: [int(x[0:2], 16)^int(x[4:6], 16)]),
	("b^g", lambda x: [int(x[2:4], 16)^int(x[4:6], 16)]),
	("r^g^b", lambda x: [int(x[0:2], 16)^int(x[2:4], 16)^int(x[4:6], 16)]),
	("rb", lambda x: [int(x[0:2], 16), int(x[4:6], 16)]),
]

for transform in transforms:
	cipher=[]
	for x in words: cipher+=transform[1](x)
	ciphers.append((transform[0], cipher))

#=====process=====#
for analyzer in analyzers:
	analyzer.setup()
	print "====="+analyzer.name()+"====="
	for cipher in ciphers:
		print cipher[0]
		analyzer.analyze(cipher[1])
		print
	print
