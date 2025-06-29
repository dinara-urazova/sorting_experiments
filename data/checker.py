from sys import argv


input()  # считываем кол-во секунд
input()  # кол-во перестановок
n = int(input()) # кол-во элементов

current = None
previous = -1000000000

for i in range(n-1):
    current = int(input())
    if previous > current:
        print (f"The sorting fails at position {i+2}: array[{i+1}] = {previous}, array[{i+2}] = {current}")
        exit()
    previous = current
print("OK")

