import random
n=0
# The line `y = random.randrange(1,100)` in the Python code snippet is generating a random integer
# number between 1 and 99 (inclusive) and assigning it to the variable `y`. The
# `random.randrange(start, stop)` function in Python is used to generate a random integer within a
# specified range. In this case, `1` is the inclusive start value and `100` is the exclusive stop
# value, so the generated random number will be between 1 and 99.
y = random.randrange(1,100)

print(y)
x = int(input("Guess a number between 1 to 100 \n:"))
max_attempts=10

# The `if(x!=y):` statement is checking if the user's input `x` is not equal to the randomly generated
# number `y`. If the user's guess is not equal to the random number, it means the user has not guessed
# the correct number yet, and the program will enter the loop to provide hints and allow the user to
# make additional guesses within the specified number of attempts.
if(x!=y):
    while(max_attempts!=0):
        n+=1
        max_attempts-=1
        if(x>y):
            print("Think Something Smaller.")
        else:
            print("Think Something Bigger.")    

        print("Attempt Left:",max_attempts)  
        if(max_attempts==0):
            print("Sorry!!!😔: You Reached your limit.")          
            break
        x=int(input("Guess Again: "))

        if(x==y):
# The line `print("You guessed ❤️ 😍it correctly in ", n ," ATTEMPTS")` is displaying a message to the
# user indicating that they have correctly guessed the number. The variable `n` stores the number of
# attempts it took the user to guess the correct number. The message is informing the user of the
# number of attempts they made before guessing the correct number.
            print("You guessed ❤️ 😍it correctly in ", n ," ATTEMPTS")          
            break

else:
    # The line `print("😳😲Whohh!!!!😲😲. You r 👑 legend 👑. you did it in first try.")` is a message
    # that is printed when the user correctly guesses the number on their first attempt. It is a
    # congratulatory message to praise the user for guessing the correct number in the first try.
    print("😳😲Whohh!!!!😲😲. You r 👑 legend 👑. you did it in 1️⃣first  try.")

