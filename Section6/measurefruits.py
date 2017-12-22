#calculate file length
i = open("fruits.txt","r")
fruitArray = i.readlines()
fruitArray = [f.rstrip("\n") for f in fruitArray]
print (fruitArray)

for f in fruitArray:
    #print(f)
    print(len(f))
