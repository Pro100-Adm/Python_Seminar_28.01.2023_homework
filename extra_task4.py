def GetNumberFromUser(message):
    userInput = input(message)
    while userInput not in ["1", "2", "3", "4"]:
        print("Wrong number!")
        userInput = input(message)
    userInput = int(userInput)
    return userInput

def GetQuarterCoordinates(quarterNumber):
    if quarterNumber == 1:
        return "x from 0 to infinity, y from 0 to infinity"
    elif quarterNumber == 2:
        return "x from -infinity to 0, y from 0 to infinity"
    elif quarterNumber == 3:
        return "x from -infinity to 0, y from -infinity to 0"
    elif quarterNumber == 4:
        return "x from 0 to infinity, y from -infinity to 0"

print(GetQuarterCoordinates(GetNumberFromUser("Enter quarter number: ")))