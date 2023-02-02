def get_input_from_user(message):
    user_input = input(message)
    while (not user_input.isnumeric() and (not user_input.replace(user_input[0],"").isnumeric()
                                          or not user_input[0]=="-")) or user_input=="0":
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input

def get_quarter_number(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

x = get_input_from_user("Enter x: ")
y = get_input_from_user("Enter y: ")

print(f"Quarter of a point is {get_quarter_number(x, y)}")