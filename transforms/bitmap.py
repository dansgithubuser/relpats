import Image
import random

def analyze_transform(input, transform, width, name):
	cipher=[]
	for x in input: cipher.append(transform(x))
	height=len(cipher)/width
	image=Image.new("RGB", (width, height), "black")
	for i in range(height):
		for j in range(width):
			image.putpixel((j, i), cipher[i*width+j])
	image.save(name)

with open("input.txt") as file: words=file.read().split()

analyze_transform(words, lambda x: int(x[0:2], 16), 41, "r.bmp")
analyze_transform(words, lambda x: int(x[4:6], 16), 41, "b.bmp")
analyze_transform(words, lambda x: random.randint(0, 255), 41, "random.bmp")
