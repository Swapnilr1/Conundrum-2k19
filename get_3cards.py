import objects

def getdeck(player):
	decks = {'C': [], 'H': [], 'D':[], 'S':[]}
	for hand in player.hand:
		decks[hand.suit].append(hand.rank)
	return decks

def get_3_init(player,to_pass):
	# to_pass can be left , right or across
	suits = ['H', 'C', 'D', 'S']
	decks = {'C': [], 'H': [], 'D':[], 'S':[]}

	Pass = set([])
	for hand in player.hand:
		decks[hand.suit].append(hand.rank)

	if 12 in decks['S']:
		if 13 in decks['S']:
			Pass.add(('S', 12))
			Pass.add(('S', 13))	#Change all extend and append to this format
		elif 14 in decks['S']:
			Pass.add(('S', 12))
			Pass.add(('S', 14))
		elif 13 in decks['S'] and 14 in decks['S']:
			Pass.add(('S', 12))
			Pass.add(('S', 13))
			Pass.add(('S', 14))
		elif len(decks['S']) < 3:
			for i in decks['S']:
				Pass.add(('S', i))


	if 12 not in decks['S']:
		if 13 in decks['S']:
			Pass.add(('S', 13))
		if 14 in decks['S']:
			Pass.add(('S', 14))
		for suit in suits:
			deck = decks[suit]
			if len(deck) <= 3 - len(Pass):
				for i in deck:
					Pass.add((suit,i))

		if 2 in decks['C']:
			Pass.add(('C', 2))

		heart = list(set(decks['H']))
		for x in range(len(heart)-1, 0, -1):
			Pass.add(('H', heart[x]))
			if len(Pass) >= 3:
				break

		for x in range(14, 2, -1):
			for s in ['D', 'C']:
				if x in decks[s]:
					Pass.add((s, x))
					if len(Pass) >=3:
						break
			if len(Pass) >=3:
				break

	while len(Pass) < 3:
		for x in range(14, 2, -1):
			for s in ['H', 'S']:
				if x in decks[s]:
					Pass.add((s, x))
			if len(Pass) >=3:
				break

	temp = []
	Pass = list(Pass)
	for i in range(len(Pass)):
		x = Pass[i]
		for z in player.hand:
			if z.suit == x[0] and z.rank == x[1]:
				temp.append(z)

	return temp[0],temp[1],temp[2]
