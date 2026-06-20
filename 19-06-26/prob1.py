def count_lines(filename):
    with open("students.txt","r") as file:
        return len(file.readlines())
def count_words(filename):
    with open("students.txt","r") as file:
        return len(file.read().split())
def count_characters(filename):
    with open("students.txt","r") as file:
        return len(file.read())