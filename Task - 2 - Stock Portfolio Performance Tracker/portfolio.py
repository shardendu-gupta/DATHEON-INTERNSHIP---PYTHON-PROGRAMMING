
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



