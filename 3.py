#task 3
#Напишіть генераторну функцію, яка повертатиме прості числа.
# Верхня межа діапазону повинна бути задана параметром цієї функції.

def prime_num(limit):
    for i in range(2, limit):
        x = 2
        while x < i:
            if i % x != 0:
                x+=1
            else:
                break
        else:
            yield i


