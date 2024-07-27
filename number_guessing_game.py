import random

n = 0
y = random.randrange(1, 100)
print(f"\nRandom number generated between 1 and 100: {y}\n")
x = int(input("Guess a number between 1 to 100:\n\t"))

max_attempts = 10
score = 100

with open("high_score.txt", 'r') as h:
    high_score = int(h.read())
h.close()

if x != y:
    while max_attempts != 0:
        n += 1
        score -= 10
        max_attempts -= 1
        if x > y:
            print("\tThink Something Smaller.\n")
        else:
            print("\tThink Something Bigger.\n")

        print(f"\tAttempts Left: {max_attempts}\n")
        if max_attempts == 0:
            print("Sorry!!!😔: You Reached your limit.\n")
            break
        x = int(input("Guess Again:\n\t"))

        if x == y:
            print(f"\nYou guessed ❤️😍 it correctly in {n} ATTEMPTS!\n")
            if high_score < score:
                with open("high_score.txt", "w") as h:
                    score_str = str(score)
                    h.write(score_str)

            print(f"\tYour Score: {score}\n")
            print(f"\tOld Best Score: {high_score}\n")
            break

else:
    print("😳😲 Whohh!!!! 😲😲 You are 👑 legend 👑. You did it on your 1️⃣ first try!\n")
    with open("high_score.txt", "w") as h:
        h.write("100")
    print(f"\tYour Score: {score}\n")
