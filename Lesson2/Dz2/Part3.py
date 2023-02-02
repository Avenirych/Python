# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input())
twokv = 2

while twokv <= num:
    print(twokv, end=" ")
    twokv *= 2