import random as rand

# Messages for the user to
print("Welcome To Guess Me!")
print("---------------------")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    # If the guess is out of range of the list number
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    # If the guess is correct on the first try.
    if guess == num:
        print("You got it right!!!!")
    guesses.append(guess)

    # If the guess is closer than the previous attempts

    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')