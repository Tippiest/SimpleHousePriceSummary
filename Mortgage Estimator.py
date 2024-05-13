currentPrice = int(input("What is the current price of the house? "))
lastPrice = int(input("What was the price of the house last month? "))

priceDifference = currentPrice - lastPrice

print("This house is $" + str(currentPrice) + " and was $" + str(lastPrice) + "last month" + ". The change in price is $" + str(priceDifference) + "\n")

estMortgage = (currentPrice * 0.051) / 12

print("The estimated monthly mortgage is $" + str(estMortgage))
