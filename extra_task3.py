def GetNumberFromUser(message):
    userInput = input(message)
    while (not userInput.isnumeric() and (not userInput.replace(userInput[0],"").isnumeric()
                                          or not userInput[0]=="-")) or userInput=="0":
        print("Wrong number!")
        userInput = input(message)
    userInput = int(userInput)
    return userInput

def GetQuarterNumber(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

print(GetQuarterNumber(GetNumberFromUser("Enter x: "), GetNumberFromUser("Enter y: ")))