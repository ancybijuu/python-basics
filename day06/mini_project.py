# ==========================================
# DAY 6 - MINI PROJECT
# NUMBER GUESSING GAME
# ==========================================

import random


print("=" * 45)
print("          NUMBER GUESSING GAME")
print("=" * 45)

print("I have selected a number between 1 and 100.")
print("Try to guess it!")


# Generate random number

secret_number = random.randint(1, 100)

attempts = 0


# Game loop

while True:

    try:
        guess = int(input("\nEnter your guess: "))

    except ValueError:
        print("Please enter a valid number.")
        continue


    # Validate range

    if guess < 1 or guess > 100:

        print("Please enter a number between 1 and 100.")
        continue


    attempts += 1


    # Compare guess

    if guess < secret_number:

        print("📉 Too low! Try again.")


    elif guess > secret_number:

        print("📈 Too high! Try again.")


    else:

        print("\n🎉 Congratulations!")

        print("You guessed the correct number!")

        print("Number:", secret_number)

        print("Attempts:", attempts)

        break


print("\n" + "=" * 45)
print("             GAME OVER")
print("=" * 45)