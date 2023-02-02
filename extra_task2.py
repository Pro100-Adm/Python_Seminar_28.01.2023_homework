def calculate_logical_equation(x,y,z):
    return (not (x or y or z)) == (not x and not y and not z)

print(f"{calculate_logical_equation(0,0,0)}")
print(f"{calculate_logical_equation(0,0,1)}")
print(f"{calculate_logical_equation(0,1,0)}")
print(f"{calculate_logical_equation(0,1,1)}")
print(f"{calculate_logical_equation(1,0,0)}")
print(f"{calculate_logical_equation(1,0,1)}")
print(f"{calculate_logical_equation(1,1,0)}")
print(f"{calculate_logical_equation(1,1,1)}")

