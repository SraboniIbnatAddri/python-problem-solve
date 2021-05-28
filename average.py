def total_value(my_list):
    result=0
    for i in my_list:
        result=result+i
    print(result)

def total_length(my_list):
    result=0
    for i in my_list:
        result=result+1
    print(result)

def average_numbers(my_list):
    sum=total_value(my_list)
    length=total_length(my_list)
    average_number=sum/length
    return average_number

if __name__ == "__main__":
    my_list = [10,20,30,40,50]
    average= average_numbers(my_list)
    print(average)

