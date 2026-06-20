class Student:
    def __init__(self,roll_number,name,attendance):
        self.roll_number=roll_number
        self.student_name=name
        self.attendence=attendance
    def calculate_attendence(self):
        present=self.attendence.count("p")
        total=len(self.attendence)
        return (present/total)*100
    def longest_attendence_streak(self):
        current=0
        maximum=0
        for ch in self.attendence:
            if ch=="p":
                current+=1
                if current>maximum:
                    maximum=current
            else:
                current=0
        return maximum
n=int(input())
students=[]
topper=None
highest_percentage=0
streak_holder=None
max_streak=0
for _ in range(n):
    roll_number=input()
    name=input()
    attendence=input()
    s=Student(roll_number,name,attendence)
    students.append(s)
print("Attendence Percentage:")
for s in students:
    percent=s.calculate_attendence()
    print(s.roll_number,s.student_name,f"{percent:2f}%")
    if percent>highest_percentage:
        highest_percentage=percent
        topper=s
    streak=s.longest_attendence_streak()
    if streak>max_streak:
        max_streak=streak
        streak_holder=s
print("Defaulters:")
for s in students:
    if s.calculate_attendence()<75:
        print(s.roll_number,s.student_name)
print("Attendence topper:",topper.roll_number,topper.student_name,f"{highest_percentage:.2f}%")
print("Maximum Streak holder:",streak_holder.roll_number,streak_holder.student_name,max_streak)