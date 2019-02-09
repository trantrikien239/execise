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
print(1)
# Find all divisor less than sqrt(num)
import math
l1 = range(1, math.floor(math.sqrt(num))+1)
l2 = []
print(2)
for i in l1:
    if num % i == 0:
        l2.append(i)
    print(3)
print(l2)
print(l1)
# Find all divisor more than sqrt num
l3 = []
for i in l2:
    l3.append(num/i)
    l3.append(i)
    print(4)

# Remove duplicate
if math.sqrt(num) == math.floor(math.sqrt(num)):
    l3.remove(math.sqrt(num))
    print(5)

print(l3)
