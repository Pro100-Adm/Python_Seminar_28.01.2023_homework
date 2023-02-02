def get_input_from_user(message):
    user_input = input(message)
    while not user_input.isnumeric():
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input

def profit_or_loss(revenue, costs):
    if revenue>=costs:
        return "Profit"
    else:
        return "Loss"

def profitability(revenue, profit):
    return profit/revenue

def profit_per_employeer(profit, staff_col):
    return profit/staff_col

revenue = get_input_from_user("Enter company revenue: ")
costs = get_input_from_user("Enter company costs: ")
profit_or_loss_var = profit_or_loss(revenue, costs)
print(f"Company has {profit_or_loss_var}")
if profit_or_loss_var == "Profit":
    company_profit_size = revenue-costs
    print(f"Company profitability is {str(profitability(revenue, company_profit_size))}")
    staff = get_input_from_user("Enter company staff quantity: ")
    print(f"Company profit per staff is {str(profit_per_employeer(company_profit_size, staff))}")


