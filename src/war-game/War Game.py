import random
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            
            for rank in ranks:
                
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
            
    def shuffle(self):
            
        random.shuffle(self.all_cards)
        
    def deal_one(self):
            
        return self.all_cards.pop()  

class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

Player1 = Player("Jose")
Player2 = Player("Juan")
new_deck = Deck() 
new_deck.shuffle()

for x in range(26):
    Player1.add_cards(new_deck.deal_one())
    Player2.add_cards(new_deck.deal_one())

def game_start():
    global game_on
    round_num = 0
    game_on = True
    while game_on == True: 
        round_num += 1
        print(f"Round {round_num}")
        if len(Player1.all_cards) == 0:
            print('Player1 is out of cards! Player2 wins!')
            game_on = False
            break
        if len(Player2.all_cards) == 0:
            print('Player2 is out of cards! Player1 wins!')
            game_on = False
            break
        Player1_cards = []
        Player1_cards.append(Player1.remove_one())
        Player2_cards = []
        Player2_cards.append(Player2.remove_one())
        at_war = True
        while at_war:
            if Player1_cards[-1].value > Player2_cards[-1].value:
                Player1.add_cards(Player1_cards)
                Player1.add_cards(Player2_cards)
                at_war = False
            elif Player2_cards[-1].value > Player1_cards[-1].value:
                Player2.add_cards(Player1_cards)
                Player2.add_cards(Player2_cards)
                at_war = False
            else:
                print('WAR!')
                if len(Player1.all_cards) < 5:
                    print('Player1 unable to declare war')
                    print('Player2 Wins!')
                    game_on = False
                    break
                elif len(Player2.all_cards) < 5:
                    print('Player2 unable to declare war')
                    print('Player1 Wins!')
                    game_on = False
                    break
                else:
                    for num in range(5):
                        Player1_cards.append(Player1.remove_one())
                        Player2_cards.append(Player2.remove_one())
game_start()
