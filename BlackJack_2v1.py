import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing1 = True
playing2 = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand_1(deck,hand):
    global playing1  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands.")
            playing1 = False

        else:
            print("Sorry, please try again.")
            continue
        break

def hit_or_stand_2(deck,hand):
    global playing2  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands.")
            playing2 = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player1, player2, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's One Hand:", *player1.cards, sep='\n ')
    print("\nPlayer's Two Hand:", *player2.cards, sep='\n ')
    
def show_all(player1, player2, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's One Hand:", *player1.cards, sep='\n ')
    print("Player's One Hand =",player1.value)   
    print("\nPlayer's Two Hand:", *player2.cards, sep='\n ')
    print("Player's Two Hand =",player2.value)   
    

def player1_busts(player1,dealer,chips1):
    print("Player One busts!")
    chips1.lose_bet()

def player1_wins(player1,dealer,chips1, player2,chips2):
    print("Player One wins!")
    chips1.win_bet()
    chips2.lose_bet()

def player2_busts(player2,dealer,chips2):
    print("Player Two busts!")
    chips2.lose_bet()

def player2_wins(player1,dealer,chips1, player2,chips2):
    print("Player Two wins!")
    chips2.win_bet()
    chips1.lose_bet()

def dealer_busts(dealer):
    print("Dealer busts!")
    
def dealer_wins(dealer):
    print("Dealer wins!")
    
def push(player1,dealer,player2):
    print("It's a tie")


# Print an opening statement
print('Lets play BlackJack! Get as close to 21 as you can without going over!\n\
Dealer hits until she reaches 17. Aces count as 1 or 11.')
# Set up the Player's chips
print("\nEach player starts with 100 marks")
player1_chips = Chips()  # remember the default value is 100   
player2_chips = Chips()  # remember the default value is 100 

while True:

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player1_hand = Hand()
    player1_hand.add_card(deck.deal())
    player1_hand.add_card(deck.deal())

    player2_hand = Hand()
    player2_hand.add_card(deck.deal())
    player2_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
             
    
    # Prompt the Player for their bet
    print("Player One: ")
    take_bet(player1_chips)
    print("Player Two: ")
    take_bet(player2_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player1_hand, player2_hand, dealer_hand)
    
    while playing1:  # recall this variable from our hit_or_stand function
        # Show total value of player's hand
        print("Player's One total value: ", player1_hand.value)
        # Prompt for Player to Hit or Stand
        print("\nPlayer One: ")
        hit_or_stand_1(deck,player1_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player1_hand, player2_hand, dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player1_hand.value > 21:
            player1_busts(player1_hand,dealer_hand,player1_chips)
            break     

    while playing2:    
        # Show total value of player's hand
        print("Player's Two total value: ", player2_hand.value)
        # Prompt for Player to Hit or Stand
        print("\nPlayer Two: ")
        hit_or_stand_2(deck,player2_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player1_hand, player2_hand, dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player2_hand.value > 21:
            player2_busts(player2_hand,dealer_hand,player2_chips)
            break   


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player1_hand.value <= 21 or player2_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player1_hand, player2_hand, dealer_hand)  
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(dealer_hand)
            if player1_hand.value > player2_hand.value:
                player1_wins(player1_hand,dealer_hand,player1_chips,player2_hand,player2_chips)
            elif player1_hand.value < player2_hand.value:
                player2_wins(player1_hand,dealer_hand,player1_chips,player2_hand,player2_chips)
            else: 
                push(player1_hand,dealer_hand,player2_hand)
        elif dealer_hand.value > player1_hand.value and dealer_hand.value > player2_hand.value:
            dealer_wins(dealer_hand)
            player1_chips.lose_bet()
            player2_chips.lose_bet()
        elif dealer_hand.value < player1_hand.value and player1_hand.value > player2_hand.value:
            player1_wins(player1_hand,dealer_hand,player1_chips,player2_hand,player2_chips)
        elif dealer_hand.value < player2_hand.value and player2_hand.value > player1_hand.value:
            player2_wins(player1_hand,dealer_hand,player1_chips,player2_hand,player2_chips)
        elif dealer_hand.value == player2_hand.value and dealer_hand.value == player1_hand.value:
            push(player1_hand,dealer_hand,player2_hand)
        else: 
            pass    
    
    # Check for 0 chips
    if player1_chips.total == 0:
        print("Player One you lost all your chips. Please leave and maybe come back later or consider not wasting all your money gambling. \nThank you to come. ")
        break
    else:
        pass

    # Check for 0 chips
    if player2_chips.total == 0:
        print("Player Two you lost all your chips. Please leave and maybe come back later or consider not wasting all your money gambling. \nThank you to come. ")
        break
    else:
        pass

    # Inform Player of their chips total 
    print("\nPlayer's One winnings stand at",player1_chips.total)
    print("Player's Two winnings stand at",player2_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    

    if new_game[0].lower()=='y':
        playing1=True
        playing2=True
        continue
    else:
        print("Thank you!")
        break