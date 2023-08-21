#Task 5
#Реалізуйте генераторну функцію, яка повертатиме елементи послідовності чисел Фібоначчі.

def fibonacci():
    previous, current = 0, 1

    def inner():
        nonlocal previous, current
        previous, current = current, current + previous
        return previous

    return inner


f = fibonacci()
for _ in range(10):
    print(f())