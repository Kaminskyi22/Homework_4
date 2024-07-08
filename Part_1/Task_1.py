string = str(input("Enter a string: "))
no_space = string.replace(" ", "")
no_space = no_space.lower()
print(no_space[::-1])
if no_space == no_space[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")