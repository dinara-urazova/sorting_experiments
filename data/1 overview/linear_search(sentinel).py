def fn(array,x,n):
    last = array[n]
    array[n] = x
    i = 0
    while array[i] != x:
        i +=1
    array[n] = last
    if i < n or array[n] == x:
        return i
    return "Not found"
    
array=[3,4,6,8,2,5]
x = 10
n = len(array)-1
result = fn(array,x,n)
if result != "Not found":
    print(f"Value {x} is on position {result} of the array")
print(f"The value {x} is not in the array")