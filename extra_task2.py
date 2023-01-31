def Calculate(x,y,z):
    return (not (x or y or z)) == (not x and not y and not z)

print(Calculate(0,0,0))
print(Calculate(0,0,1))
print(Calculate(0,1,0))
print(Calculate(0,1,1))
print(Calculate(1,0,0))
print(Calculate(1,0,1))
print(Calculate(1,1,0))
print(Calculate(1,1,1))

