from art import logo
from clear import clear

#HINT: You can call clear() to clear the output in the console.

print(logo)

print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

def finding_highest_bidders(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bidding_record[bidder] > highest_bid:
            highest_bid = bid_amount 
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = (input("What is your name?: "))
    price  = int(input("What's your bid? $"))
    bids[name] = price
    should_continue = (input("Are there any bidders? Type 'yes' or 'no'. ")).lower()
    if should_continue == 'no':
        bidding_finished = True
        finding_highest_bidders(bids)
    elif should_continue == 'yes':
        clear()


        
