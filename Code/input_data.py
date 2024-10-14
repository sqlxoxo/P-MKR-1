def input_personal_data():
    student = {}
    student['name'] = input("Введіть ПІБ: ")
    student['gender'] = input("Введіть стать: ")
    student['age'] = int(input("Введіть вік: "))
    student['phone'] = input("Введіть номер телефону: ")
    return student

def input_hobbies():
    hobbies = []
    for i in range(3):  # Введемо 3 хобі
        hobby = {}
        hobby['name'] = input(f"Введіть назву хобі #{i+1}: ")
        hobby['description'] = input("Опишіть своє хобі у 3х реченнях: ")
        hobbies.append(hobby)
    return hobbies
