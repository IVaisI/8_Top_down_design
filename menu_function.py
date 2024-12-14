from pyexpat.errors import messages
from new_functions import input_text, random_text, is_int
from collections import Counter
import re
def f1():
    global message
    print("Выберите тип ввода:\n1. Ввод текста с клавиатуры\n2. Случайная генерация")
    type = input()

    if is_int(type):
        type = int(type)
    if type == 1:
        message = input_text()
        print(f"Вы ввели следующий текст: {message} ")
    elif type == 2:
        message = random_text()
        print(f"Сгенерированный текст: {message}")
    else:
        print('error')
    return True

def f2():
    text = message.lower()
    text = re.sub(r'[^\w\s]', '', text)

    words = text.split()
    result_word_count = len(words)
    print("Алгоритм выполнен\n")
    return result_word_count

def f3(word_count):
    print(f"Количество слов в тексте: {word_count}")

def print_text():
    print(f"Введенный текст:\n{message}")