stocks = {
    "Google": 70.23,
    "Amazon": 59.89,
    "Microsoft": 65.39,
    "LinkedIn": 24.61,
    "Facebook": 30.56
}

zippedTogether = zip(stocks.values(), stocks.keys())

#print(max(zippedTogether))
#print(min(zippedTogether))

print(sorted(zippedTogether))