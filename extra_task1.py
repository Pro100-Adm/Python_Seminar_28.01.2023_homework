def get_input_from_user(message):
    user_input = input(message)
    while user_input not in ["1","2","3","4","5","6","7"]:
        print(f"Wrong number!")
        user_input = input("Enter week day number: ")
    user_input = int(user_input)
    return user_input

def is_holiday(week_day_number):
    if week_day_number in [6,7]:
        return True
    else:
        return False

print(f"{is_holiday(get_input_from_user())}")