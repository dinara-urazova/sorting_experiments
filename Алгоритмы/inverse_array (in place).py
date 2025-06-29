
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))

#Вариант 2
# def reverse_list(arr):
#     n = len(arr)
#     i = 0
#     for i in range(n//2):
#         arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
#     return arr

# arr = [1, 2, 3, 4, 5, 6, 7]
# print(reverse_list(arr))

