def degreeCtoF(degf):
    x = float(degf)
    if x < -273.15:
        return "That's below absolute zero."
    else:
        f = x * 9 / 5 + 32
        return f

print(degreeCtoF(input("Please input degrees Celsius: ")))
