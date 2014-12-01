with open("input.txt") as file: words=file.read().split()

cipher=[]
for x in words: cipher.append(int(x[2:4], 16))
plain=""
for x in cipher: plain+=chr(x^0b1011)
print plain
print
print "NOTE: if you see strange punctuation characters, they do not have to do with the puzzle. The message is encoded in extended ASCII, which is no longer popular."