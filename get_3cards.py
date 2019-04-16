def get_3_init(player,to_pass):
	# to_pass can be left , right or across
	suits = {'C': [], 'H': [], 'D':[], 'S':[]}
	for hand in player.hand:
		suits[hand.suit].append(hand.rank)
	print(suits)
	return player.hand[0],player.hand[1],player.hand[2]
