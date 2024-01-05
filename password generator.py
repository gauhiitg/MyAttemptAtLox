import random 
import string 

def password_generate(min_length, numbers = True, spl_char = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers == True :
        characters += digits
    if spl_char == True :
        characters += special

    password = ''

    Flag_criteria = False
    has_num = False
    has_spl = False

    while not(Flag_criteria or len(password)< min_length):
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_num = True 
        elif new_char in spl_char:
            has_spl = True
        
        Flag_criteria = True
        if numbers:
            Flag_criteria = has_num
        if spl_char:
            Flag_criteria = has_spl and Flag_criteria
    return password

print (password_generate(10))