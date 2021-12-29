'''
Simple Black Jack game for one player. The player plays against the computer dealer.
The game follows the soft 17 rule of black jack.
Can be easily expanden for more players.
'''


import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#Card Class > for representation of the individual cards
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

#Deck Class > stores cards in the Deck
class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        
        for suit in suits:
            for rank in ranks:
                current_card = Card(suit,rank)
                self.deck.append(current_card)
                
    def __str__(self):
        result = len(self.deck)
        result = str(result) + " cards in Deck \n"
        for card in self.deck:
            result = result + card.__str__() + "\n"
        
        return result
 
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

#Hand Class > stores current hand of the player
class Hand():
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def __str__(self):
        result = len(self.cards)
        result = str(result) + " cards in this hand \n"
        for card in self.cards:
            result = result + card.__str__() + "\n"
        return result
        
    def add_card(self,card):
        self.cards.append(card)
        self.value = self.value + card.value
        
        # track aces
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces: #self.aces > 0
            self.value -= 10
            self.aces -= 1

#Chips Class > stores chip balance of the player
class Chips():
    
    def __init__(self,total=100):
        self.total = total 
        self.bet = 0
    
    def __str__(self):
        return f"Chip value: {self.total}"
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total +- self.bet

#USER PROMPT: Taking Bets
def take_bet(chips):  
    keep_asking = True
    
    while keep_asking:
        
        try:
            chips.bet = int(input("How much do you want to bet?"))
            
        except:
            print("Please enter a valid number.")
        else:
            if chips.bet > chips.total:
                print(f"You only have {chips.total} chips to bet!")
            else:
                keep_asking = False 

#HIT (Drawing another card)
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#USER PROMPT: HIT OR STAND?
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    answer = "wrong"
    while answer not in ["H", "S"]:
        answer = input("Do you want to Hit (H) or Stand (S)?")
        answer = answer.upper()
        
        if answer not in ["H", "S"]:
            print("Please choose H for Hit or S for Stand")
    
    if answer == "H":
        hit(deck,hand)
    elif answer == "S":
        print("Player stands, dealer's turn")
        playing = False

#DISPLAYING OF THE GAME
def show_some(player,dealer):
    #show player
    print("PLAYER'S HAND:")
    for card in player.cards:
        print(card)
    print("\n")
    
    #show dealer
    print("DEALER'S HAND:")
    print("First card is hidden!")
    print(dealer.cards[1])
    
def show_all(player,dealer):
    #show player
    print("PLAYER'S HAND:")
    for card in player.cards:
        print(card)
    print(f"The value of hand is: {player.value}") #COOL!
    print("\n")
    
    #show dealer
    print("DEALER'S HAND:",*dealer.cards,sep="\n")
    print(f"The value of hand is: {dealer.value}")

#HANDLING GAME SCENARIOS
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer Busted! Player wins!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and player tie! PUSH!")


#GAME PLAY
playing = True
while True:
    # Print an opening statement
    print("Welcome to the game of Black Jack")
    time.sleep(1)
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    # Create hands and deal from deck
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal()) 
        
    # Set up the Player's chips
    if player_chips.total:
        player_chips = Chips(player_chips.total)
    else:
        player_chips = Chips()
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
            
        print("XXXXXX \n")

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        
    
    # Inform Player of their chips total
    print(f"\nPlayers total chips are at: {player_chips.total}")
    
    # Ask to play again
    play_again = ""
    while play_again not in ["Y","N"]:
        play_again = input("Play again? Y/N")
        if play_again not in ["Y","N"]:
            print("Please select Y or N")
        
    if play_again.upper() == "Y":
        pass
        playing = True
        continue
    elif play_again.upper() == "N":
        print("Thank you for playing")
        break
