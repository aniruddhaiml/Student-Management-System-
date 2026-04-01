# Student Management System (Best Version)

import json

# 🔹 Load students
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except:
        return []

# 🔹 Save students
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

# 🔹 Add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    # 🚫 Prevent duplicate roll number
    for s in students:
        if s["roll"] == roll:
            print("❌ Roll number already exists!")
            return

    student = {"name": name, "roll": roll, "course": course}
    students.append(student)
    save_students()
    print("✅ Student added successfully!")

# 🔹 Show students
def show_students():
    if not students:
        print("⚠️ No students found.")
    else:
        print("\n📋 Student List:")
        for s in students:
            print(f"Name: {s['name']} | Roll: {s['roll']} | Course: {s['course']}")

# 🔹 Search student
def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print("✅ Student Found:")
            print(f"Name: {s['name']} | Roll: {s['roll']} | Course: {s['course']}")
            return
    print("❌ Student not found!")

# 🔹 Delete student
def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students()
            print("🗑️ Student deleted successfully!")
            return
    print("❌ Student not found!")

# 🔹 Update student
def update_student():
    roll = input("Enter roll number to update: ")
    for s in students:
        if s["roll"] == roll:
            print("Leave blank to keep old value")

            new_name = input("Enter new name: ")
            new_course = input("Enter new course: ")

            if new_name:
                s["name"] = new_name
            if new_course:
                s["course"] = new_course

            save_students()
            print("✏️ Student updated successfully!")
            return
    print("❌ Student not found!")

# 🔥 Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT MENU =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice == "6":
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice, try again!")