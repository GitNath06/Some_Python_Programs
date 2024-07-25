import random
import string
def generate(length):
    password=""
    characters=string.ascii_letters
    numbers= string.digits
    symbols=string.punctuation
    
    
    char_sets=characters+numbers+symbols
    
    #also can be done shortly as: 
    # password= "".join([random.choice(char_sets) for i in range(length)])
    
    for i in range(length):
        password += random.choice(char_sets)
    
    return password     
    
pass_len= int(input("Enter the lenght of password: "))
print("The generated random password is " ,'"' ,generate(pass_len),'"')