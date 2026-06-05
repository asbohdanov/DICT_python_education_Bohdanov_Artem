#↓ Функція, що виводить список доступних команд
def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line line-break")
    print("Special commands: !help !done")


#↓ Основна функція консолі
def main():
    #↓ Список підтримуваних засобів форматування
    formatters={"plain", "bold", "italic", "header", "link","inline-code", "ordered-list", "unordered-list", "new-line", "line-break"}

    #↓ Змінна для накопичення результату форматування
    markdown_text = ""

    while True:
        user_input = input("Choose a formatter: > ").strip()

        #↓ Обробка спеціальних команд
        if user_input == "!done":
            with open("output.md", "w", encoding="utf-8") as file:
                file.write(markdown_text)
            break
        elif user_input == "!help":
            print_help()
            continue

        #↓ Перевірка правильності введення
        if user_input not in formatters:
            print("Unknown formatting type or command")
            continue

        #↓ Обробка засобів форматування
        formatted_chunk = ""

        if user_input == "new-line" or user_input == "line-break":
            formatted_chunk = "\n"

        elif user_input == "header":
            while True:
                try:
                    level = int(input("Level: > "))
                    if 1 <= level <= 6:
                        break
                    else:
                        print("The level should be within the range of 1 to 6")
                except ValueError:
                    print("The level should be within the range of 1 to 6")

            text = input("Text: > ")

            formatted_chunk = f"{'#' * level} {text}\n"

        elif user_input == "link":
            label = input("Label: > ")
            url = input("URL: > ")
            formatted_chunk = f"[{label}]({url})"

        elif user_input in {"ordered-list", "unordered-list"}:
            #↓ Перевірка кількості рядків списку
            while True:
                try:
                    rows_count = int(input("Number of rows: > "))
                    if rows_count > 0:
                        break
                    else:
                        print("The number of rows should be greater than zero")
                except ValueError:
                    print("The number of rows should be greater than zero")

            # Введення елементів списку
            list_items = []
            for i in range(1, rows_count + 1):
                row_text = input(f"Row #{i}: > ")

                if user_input == "ordered-list":
                    list_items.append(f"{i}. {row_text}\n")
                else:
                    list_items.append(f"* {row_text}\n")

            #↓ Об'єднуємо всі рядки в один текст
            formatted_chunk = "".join(list_items)

        else:
            text = input("Text: > ")

            if user_input == "plain":
                formatted_chunk = text
            elif user_input == "bold":
                formatted_chunk = f"**{text}**"
            elif user_input == "italic":
                formatted_chunk = f"*{text}*"
            elif user_input == "inline-code":
                formatted_chunk = f"`{text}`"

        #↓ Додаємо відформатований текст до загального
        markdown_text += formatted_chunk

        #↓ Виводимо всю накопичену розмітку
        print(markdown_text)

main()