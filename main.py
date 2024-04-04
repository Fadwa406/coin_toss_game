import random

print("Welcome to the Coin Guessing Game!")

print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")


choice = input("Enter your choise (1 or 2): ")
computer_result = ""

if choice == "1":
  random_number = random.random()
  if random_number >= 0.5:
    computer_result = "Heads"
  else:
    computer_result = "Tails"
elif choice == "2":
  if random.randint(0, 1) == 0:
    computer_result = "Heads"
  else:
    computer_result = "Tails"

else:
  print("Invalid choice> Please select either 1 or 2")


user_choice = input("Enter your Guess (Heads or Tails): ")

if user_choice.lower() == computer_result.lower():
  print("Congratulations! You won!")
else:
  print("Sorry, you lost!")


print(f"The computer's coin toss result was: {computer_result}")