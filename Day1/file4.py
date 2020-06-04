cost = float(input('enter the cost price'))
sell = float (input('enter the selling price'))
profit = sell-cost
print('Profit from the sale is ', profit)
print('To increase profit by 5% we need to sell at', ((0.05*profit)+cost))