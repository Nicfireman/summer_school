a = int(input())
b = int(input())
sign = input()
if sign == "+":
    print(a + b)
elif sign == "-":
    print(a - b)
elif sign == "*":
    print(a * b)
elif sign == "/":
    if b != 0:
        print(a / b)
    else:
        print("На ноль делить нельзя")
else:
    print("Недостаёт знака")#gg

