# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

# task 1
#
my_value = float(input('Введи число '))

while my_value <= 0 or my_value >= 10:
    my_value=float(input('Неверно '))

my_value=my_value ** 2
print(my_value)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

# task 2

a = int(input('Введи значение A '))
b = int(input('Введи значение B '))

b = a + b
a = b - a
b = b - a

print('a=', a, 'b=', b)
