
                             #NESTED - IF - ELSE

'''
sms --> click on this link to get 100rs
if sms has "click on link"
print("it is spam")
win money 200000 by playing games
nested if or elif to check if sispicious are available
spam msg

message = input()
if "win money" in message:
 print ("spam message")
'''
'''
message = input ("enter the message :")
#conversion of message to small letters
message = message.lower()

#now we have to perform the spam detection
if "win money" in message:
    print("spam message")
elif "free offer" in message :
    print("spam detected")
elif "click this" in message:
    print("spam detected")
else:
    print("spam not detected")
    '''


'''
a = 10 
b = 10 
a is b (true) because is checks for the reference(identity)(memory)
each variable has a different locations


where as a in b condition in --->checks for the value


example 2
a = [1,2,3]
b = [1,2,3]
c = a

 a is b --- false #because a and b have the different memory locations
 a in b --- false #because this condition checks that if the a variable is present  in b
 a is c --- true

 membership operator : in , not in
 identity : is , is not
'''
