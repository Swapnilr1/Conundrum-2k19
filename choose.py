def getindex(player, suit, rank):
	index = 0
	for hand in player.hand:
		if hand.rank == rank and hand.suit==suit:
			return index
		index += 1	


def get_card_from_user(player,player_1_name,player_2_name,player_3_name,player_1_score,player_2_score,player_3_score,player_1_round_score,player_2_round_score,player_3_round_score,player_1_passed_cards,player_2_passed_cards,player_3_passed_cards,cardsforhand):
	# function returns a card from your hand for the current round.
	decks = {'C': [], 'H': [], 'D':[], 'S':[]}
	for hand in player.hand:
		decks[hand.suit].append(hand.rank)
	#print decks
	print "PART 1"
	card = 0 #Selecting card to pick
	if len(cardsforhand)==0: #My move is first in the trick
		
	else:
		suit = cardsforhand[0].suit
		if (len(decks[suit])==0): #Not having this suit
			if 12 in decks['S']:
				return player.hand[getindex(player, 'S', 12)]
		sortedsuit = sorted(decks[suit])
		if (sortedsuit[-1] > )

	for card in cardsforhand:
		print card.suit, card.rank
	print "PART 2"
	print player.hand[0].suit, player.hand[0].rank
	return player.hand[0]