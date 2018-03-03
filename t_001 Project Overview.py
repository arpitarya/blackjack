
# coding: utf-8

# In[174]:


import random
from datetime import datetime
import sys


# In[175]:


#stores th status of program
_status = ''
_count = 0

def addStatus(text):
    global _status, _count
    _status += "\n" + str(datetime.now()) + " : " + text
    _count += 1

def clsStatus():
    global _status, _count
    _status = ''
    _count = 0


# In[176]:


#chips
chips = (1, 2, 5, 25, 50, 100, 200, 500)

#hearts, spades, clubs, diamonds
suits = ('H', 'S', 'C', 'D')

#card ranking
faces = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K')

#value of the cards A : 1 or 11; J, Q, K = 10; rest : face value
vals = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'J':10, 'Q':10, 'K':10}


# In[177]:


class Player(object):
    
    def __init__(self, bankroll = 1000):
        addStatus("Player created <Player->__init__()>")
        addStatus("Bankrolled for {x} bucks <Player->__init__()>".format(x = bankroll))
        self.bankroll = bankroll
    
    def addBankroll(self, amount):
        addStatus("Bankroll added for {x} bucks <Player->addBankRoll()>".format(x = amount))
        self.bankroll += amount
        
    def subBankroll(self, amount):
        addStatus("Bankroll deducted for {x} bucks <Player->addBankRoll()>".format(x = amount))
        self.bankroll -= amount
        
    def __str__(self):
        return str(self.bankroll)


# In[178]:


class Card(object):
    
    def __init__(self, suit, face):
        addStatus("Card created <Card->__init__()>")
        self.suit = suit
        self.face = face
        global vals
        self.val = vals[face]
    
    def __str__(self):
        return str(self.suit) + str(self.face)
    
    def cardVal(self):
        return self.val
    
    def cardFace(self):
        return self.face
    
    def cardSuit(self):
        return self.suit
    
    def draw(self):
        print(self.suit + self.face + self.val)


# In[179]:


class Deck(object):
    
    def __init__(self, suits, faces):
        addStatus("Deck created <Deck->__init__()>")
        deck = []
        for s in suits:
            for f in faces:
                temp = {'suit':s,'face':f}
                deck.append(temp)
        self.deck = deck
            
    def deckShuffle(self):
        addStatus("Deck shuffled <Deck->__init__()>")
        random.shuffle(self.deck)
        
    def deckPopCard(self):
        card = self.deck.pop()
        return card
        
    def __str__(self):
        temp_deck = ''
        for i, t in enumerate(self.deck, 1):
            temp_deck += str(i) + ": " + str(t['suit']) + str(t['face']) + "\n"
        return str(temp_deck)
    
    def __len__(self):
        return len(self.deck)


# In[180]:


class Hand:
    
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.hand_bet = 0
        self.hasAce = False
    
    def addCard(self, card, value_add_cond = True):
        self.hand.append(card)
        if value_add_cond:
            t_card = Card(card['suit'], card['face'])
            self.hand_value += t_card.cardVal()
            del t_card
            
    def addAllCardValue(self):
        self.hand_value = 0
        for h in self.hand:
            t_card = Card(h['suit'], h['face'])
            self.hand_value += t_card.cardVal()
            del t_card
            
    def setBet(self, amount):
        self.hand_bet = amount
        
    def getBet(self):
        return self.hand_bet
    
    def clsBet(self):
        self.hand_bet = 0
        
    def handValue(self):
        return self.hand_value
        
    def handFace(self):
        hand = ''
        for h in self.hand:
            hand = str(h['suit']) + str(h['face'])
        return hand
    
    def clsHand(self):
        self.hand = []
        self.hand_value = 0
        self.hand_bet = 0
        
    def handDealer(self):
        hand = ''
        hand = str(self.hand[0]['suit']) + str(self.hand[0]['face'])
        return str(hand)
        
    def handPlayer(self):
        hand = ''
        for i, h in enumerate(self.hand, 1):
            if i > 1:
                hand += ', '
            hand += str(h['suit']) + str(h['face'])
        return str(hand)


# In[181]:


def setPlayerBet():
    while(True):
        print('Place your bet : ')
        amt = int(input())
        if amt > int(str(player1)):
            print('Bet should be less than bankroll !!!')
            continue
        else:
            player1.subBankroll(amt)
            break
    player1hand.setBet(amt)


# In[182]:


def checkForWin(stand = False):
    if stand == False:
        if player1hand.handValue() == 21:
            player1.addBankroll(int(player1hand.getBet()) * 2)
            player1hand.clsBet()
            gameRound()
            print('\n')
            print('------------------------------------------------')
            print("Player Wins")
            print('------------------------------------------------')
            print('\n\n')
            return 1
        elif player1hand.handValue() > 21:
            player1hand.clsBet()
            gameRound()
            print('\n')
            print('------------------------------------------------')
            print("Player Bust")
            print('------------------------------------------------')
            print('\n\n')
            return 1
        return 0
    elif stand == True:
        
        gameRound()
        print('\n')
        print('-----------------------------------------------')
        if player1hand.handValue() > 21 and dealer1hand.handValue() > 21:
            player1hand.clsBet()
            print("Player Bust")
        elif player1hand.handValue() <= 21 and dealer1hand.handValue() > 21:
            player1.addBankroll(int(player1hand.getBet()) * 2)
            player1hand.clsBet()
            print("Player Wins")
        elif player1hand.handValue() == 21 and dealer1hand.handValue() < 21:
            player1.addBankroll(int(player1hand.getBet()) * 2)
            player1hand.clsBet()
            print("Player Wins")
        elif player1hand.handValue() > 21 and dealer1hand.handValue() <= 21:
            player1hand.clsBet()
            print("Player Bust")
        elif player1hand.handValue() < 21 and dealer1hand.handValue() == 21:
            player1hand.clsBet()
            print("Player Bust")
        elif player1hand.handValue() > dealer1hand.handValue():
            player1.addBankroll(int(player1hand.getBet()) * 2)
            player1hand.clsBet()
            print("Player Wins")
        elif player1hand.handValue() < dealer1hand.handValue():
            player1hand.clsBet()
            print("Player Bust")
        elif player1hand.handValue() == dealer1hand.handValue():
            player1.addBankroll(int(player1hand.getBet()))
            player1hand.clsBet()
            print("Push")
        print('------------------------------------------------')
        print('\n\n')
        return 1


# In[183]:


def gameOption():
    while(True):
        print('\nq : quit, h : hit, s : stand, r : surrender')
        print('Enter Option : ')
        option = input()
        if option == 'q':
            sys.exit()
        elif option == 'h':
            player1hand.addCard(deck.deckPopCard())
            temp = checkForWin()
            return temp
        elif option == 's':
            dealer1hand.addCard(deck.deckPopCard())
            dealer1hand.addCard(deck.deckPopCard())
            temp = checkForWin(True)
            return temp
        elif option == 'r':
            pass


# In[184]:


def gameRound(game_round = False):
    if game_round:
        print('\n------------Round {x}------------'.format(x = game_round))
    else:
        print('\n------------End of Round------------')
    print('Bankroll\t: ' + str(player1))
    print('Bet\t\t: ' + str(player1hand.getBet()))
    print('Dealer\t\t: ' + str(dealer1hand.handValue()) + "\t: " + str(dealer1hand.handDealer()))
    print('Player\t\t: ' + str(player1hand.handValue()) + "\t: " + str(player1hand.handPlayer()))


# In[185]:


def createDeck():
    global deck
    deck = Deck(suits, faces)
    deck.deckShuffle()


# In[186]:


if __name__ == '__main__':
    game_round = 0

    while(True):

        if game_round == 0:
            game_round += 1
            print('--------------------Blackjack--------------------')
            print('****Start****')
            createDeck()
            print('Enter the bankroll amount : ')
            amt = int(input())
            player1 = Player(amt)
            dealer1hand = Hand()
            player1hand = Hand()

            setPlayerBet()

            dealer1hand.addCard(deck.deckPopCard())
            player1hand.addCard(deck.deckPopCard())

            gameRound(game_round)
            option = gameOption()
            if option == 1:
                game_round += 1
                continue

        elif game_round >= 1:
            gameRound(game_round)
            option = gameOption()
            if option == 1:
                game_round += 1
                dealer1hand.clsHand()
                player1hand.clsHand()
                setPlayerBet()
                dealer1hand.addCard(deck.deckPopCard())
                player1hand.addCard(deck.deckPopCard())
                continue