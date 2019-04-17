def getdeck(player):
	decks = {'C': [], 'H': [], 'D':[], 'S':[]}
	for hand in player.hand:
		decks[hand.suit].append(hand.rank)
	return decks

def get_card_from_user(player,player_1_name,player_2_name,player_3_name,player_1_score,player_2_score,player_3_score,player_1_round_score,player_2_round_score,player_3_round_score,player_1_passed_cards,player_2_passed_cards,player_3_passed_cards,cardsforhand):
	# function returns a card from your hand for the current round.
	decks = getdeck(player)
	if len(decks[cardsforhand[0].suit]) != 0:
		deck = decks[cardsforhand[0].suit].sorted().reverse()
		card_to_play = (cardsforhand[0].suit,deck[0])
		for i in range(1, len(deck)):
			if deck[i] < cardsforhand[0].rank:
				card_to_play = deck[i]
	
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
			
	return player.hand[0]