import csv
SPYdates = [] # list of trading dates
SPYclose = [] # list of adjusted closing prices
commission = 1 # commission for buying and selling
# read in the dates and prices
with open('/Users/lfortnow6/Downloads/SPY.csv') as csvfile:
    SPYreader = csv.DictReader(csvfile)
    for row in SPYreader:
        SPYdates.append(row['Date'])
        SPYclose.append(float(row['Adj Close']))
days = len(SPYdates)
# earnings(i) = best earnings using data up to time i
# transactions(i) = list of strings of transactions (buy and sell repeating) to get best earnings up to time i
earnings = [0]
transactions = ['']
for i in range(1,days):
    # set best so far to be best so far up to previous day
    improved = False # flag to check if we can do better
    # bestearnings to find the max.
    bestearnings = earnings[i-1]
    if SPYclose[i]>SPYclose[i-1]: # otherwise no reason to sell today
        for j in range(i):
            newearnings = earnings[j]+SPYclose[i]-SPYclose[j]-2*commission
            if newearnings > bestearnings:
                improved = True
                bestearnings = newearnings
                tradebuy = j
                tradesell = i
    earnings.append(bestearnings)
    if improved: # add new transaction to best transaction at time tradebuy
        besttransactions = transactions[tradebuy] + ' Buy ' + SPYdates[tradebuy] + ' Sell ' + SPYdates[tradesell]
    else:
        besttransactions = transactions[i-1]
    transactions.append(besttransactions)
print (earnings[days-1])
print (transactions[days-1])





