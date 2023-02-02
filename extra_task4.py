def get_input_from_user(message):
    user_input = input(message)
    while user_input not in ["1", "2", "3", "4"]:
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input

def get_quarter_coordinates(quarter_number):
    if quarter_number == 1:
        return "x from 0 to infinity, y from 0 to infinity"
    elif quarter_number == 2:
        return "x from -infinity to 0, y from 0 to infinity"
    elif quarter_number == 3:
        return "x from -infinity to 0, y from -infinity to 0"
    elif quarter_number == 4:
        return "x from 0 to infinity, y from -infinity to 0"

print(f"{get_quarter_coordinates(get_input_from_user('Enter quarter number: '))}")