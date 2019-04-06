from random import shuffle
suits=["D","S","H","C"]
ranks=[14,13,12,11,10,9,8,7,6,5,4,3,2]
class Card():
	"""docstring for Card"""
	def __init__(self, suit,rank):
		self.suit=suit
		self.rank=rank
class Deck(object):
	"""docstring for Deck"""
	def __init__(self):
		num_of_cards=52
		self.deck=[]
		for i in range(4):
			for j in range(13):
				self.deck.append(Card(suits[i],ranks[j]))
		shuffle(self.deck)
	def divide_into_parts(self,num):
		self.res=[]
		if 52%num==0:
			for i in range(0, len(self.deck), 52/num):
			        self.res.append(self.deck[i:i + 52/num])
		return self.res
class player():
	"""docstring for player"""
	def __init__(self,name):
		self.name=name
		self.hand=[]  #private
		self.round_score=0
		self.score=0
		self.passed_cards=[]
	def init_round_score(self):
		self.round_score=0
	def give_cards(self,hand):
		self.hand=hand
	def update_round_score(self,num):
		self.round_score+=num
	def update_total_score(self,num):
		self.score+=num
	def select_3_init(self,to_pass):
		a,b,c =	self.hand[0],self.hand[1],self.hand[2]
		self.hand.remove(a)
		self.hand.remove(b)
		self.hand.remove(c)
		# make fn
	def get_3_init(self,cards):
		# make fn
		self.hand.append(cards[0])
		self.hand.append(cards[1])
		self.hand.append(cards[2])
	def choose(self,player_1_score,player_2_score,player_3_score,player_1_round_score,player_2_round_score,player_3_round_score,player_1_passed_cards,player_2_passed_cards,player_3_passed_cards,cardsforhand):
		# card=get_card(self.hand,player1,player2,player3)
		print "cards player till now in round:- "
		for i in cardsforhand:
			print i.suit,i.rank
		print 
		print "Hand for player",self.name
		for i in range(len(self.hand)):
			print i,"-->",self.hand[i].suit,self.hand[i].rank
		print "give index of card:-"
		index=input()
		return self.hand[index]
		# make fn
		# check if valid card
	def get_hand(self):
		return self.hand
	def add_passed_cards(self,card):
		self.hand.remove(card)
		self.passed_cards.append(card)
		# bool valid=False
		# for i in self.hand:
		# 	if card==self.hand[i]:
		# 		valid=True
		# 		break
		# if(valid):
		# 	return card	
		# else:
		# 	print "wrong selection"	
		# 	self.score-=5
