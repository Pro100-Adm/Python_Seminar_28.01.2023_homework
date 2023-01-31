def GetNumberFromUser(message):
    userInput = input(message)
    while (not userInput.isnumeric() and (not userInput.replace(userInput[0],"").isnumeric()
                                          or not userInput[0]=="-")):
        print("Wrong number!")
        userInput = input(message)
    userInput = int(userInput)
    return userInput

def CalculateDistanceBetweenTwoPoints(x1, y1, x2, y2):
    return (float((x2-x1)**2)+float((y2-y1)**2))**0.5

print(CalculateDistanceBetweenTwoPoints(GetNumberFromUser("Enter x1: "), GetNumberFromUser("Enter y1: "),
                                        GetNumberFromUser("Enter x2: "), GetNumberFromUser("Enter y2: ")))