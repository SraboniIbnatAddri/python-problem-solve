def multiple(n):
    for i in range(10):
        print(n,"*",(i+1),"=",(n*(i+1)))


if __name__ == "__main__":
    number = input("Enter any number: ")
    number = int(number)
    multiple(number)