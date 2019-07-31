#1
import math
"""""
b = -5.4
m = 4
u = 0.05 * 10**(-4)
k = [6, 4, 0.3, -7]
for i in range(len(k)):
    v = u + b - 2 * (0.7 * k[i] + m)**(0.5)
    print(" v(k=", k[i], ")=", v, "\n")
    w = 100 * math.exp(-0.2 * u) - math.log(8.1 * u)
    print(" w(k=", k[i], ")=", w, "\n")
"""""
#2
"""""
b = -5.4
m = 4
u = 0.05 * 10**(-4)
k = 3
while k <= 4:
    v = u + b - 2 * (0.7 * k + m)**(0.5)
    print(" v(k=", k, ")=", v, "\n")
    w = 100 * math.exp(-0.2 * u) - math.log(8.1 * u)
    print(" w(k=", k, ")=", w, "\n")
    k = round(k + 0.2, 2)
"""""
#3
m = [-1.3, -2, 4.9]
u = 0.05 * 10**(-4)
k = 4
b = 7
for i in range(len(m)):
    while b <= 8:
        v = u + b - 2 * (0.7 * k + m[i])**(0.5)
        print(" v(m=", m[i],",b=", b, ")=", v, "\n")
        w = 100 * math.exp(-0.2 * u) - math.log(8.1 * u)
        print(" w(m=", m[i],",b=", b, ")=", w, "\n")
        b = round(b + 0.2, 2)
    b = 7
