from objects import *
def get_score(cardforhand):
	score=0
	for i in range(4):
		if cardforhand[i].suit=="H":
			score+=1
		if cardforhand[i].suit=="S" and cardforhand[i].rank==13:
			score+=13
	return score
def evaluate_hand(cardforhand,players):
	suit_for_hand=cardforhand[0].suit
	index=-1
	max_rank=1
	winner=""
	for i in range(4):
		if suit_for_hand==cardforhand[i].suit:
			if(cardforhand[i].rank>max_rank):
				max_rank=cardforhand[i].rank
				index=i
	score=get_score(cardforhand)
	players[index].update_round_score(score)
	# rotate st winner has to move first next tym
	return index
def evaluate_round(players):
	A=players[0]
	B=players[1]
	C=players[2]
	D=players[3]
	if A.round_score==26:
		A.score=0
		B.score=26
		C.score=26
		D.score=26
	elif B.round_score==26:
		A.score=26
		B.score=0
		C.score=26
		D.score=26
	elif C.round_score==26:
		A.score=26
		B.score=26
		C.score=0
		D.score=26
	elif D.round_score==26:
		A.score=26
		B.score=26
		C.score=26
		D.score=0
	else:
		A.score=A.round_score
		B.score=B.round_score
		C.score=C.round_score
		D.score=D.round_score
def find_suit(Arr,Suit):
	for i in Arr:
		if i.suit==Suit:
			return True
	return False
players=[]
names=["A","B","C","D"]
for i in range(4):
	players.append(player(names[i]))
deck=Deck()
while(1):#entire game
	for i in range(4):
		print players[i].name,players[i].score
	hands=deck.divide_into_parts(4)
	for i in range(4):
		players[i].give_cards(hands[i])#distribute cards
		players[i].init_round_score()#initialize round score to 0
	heart_break=0
	while(players[0].get_hand()):#for every round while hand is not empty
		cardforhand=[]
		curr_suit=""
		print "Throw",players[0].name
		card_a=players[0].choose(players[1].score,players[2].score,players[3].score,players[1].round_score,players[2].round_score,players[3].round_score,players[1].passed_cards,players[2].passed_cards,players[3].passed_cards,cardforhand)
		if(card_a.suit=="H"):
			if heart_break==1:
				curr_suit="H"
				cardforhand.append(card_a)
			else:
				if(find_suit(players[0].get_hand(),"S")==False and find_suit(players[0].get_hand(),"C")==False and find_suit(players[0].get_hand(),"D")==False):
					heart_break=1
					curr_suit="H"
					cardforhand.append(card_a)
				else:
					print "cant throw heart"
					exit()
		else:
			curr_suit=card_a.suit
			cardforhand.append(card_a)
		players[0].add_passed_cards(card_a)
		print "Throw",players[1].name
		card_b=players[1].choose(players[0].score,players[2].score,players[3].score,players[0].round_score,players[2].round_score,players[3].round_score,players[0].passed_cards,players[2].passed_cards,players[3].passed_cards,cardforhand)
		if card_b.suit!=curr_suit:
			if(find_suit(players[1].get_hand(),curr_suit)==False):
				if card_b.suit=="H":
					heart_break=1
			else:
				print "wrong Card"
				exit()
		cardforhand.append(card_b)
		players[1].add_passed_cards(card_b)
		print "Throw",players[2].name
		card_c=players[2].choose(players[0].score,players[1].score,players[3].score,players[0].round_score,players[1].round_score,players[3].round_score,players[0].passed_cards,players[1].passed_cards,players[3].passed_cards,cardforhand)
		if card_c.suit!=curr_suit:
			if(find_suit(players[2].get_hand(),curr_suit)==False):
						if card_c.suit=="H":
							heart_break=1
						else:
							print "wrong Card"
							exit()
		cardforhand.append(card_c)
		players[2].add_passed_cards(card_c)
		print "Throw",players[3].name
		card_d=players[3].choose(players[0].score,players[1].score,players[2].score,players[0].round_score,players[1].round_score,players[2].round_score,players[0].passed_cards,players[1].passed_cards,players[2].passed_cards,cardforhand)
		if card_d.suit!=curr_suit:
			if(find_suit(players[3].get_hand(),curr_suit)==False):
						if card_d.suit=="H":
							heart_break=1
						else:
							print "wrong Card"
							exit()
		cardforhand.append(card_d)
		players[3].add_passed_cards(card_d)
		index=evaluate_hand(cardforhand,players)		
		for i in range(4-index):
			players=[players[-1]] + players[0:-1]
	evaluate_round(players)