import math
strings = input("Please provide a string: ")
# print(type(strings))
ln = math.floor(len(strings)/2)
test = True
for i in range(ln):
    test = test and (strings[i] == strings[-i])

if test:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")