
'''
logic for password verifier
          store the original password
                     |
            ask the user for input
                     |
            compare the enetered password with original password
                     |
            if wrong:
               show error message
               try again
                     |
            if correct:
                    stop loop
                    login successful

'''

org_password = "Mona"
password = ""
while org_password != password:
   password = input()
   if org_password != password:
      print("password doesn't match")
      print("Try again")
print("login sucessful")
     
