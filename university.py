from models import Student, Professor, Course
from data.file_handler import (
    append_json, read_json, write_json,
    update_json, delete_json
)
from validators import validate_email, InvalidEmailError

class University:
    """Service layer for managing students, professors, and courses."""

    @staticmethod
    def add_student():
        try:
            id_ = input("Enter student's ID: ").strip()
            name = input("Enter student's name: ").strip()
            email = input("Enter student's Email: ").strip()
            validate_email(email)
        except InvalidEmailError as e:
            print(e)
            return
        students = read_json("students.json")
        if any(s["id"] == id_ or s["email"] == email for s in students):
            print("Student ID or Email already exists.")
            return
        new_student = Student(id_, name, email)
        append_json("students.json", new_student.to_dict())
        print("Student added successfully!")

    @staticmethod
    def get_student():
        id_ = input("Enter student's ID: ").strip()
        students = read_json("students.json")
        for s in students:
            if s["id"] == id_:
                print("Student Details\n" + "-"*20)
                print(f"ID: {s['id']}\nName: {s['name']}\nEmail: {s['email']}")
                return
        print(f"Error: Student ID {id_} not found.")

    @staticmethod
    def list_students():
        students = read_json("students.json")
        header = f"{'ID':<10} | {'Name':<20} | {'Email':<30}"
        print(header)
        print("-" * len(header))
        for s in students:
            print(f"{s['id']:<10} | {s['name']:<20} | {s['email']:<30}")

    @staticmethod
    def delete_student():
        id_ = input("Enter student's ID: ").strip()
        students = read_json("students.json")
        student = next((s for s in students if s['id'] == id_), None)
        if not student:
            print(f"Error: Student ID {id_} not found.")
            return
        confirm = input(f"Delete {student['name']} (ID: {id_})? [y/N]: ").strip().lower()
        if confirm == 'y':
            delete_json("students.json", 'id', id_)
            print("Student deleted successfully.")

    @staticmethod
    def add_professor():
        try:
            id_ = input("Enter professor's ID: ").strip()
            name = input("Enter professor's name: ").strip()
            email = input("Enter professor's Email: ").strip()
            validate_email(email)
            department = input("Enter department: ").strip()
        except InvalidEmailError as e:
            print(e)
            return
        profs = read_json("professors.json")
        if any(p["id"] == id_ or p["email"] == email for p in profs):
            print("Professor ID or Email already exists.")
            return
        new_prof = Professor(id_, name, email, department)
        append_json("professors.json", new_prof.to_dict())
        print("Professor added successfully!")

    @staticmethod
    def get_professor():
        id_ = input("Enter professor's ID: ").strip()
        profs = read_json("professors.json")
        for p in profs:
            if p["id"] == id_:
                print("Professor Details\n" + "-"*20)
                print(f"ID: {p['id']}\nName: {p['name']}\nEmail: {p['email']}\nDepartment: {p['department']}")
                return
        print(f"Error: Professor ID {id_} not found.")

    @staticmethod
    def list_professors():
        profs = read_json("professors.json")
        header = f"{'ID':<10} | {'Name':<20} | {'Email':<30} | {'Department':<20}"
        print(header)
        print("-" * len(header))
        for p in profs:
            print(f"{p['id']:<10} | {p['name']:<20} | {p['email']:<30} | {p['department']:<20}")

    @staticmethod
    def delete_professor():
        id_ = input("Enter professor's ID: ").strip()
        profs = read_json("professors.json")
        prof = next((p for p in profs if p['id'] == id_), None)
        if not prof:
            print(f"Error: Professor ID {id_} not found.")
            return
        confirm = input(f"Delete {prof['name']} (ID: {id_})? [y/N]: ").strip().lower()
        if confirm == 'y':
            delete_json("professors.json", 'id', id_)
            print("Professor deleted successfully.")

    @staticmethod
    def add_course():
        code = input("Enter course code: ").strip()
        title = input("Enter course title: ").strip()
        credits = input("Enter credits (integer): ").strip()
        professor = input("Enter professor ID: ").strip()
        if not credits.isdigit():
            print("Credits must be a number.")
            return
        courses = read_json("courses.json")
        if any(c["code"] == code for c in courses):
            print("Course code already exists.")
            return
        new_course = Course(code, title, int(credits), professor)
        append_json("courses.json", new_course.to_dict())
        print("Course added successfully!")

    @staticmethod
    def get_course():
        code = input("Enter course code: ").strip()
        courses = read_json("courses.json")
        for c in courses:
            if c["code"] == code:
                print("Course Details\n" + "-"*20)
                print(f"Code: {c['code']}\nTitle: {c['title']}\nCredits: {c['credits']}\nProfessor: {c['professor']}")
                return
        print(f"Error: Course code {code} not found.")

    @staticmethod
    def list_courses():
        courses = read_json("courses.json")
        header = f"{'Code':<10} | {'Title':<30} | {'Credits':<7} | {'Professor':<10}"
        print(header)
        print("-" * len(header))
        for c in courses:
            print(f"{c['code']:<10} | {c['title']:<30} | {c['credits']:<7} | {c['professor']:<10}")

    @staticmethod
    def delete_course():
        code = input("Enter course code: ").strip()
        courses = read_json("courses.json")
        course = next((c for c in courses if c['code'] == code), None)
        if not course:
            print(f"Error: Course code {code} not found.")
            return
        confirm = input(f"Delete {course['title']} (Code: {code})? [y/N]: ").strip().lower()
        if confirm == 'y':
            delete_json("courses.json", 'code', code)
            print("Course deleted successfully.")