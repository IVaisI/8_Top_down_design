import random
def is_int(choice):
    """ Проверка на то, что s - целое число для меню"""
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False
def input_text():
    text = input("Введите текст для обработки (для завершения ввода нажмите клавишу Enter): ")
    while 1:
        line = input()
        if line == "":
            break
        text += "\n" + line
    return text

def random_text():
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' + ' ' * 7
    length = random.randint(20, 100)  # Генерация случайной длины
    return ''.join(random.choice(letters) for i in range(length))
#commit