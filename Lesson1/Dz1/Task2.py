# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#  Сколько журавликов сделал каждый ребенок, если известно,
#  что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
s = int(input("Amount:  "))
a = s / 2
P = int(a // 2)
S = int(a // 2)
K = int(a)
if s % 2 == 0:
    print(
        f"Петя сделал {int(P)} шт, Сережа сделал {int(S)} шт , Катя сделала {int(K)} шт")
else:
    print("Число не может быть не четным")
