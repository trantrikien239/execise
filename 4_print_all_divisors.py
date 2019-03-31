#4.Print all divisor
import math
def get_int(text):
    try:
        intInput = int(input(text))
        if intInput <= 0:
            raise
        return intInput
    except Exception:
        print("Input must be a positive integer, please try again")
        return get_int(text)
num = get_int("Give me a positive integer: ")

# Find all divisor 
def find_all_divisors(num):
    l2 = []

    for i in range(1, math.floor(math.sqrt(num))+1):
        if num % i == 0:
            l2.append(i)
            l2.append(num/i)
    # Remove duplicate
    try:
        l2.remove(math.sqrt(num))
    except(Exception):
        print('')

    return(l2)

print(find_all_divisors(num))
