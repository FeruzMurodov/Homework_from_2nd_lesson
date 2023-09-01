# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random
count = int(input("Введите количество монеток: "))
stampSideOfCoin = 0
tailSideOfCoin = 0
for i in range(count) :
    coin = random.randrange(2)
    print(coin, end = " ")
    if coin == 0 :
        stampSideOfCoin += 1
    if coin == 1 :
        tailSideOfCoin += 1
print()
if stampSideOfCoin < tailSideOfCoin :
    print(stampSideOfCoin)
else :
    print(tailSideOfCoin)
