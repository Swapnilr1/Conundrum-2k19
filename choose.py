from random import randint

def getindex(player, suit, rank):
	index = 0
	for hand in player.hand:
		if hand.rank == rank and hand.suit==suit:
			return index
		index += 1

def getdeck(player):
	decks = {'C': [], 'H': [], 'D':[], 'S':[]}
	for hand in player.hand:
		decks[hand.suit].append(hand.rank)
	return decks

def get_card_from_user(player,player_1_name,player_2_name,player_3_name,player_1_score,player_2_score,player_3_score,player_1_round_score,player_2_round_score,player_3_round_score,player_1_passed_cards,player_2_passed_cards,player_3_passed_cards,cardsforhand):
	# function returns a card from your hand for the current round.
	decks = getdeck(player)
	if 2 in decks['C']:
		return player.hand[getindex(player, 'C', 2)]
	if len(cardsforhand)==0: #My turn is first
		heart=False
		for i in cardsforhand:
			if i.suit == 'H':
				heart = True
				break
		for i in player_1_passed_cards:
			if i.suit == 'H':
				heart = True
				break
		for i in player_2_passed_cards:
			if i.suit == 'H':
				heart = True
				break
		for i in player_3_passed_cards:
			if i.suit == 'H':
				heart = True
				break
		available_suits = []
		if (len(decks['C'])>0):
			available_suits.append('C')
		if (heart and len(decks['H'])>0):
			available_suits.append('H')
		if (len(decks['D'])>0):
			available_suits.append('D')

		if (len(available_suits)==0): #only Spades remaining
			sortedspades = sorted(decks['S'])
			return player.hand[getindex(player, 'S', decks['S'][0])]
		
		suitn = randint(1, len(available_suits)) - 1
		suit = available_suits[suitn]
		rank = decks[suit][randint(0, len(decks[suit]) -1)]
		return player.hand[getindex(player, suit, rank)]


	else:

		#We have a card from the deck being played.
		if len(decks[cardsforhand[0].suit]) != 0:
			largest_already_played = cardsforhand[0].rank
			for i in range(1,len(cardsforhand)):
				largest_already_played = max(largest_already_played, cardsforhand[i].rank)
			deck = sorted(decks[cardsforhand[0].suit])[::-1]
			cards_to_play = [(cardsforhand[0].suit,deck[0])]
			for i in range(1, len(deck)):
				if deck[i] < largest_already_played:
					cards_to_play.append((cardsforhand[0].suit,deck[i]))
					break
			heart_or_queen = False
			for i in cardsforhand:
				if i.suit == 'H' or (i.rank==12 and i.suit=='S'):
					heart_or_queen = True
					break
			if heart_or_queen:
				card_to_play = cards_to_play[-1]
			else:
				card_to_play = cards_to_play[randint(0,len(cards_to_play)-1)]
		else:
			if 12 in decks['S']:
				card_to_play = ('S', 12)
			if 13 in decks['S']:
				card_to_play = ('S', 13)
			if 14 in decks['S']:
				card_to_play = ('S', 14)
			elif len(decks['H']) != 0:
				card_to_play = ('H', sorted(decks['H'])[-1])	
			elif len(decks['D']) != 0:
				card_to_play = ('D', sorted(decks['D'])[-1])
			elif len(decks['C']) != 0:
				card_to_play = ('C', sorted(decks['C'])[-1])
			elif len(decks['S']) != 0:
				card_to_play = ('S', sorted(decks['S'])[-1])
			
		return player.hand[getindex(player, card_to_play[0], card_to_play[1])]