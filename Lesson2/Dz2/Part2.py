# n = int(input())
# sum = int(input())
# mult = int(input())
# first, second = 0
# sum = first + second
# mult = first * second
# for _ in range(n):
#     if (first, second < 1000):
#         first += 1
#         second += 1
#     print(first)
#     print(second)

# Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница. Петя помогает Кате
# по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input())
p = int(input())

x1 = (-(-s) - (s**2 - 4 * p)**0.5) / 2
x2 = (-(-s) + (s**2 - 4 * p)**0.5) / 2

print(f'The first {int(x1)}, the second {int(x2)}.')
