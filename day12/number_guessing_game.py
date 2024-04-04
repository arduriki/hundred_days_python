from art import logo
from random import randint

# FUNCTIONS
def one_random_number():
    """Take a random number to play"""
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    # print(f"Pssst, the correct answer is {numbers[0]}")
    return number


def num_attempts():
    """Set the number of attempts for the player according to the difficulty chosen"""
    flag = True
    while flag:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            attempts = 10
            print(f"You have {
                  attempts} attempts remaining to guess the number.")
            flag == False
            return attempts
        elif difficulty == "hard":
            attempts = 5
            print(f"You have {
                  attempts} attempts remaining to guess the number.")
            flag == False
            return attempts
        else:
            print("Set a proper level.")


def guess_the_number(attempts_counter, number_chosen):
    """Player has to guess the number."""
    player_num_guess = None
    flag = True
    while player_num_guess != number_chosen and flag:
        player_num_guess = int(input("Make a guess: "))
        if player_num_guess < number_chosen:
            print("Too low.")
            attempts_counter -= 1
            if attempts_counter == 0:
                print("You've run out of guesses, you lose.")
                flag = False
            else:
                print(f"You have {
                      attempts_counter} remaining to guess the number.")
        elif player_num_guess > number_chosen:
            print("Too high.")
            attempts_counter -= 1
            if attempts_counter == 0:
                print("You've run out of guesses, you lose.")
                flag = False
            else:
                print(f"You have {
                      attempts_counter} remaining to guess the number.")
        else:
            print(f"You got it! The answer was {number_chosen}.")


def main_game():
    """Main game"""
    # Print logo
    print(logo)
    # Take a random number
    random_number = one_random_number()
    # Choose a level of difficulty
    attempts = num_attempts()
    guess_the_number(attempts_counter=attempts, number_chosen=random_number)


# MAIN CODE
main_game()
