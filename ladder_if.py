marks = int(input("Enter The Marks: \n"))

if marks >= 90:
    grade = 'A'
elif marks >=80:
    grade = 'B'
elif marks >=70:
    grade = 'C'
elif marks >=60:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is: " + grade)