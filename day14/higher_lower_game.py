# TODO: Import the necessary variables from other files
from art import logo
from art import vs
from game_data import data
import random
import os


# TODO: Clear terminal and add 1 to player's score if is right.
# TODO: Keep who has more followers and compare with the next one.
# TODO: If wrong, clear terminal and indicate the final score.

def shuffle_data(data_list):
    """Shuffles the game_data's list variable"""
    random.shuffle(data_list)
    return data_list


def compare(data_list, index_a, index_b):
    """Compares on screen index A and index B and asks user for his/her opinion."""
    print(f"Compare A: {data_list[index_a]['name']}, a/an {
        data_list[index_a]['description']}, from {data_list[index_a]['country']}")
    print(vs)
    print(f"Against B: {data_list[index_b]['name']}, a/an {
        data_list[index_b]['description']}, from {data_list[index_b]['country']}")
    more_follows = input("Who has more followers? Type 'A' or 'B': ").upper()
    return more_follows


def right(player_score):
    """Result if the player is right."""
    os.system('clear')
    print(logo)
    print(f"You're right! Current score: {player_score}")


def wrong(player_score):
    """Result if the player is wrong."""
    os.system('clear')
    print(logo)
    print(f"Sorry, that's wrong. Final score: {player_score}")
    return True


def game():
    os.system('clear')
    # local variables
    a = 0
    b = 1
    score = 0
    flag_finish = False

    # shuffle the game data list
    data_shuffled = shuffle_data(data_list=data)
    # start game
    print(logo)
    who_more_follows = compare(data_list=data_shuffled, index_a=a, index_b=b)

    while flag_finish == False and b <= 50:
        if who_more_follows == "A":
            if data[a]["follower_count"] > data[b]["follower_count"]:
                score += 1
                a += 1
                b += 1
                right(player_score=score)
                who_more_follows = compare(
                    data_list=data, index_a=a, index_b=b)
            else:
                flag_finish = wrong(player_score=score)
        elif who_more_follows == "B":
            if data[a]["follower_count"] < data[b]["follower_count"]:
                score += 1
                a += 1
                b += 1
                right(player_score=score)
                who_more_follows = compare(
                    data_list=data, index_a=a, index_b=b)
            else:
                os.system('clear')
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                flag_finish = wrong(player_score=score)
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            flag_finish = wrong(player_score=score)
    return score


end_score = game()
print(f"Game's done! Your score is: {end_score}")
