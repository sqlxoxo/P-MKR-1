def first_sentence_of_hobbies(hobbies):
    for hobby in hobbies:
        first_sentence = hobby['description'].split('.')[0]
        print(f"Перша пропозиція хобі '{hobby['name']}': {first_sentence}")

def count_characters_in_hobbies(hobbies):
    total_characters = sum(len(hobby['name']) for hobby in hobbies)
    print(f"Загальна кількість символів у назвах хобі: {total_characters}")

def count_words_in_hobbies(hobbies):
    total_words = sum(len(hobby['description'].split()) for hobby in hobbies)
    print(f"Загальна кількість слів в описах хобі: {total_words}")
