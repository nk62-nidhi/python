cost_price=int(input("enter cost price....>"))
sale_price=int(input("enter selling price.....>"))
if cost_price> sale_price:
    print("no profit")
elif cost_price<sale_price:
    print("profit is {}".format(sale_price-cost_price))
else:
    print("neither profit nor loss")