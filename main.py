import csv

h = {}
cords = []

with open('file.csv') as file:
    file = csv.reader(file)
    for index, line in enumerate(file):
        h[index] = list(line[0])

for i in h:
    for j in range(len(h[i])):
        if h[i][j] == '#':
            cords.append([i, j])

length = len(h[0])
height = len(h)
length_arr = [x for x in range(length)]
height_arr = [x for x in range(height)]

for i in cords:
    if i[0] in height_arr:
        height_arr.remove(i[0])
    if i[1] in length_arr:
        length_arr.remove(i[1])

"""first part this plus where loop to check"""
# h1 = {}
# key = 0
# with open('file.csv') as file:
#     file = csv.reader(file)
#     for line in file:
#         h1[key] = list(line[0])
#         if key in height_arr:
#             key += 1
#             h1[key] = list(line[0])
#             height_arr = [x + 1 for x in height_arr]
#
#         key += 1
#
# m = 0
# for i in length_arr:
#     for j in h1:
#         h1[j].insert(i + m, '.')
#     m += 1


where = []
x = 0
y = 0

for i in h:
    for j in range(len(h[i])):
        if h[i][j] == "#":
            for length in range(len(length_arr) - 1):
                if j > length_arr[len(length_arr) - 1]:
                    x = (len(length_arr)) * 999999 + j
                    break
                elif length_arr[length] < j < length_arr[length + 1]:
                    x = (length + 1) * 999999 + j
                    break
                else:
                    x = j
            y = i
            where.append([y, x])

res = 0

for index, each in enumerate(where):
    n = index
    while n < len(where):
        res += abs(where[n][0] - each[0])
        res += abs(where[n][1] - each[1])
        n += 1

print(res)
