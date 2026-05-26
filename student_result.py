student_name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total_marks = maths + science + english
percentage = total_marks / 3

print("\nStudent Name:", student_name)
print("\nTotal Marks:", total_marks)
print("\nPercentage: {:.2f}".format(percentage))

if maths >= 35 and science >= 35 and english >= 35:
    print("\nStatus: PASS")

    if percentage >= 75:
        print("\nGrade: A")
    elif percentage >= 60:
        print("\nGrade: B")
    elif percentage >= 50:
        print("\nGrade: C")
    else:
        print("\nGrade: D")
else:
    print("\nStatus: FAIL")