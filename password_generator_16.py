import random as rd

CHAR = 'qwertyuiopasdfghjklzxcvbnm'
SYMBOL = '!@#%$%^&*()_+{}|:"<>?-=[]\';\,./'
NUMBER = '1234567890'
LIBS = [NUMBER, CHAR, SYMBOL]
STRENGTH_ANSWERS = {
                   'weak':{'number_of_lib_used': 1, 'length_range':[4,8]},
                   'medium':{'number_of_lib_used': 2, 'length_range':[6,10]},
                    'strong':{'number_of_lib_used': 3, 'length_range':[8,12]},
                    'super strong':{'number_of_lib_used': 3, 'length_range':[12,24]}}
def main():
    strength = strength_input()
    password = password_generator(strength)
    print('Your password is: ', password)


def strength_input():
    strength = input("How strong do you want your password to be? (weak/medium/strong/super strong): ")
    if strength.lower() not in STRENGTH_ANSWERS.keys():
        print('Input error, please pick the strength again')
        strength = strength_input()
    return strength

def password_generator(strength):
    lib = ''
    password = ''
    # Establish the lib
    for i in range(STRENGTH_ANSWERS[strength]['number_of_lib_used']):
        lib = lib + LIBS[i]


    password_len = rd.randint(STRENGTH_ANSWERS[strength]['length_range'][0],STRENGTH_ANSWERS[strength]['length_range'][1])
    for i in range(password_len):
        password = password + lib[rd.randint(0,len(lib)-1)]

    return password

main()