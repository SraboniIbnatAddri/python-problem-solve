name = input("enter an input: ")
new_name = name[ : :-1]

if new_name == name:
    print(name,"is palindrome")
else:
    print(name,"is not palindrome")