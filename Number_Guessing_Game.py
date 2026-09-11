import random

print("🎯 Welcome to the Number Guessing Game!")
print("I have selected a number between 0 and 20.")
print("You have 4 attempts to guess it.\n")

computer = random.randint(0, 20)

for attempt in range(1, 5):

    print(f"Attempt {attempt} of 4")
    user_input = int(input("👉 Enter your guess: "))

    if user_input < 0 or user_input > 20:
        print("⚠️ Please enter a number between 0 and 20.")
        continue

    if user_input == computer:
        print("🎉 Correct! You guessed the number!")
        break

    elif user_input > computer:
        print("📈 Too high!")

    else:
        print("📉 Too low!")

else:
    print("😔 Game over!")
    print(f"The correct number was {computer}.")