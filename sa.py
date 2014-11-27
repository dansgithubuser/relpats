import sequence
import random

def analyze_transform(input, transform):
	cipher=[]
	for x in input: cipher.append(transform(x))
	r=sequence.repetition(cipher)
	print sequence.repetition_value(r)
	return cipher, r

with open("input.txt") as file: words=file.read().split()
channels=[]
for i in range(3):
	transform=lambda x: chr(int(x[i*2:i*2+2], 16))
	print i,
	channels.append(analyze_transform(words, transform))

print channels[0][1]
print channels[2][1]

print "noise",
noise, noiseRepetitions=analyze_transform(words, lambda x: chr(random.randint(0, 255)))

analyze_transform(words, lambda x: chr(int(x[0:2], 16)^int(x[4:6], 16)))
analyze_transform(words, lambda x: chr(int(x[0:2], 16)^int(x[2:4], 16)))
analyze_transform(words, lambda x: chr(int(x[4:6], 16)^int(x[2:4], 16)))
analyze_transform(words, lambda x: chr(int(x[4:6], 16)^int(x[2:4], 16)^int(x[0:2], 16)))