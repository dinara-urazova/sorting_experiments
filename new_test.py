# name = input('Enter file:')
# handle = open(name, 'r')
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# bigcount = None
# bigword = None
# for word, count in list(counts.items()):
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)


def find_num():
    nums = []
    for i in range(1, 2000):
        if i * 2 + 3 == i ** 2:
            nums.append(i)
    return nums

res = find_num()
print(res)