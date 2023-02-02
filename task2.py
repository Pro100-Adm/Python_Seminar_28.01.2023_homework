def get_input_from_user(message):
    user_input = input(message)
    while not user_input.isnumeric():
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input

time_in_seconds = get_input_from_user("Enter time in seconds: ")
print(f"Time in h:m:s format: {time_in_seconds/3600} : {time_in_seconds/60} : {time_in_seconds}")


