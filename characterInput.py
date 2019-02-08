name = input("Give me your name: ")
print("Your name is ", name)
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
    
# Test this
age = getInt("How old are you?")
numberOfCopies = getInt("How many copies do you want?")

print("You are now", age, "years old")
ansStr = str(100 - age)
print(numberOfCopies * ("You're gonna get to 100 years old in " + ansStr + " years \n"))
