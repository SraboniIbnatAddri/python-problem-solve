import random
num=random.randint(1,1000)
high=1000
low=1
attempts=0

while True:
    input_value=(low+high)/2
    attempts+=1
    if num==input_value:
        print("right")
    elif num>input_value:
        print("choose larger")
    else:
        print("choose smaller")
print("you tried",attempts,"time")