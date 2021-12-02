#  Blackjack- game written by L. M. Serafin

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
ask = ""
score = 0
table = []
player = []
deck = []
#pos=[0,0]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos,FaceDown):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]   
    
    def __str__(self):
        s = " "
        for i in self.hand:
            s= s+str(i) +""
        return s    
        

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        handvalue = 0
        Aces = 0
        for x in self.hand:
            if x.get_rank() == 'A':
                Aces += 1
            handvalue += VALUES.get(x.get_rank())
        if Aces > 0 and (handvalue + 10) <= 21:
            handvalue += 10
        return handvalue

        
    def busted(self):
        global busted
        sum = self.get_value()
        if sum > 21:
                return True
            
    def hit(self, deck):
        self.add_card(deck.deal_card())
    
       
    def draw(self, canvas, p):
        for s in self.hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(s.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(s.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [p[0] + CARD_CENTER[0] + 73 * self.hand.index(s), p[1] + CARD_CENTER[1]], CARD_SIZE)
 
    
    
        
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
        #self.shuffle()
        
    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck) 

    def deal_card(self):
        return self.deck.pop()
    
   


#define event handlers for buttons
def deal():
    global outcome, in_play,ask,table, player, deck, score
    deck=Deck()
    deck.shuffle()
    table=Hand()
    player=Hand()
    outcome = ""
    ask = " Your move, hit or stand?"    
    in_play = True
    table.hit(deck)
    player.hit(deck)
    table.hit(deck)
    player.hit(deck)
    
    
def hit():
    global  in_play, outcome,ask,score
    if in_play == True:
        player.hit(deck)
    if player.busted():
        outcome = "You are busted!"
        ask = "Want to play again?"
        in_play = False
        score -=1
    if player.get_value() == 21:
        in_play = False
        outcome= "You got BLACKJACK!"
        ask = "Want to play again?"
        score +=1
    
       
def stand():
    global in_play, outcome,ask,score
    if in_play == True :
        while table.get_value() < 17 :
            table.hit(deck)
        if table.busted():
            outcome = "Casino are busted!"
            ask = "Want to play again?"
            in_play = False
            score +=1
    if not table.busted() and table.get_value() > player.get_value() :
        outcome = "Casino won!"
        score -= 1
    if not table.busted() and table.get_value() == player.get_value() :
        outcome = "It's tie !"
    if not table.busted() and table.get_value() < player.get_value() :
        outcome = "you won!"
        score +=1
    in_play = False
    ask = "Want to play again?"
# draw handler    
def draw(canvas):
    global in_play
    canvas.draw_text("Score: "+str(score), (400,100) ,28 , "Pink")
    canvas.draw_text("Blackjack",(250,50),36,"Black")
    canvas.draw_text("Casino", (70,180),28,"Blue")
    canvas.draw_text(outcome, (240,180),28, "White")
    canvas.draw_text("Player",(70,380),28,"Blue")
    canvas.draw_text(ask,(260,380),28,"White")
    table.draw(canvas, [0, 200])    
    player.draw(canvas, [0, 400])
    card=Hand()
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_SIZE)    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

#initial
deal()

# get things rolling
frame.start()


# remember to review the gradic rubric
