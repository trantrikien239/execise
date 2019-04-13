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
# Ask for input
check = getInt("Give me another positive integer to check: ")
num = getInt("Give me a positive integer to divide it by: ")

if check % num == 0:
    print("check divide evenly into num")
else:
    print("check does not devide evenly into num")
