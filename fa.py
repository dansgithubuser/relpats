import histogram
import glob, random

def analyze_transform(corpus, input, transform):
	cipher=[]
	for x in words: cipher.append(transform(x))
	h=histogram.Histogram()
	h.add(cipher)
	print corpus.matched_frequency_distance(h)
	return cipher, h

corpus=histogram.Histogram()
for file_name in glob.glob("books/*.txt"):
	with open(file_name) as file:
		corpus.add(file.read())

with open("input.txt") as file: words=file.read().split()
channels=[]
for i in range(3):
	transform=lambda x: int(x[i*2:i*2+2], 16)
	print i,
	channels.append(analyze_transform(corpus, words, transform))

print "noise",
noise, noiseHistogram=analyze_transform(corpus, input, lambda x: random.randint(0, 255))

analyze_transform(corpus, input, lambda x: int(x[0:2], 16)^int(x[4:6], 16))
analyze_transform(corpus, input, lambda x: int(x[0:2], 16)^int(x[2:4], 16))
analyze_transform(corpus, input, lambda x: int(x[4:6], 16)^int(x[2:4], 16))
analyze_transform(corpus, input, lambda x: int(x[4:6], 16)^int(x[2:4], 16)^int(x[0:2], 16))