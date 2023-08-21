#Task 1
#Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.
def geometry(start, stop):
    index = 1
    while index <= stop:
        new_number = start * 2
        yield new_number
        start = new_number
        index += 1
    return

for i in geometry(1, 10):
    print(i)

# 2-й вариант
def geometry(start, stop):
    index = 1
    while index <= stop:
        new_number = start * 3
        yield new_number
        start = new_number
        index += 1
    return

for i in geometry(1, 10):
    print(i)

# 3-й вариант
def gen(max_number, factor):
    i = 1
    while i <= max_number:
        yield i
        i = i * factor
    return


g = gen(100, 4)
print(next(g))
print(next(g))
print(g.close())