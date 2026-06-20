class Employee:
    def __init__(self,id,name,skills):
        self.employee_id=id
        self.employee_name=name
        self.employee_skills=skills
    def get_employee_id(self):
        return self.employee_id
    def get_employee_name(self):
        return self.employee_name
    def get_employee_skills(self):
        return self.employee_skills
n=int(input())
employees=[]
unique_skills=set()
max_skills=0
max_employee=None
for _ in range(n):
    id=input()
    name=input()
    skills=input().split(",")
    skills=list(set(skills))
    emp=Employee(id,name,skills)
    employees.append(emp)
    unique_skills.update(skills)
    if len(skills)>max_skills:
        max_skills=len(skills)
        max_employee=emp
print("unique skills count:",len(unique_skills))
print("Employee with maximum skills:",max_employee.get_employee_id(),max_employee.get_employee_name())
print("Employee knowing python:")
for emp in employees:
    if "Python" in emp.get_employee_skills():
        print(emp.get_employee_id(),emp.get_employee_name())
print(unique_skills)