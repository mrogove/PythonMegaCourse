#goal: read fruits.txt, print each line to command Line

i = open("fruits.txt","r")
fruitArray = i.read()
i.close()

print(fruitArray)
