# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4
n = int(input('Введите целое число от 1 до 9: '))
while n < 1 or n > 9:
    print('Число введено неверно')
    n = int(input('Введите целое число от 1 до 9: '))
print('n^2 = ' + str(n ** 2))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))
n = n + m # в первой переменной сумма, вторая осталась неизменной
m = n - m # теперь во второй переменной оказывается первое значение
n = n - m # а в первой переменной - второе
print(n, m)

