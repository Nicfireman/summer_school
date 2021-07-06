def get():
    return int(input("Введите сумму денег которую вы хотите поменять: "))
def main():
    Dollar = 73
    EURO = 87
    grivna = 2
    p = int(input())
    all_money = int(input(print("Введите сумму денег которую вы хотите поменять: ")))
    key = input("Введите значение валюты (400 - EUR, 401 - USD, 402 - GRIV): ")
    if all_money > 0:
        if key == "400":
            print("К получению {0:0.2f} EUR".format(all_money/EURO))
        elif key == "401":
            print("К получению {0:0.2f} USD".format(all_money/Dollar))
        elif key == "402":
            print("К получению {0:0.2f} GRIV".format(all_money/grivna))
        else:
            print("{} - не правильное значение".format(key))
    else:
        print("Отрицательнная сумма")
if __name__ == "__main__":
    main()