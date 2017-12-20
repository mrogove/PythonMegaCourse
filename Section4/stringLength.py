def stringLength(strVal):
    if type(strVal) != str:
        return "We need a string."
    else:
        return len(strVal)

print (stringLength("Mercurial"))
