k = int(input("Введите k:\n"))
s = ""
i = 0
temp = 0
while len(s) < k:
    temp = 2 ** i
    s += str(temp)
    i += 1
print(s)
print(k," цифра в последовательности: ", (int(s)%10**(len(s)-k+1))//10**((len(s)-k)))
