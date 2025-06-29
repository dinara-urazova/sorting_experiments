from sys import argv

def compare_increase (prev: int, curr: int) -> bool:
      return prev <= curr

def compare_decrease (prev: int, curr: int) -> bool:
      return prev >= curr

mode = str(argv[1])
if mode == "increase":
      compare_fn = compare_increase 
elif mode=="decrease":
      compare_fn = compare_decrease 
else:
      print("Warning. I will compare using compare strategy")
      compare_fn = compare_increase

input()  # считываем кол-во секунд
input()  # кол-во перестановок
n = int(input()) # кол-во элементов



current = None
previous = -1000000000

for i in range(n-1):
    current = int(input())
    if not compare_fn(previous, current):
            print (f"The sorting fails at position {i+2}: array[{i+1}] = {previous}, array[{i+2}] = {current}")
            exit()
    previous = current
print("OK")



# def compare_increase(a: int, b: int) -> bool:
#     if a < b :
#         return True
#     else:
#         return False
    
# def compare_decrease(a: int, b: int) -> bool:
#     if a > b :
#         return True
#     else:
#         return False