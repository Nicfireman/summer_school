def get_currensy_key(currensy_cods):
    for cod in currensy_cods:
        print(cod)
    print("Введите значение валюты: " , end = ' ')
    key = input()
    if key in currensy_cods:
        return key
    else:
        return 0
def get_money():
    money = int(input("Введите сумму денег которую вы хотите поменять: "))
    if money > 0:
        return money
    return 0
def main():
    EUR = 87
    USD = 73
    grivna = 2.5
    currensy_cods = ["EUR 400", "USD 401", "GRI 402"]
    money = get_money()
    if not money:
        print("ERROR")
        return
    key = get_currensy_key(currensy_cods)
    if key:
        if key == currensy_cods[0]:
            print("К получению {0:0.2f} EUR".format(money/EUR))
        elif key == currensy_cods[1]:
            print("К получению {0:0.2f} USD".format(money/USD))
        elif key == currensy_cods[2]:
            print("К получению {0:0.2f} GRIV".format(money/grivna))
    else:
        print("Ошибка")
if __name__ == "__main__":
    main()