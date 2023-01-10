# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
os.system('cls')
import random

rand_list = []
n = random.randint(3,9)
for _ in range(n):
    rand_list.append(random.uniform(1, 20))
print(f'{rand_list}\n Кол-во эл-тов в списке: {n}')
def max_decimal (lst):
    decimal_parts = [x-int(x) for x in lst]
    return max (decimal_parts)
print(f'Максимальное значение дробной части элемента списка равно: {max_decimal (rand_list)}')
def min_decimal (lst):
    decimal_parts = [x-int(x) for x in lst]
    return min (decimal_parts)
print(f'Минимальное значение дробной части элемента списка равно: {min_decimal (rand_list)}')
def decimal_difference (lst):
    decimal_parts = [x-int(x) for x in lst]
    return max (decimal_parts) - min(decimal_parts)
print(f'Разница между между максимальным и минимальным значением дробной части элементов списка равна: {decimal_difference (rand_list)}')