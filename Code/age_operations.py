def check_age_and_display_birth_info(student):
    if student['age'] % 2 == 0:
        birth_year = 2024 - student['age']
        print(f"Ваш рік народження: {birth_year}")
    else:
        print("Ваш місяць народження: вересень")  # Як приклад місяця
