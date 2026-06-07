import random
from datetime import datetime

def test_ex(level):
    #↓ Рівень 1 - прості операції
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        c = random.randint(1, 3)

        if c == 1:
            correct_answer = a + b
            operator = "+"
        elif c == 2:
            correct_answer = a - b
            operator = "-"
        elif c == 3:
            correct_answer = a * b
            operator = "*"

        print(a, operator, b)

    #↓ Рівень 2 - зведення у квадрат чисел від 11 до 29
    elif level == 2:
        a = random.randint(11, 29)
        correct_answer = a ** 2
        print(a)

    #↓ Перевірка корректності вводу
    while True:
        try:
            answer = int(input("> "))
            break
        except ValueError:
            print("Incorrect format.")

    #↓ Перевірка правильності відповіді
    if answer == correct_answer:
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


#↓ Вибір рівня складності
while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    level_input = input("> ")
    if level_input == "1" or level_input == "2":
        level = int(level_input)
        break
    else:
        print("Incorrect format.")


#↓ Проведення тесту з 5 завдань
mark1 = 0
for i in range(5):
    mark1 += test_ex(level)

#↓ Виведення результату
print(f"Your mark is {mark1}/5.")

#↓ Запит на проходження 2 рівня
if level == 1:
    print("Would you like to complete 2-nd level?")
    rerun = input("> ").strip().lower()

    # ↓ Перевірка вибору
    if rerun in ["yes", "y"]:
        #↓ Другий цикл проходження
        mark2 = 0
        level = 2

        for i in range(5):
            mark2 += test_ex(level)
        print(f"Your mark is {mark2}/5.")

        # ↓ Запит на збереження файлу
        print("Would you like to save your result to the file? Enter yes or no.")
        save_choice = input("> ").strip().lower()

        # ↓ Перевірка вибору
        if save_choice in ["yes", "y"]:
            # ↓ Визначення опису для файлу
            name = input("What is your name?\n> ")

            # ↓ Запис у файл
            time = datetime.now()
            with open("results.txt", "a", encoding="utf-8") as file:
                file.write(f"{name}: {mark1}/5 in level 1 (simple operations with numbers 2-9), {mark2}/5 in level 2 (integral squares of 11-29), time: {time}.\n")
            print('The results are saved in "results.txt".')
        else:
            print("Exiting program.")

    else:
        print("Would you like to save your result to the file? Enter yes or no.")
        save_choice = input("> ").strip().lower()

        if save_choice in ["yes", "y"]:

            name = input("What is your name?\n> ")

            time = datetime.now()
            with open("results.txt", "a", encoding="utf-8") as file:
                file.write(f"{name}: {mark1}/5 in level 1 (simple operations with numbers 2-9), time: {time}.\n")
            print('The results are saved in "results.txt".')

        else:
            print("Exiting program.")

else:

    print("Would you like to save your result to the file? Enter yes or no.")
    save_choice = input("> ").strip().lower()


    if save_choice in ["yes", "y"]:

        name = input("What is your name?\n> ")

        time = datetime.now()
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"{name}: {mark1}/5 in level 2 (integral squares of 11-29), time: {time}.\n")
        print('The results are saved in "results.txt".')

    else:
        print("Exiting program.")
#↑ Виведення результату в файл мало би бути функцією, але вже пізно, до того ж є свої справи, тому хай залишається так...