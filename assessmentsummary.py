# # class Employee:
# #     def __init__(self,name,task):
# #         self.name=name
# #         self.task=task
# #     def get_name(self):
# #         return self.name
# #     def get_task(self):
# #         return self.task
# # N=int(input())
# # name,task=input().split(":")
# # name=name.lower()
# # tasks=[]
# # count=0
# # max_count=0
# # emp=Employee(name,task)
# # tasks.append(emp)
# # for i in tasks:
# #     if i in tasks:
# #         count+=1
# #     else:
# #         count=0
# #     if count> max_count:
# #         max_count=count
# #         emp.sort()
# # print(f"{name} {count}")
'''
key:values --> Mutable
   |
 Immutable
'''
student_marks = {
    "john": 85,
    "alice": 98,
    "bob" : 78
}
print(student_marks.items())

'''
dict_items(
           [('John', 85), 
           ('alice', 98), 
           ('bob', 78)])


collection of tuples inside  the list
Now each item is a tuple
t = (key,value)
     0    1  
Dict themselves cannot be
sorted

#list = [1,2,3,4]
#sort(list)

students = list(student_marks.items())
'''

students = list(student_marks.items())
#print(students)

# print(students.sort())
# print(students)

# students = list(student_marks.items())
# def sort_by_marks(item):
#     #tuple --> John,85
#     #           0   1
#     return item[1]
# students.sort(key = sort_by_marks,reverse = True)
# print(students)


'''
#problem perspective
count ={
    "john": 2,
    "alice" : 2,
    "bob" : 1
}

print(count.items())

dict_items(
          [('john', 2), 
          ('alice', 2), 
          ('bob', 1)])


employees = list(count.items())
print(employees)
'''
count ={
    "john": 2,
    "alice" : 2,
    "bob" : 1
}

print(count.items())
employees = list(count.items())
#print(employees)
employees.sort()
print(employees)

def sort_by_work(item):
    return item[1]

employees.sort(key = sort_by_work,reverse = True)
print(employees)
def productivity_report(activities):
    #dict to store employee task count
    count = {}

    #traverse each activity
    for activity in activities:
        #John:Login --> name = John
        #task = Login
        name,task = activity.split()
        name = name.lower()                         #case sensitive --> name.lower

        #check if employee
        #already exsits in dict
        if name in count:
            count[name] +=1
        else:
            #add a new employee with count 1
            count[name] = 1
    employees = list(count.items())

#sort alphabetically by name
    def sort_by_name(item):
    #(John,2) --> tuple format
    #  0   1
        return item[0]
        employees.sort(key = sort_by_name)

#sort by task count
    def sort_by_count(item):
        return item[1]
        employees.sort(key = sort_by_count,reverse = True)
#input section
n = int(input())
#list to store activities
activities = []
for i in range(n):
    activity = input()

    activities.append(activity)
productivity_report(activities)
