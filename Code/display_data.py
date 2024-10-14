def display_data(student, hobbies):
    print("\nОсобисті дані:")
    for key, value in student.items():
        print(f"{key}: {value}")
    print("\nХобі:")
    for hobby in hobbies:
        print(f"Назва: {hobby['name']}")
        print(f"Опис: {hobby['description']}")
