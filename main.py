from university import University

def display_menu(title: str, options: list[str]) -> int:
    print(f"\n{title}")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    c = input("Choose: ").strip()
    return int(c) if c.isdigit() else -1


def main():
    uni = University()
    while True:
        cmd = display_menu("Welcome: ", ["Register", "Login", "Exit"] )
        if cmd == 1:
            uni.register()
        elif cmd == 2:
            uni.login()
            if uni.current_user:
                role = uni.current_user["role"]
                while True:
                    if role == "student":
                        opts = ["Apply Course", "List My Courses", "Logout"]
                        a = display_menu("Student Menu", opts)
                        if a == 1: uni.apply_course()
                        elif a == 2: uni.list_enrolled_courses()  # or list enrolled
                        else: break
                    else:
                        opts = ["Create Course", "List Applicants", "Accept Applicant",
                                "Assign Student", "Remove Student", "Logout"]
                        a = display_menu("Professor Menu", opts)
                        if a == 1: uni.create_course()
                        elif a == 2: uni.list_applicants()
                        elif a == 3: uni.accept_applicant()
                        elif a == 4: uni.assign_student()
                        elif a == 5: uni.remove_student()
                        else: break
        elif cmd == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
