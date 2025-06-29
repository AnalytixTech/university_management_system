from university import University


def display_menu(title: str, options: list[str]) -> int:
    print(f"\n{title}")
    for idx, opt in enumerate(options, 1):
        print(f"{idx}. {opt.title()}")
    choice = input("Choose an option: ").strip()
    return int(choice) if choice.isdigit() else -1


def main():
    uni = University()
    while True:
        main_opts = ["students", "courses", "professors", "exit"]
        choice = display_menu("Main Menu", main_opts)
        sub = ["add", "search", "list", "delete", "back"]
        if choice == 1:
            action = display_menu("Student Menu", sub)
            {1: uni.add_student, 2: uni.get_student, 3: uni.list_students, 4: uni.delete_student}.get(action, lambda: None)()
        elif choice == 2:
            action = display_menu("Course Menu", sub)
            {1: uni.add_course, 2: uni.get_course, 3: uni.list_courses, 4: uni.delete_course}.get(action, lambda: None)()
        elif choice == 3:
            action = display_menu("Professor Menu", sub)
            {1: uni.add_professor, 2: uni.get_professor, 3: uni.list_professors, 4: uni.delete_professor}.get(action, lambda: None)()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()