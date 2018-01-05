import glob2
import datetime

filenames = glob2.glob("*.txt")

print(filenames)
"""
Use a "with" statement to create a new text file
and then iterate through the file list inside that "with" statement
and open and read existing file contents in each iteration
and write them to new text file.
"""
now = datetime.datetime.now()

with open(now.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","w") as file:
    for i in filenames:
        with open(i,"r") as f: #use open,read. assign to f
            file.write(f.read()+"\n") #write the contents of each f
