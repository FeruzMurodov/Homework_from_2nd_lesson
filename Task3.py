# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.


n = int(input("Введите число: "))
multiply = 2
degree = 1
print(f"2^{degree}; ")
while multiply < n :
    multiply *= 2
    degree += 1
    if multiply <= n :
        print(f"2^{degree}; ")
    else :
        print(f"2^{degree-1}; ")