# Посчитать, сколько раз встречается определенная цифра в введенной
# последовательности чисел. Количество вводимых чисел и цифра,
# которую необходимо посчитать, задаются вводом с клавиатуры.

import re

sequence = input('Введите последовательноть: ')
query = input('Введите число для поиска: ')
s_res = re.findall(query, sequence)
print(f'Найдено {len(s_res)} вхождений')
