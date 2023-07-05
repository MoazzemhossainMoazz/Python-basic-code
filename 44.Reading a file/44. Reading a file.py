#for readable
file = open("44.studentRead.txt", "r")
print(file.readable())

#for wirtable
file2 = open("44.studentWrite.txt", "w")
print(file2.writable())


#for readable and writable
file3 = open("44.studentReadWrite.txt", "r+")
print(file3.writable())


#print file text
file4 = open("44.studentRead.txt", "r+")
#print(file4.writable())
text = file4.read()
print(text)
size = len(text)
print(size)
text = file4.readlines()[1]
print(text)

for line in file4:
    print(line)
file.close