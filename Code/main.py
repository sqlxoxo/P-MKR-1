from input_data import input_personal_data, input_hobbies
from display_data import display_data
from sort_operations import set_hobby_priorities, sort_hobbies, sort_phone_number
from hobbies_analysis import first_sentence_of_hobbies, count_characters_in_hobbies, count_words_in_hobbies
from age_operations import check_age_and_display_birth_info

def main():
    # Введення даних
    student = input_personal_data()
    hobbies = input_hobbies()

    # Виведення введених даних
    display_data(student, hobbies)

    # Пріоритети та сортування
    hobbies = set_hobby_priorities(hobbies)
    sorted_hobbies = sort_hobbies(hobbies, order="descending")
    print("\nХобі, відсортовані за пріоритетом:")
    for hobby in sorted_hobbies:
        print(f"{hobby['name']} (Пріоритет: {hobby['priority']})")

    # Сортування номеру телефону
    sort_phone_number(student)

    # Обробка опису хобі
    print("\nПерша пропозиція для кожного хобі:")
    first_sentence_of_hobbies(hobbies)

    # Кількість символів та слів
    count_characters_in_hobbies(hobbies)
    count_words_in_hobbies(hobbies)

    # Перевірка віку
    check_age_and_display_birth_info(student)

if __name__ == "__main__":
    main()
