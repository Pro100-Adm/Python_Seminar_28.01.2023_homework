def get_input_from_user(message):
    user_input = input(message)
    while not user_input.isnumeric():
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input

num = get_input_from_user("Enter number: ")
result = num + num + num*10 + num + num * 10 + num * 100
print(f"n + nn + nnn = {str(result)}")