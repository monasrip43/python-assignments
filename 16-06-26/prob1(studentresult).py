class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_pass(self):
        return self.marks>=40
try:
    pass_count=0
    with open("students.txt","r") as file:
        for line in file:
            line=line.strip()
            if not line:
                continue
            if "," in line:
                name,marks_str=line.split(",",1)
                try:
                    marks=int(marks_str)
                    student=Student(name,marks)
                    if student.is_pass():
                        pass_count+=1
                except ValueError:
                    pass
    print(pass_count)
except FileNotFoundError:
    print("File Not Found")
