students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        for roll, info in students.items():
            print("Roll:", roll, "| Name:", info["Name"], "| Marks:", info["Marks"])

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        marks = input("Enter new marks: ")
        students[roll]["Marks"] = marks
        print("Student updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")