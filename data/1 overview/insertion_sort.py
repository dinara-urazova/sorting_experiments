def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1]= arr[j]
            j = j - 1
        arr[j+1] = key

array = [12,9,3,7,14,11]
n = len(array)
insertion_sort(array, n)
print(array) 