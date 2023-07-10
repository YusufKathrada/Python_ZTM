# generate number from 1-10
# get input from user
# check that number in correct range
# check if number is correct answer - otherwise ask user again

# could add limited number of guesses for user

from random import randint

answer = randint(1, 10)

while True:
  try:

    user_guess = int(input("Guess the random number between 1 and 10:  "))

    if user_guess > 10 or user_guess < 1:
      print(
        "Oops! Make sure the number you enter is within the correct range. Please try again."
      )
      continue

    if user_guess != answer:
      print("That is incorrect! Please try again!")
    else:
      print("You got it!")
      break

  except ValueError:
    print("Make sure you enter a valid integer.")
