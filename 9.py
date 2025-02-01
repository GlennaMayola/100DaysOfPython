def highest_bidder(bidding_dictionary): #when we loop through dictionaries we loop through the keys
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bidder_amount=bidding_dictionary[bidder]
        if bidder_amount>highest_bid:
            highest_bid=bidder_amount
            winner=bidder
    
    print(f"The winner of the bid is {winner}")


repeat=True
auction={}
while repeat:
    name=input("Enter you name")
    bid=int(input("Enter your bid"))
    auction[name]=bid
    should_continue=input("Are there any more bidders?(type yes or no)").lower()
    if should_continue=="no":
        '''
        max_bid=max(auction,key=auction.get)  #max(dictionary_name, key=dictionary_name.get)
        print(max_bid) 
        exit()
        '''
        highest_bidder(auction)
    else:
        print("\n"*100)
        





        
    
