if __name__ == "__main__":
    year = input("Enter any year:")
    year = int(year)

    if year%4==0 and year%100!=0:
        print(year,"is leap year")
    elif year%100==0 and year%400==0:
        print(year,"is leap year")
    else:
        print(year,"not leap year")
