# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше
# введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random as rnd

print('** Отгадайте целое число от 0 до 100 **')
nmb = rnd.randint(0, 100)

max_tries = 10

for i in range(max_tries + 1):
    if i == max_tries:
        print(f'Попытки кончились. Загаданное число это {nmb}')
        break

    vrs = int(input(f'Попытка {i+1}: '))

    if(vrs == nmb):
        print('Вы угадали!')
        break
    else:
        print('Больше' if nmb > vrs else 'Меньше')
