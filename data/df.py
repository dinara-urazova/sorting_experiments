val = '1010'
res = 0
for i in val:
    res = res << 1
    res = res or i
print(str(res))