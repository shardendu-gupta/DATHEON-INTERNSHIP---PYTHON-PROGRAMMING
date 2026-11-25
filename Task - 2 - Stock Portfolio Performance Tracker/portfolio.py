import csv

portfolio = {}
current_prices = {}

# Take stock details from user

while True:

    stock_symbol = input("Enter stock symbol: ").strip().upper()
    buying_price = float(input("Enter buying price: "))
    quantity = int(input("Enter quantity: "))
    portfolio[stock_symbol] = {"buying_price": buying_price, "quantity": quantity}
    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice == "no":
        break


with open("stock_prices.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    for row in reader:

        if len(row) < 3:
            continue

        if row[0].strip().lower() == "symbol":
            continue

        stock_symbol = row[0].strip().upper()
        current_price = float(row[2].strip())
        current_prices[stock_symbol] = current_price


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


with open("portfolio_summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock Symbol", "Buying Price", "Current Price", "Quantity", "Investment", "Market Value", "Profit/Loss", "Return Percentage"])

    for stock, details in portfolio.items():
        if stock in current_prices:

            buying_price = details["buying_price"]
            quantity = details["quantity"]
            current_price = current_prices[stock]
            invested_amount = buying_price * quantity
            market_value = current_price * quantity
            profit_loss = market_value - invested_amount
            percentage = (profit_loss / invested_amount) * 100
            writer.writerow([stock, buying_price, current_price, quantity, invested_amount, market_value, round(profit_loss, 2), round(percentage, 2)])


print("\nPortfolio report saved successfully!")
