a = input().split()
sum = 0
sum2 = 0
for num in a:
    if not int(num) % 2:
        sum = sum + int(num)#Сумма нечётных чисел
    if int(num) % 2:
        sum2 = sum2 + int(num)#Сумма чётных чисел




print(sum, sum2)
        