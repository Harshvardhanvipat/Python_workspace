# generate a number between 0 to 10
import random

# print(answer)
# input from user
# check that input is a number 1 -10


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius')
            return True
    else:
        print('Hey I said 1 - 10 ')


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:

        try:
            guess = int(input('guess a number 1 - 10 : '))
            if(run_guess(guess, answer)):
                break
        except ValueError:
            print('Please enter a number')
            continue

# check if the number is right guess/ Otherwise

# ask again
