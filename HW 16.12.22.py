# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = input('Введите число: ')
sum = 0
for i in range(len(n)):
    if n == float(n):
        z = int(n)
        x = (n - z)
        x = x * 10**(len(str(x))-2)
        while z > 0:
            sum += z % 10
            z //= 10
        while x > 0:
            sum += x % 10
            x //= 10
    else:
        sum += int(n[i])
print(sum)

# 2. Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Введите число '))
my_list = []
sum=0
for i in range(1,n+1):
    z = round((1 + 1/i)**i,2)
    my_list.append(z)
    sum += z
print(f'Для n = {n} -> {my_list}')
print(f'Сумма {sum}')


# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

from random import randint as ri
n = int(input('Введите кол-во чисел: '))
my_list = []
for i in range(n):
    my_list.append(ri(0, 20))
print(my_list)
for i in range(n):
    indeks = ri(0, n-1)
    z = my_list[i]
    my_list[i] = my_list[indeks]
    my_list[indeks] = z
print(my_list)
