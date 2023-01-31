def GetTimeInSecondsFromUser():
    userInput = input("Enter time in seconds: ")
    while not userInput.isnumeric():
        print("Wrong number!")
        userInput = input("Enter time in seconds: ")
    userInput = int(userInput)
    result = "Time in h:m:s format: {} : {} : {}".format(userInput/3600, userInput/60, userInput)
    return result

print(GetTimeInSecondsFromUser())


