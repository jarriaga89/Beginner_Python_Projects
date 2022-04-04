from replit import clear
from art import logo

print(logo)

print("Welcome to Josh's Blind Auction program. Participants can add their bids (Unknown to other participants) and the highest bid is presented at the end. Good luck! \n")

full_list_of_participants = False
current_participants = {}
highest_bid = {
"name": "noone",
"bid": 0    
}

def request_participant_info():
    global bidname
    global bidammount
    global total_participants
    global highest_bid
    bidname = input("What is your name? ")
    bidammount = int(input("What's your name bid? $"))
    name = bidname
    bid = bidammount    
    current_participants[name] = bid
    if bidammount > highest_bid["bid"]:
        highest_bid = {
        "name": bidname,
        "bid": bidammount    
        }

def run_bid():
    global highest_bid
    global current_participants
    global full_list_of_participants
    while full_list_of_participants == False:
        request_participant_info()
        highestbidname = highest_bid["name"]
        highestbidammount = highest_bid["bid"]
        list_check = input("Is there another participant in the bid? Yes/No: ").lower()
        clear()
        if list_check == "no":
            full_list_of_participants = True
            print(f"in this bid, the participands and their bids are: {current_participants}")
            print(f"The winner is {highestbidname} with a bid of ${highestbidammount}.")
        elif list_check == "yes":
            request_participant_info
    run_again = input("Want to run another blind bid? Yes/No: ").lower()
    clear()
    if run_again == "yes":
        highest_bid = {
        "name": "noone",
        "bid": 0    
        }
        current_participants = {}
        full_list_of_participants = False
        run_bid()
    else:
        print("This concludes the blind bid. Take care.")

run_bid()