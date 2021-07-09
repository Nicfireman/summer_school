users = []
#from compary import *
def compare_user_name(name):
    for user in users:
            if name == user[0]:
                return 1, user
    return 0, 0

def compare_password(pwd, user):
    if pwd == user[1]:
        return 1
    return 0

    def main():
        pass
def add_new_user():
    print("enter user name")
    for i in range(2):
        user_name = input()
        flag, _ = compare_user_name(user_name)
        if not flag:
            break
        print("bad name, try again")
        return 
    
    for i in range(3):
        print("enter password")
        password1 = input()
        x = len(password1)
        if x >= 3:
            print("repeat password")
            password2 = input()
            if password1 == password2:
                users.append([user_name, password1, 0, 0])
                f = open("data_base.txt", 'w')
                for user in users:
                    f.write("{} {} {} {}\n".format(user[0], user[1], user[2], user[3]))
                print(users)
                f.close()
                return
        else:
            print("The password is too short")
    print("You have run out of attempts")

def enter():
    print(users)
    while 1:
        print("enter user name")
        flag, user = compare_user_name(input())
        if flag:
            break
        print("no such user")
    while 1:
        print("enter password")
        password = input()
        if compare_password(password, user):
            break
        print("try again")
    print("WELCOME!")
    while 1:
        if in_user(user):
            break

def get_mode_number(mods):
    mod = input()
    if mod in mods:
        return mod
    else:
        return 0

def print_user_list():
    for user in users:
        print("{}".format(user[0]))
    return 0
def add_money(user):
    while 1:
        print("Enter the amount you want to give yourself: ")
        your_money = int(input())
        f = open("data_base.txt", 'w')
        user[3] += your_money
        for user in users:
            f.write("{} {} {} {}\n".format(user[0], user[1], user[2], user[3]))
        print(your_money)
        f.close()
        return 0

def transfer_money(user):
     while 1:
        for user in users:
            print("Enter the amount you want to deposit to your account:")
            money = int(input())
        #user[2] += money
            if user[3] >= money:
                print("The transaction is completed")
                user[3] -= money
                user[2] += money
                print(user[2])
                obnov()
                return 0
            else:
                print("You don't have enough money")
                return 0

            

            return 0

def obnov():
    f = open("data_base.txt", 'w')
    for user in users:
        f.write("{} {} {} {}\n".format(user[0], user[1], user[2], user[3]))
    f.close()

def view_the_invoice(user):
    print("cash money:{} ".format(user[3]))
    print("Money in the account:{} ".format(user[2]))

def leave(_):
    return 0

def change_name(user):
    while 1:
        print("enter new name")
        new_name = input()
        flag, _ = compare_user_name(new_name)
        if not flag:
            break
        print("bad name, try again")
    user[0] = new_name
    f = open("data_base.txt", 'w')
    for user in users:
        f.write("{} {} {} {}\n".format(user[0], user[1], user[2], user[3]))
    print(users)
    f.close()
    return 0

def change_password(user):
    while 1:
        print("enter new password")
        password1 = input()
        x = len(password1)
        if len(password1) < 3:
            break
        print("password is too short")
    while 1:
        print("repeat password")
        password2 = input()
        if password1 == password2:
            break
    user[1] = password1
    f = open("data_base.txt", 'w')
    for user in users:
        f.write("{} {} {} {}\n".format(user[0], user[1], user[2], user[3]))
    print(users)
    f.close()
    return 0

def log_out(_):
    return 1
def actions_with_money(user):
    mods = {'1':add_money,
            '2':transfer_money,
            '3':view_the_invoice,
            '4':leave}
    print("1 - add money")
    print("2 - transfer money")
    print("3 - view the invoice")
    print("4 - leave")
    mod = get_mode_number(mods)
    if mod:
        return mods[mod](user)
    else:
        print("wrong number!") 
def in_user(user):
    mods = {'1': print_user_list,
           '2': actions_with_money,
           '3': change_name,
           '4': change_password,
           '5': log_out}
           
    print("1 - user list")
    print("2 - actions with money")
    print("3 - change name")
    print("4 - change password")
    print("5 - log out")
    mod = get_mode_number(mods)
    if mod:
        return mods[mod](user)
    else:
        print("wrong number!") 

def menu():
    mods = {'1': enter,
            '2': add_new_user,
            '3': exit}
    print("1 - enter")
    print("2 - new user")
    print("3 - exit")
    mod = get_mode_number(mods)
    if mod:
        mods[mod]()
    else:
        print("wrong number!")

def main():
    while 1:
        menu()

if __name__ == "__main__":
    f = open("data_base.txt", 'r')
    users = f.read().split('\n')
    for i in range(len(users) - 1):
        users[i] = users[i].split()
        users[i][2] = int(users[i][2])
        users[i][3] = int(users[i][3])
    users.pop(len(users) - 1)
    f.close
    main()