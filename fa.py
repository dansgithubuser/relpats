import helpers
import glob, random

corpus=helpers.Histogram()
for file_name in glob.glob("books/*.txt"):
	with open(file_name) as file:
		corpus.add(file.read())

with open("input.txt") as file: words=file.read().split()
ciphers=[]
histograms=[]
for i in range(3):
	ciphers.append([])
	histograms.append(helpers.Histogram())
for i in range(len(ciphers)):
	for x in words: ciphers[i].append(int(x[i*2:i*2+2], 16))
	histograms[i].add(ciphers[i])
	print i, corpus.matched_frequency_distance(histograms[i])

noise=[]
for i in range(2296): noise.append(random.randint(0, 256))
h=helpers.Histogram()
h.add(noise)
print "baseline", corpus.matched_frequency_distance(h)
