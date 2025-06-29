# n - number of elements to generate
# min - maximum possible value 
# max - maximum possible value
from sys import argv
from random import randint

# n = int(argv[1])
# min = int(argv[2])
# max = int(argv[3])

[n, min, max] = [int(v) for v in argv[1:]]

print(n)
for _ in range (n):
    print (randint(min, max))
    