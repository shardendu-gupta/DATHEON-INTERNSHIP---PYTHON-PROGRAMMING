
import csv

portfolio = {}
current_prices = {}

# Take stock details from user

while True:

    stock_symbol = input("Enter stock symbol: ").upper()
    buying_price = float(input("Enter buying price: "))
    quantity = int(input("Enter quantity: "))

    portfolio[stock_symbol] = {
        "buying_price": buying_price,
        "quantity": quantity
    }

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice == "no":
        break


# Read current stock prices from CSV

with open("stock_prices.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        current_prices[row["Symbol"]] = float(row["Current Price"])


# Calculate portfolio value

total_investment = 0
total_market_value = 0

print("\n------ PORTFOLIO SUMMARY ------")

for stock, details in portfolio.items():

    buying_price = details["buying_price"]
    quantity = details["quantity"]

    if stock in current_prices:

        current_price = current_prices[stock]

        invested_amount = buying_price * quantity
        market_value = current_price * quantity

        profit_loss = market_value - invested_amount
        percentage = (profit_loss / invested_amount) * 100

        total_investment += invested_amount
        total_market_value += market_value

        print("\nStock:", stock)
        print("Buying Price:", buying_price)
        print("Current Price:", current_price)
        print("Quantity:", quantity)
        print("Investment:", invested_amount)
        print("Market Value:", market_value)
        print("Profit/Loss:", round(profit_loss, 2))
        print("Return:", round(percentage, 2), "%")

    else:
        print("\nStock price not found:", stock)


total_profit_loss = total_market_value - total_investment

if total_investment > 0:
    total_percentage = (total_profit_loss / total_investment) * 100
else:
    total_percentage = 0

print("\n------ TOTAL PORTFOLIO ------")
print("Total Investment:", round(total_investment, 2))
print("Total Market Value:", round(total_market_value, 2))
print("Total Profit/Loss:", round(total_profit_loss, 2))
print("Total Return:", round(total_percentage, 2), "%")



