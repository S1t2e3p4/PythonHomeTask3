# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
os.system('cls')
import random

rand_list = []
n = random.randint(1,99)
for _ in range(n):
    rand_list.append(random.randint(1, 99))
print(f'{rand_list}\n Кол-во эл-тов в списке: {n}')
def sum_of_odd_position_elements (lst):
    return sum (lst[i] for i in range (len(lst)) if i%2!=0)
print(f'Сумма элементов стоящих на начётной позиции равна: {sum_of_odd_position_elements (rand_list)}')