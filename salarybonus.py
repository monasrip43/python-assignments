salary = float(input("enter salary: "))
experience = int(input("enter experience: "))

if experience >= 5 :
   if salary < 30000:
      bonus_percent = 0.20
elif (30000 <= salary <=50000):
      bonus_percent = 0.15
else:
      bonus_percent = 0.05
bonus_amount = salary * bonus_percent
final_salary = salary + bonus_amount

print(f"bonus ={bonus_amount}")
print(f"final salary ={final_salary}")