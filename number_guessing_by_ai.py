import random

n = 0
y = random.randrange(1, 101)  # Adjusted range to include 100
max_attempts = 10  # Added maximum number of attempts

while n < max_attempts:
    try:
        x = int(input("Guess a number between 1 to 100: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if x < 1 or x > 100:
        print("Please enter a number between 1 and 100.")
        continue

    n += 1

    if x == y:
        print("Congratulations! You guessed it correctly in", n, "attempts.")
        break
    elif x > y:
        print("Think something smaller.")
    else:
        print("Think something bigger.")
else:
    print("Sorry, you've reached the maximum number of attempts. The number was:", y)
