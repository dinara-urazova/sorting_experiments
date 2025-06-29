def countBits(n: int) -> list[int]:
        counter = 0
        res =[0] * (n+1)
        for i in range(n+1):
            num = i
            while num:
                counter += 1
                res[i] += num & 1
                num>>=1
        return counter

res= countBits(50000)
print(res)