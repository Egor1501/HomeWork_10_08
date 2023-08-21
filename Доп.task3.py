#Task 3
#Напишіть функцію, яка застосує до списку чисел довільну функцію користувача
# і поверне суми елементів отриманого списку.

def function(list,numbers):
    return sum(numbers(x) for x in list)

def function_add(x):
    return x * 3

list = [2,4,5,6,18,3,7]

print(function(list,function_add))