from replit import clear
from art import logo
from sys import exit
#HINT: You can call clear() to clear the output in the console.

max_bid = 0
highest_bidder = ""
blind_auction = {}
another_bid = True

print(logo)
print("Welcome to the secret auction program.")

while another_bid:
    # key
    name = input("What is your name?: ")
    # value
    bid = float(input("What's your bid?: $"))
    blind_auction = {
        "name": name,
        "bid": bid,
    }

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == 'no':
        clear()
        another_bid = False
    elif other_bidders == 'yes':
        clear()
    else:
        print("Please enter the correct word.")
        exit()
    
    clear()

for key in blind_auction:
    if max_bid < blind_auction["bid"]:
        max_bid = blind_auction["bid"]
        highest_bidder = blind_auction["name"]

clear()
print(f"The winner is {highest_bidder} with a bid of ${max_bid}")
