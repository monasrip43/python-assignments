#calculate the electricity bill using the conditions:
#1.first 100 units-->5rs
#2.next 100 units -->7rs
#3.above 200 units-->10rs
units=int(input("enter the number of units:"))#250
if units<=100:
    bill=units*5
    print("the electricitybill:",bill)
elif units<=200:
    bill=(100*5)+(units-100)*7
    print("the electricitybill:",bill)
else:
    #first-5
    #next 100-7
    #above 200-10
    bill=(100*5)+(100*7)+((units-200)*10)
#display the whole bill
print("Final bill:",bill)
'''
units=250
100*5=500
100*7=700
50*10=500
totalo=1700


'''