from art import logo


print(logo)


bids = {}
bidding_finished = False


def highest_bidder(bidding_record,finish=False):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    if finish:
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    return highest_bid

while not bidding_finished:
    name = input("Whats your name?\t")
    price = int(input("Whats your bid\t"))
    if price > highest_bidder(bids):
        bids[name] = price
        should_continue = input("Are there another bidders? [yes/no]")
        if should_continue == "no":
            highest_bidder(bids,True)
            bidding_finished = True
        elif should_continue == "yes":
            bids[name] = price
    else:
        print("Invalid bid")













