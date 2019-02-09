#List less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#Original requirement
print("First requirement")
for x in a:
    if x < 5:
        print(x)
#Second requirement
print("Second requirement: Make a new list")
b = []
for x in a:
    if x < 5:
        b.append(x)
print(b)
#3rd requirement
def getFloat(text):
    try:
        floatInput = input(text)
        floatInput = float(floatInput)
        return floatInput
    except Exception:
        print("Input must be a float, please try again")
        return getFloat(text)
y = getFloat("Give me a float: ")
b = []
for x in a:
    if x < y:
        b.append(x)
print(b)
