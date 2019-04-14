import print_all_divisors as dvs
print("Sorry, wrong request, I thought you were asking for divisors. Now, what integer do you want to check primality?")
num = dvs.get_int("Give me a positive integer: ")
if len(dvs.find_all_divisors(num)) == 2:
    print("It's a prime number")
else:
    print("It's not a prime number")