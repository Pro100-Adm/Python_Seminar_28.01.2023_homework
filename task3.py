def GetNumberFromUser():
    userInput = input("Enter number n: ")
    while not userInput.isnumeric():
        print("Wrong number!")
        userInput = input("Enter number: ")
    userInput = int(userInput)
    return userInput

num = GetNumberFromUser()
print("n + nn+ nnn = " + str(num + num + num*10 + num + num * 10 + num * 100))