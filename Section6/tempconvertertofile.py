temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c>= -273.15:
        f=c*9/5+32
        return f

tempfile = open("temperaturefile.txt","w")
for t in temperatures:
    if type(t) is int:
        tempfile.write(str(c_to_f(t))+"\n")

tempfile.close()
