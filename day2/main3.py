import math

a = int(input())
b = int(input())
c = int(input())

if  a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    p = (a + b + c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S)
else:
    print("Треугольник не существует")



