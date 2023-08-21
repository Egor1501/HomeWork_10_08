#task 2
#Реализуйте свой аналог генераторной функции range().


def my_range(start, stop, step):

    while start <= stop:
        yield start
        start += step

    return

for i in my_range(1, 50, 3):
    print(i)