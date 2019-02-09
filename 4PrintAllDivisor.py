#4.Print all divisor
def getInt(text):
    try:
        intInput = input(text)
        intInput = int(intInput)
        if intInput <= 0:
            raise
        return intInput
    except Exception:
        print("Input must be a positive integer, please try again")
        return getInt(text)
num = getInt("Give me a positive integer: ")

# Find all divisor 
import math
l2 = []

for i in range(1, math.floor(math.sqrt(num))+1):
    if num % i == 0:
        l2.append(i)
        l2.append(num/i)
# Remove duplicate
try:
    l2.remove(math.sqrt(num))
    print('')
except(Exception):
    print('')

print(l2)
