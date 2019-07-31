import random
n = int(input("Введите длину списка:"))
L = []
for i in range(n):
    l = random.randint(0, 99)
    L.append(l)
print(L)
s = int(input("Введите искомое число:"))
if s in L:
    while L.remove(s):
        L.remove(s)
print(L)