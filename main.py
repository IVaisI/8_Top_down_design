from menu_function import f1, f2, f3, print_text
from new_functions import is_int

def menu():
    result = []
    text_input = False

    while 1:
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста \n"
              "2. Выполнение алгоритма подсчета количества слов в тексте\n"
              "3. Вывод результата\n"
              "4. Вывод текста\n"
              "5. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)

        if choice == 1:
            text_input = f1()

        elif choice == 2:
            if text_input:
                result = f2()
            else:
                print("Ошибка!\nСначала введите текст\n\n")
        elif choice == 3:
            if text_input:
                f3(result)
        elif choice == 4:
            if text_input:
                print_text()
            else:
                print("Ошибка!\nСначала введите текст\n\n")
        elif choice == 5:
            break
        else:
            print('error')

if __name__ == "__main__":
    menu()
