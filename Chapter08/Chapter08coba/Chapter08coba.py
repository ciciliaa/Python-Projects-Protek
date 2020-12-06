a = [1, 5, 10, 6, 3, 6, 9, 11, 20, 12, 4]
b = [7, 15, 4, 5, 6, 7, 1, 12, 5, 9, 8]
a.sort()
b.sort()
print(a, b)

c = [1, 5, 6, 3, 6, 4]
d = [7, 4, 5, 6, 7, 5, 9, 8]
for i in range(c + d):
    print(i)
    

for x in c:
    for y in d:
        print(x + y)
