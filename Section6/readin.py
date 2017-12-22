i = open("example.txt", "r") #wrapper
array = i.readlines()
array = [x.rstrip("\n") for x in array]

print(array)
