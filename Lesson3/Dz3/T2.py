# Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
#  В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Input how many numbers in array: "))
list = [int(input()) for _ in range(n)]
num = int(input("Number: "))

list.append(num)
list.sort()
if num != max(list):
    i_number = list.index(num)
    if list[i_number] - list[i_number - 1] > list[i_number + 1] - list[i_number]:
        print(f"Neighbour of number {num} is {list[i_number + 1]}")
    elif list[i_number] - list[i_number - 1] == list[i_number + 1] - list[i_number]:
        print(f"Neighbour of number {num} is {min(list[i_number + 1], list[i_number - 1])}")
    else:
         print(f"Neighbour of number {num} is {list[i_number - 1]}")

else:
    print(f"Neighbour of number {num} is {list[len(list)-2]}")