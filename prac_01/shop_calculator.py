total_price=0
num=int(input("Number of items:"))
while num<0:
    print("Invalid price!!!")
for i in range(0,num):
    price=float(input("Price of item:"))
    total_price+=price
if total_price>100:
    discount=total_price*0.9
    print("Total price for",num, "items is", "$",'{:.2f}'.format(discount))





