
# class InvalidUsernameError(Exception):
#     pass

# class UserNotFoundError(Exception):
#     pass

# class ShortUsernameError(Exception):
#     pass

# class LoginSystem:
#     def __init__(self, usernames):
#         self.valid_usernames = [u.lower() for u in usernames]

#     def login(self, username):
#         if len(username) < 4:
#             raise ShortUsernameError("ShortUsernameError: Username length must be at least 4.")

#         if not username.isalpha():
#             raise InvalidUsernameError("InvalidUsernameError: Username must only contain alphabets.")

#         if username.lower() not in self.valid_usernames:
#             raise UserNotFoundError(f"UserNotFoundError: '{username}' not found in the system.")

#         print("Login Successful")

# if __name__ == "__main__":
#     try:
#         num_users = int(input())
#         user_list = []
#         for _ in range(num_users):
#             user_list.append(input())
        
#         login_query = input()

#         system = LoginSystem(user_list)
#         system.login(login_query)

#     except (InvalidUsernameError, UserNotFoundError, ShortUsernameError) as e:
#         print(e)
#     except ValueError:
#         pass

'''
Student result login:

the program should accept the :
marks of 5 subjects:
raise an exception
if:
1.marks are negative
2.marks exceed 100
3.non numeric input
4.calculate the average and grade

rules:
avg>=75 --> distinction
avg >= 60  --> first class
avg>= 40 ---> pass

'''
# class InvalidMarksError(Exception):
#      pass
# class Student:
#     def __init__(self):
#         self.marks=[]
#     def input_marks(self):
#         try:
#             for i in range(5):
#                 marks=int(input(f"enter the subject{i+1} marks"))
#                 if marks<0 or marks>100:
#                   raise InvalidMarksError("Marks should be between 0 and 100")
#                 self.marks.append(mark)  
#             average = sum(self.marks)/5
#             print("Average:",average)
#             if average >= 75:
#                 print("Distinction")
#             elif average >= 60:
#                 print("first class")
#             elif average >= 40:
#                 print("pass")
#             else:
#                 print("fail")
#         except ValueError:
#             print("only numerics are allowed")
#         except InvalidMarksError as e:
#             print(e)
# s1=Student()  
# s1.input_marks()