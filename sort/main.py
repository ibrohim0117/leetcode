# # 1331. Rank Transform of an Array
# arr = [40,10,20,30, 10]
# c = 1
# l = []
# for i in sorted(arr):
#     print(i)
#     l.append((i, c))
#     c = c + 1
#
# print(l)
# a = 0
# new = []
# for i in l:
#     if i[0] in arr:
#         new.append(i[1])
#         a = a + 1
# print(new)
#

arr = [40,10,20,30,10]
new_arr = sorted(list(set(arr)))
c = 1
l = []
for i in sorted(new_arr):
    print(i)
    l.append((i, c))
    c = c + 1
print(l)
result = []
for i in arr:
    for son, daraja in l:
        if i == son:
            result.append(daraja)
            arr.remove(i)

print(result)


