#Використовуючи замикання, реалізуйте такий прийом програмування
# як Мемоізація - https://en.wikipedia.org/wiki/Memoization .
#Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
# Порівняйте швидкість виконання із просто рекурсивним підходом.

from datetime import datetime
import time


def fib(n):
      if n <= 1:
          return n
      else:
          return fib(n - 1) + fib(n - 2)


start_time = datetime.now()
print(fib(30))
print(start_time)


cache = {}


def fibonachi(cache = {}):
    def get_num(a):
        if a in cache:
            return cache[a]
        result = 0
        if a <= 1:
            result = a
        else:
            result = fibonachi(a - 1) + fibonachi(a - 2)
        cache[a] = result
        return cache
    return get_num


start_fib = datetime.now()
print(fib(30))
print(start_fib)

start_fibonachi = datetime.now()
print(fibonachi(30))
print(start_fibonachi)
print(start_fibonachi - start_fib)






