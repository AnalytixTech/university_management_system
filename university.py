from db import users_col, students_col, professors_col, courses_col
from models import Student, Professor, Course
from validators import (validate_email, InvalidEmailError,
                        hash_password, verify_password, AuthenticationError)

class University:
    def __init__(self):
        self.current_user = None

    def register(self):
        print("--- Registration ---")
        role = input("Select role (student/professor): ").strip().lower()
        if role not in ("student", "professor"):
            print("Invalid role.")
            return
        id_    = input(f"Enter {role} ID: ").strip()
        name   = input(f"Enter {role} name: ").strip()
        email  = input("Enter email: ").strip()
        pwd    = input("Enter password: ").strip()
        try:
            validate_email(email)
        except InvalidEmailError as e:
            print(e); return
        if users_col.find_one({"email": email}):
            print("Email already registered.")
            return
        users_col.insert_one({
            "id": id_, "name": name, "email": email,
            "password": hash_password(pwd), "role": role
        })
        if role == "student":
            students_col.insert_one(Student(id_, name, email).to_dict())
        else:
            dept = input("Enter department: ").strip()
            professors_col.insert_one(Professor(id_, name, email, dept).to_dict())
        print("Registration successful!")

    def login(self):
        print("--- Login ---")
        email = input("Email: ").strip()
        pwd   = input("Password: ").strip()
        user = users_col.find_one({"email": email}, {"_id": 0})
        if not user or not verify_password(pwd, user["password"]):
            print("Invalid credentials.")
            return
        self.current_user = user
        print(f"Logged in as {user['role']} {user['name']}")

    def require_login(func):
        def wrapper(self, *args, **kwargs):
            if not self.current_user:
                print("Please login first.")
                return
            return func(self, *args, **kwargs)
        return wrapper

    def require_role(role):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if not self.current_user or self.current_user.get("role") != role:
                    print(f"Action requires {role} role.")
                    return
                return func(self, *args, **kwargs)
            return wrapper
        return decorator

    @require_login
    @require_role("professor")
    def create_course(self):
        code = input("Course code: ").strip()
        if courses_col.find_one({"code": code}):
            print("Course code exists.")
            return
        title   = input("Title: ").strip()
        creds   = input("Credits: ").strip()
        if not creds.isdigit():
            print("Credits must be numeric.")
            return
        prof_id = self.current_user["id"]
        c = Course(code, title, int(creds), prof_id)
        courses_col.insert_one(c.to_dict())
        print("Course created.")

    @require_login
    @require_role("student")
    def apply_course(self):
        code = input("Course code to apply: ").strip()
        if not courses_col.find_one({"code": code}):
            print("Course not found.")
            return
        courses_col.update_one({"code": code}, {"$addToSet": {"applications": self.current_user["id"]}})
        print("Applied to course.")

    @require_login
    @require_role("professor")
    def list_applicants(self):
        code = input("Course code: ").strip()
        course = courses_col.find_one({"code": code}, {"_id": 0})
        if not course:
            print("Course not found.")
            return
        apps = course.get("applications", [])
        print(f"Applicants: {apps}")

    @require_login
    @require_role("professor")
    def accept_applicant(self):
        code = input("Course code: ").strip()
        sid  = input("Student ID to accept: ").strip()
        res = courses_col.update_one(
            {"code": code},
            {"$pull": {"applications": sid}, "$addToSet": {"enrolled": sid}}
        )
        if res.modified_count:
            print("Student accepted.")
        else:
            print("No such application or already enrolled.")

    @require_login
    @require_role("professor")
    def assign_student(self):
        code = input("Course code: ").strip()
        sid  = input("Student ID to assign: ").strip()
        courses_col.update_one({"code": code}, {"$addToSet": {"enrolled": sid}})
        print("Student assigned.")

    @require_login
    @require_role("professor")
    def remove_student(self):
        code = input("Course code: ").strip()
        sid  = input("Student ID to remove: ").strip()
        courses_col.update_one({"code": code}, {"$pull": {"enrolled": sid}})
        print("Student removed.")

    @require_login
    @require_role("student")
    def list_enrolled_courses(self):
        sid = self.current_user["id"]
        enrolled = courses_col.find({"enrolled": sid}, {"_id": 0})
        print("--- My Courses ---")
        for course in enrolled:
            print(f"{course['code']} - {course['title']}")
