import kasiski
import random

def analyze_transform(input, transform):
	cipher=[]
	for x in input: cipher.append(transform(x))
	r=kasiski.shift(cipher, 16)
	print r
	return r

with open("input.txt") as file: words=file.read().split()

channels=[]
for i in range(3):
	transform=lambda x: int(x[i*2:i*2+2], 16)
	print i,
	channels.append(analyze_transform(words, transform))

test=[chr(int(x[2:4], 16)^0b1011) for x in words]
keyword="relpats_eht"
for i in range(len(test)): test[i]=chr(ord(test[i])^ord(keyword[i%len(keyword)]))
test="".join(test)
print "test",
noise=analyze_transform(test, lambda x: x)
	
print "noise",
noise=analyze_transform(words, lambda x: random.randint(0, 255))

print "r xor b",
analyze_transform(words, lambda x: int(x[0:2], 16)^int(x[4:6], 16))
print "r xor g",
analyze_transform(words, lambda x: int(x[0:2], 16)^int(x[2:4], 16))
print "b xor g",
analyze_transform(words, lambda x: int(x[4:6], 16)^int(x[2:4], 16))
print "r xor g xor b",
analyze_transform(words, lambda x: int(x[4:6], 16)^int(x[2:4], 16)^int(x[0:2], 16))
