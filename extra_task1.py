def GetWeekDayNumberFromUser():
    userInput = input("Enter week day number: ")
    while userInput not in ["1","2","3","4","5","6","7"]:
        print("Wrong number!")
        userInput = input("Enter week day number: ")
    userInput = int(userInput)
    return userInput

def IsHoliday(weekDayNumber):
    if weekDayNumber in [6,7]:
        return True
    else:
        return False

print(IsHoliday(GetWeekDayNumberFromUser()))