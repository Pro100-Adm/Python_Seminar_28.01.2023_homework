def get_input_from_user(message):
    user_input = input(message)
    while (not user_input.isnumeric() and (not user_input.replace(user_input[0],"").isnumeric()
                                          or not user_input[0]=="-")):
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input

def calculate_distance_between_two_points(x1, y1, x2, y2):
    return (float((x2-x1)**2)+float((y2-y1)**2))**0.5

x1 = get_input_from_user('Enter x1: ')
y1 = get_input_from_user('Enter y1: ')
x2 = get_input_from_user('Enter x2: ')
y2 = get_input_from_user('Enter y2: ')
print(f"Distance between two points = {calculate_distance_between_two_points(x1, y1, x2, y2)}")