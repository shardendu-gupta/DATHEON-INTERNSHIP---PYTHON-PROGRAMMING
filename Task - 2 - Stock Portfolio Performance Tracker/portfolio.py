portfolio = {}


while True:

    stock_symbol = input("Enter symbol : ")
    buying_price = float(input("Enter buying price :"))
    quantity = int(input("Enter quantity : "))


    portfolio[stock_symbol] = {"buying_price" : buying_price, "quantity" : quantity}

    choice = input("Do you want to add  another stock (yes/no) : ")

    if choice == "no":
        break


print("\n ========YOUR PORTFOLIO=======")


for stock, details in portfolio.items():
    print("\n Stock", stock)
    print("Buying Price", details["buying_price"])
    print("Quantity", details["quantity"])

