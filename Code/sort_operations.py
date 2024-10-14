def set_hobby_priorities(hobbies):
    for hobby in hobbies:
        hobby['priority'] = int(input(f"Задайте пріоритет для хобі '{hobby['name']}' (1-5): "))
    return hobbies

def sort_hobbies(hobbies, order="descending"):
    if order == "descending":
        return sorted(hobbies, key=lambda x: x['priority'], reverse=True)
    else:
        return sorted(hobbies, key=lambda x: x['priority'])

def sort_phone_number(student):
    phone_digits = [int(digit) for digit in student['phone'] if digit.isdigit()]
    # Сортування методом бульбашки
    for i in range(len(phone_digits)):
        for j in range(0, len(phone_digits) - i - 1):
            if phone_digits[j] > phone_digits[j + 1]:
                phone_digits[j], phone_digits[j + 1] = phone_digits[j + 1], phone_digits[j]
    print(f"Відсортовані цифри номеру телефону: {''.join(map(str, phone_digits))}")
