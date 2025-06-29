
def input_data():
    n = int(input())
    sum=0
    for i in range(n):
        sum+=i
    return sum
    
def exp (dig):
    return dig**2
    
def output(a,b):
    print(a,b)

nums = input_data()  
res = exp(nums)
output(nums,res)