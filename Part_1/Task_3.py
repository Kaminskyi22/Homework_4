user_input = input("Enter a string: ")
my_list = list(user_input)

count = 0

for i in my_list:
    if i in "!.?":
        count += 1

print(f"The number of sentences in your text is: {count}.")