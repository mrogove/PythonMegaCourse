#write list to file:
numbers = [1,2,3]

numberfile = open("numberlist.txt","a")
for idx in numbers:
    numberfile.write(str(idx)+"\n")

numberfile.close()
