#simulate the atm system:
#enter the pin
#check for the balance for widthdraw
#widthdraw is successfull then show balance after the widthdraw
crtpin=2006
balance=5000
pin=int(input("enter the pin:"))
if pin == crtpin :
    widthdraw=int(input("the amount to be widthdraw"))
    if balance >=widthdraw:
        balance-=widthdraw
        finalbalance=balance
        print("successful widthdraw")
        print("final balance:",finalbalance)
    else:
        print("insufficient balance")
else:
    print("invalid pin")