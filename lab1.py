#1
n = int(input("Введите трёхзначное число: "))
if n >= 100 and n <= 999:
    s = str(n)
    f = False
    for i in range(len(s)):
        if s[i] == "0" or s[i] == "9":
            f = True
    if f == True:
        print("Цифры 0 или 9 есть в числе.")
    else:
        print("Цифр 0 и 9 в числе нет.")
else:
    print("Введённые данные некорректны.")
