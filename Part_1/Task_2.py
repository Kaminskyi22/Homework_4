while True:
    try:
        user_input = str(input("Enter a string: "))
        my_list = user_input.split()
        user_input2 = input("Enter words to change in Upper case: ")
        words_to_change = user_input2.split()
        for i in range(len(my_list)):
            if my_list[i] in words_to_change:
                my_list[i] = my_list[i].upper()
        print(" ".join(my_list))
        break
    except:
        print("Invalid input, please try again")
        continue