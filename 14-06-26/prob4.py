class Order:
    def __init__(self,name,amount):
        self.customer_name=name
        self.amount=amount
    def calculate_bill(self):
        return self.amount
class Veg(Order):
    def calculate_bill(self):
        return self.amount+(self.amount*0.05)
class NonVeg(Order):
    def calculate_bill(self):
        return self.amount+(self.amount*0.12)
class Dessert(Order):
    def calculate_bill(self):
        return self.amount+(self.amount*0.18)
n=int(input())
orders=[]
highest_bill=0
highest_order=None
count=0 
for _ in range(n):
    order_type,name,amount=input().split()
    amount=float(amount)
    order_type=order_type.lower()
    if order_type=="veg":
        o=Veg(name,amount)
    elif order_type=="nonveg":
        o=NonVeg(name,amount)
    elif order_type=="dessert":
        o=Dessert(name,amount)
    orders.append(o)
for o in orders:
    final_bill=o.calculate_bill()
    print(o.customer_name,round(final_bill,2))
    if final_bill>highest_bill:
        highest_bill=final_bill
        highest_order=o
    if final_bill>500:
        count+=1
    print("Highest order:",highest_order.customer_name,round(final_bill,2))
    print("Counnt of orders above 500:",count)