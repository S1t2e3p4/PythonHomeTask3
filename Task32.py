# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import os
os.system('cls')
import random

rand_list = []
n = random.randint(1,99)
for _ in range(n):
    rand_list.append(random.randint(1, 99))
print(f'{rand_list}\n Кол-во эл-тов в списке: {n}')
def product_of_pairs (lst):
    return [lst[i]*lst[-i-1] for i in range(len(lst)//2)]
print(f'Произведение "условных" пар чисел равно: {product_of_pairs (rand_list)}')