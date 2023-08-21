#Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
# закон якої задається за допомогою функції користувача.
# Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів,
# що видаються послідовностю. Генератор повинен зупинити свою роботу або по досягненню n-го члена,
# або при передачі команди на завершення.

def val(x):
    return x ** 2


def some_gen(start, stop, func):
    for i in range(stop):
        yield start
        start = func(start)


print(list(some_gen(2, 5, val)))
