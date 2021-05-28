new_str=input("Enter input: ")

capital_str = " "
small_str = " "
digit_str = " "
others_str = " "

for i in new_str:
    if i.isupper():
        capital_str = capital_str + i
    elif i.islower():
        small_str = small_str + i
    elif i.isnumeric():
        digit_str = digit_str + i
    else:
        others_str = others_str + i

print(capital_str)
print(small_str)
print(digit_str)
print(others_str)
