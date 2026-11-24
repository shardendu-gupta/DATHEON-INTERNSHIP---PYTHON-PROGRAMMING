portfolio = {}


while True:

    stock_symbol = input("Enter symbol : ")
    buying_price = float(input("Enter buying price :"))
    quantity = int(input("Enter quantity : "))


    portfolio[stock_symbol] = {"Buying Price" : buying_price, "Quantity" : quantity}

    choice = input("Do you want to add  another stock (yes/no) : ")

    if choice == "no":
        break
print(portfolio)
