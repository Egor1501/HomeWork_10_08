#task4
#Напишіть генераторний вираз для заповнення списку.
# Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.

def my_list(A):
    return [i ** 3 for i in range(2, A)]


print(my_list(10))


# Вариант 2
list_1 = [x**3 for x in range(2,11)]
print(list_1)

# Вариант 3
list_2 = []
[list_2.append(x**3) for x in range(2,11)]
print(list_2)