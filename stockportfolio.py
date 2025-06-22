import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 310
}

portfolio = {}
print("Enter your stock holdings (type 'done' to finish):")
while True:
    stock = input("Stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Try again.")

# Calculate and display summary
total_value = 0
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares @ ${price} = ${value}")

print(f"\nTotal Investment: ${total_value}")

# Save results
save = input("\nDo you want to save the result? (yes/no): ").lower()
if save == 'yes':
    file_type = input("Choose file type (.txt or .csv): ").lower()
    filename = "portfolio_output" + file_type

    try:
        if file_type == '.txt':
            with open(filename, 'w') as file:
                for stock, qty in portfolio.items():
                    file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
                file.write(f"\nTotal Investment: ${total_value}")
        elif file_type == '.csv':
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Stock', 'Quantity', 'Price', 'Total'])
                for stock, qty in portfolio.items():
                    writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
                writer.writerow(['', '', 'Total Investment', total_value])
        else:
            print("Unsupported file type. Not saved.")
        print(f"Results saved to {filename}.")
    except Exception as e:
        print(f"Error saving file: {e}")
