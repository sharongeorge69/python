from art import logo

print(logo)


def find_highest_bid(bidding_record):  #biggind_record = bids
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f"The winner is {bidder} with an amount of {highest_bid}")


conti = True
bids = {}
while conti:
    name = input("What is your name : ")
    bid = int(input("What is your bid : "))
    bids[name] = bid
    conti = input('Are there any other bidders : "yes" or "no" : ').lower()
    if conti == "no":
        conti = False
        find_highest_bid(bids)
    elif conti == "yes":
        print("\n" * 20)
