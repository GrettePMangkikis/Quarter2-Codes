students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))
class_total = 0
for s in range(1, students + 1):
    print("Student", s)
    total = 0
    for S in range(1, subjects + 1):
            total = total + float(input(f"Enter score {S}:"))
            average = total / subjects
    print("Average for Student", s, "=", average)
    class_total = class_total + average
print("Class Average =", class_total)