def GetNumberFromUser(message):
    userInput = input(message)
    while not userInput.isnumeric():
        print("Wrong number!")
        userInput = input(message)
    userInput = int(userInput)
    return userInput

def ProfitOrLoss(revenue, costs):
    if revenue>=costs:
        return "Profit"
    else:
        return "Loss"

def Profitability(revenue, profit):
    return profit/revenue

def ProfitPerEmployeer(profit, staff_col):
    return profit/staff_col

revenue = GetNumberFromUser("Enter company revenue: ")
costs = GetNumberFromUser("Enter company costs: ")
profitOrLoss = ProfitOrLoss(revenue, costs)
print("Company has " + profitOrLoss)
if profitOrLoss == "Profit":
    print("Company profitability is " + str(Profitability(revenue, revenue-costs)))
    staff = GetNumberFromUser("Enter company staff quantity: ")
    print("Company profit per staff is " +
          str(ProfitPerEmployeer(revenue-costs, staff)))

