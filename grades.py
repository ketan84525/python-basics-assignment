students = {}

while True:
    print("\nStudent Grade Menu")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Display All Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully.")

    elif choice == '2':
        name = input("Enter student name to update: ")

        if name in students:
            new_grade = input("Enter new grade: ")
            students[name] = new_grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == '3':
        print("\nStudent Grades:")

        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")