# Python Basics Assignment

## 1. Grade Checker

### Code

```python
score = int(input("Enter the student's score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Explanation

* Takes marks as input from the user.
* Uses `if-elif-else` conditions to check grade ranges.
* Displays the corresponding grade.

---

# 2. Student Grades Dictionary

### Code

```python
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
```

### Explanation

* Uses a dictionary to store student names and grades.
* Allows adding new students.
* Updates existing grades.
* Displays all records using loops and conditions.

---

# 3. Write to a File

### Code

```python
file = open("sample.txt", "w")

file.write("Hello! This is my first file handling program in Python.\n")
file.write("Python makes file operations easy.")

file.close()

print("Content written successfully.")
```

### Explanation

* `open()` with `"w"` mode creates or writes to a file.
* `write()` adds content to the file.
* `close()` saves and closes the file.

---

# 4. Read from a File

### Code

```python
file = open("sample.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()
```

### Explanation

* `open()` with `"r"` mode opens the file in read mode.
* `read()` reads the file content.
* `print()` displays the content on the screen.

---

# Author

Ketan Vyas
