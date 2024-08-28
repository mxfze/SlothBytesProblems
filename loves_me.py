def loves_me(amount):
    if amount % 2 == 0:
        is_even = True
    else:
        is_even = False

    added_string = "Loves me, "
    final_str = ""

    if is_even == True:
        for i in range(amount - 1):
            final_str += added_string
            added_string = "Loves me not, " 

        final_str += "LOVES ME NOT"

    else:
        for i in range(amount - 1):
            final_str += added_string
            added_string = "Loves me not, " 

        final_str += "LOVES ME"
    print(final_str)


loves_me(3)
loves_me(6)
loves_me(1)
