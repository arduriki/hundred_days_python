import random
from art import logo
import os


# Functions


def deal_cards(cards, who_cards):
    random.shuffle(cards)
    for card in cards:
        who_cards.append(card)
    return who_cards


def add_to_shown_cards(who_cards, who_shown, cards_to_draw):
    for i in range(0, cards_to_draw):
        random.shuffle(who_cards)
        who_shown.append(who_cards[i])
    return who_shown


def compare_hands(player_sum_shown, cpu_sum_shown):
    print("I'm in compare hands function.")
    if player_sum_shown > 21 and cpu_sum_shown <= 21:
        print("You went over. Opponent wins!")
    elif cpu_sum_shown > 21 and player_sum_shown <= 21:
        print("Opponent went over. You win!")
    elif cpu_sum_shown > 21 and player_sum_shown > 21:
        print("Both went over, it's a draw...")
    elif player_sum_shown > cpu_sum_shown:
        print("Your score is higher than the opponent. You win!")
    elif cpu_sum_shown > player_sum_shown:
        print("Your opponent's score is higher than yours. Opponent wins!")
    elif cpu_sum_shown == player_sum_shown:
        print("It's a draw...")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


play = input("Do you want to play a game of Blackjack?\nType 'y' or 'n': ")


def blackjack(play):
    # Variables
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    while play == "y":
        another_card_player = 'y'
        another_card_cpu = 'y'
        cpu_cards = []
        cpu_shown = []
        player_cards = []
        player_shown = []
        clear_terminal()
        print(logo)
        cpu_cards = deal_cards(cards=cards, who_cards=cpu_cards)
        cpu_shown = add_to_shown_cards(
            who_cards=cpu_cards, who_shown=cpu_shown, cards_to_draw=1)
        player_cards = deal_cards(cards=cards, who_cards=player_cards)
        player_shown = add_to_shown_cards(
            who_cards=player_cards, who_shown=player_shown, cards_to_draw=2)
        player_sum_shown = sum(player_shown)
        if player_sum_shown == 21:
            print("It's a Blackjack! You win!")
            blackjack()
        print(f"Your cards: {player_shown}, current score: {player_sum_shown}")
        print(f"Computer's first card: {cpu_shown[0]}")

        while another_card_player == 'y':
            another_card_player = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if another_card_player == 'y':
                player_shown = add_to_shown_cards(
                    who_cards=player_cards, who_shown=player_shown, cards_to_draw=1)
                player_sum_shown = sum(player_shown)
                if player_sum_shown > 21:
                    print(f"Your cards: {player_shown}, current score: {
                          player_sum_shown}")
                    print("Sorry, you've surpassed, you lose!")
                    break  # End the current game
                elif player_sum_shown == 21:
                    print(f"Your cards: {player_shown}, current score: {
                          player_sum_shown}")
                    print("It's a Blackjack! You win!")
                    break  # End the current game
                print(f"Your cards: {player_shown}, current score: {
                      player_sum_shown}")
            else:
                another_card_player = 'n'

        while another_card_cpu == 'y':
            cpu_shown = add_to_shown_cards(
                who_cards=cpu_cards, who_shown=cpu_shown, cards_to_draw=1)
            if sum(cpu_shown) < 17:
                cpu_shown = add_to_shown_cards(
                    who_cards=cpu_cards, who_shown=cpu_shown, cards_to_draw=1)
            else:
                another_card_cpu = 'n'

        cpu_sum_shown = sum(cpu_shown)

        print(f"Your final hand: {
              player_shown}, final score: {player_sum_shown}")
        print(f"Computer's final hand: {
              cpu_shown}, final score: {cpu_sum_shown}")

        compare_hands(player_sum_shown=player_sum_shown,
                      cpu_sum_shown=cpu_sum_shown)

        print()

        play = input(
            "Do you want to play a game of Blackjack?\nType 'y' or 'n': ")


if play == 'y':
    blackjack(play=play)
