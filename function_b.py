# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    sum = 0
    cont = True
    while cont:
        user_input = int(input("Please input a number between 0 and 1000: "))
        if user_input == 0 or user_input > 1000:
            cont = False
        else:
            sum += user_input

    return sum

if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
