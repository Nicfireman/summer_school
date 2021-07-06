
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
    print("!!!!!!!")
def main():
    fact(int(input()))

if __name__ == "__main__":
    main()