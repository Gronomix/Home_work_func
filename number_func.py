'''Напишите функцию, которая может принимать произвольное колличество аргументов (целых чисел)
 и определятьб сколько среди них двухзначных и трехзначных чисел. Определение количетсва разрядов  в числе
  также оформить в виде отдельной функции'''


def discharge(*args):
    k, t = [len(list(filter(lambda x: digits_amount(x) == z, args))) for z in (3, 2)]
    return {'Всего трехзначных чисел': k, 'Всего двухзначных чисел': t}


def digit(*args):
    s = {}
    for i in args:
        n = str(i)
        len_n = len(n)
        s.update({i: len_n})
    return s

def digits_amount(n):
    return len(str(n))


print(discharge(3, 2, 86, 1423, 4234, 25, 332))
print(discharge(222, 4444, 3, 33, 55, 67, 765))
print(digits_amount(discharge()))
print(digit(3, 2, 86, 1423, 4234, 25, 332))