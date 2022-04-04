import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_score = 0
dealer_cards = []
dealer_display = []
dealer_score = 0
dealer_score_secret = "?"
lose = False
win = False
hold = False
player_blackjack = False
dealer_blackjack = False
draw = False

def game_status():
    print(f"Your cards are {player_cards} and your score is {player_score}. \n")
    print(f"The dealer's cards are {dealer_display} and their score is {dealer_score_secret}. \n")

def initial_hand():
    global dealer_score_secret
    player_cards.append(cards[random.randint(0, 9)])
    player_cards.append(cards[random.randint(0, 9)])
    dealer_cards.append(cards[random.randint(0, 9)])
    dealer_cards.append(cards[random.randint(0, 9)])
    dealer_display.append(dealer_cards[0])
    dealer_display.append("?")
    dealer_score_secret = str(dealer_cards[0]) + "(?)"

def check_player():
    clear()
    global player_score
    global player_cards
    player_score = 0
    for checkplayer in player_cards:
        player_score += checkplayer
    while player_score > 21 and 11 in player_cards:
            position11 = player_cards.index(11)
            player_cards[position11] = 1
    game_status()    
    
def check_dealer():
    clear()
    global dealer_score
    global dealer_cards
    dealer_score = 0
    for checkdealer in dealer_cards:
        dealer_score += checkdealer
    while dealer_score > 21 and 11 in dealer_cards:
        position22 = dealer_cards.index(11)
        dealer_cards[position22] = 1
        dealer_score  = 0
        for checkdealer in dealer_cards:
            dealer_score += checkdealer
    game_status()
    
def player_draw_card():
    global player_cards
    player_cards.append(cards[random.randint(0, 9)])
    check_player()

def dealer_draw_card():
    global dealer_cards
    global dealer_display
    global dealer_score_secret
    global player_score
    dealer_cards.append(cards[random.randint(0, 9)])
    check_dealer()    

def compare_scores():
    global win
    global player_blackjack
    global lose
    global dealer_blackjack
    global draw
    if player_score > 21:
        lose = True
        return lose
    elif player_score == dealer_score:
        if 11 in player_cards and not 11 in dealer_cards:
            player_blackjack = True
            return player_blackjack
        elif 11 in dealer_cards and not 11 in player_cards:
            dealer_blackjack = True
            return dealer_blackjack    
        else:
            draw = True
            return draw
    elif player_score == 21 and not dealer_score == 21:
        if 11 in player_cards:
            player_blackjack = True
            return player_blackjack
        else:
            win = True
            return win
    elif dealer_score == 21 and not player_score == 21: 
        if 11 in dealer_cards:
            dealer_blackjack = True
            return dealer_blackjack
        else:
            lose = True
            return lose        
    elif player_score < 21 and dealer_score > 21:
        win = True
        return win
    elif player_score < 21 and dealer_score < 21 and dealer_score > player_score:    
        lose = True
        return lose
    elif player_score < 21 and dealer_score < 21 and dealer_score < player_score:    
        win = True 
        return win

def blackjack():
    global player_cards
    global player_score
    global dealer_cards
    global dealer_display
    global dealer_score
    global lose
    global win
    global hold
    global player_blackjack
    global dealer_blackjack
    global draw 
    global dealer_score_secret
    initial_hand()
    check_player()
    check_dealer()
    if player_score >= 21:
        hold = True
    while hold == False:
        if input("Will you draw another card (HIT) or pass your turn (HOLD)? Hit/Hold: ").lower() == "hit":
            player_draw_card()
            check_player()
            if player_score >= 21:
                hold = True
        else:
            hold = True           
    check_dealer()    
    while dealer_score < 17:
        dealer_draw_card()
    if hold == True and not player_score > 21:
        dealer_display = dealer_cards
        dealer_score_secret = dealer_score 
        check_dealer()    
    if hold == True:
        compare_scores()        
        if win == True:
            print("You win the game!")
        elif lose == True:
            print("You lose the game.")
        elif draw == True:
            print("It's a draw.")
        elif player_blackjack == True:
            print("Blackjack! You win!")
        elif dealer_blackjack == True:
            print("The dealer has a Blackjack. You lose the game.")
    if input("Want to play again? Yes/No: ").lower() == "yes":
        player_cards = []
        player_score = 0
        dealer_cards = []
        dealer_display = []
        dealer_score = 0
        dealer_score_secret = "?"
        lose = False
        win = False
        hold = False
        player_blackjack = False
        dealer_blackjack = False
        draw = False    
        blackjack()
    else:
        print("Take care.")


print(logo)
if input("""Welcome to Josh's fully-fledged Blackjack game! The rules are simple: The player with the score CLOSEST to but UNDER 21 wins.
         
- You and the dealer get 2 initial cards. 
- If your score is equal to or under 21: You can chose to draw another card (Hit) or end your turn (Hold). You only get to see the Dealer's first card, so choose wisely.
- The dealer gets to draw, but only if their score is under 17 (They MUST draw until their score is at least 17).
- Once the dealer's turn ends, scores are compared: The player with the score CLOSEST to but UNDER 21 wins.          
- If you exceed 21 points: You lose regardless of the dealer's score.         
- An Ace ('A') works as both 1 -or- 11 points depending on your score being under 21. This means you can risk drawing another card while you have an 11. If your score exceeds 21: The 11 becomes 1. Your score is then re-calculated.
- The J, Q, and K are worth 10 points each.
- A 'Blackjack' 21 (A + J/Q/K) is an AUTOMATIC win!         
- For ease of score tracking, your cards will show the value of A/J/Q/K (11/10/10/10) instead of letters. 
         
Are you ready? Yes/No: """).lower() == "yes":
    blackjack()