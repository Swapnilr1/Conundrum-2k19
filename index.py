from objects import *
from get_3cards import *
heart_break=0
curr_suit=""
max_penals=10
def set_heart_break(val):
	global heart_break
	print heart_break
	heart_break=val	
def isValid_first(card_a,player):
	# exit()
	if(card_a.suit=="H"):
		if(heart_break==1):
			curr_suit="H"
			return True
		else:
			# print "ball"
			if(find_suit(player.get_hand(),"S")==False and find_suit(player.get_hand(),"C")==False and find_suit(player.get_hand(),"D")==False):
				set_heart_break(1)
				curr_suit="H"
				return True
			else:
				return False
	else:
		curr_suit=card_a.suit
		return True
def check_pass(round_num):
	if round_num%4==0:
		return "no"
	elif round_num%4==1:
		return "left"
	elif round_num%4==2:
		return "right"
	else:
		return "across"
def isValid(card_b,player):
	if card_b.suit!=curr_suit:
		if(find_suit(player.get_hand(),curr_suit)==False):
			if card_b.suit=="H":
				set_heart_break(1)
				return True
			return True	
		else:
			return False
	return True		
def get_score(cardforhand):
	score=0
	for i in range(4):
		if cardforhand[i].suit=="H":
			score+=1
		if cardforhand[i].suit=="S" and cardforhand[i].rank==12:
			score+=13
	return score
def find_suit(Arr,Suit):
	for i in Arr:
		if i.suit==Suit:
			return True
	return False
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
		players[0].score=0
		players[1].score=26
		players[2].score=26
		players[3].score=26
	elif B.round_score==26:
		players[0].score=26
		players[1].score=0
		players[2].score=26
		players[3].score=26
	elif C.round_score==26:
		players[0].score=26
		players[1].score=26
		players[2].score=0
		players[3].score=26
	elif D.round_score==26:
		players[0].score=26
		players[1].score=26
		players[2].score=26
		players[3].score=0
	else:
		for i in range(4):
			players[i].score+=players[i].round_score
def give_cards(players,to_pass):
	if to_pass=="right":
		for i in range(1,4):
			for j in range(3):
				players[i].hand.append(cards_to_pass[i-1][j])
		for j in range(3):
			players[0].hand.append(cards_to_pass[3][j])
	elif to_pass=="left":
		for i in range(3):
			for j in range(3):
				players[i].hand.append(cards_to_pass[i+1][j])
		for j in range(3):
			players[3].hand.append(cards_to_pass[0][j])
	elif to_pass=="across":
		for i in range(3):
			players[0].hand.append(cards_to_pass[2][i])
		for i in range(3):
			players[2].hand.append(cards_to_pass[0][i])
		for i in range(3):
			players[1].hand.append(cards_to_pass[3][i])
		for i in range(3):
			players[3].hand.append(cards_to_pass[1][i])
players=[]
players.append(player1("Fer"))
players.append(player2("Fallen"))
players.append(player3("Taco"))
players.append(player4("Cold"))
deck=Deck()
round_num=0
while(1):#entire game
	hand_num=0
	round_num+=1
	for i in range(4):
		print players[i].name,players[i].score
	hands=deck.divide_into_parts(4)
	cards_to_pass=[]
	for i in range(4):
		players[i].give_cards(hands[i])#distribute cards
		players[i].init_round_score()#initialize round score to 0
		cards_to_pass.append(players[i].give_3_init(check_pass(round_num)))
	give_cards(players,check_pass(round_num))
	heart_break=0
	two_of_club=-1
	for i in range(4):
		for j in players[i].hand:
			if j.suit=="C" and j.rank==2:
				two_of_club=i
				break
	for i in range(4-two_of_club):
		players=[players[-1]] + players[0:-1]
	while(players[0].get_hand()):#for every round while hand is not empty
		cardforhand=[]
		curr_suit=""
		print "Move",players[0].name
		card_a=players[0].choose(players[1].name,players[2].name,players[3].name,players[1].score,players[2].score,players[3].score,players[1].round_score,players[2].round_score,players[3].round_score,players[1].passed_cards,players[2].passed_cards,players[3].passed_cards,cardforhand)
		if hand_num==0:
			if card_a.suit!="C" or card_a.rank!=2:
				print "wrong card"
				players[0].num_penalties+=1
				while(players[0].num_penalties<max_penals):
					card_a=players[0].choose(players[1].name,players[2].name,players[3].name,players[1].score,players[2].score,players[3].score,players[1].round_score,players[2].round_score,players[3].round_score,players[1].passed_cards,players[2].passed_cards,players[3].passed_cards,cardforhand)
					if card_a.suit=="C" and card_a.rank==2:
						curr_suit=card_a.suit
						cardforhand.append(card_a)
						players[0].add_passed_cards(card_a)
						break
					else:
						print "wrong card"
						players[0].num_penalties+=1
				if(players[0].num_penalties>=max_penals):
					players[0].score+=100
					break
			else:
				card_suit="C"
				cardforhand.append(card_a)
				players[0].add_passed_cards(card_a)

		else: 
			if(isValid_first(card_a,players[0])==True):
				curr_suit=card_a.suit
				cardforhand.append(card_a)
				players[0].add_passed_cards(card_a)
			else:
				print "wrong card"
				players[0].num_penalties+=1
				while(players[0].num_penalties<max_penals):
					card_a=players[0].choose(players[1].name,players[2].name,players[3].name,players[1].score,players[2].score,players[3].score,players[1].round_score,players[2].round_score,players[3].round_score,players[1].passed_cards,players[2].passed_cards,players[3].passed_cards,cardforhand)
					if (isValid_first(card_a,players[0])==True):
						curr_suit=card_a.suit
						cardforhand.append(card_a)
						players[0].add_passed_cards(card_a)
						break
					else:
						print "wrong card"
						players[0].num_penalties+=1
				if(players[0].num_penalties>=max_penals):
					players[0].score+=100
					break		
		print "Move",players[1].name
		card_b=players[1].choose(players[0].name,players[2].name,players[3].name,players[0].score,players[2].score,players[3].score,players[0].round_score,players[2].round_score,players[3].round_score,players[0].passed_cards,players[2].passed_cards,players[3].passed_cards,cardforhand)
		if(isValid(card_b,players[1])==True):
			cardforhand.append(card_b)
			players[1].add_passed_cards(card_b)
		else:
			print "wrong card"
			players[1].num_penalties+=1
			while(players[1].num_penalties<max_penals):
				card_b=players[1].choose(players[0].name,players[2].name,players[3].name,players[0].score,players[2].score,players[3].score,players[0].round_score,players[2].round_score,players[3].round_score,players[0].passed_cards,players[2].passed_cards,players[3].passed_cards,cardforhand)
				if(isValid(card_b,players[1])==True):
					cardforhand.append(card_b)
					players[1].add_passed_cards(card_b)
					break
				else:
					print "wrong card"
					players[1].num_penalties+=1
			if(players[1].num_penalties>=max_penals):
				players[1].score+=100
				break
		print "Move",players[2].name
		card_c=players[2].choose(players[0].name,players[1].name,players[3].name,players[0].score,players[1].score,players[3].score,players[0].round_score,players[1].round_score,players[3].round_score,players[0].passed_cards,players[1].passed_cards,players[3].passed_cards,cardforhand)
		if(isValid(card_c,players[2])==True):
			cardforhand.append(card_c)
			players[2].add_passed_cards(card_c)
		else:
			print "wrong card"
			players[2].num_penalties+=1
			while(players[2].num_penalties<max_penals):
				card_c=players[2].choose(players[0].name,players[1].name,players[3].name,players[0].score,players[1].score,players[3].score,players[0].round_score,players[1].round_score,players[3].round_score,players[0].passed_cards,players[1].passed_cards,players[3].passed_cards,cardforhand)
				if(isValid(card_c,players[2])==True):
					cardforhand.append(card_c)
					players[2].add_passed_cards(card_c)
					break
				else:
					print "wrong card"
					players[2].num_penalties+=1
			if(players[2].num_penalties>=max_penals):
				players[2].score+=100
				break
		print "Move",players[3].name
		card_d=players[3].choose(players[0].name,players[1].name,players[2].name,players[0].score,players[1].score,players[2].score,players[0].round_score,players[1].round_score,players[2].round_score,players[0].passed_cards,players[1].passed_cards,players[2].passed_cards,cardforhand)
		if(isValid(card_d,players[3])==True):
			cardforhand.append(card_d)
			players[3].add_passed_cards(card_d)
		else:
			print "wrong card"
			players[3].num_penalties+=1
			while(players[3].num_penalties<max_penals):
				card_d=players[3].choose(players[0].name,players[1].name,players[2].name,players[0].score,players[1].score,players[2].score,players[0].round_score,players[1].round_score,players[2].round_score,players[0].passed_cards,players[1].passed_cards,players[2].passed_cards,cardforhand)
				if(isValid(card_d,players[3])==True):
					cardforhand.append(card_d)
					players[3].add_passed_cards(card_d)
					break
				else:
					print "wrong card"
					players[3].num_penalties+=1
			if(players[3].num_penalties>=max_penals):
				players[3].score+=100
				break
		index=evaluate_hand(cardforhand,players)		
		print "HAND FOR PLAYER",players[index].name
		for i in range(4-index):
			players=[players[-1]] + players[0:-1]
		hand_num+=1
	print "END OF ROUND"
	evaluate_round(players)
	Min=9999
	Min_index=-1
	Max=-1
	for i in range(4):
		Max=max(Max,players[i].score)
		if(Min>min(Min,players[i].score)):
			Min=players[i].score
			index=i
	winners=[]
	for i in range(4):
		if players[i].score==players[index].score:
			winners.append(players[i].name)
	if Max>=100:
		for i in winners:
			print i," "
		print "wins"
		break