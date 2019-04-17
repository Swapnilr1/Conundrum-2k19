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

	Pass = []
	taken_Pass = 0
	for hand in player.hand:
		decks[hand.suit].append(hand.rank)

	if 12 in decks['S']:
		if 13 in decks['S']:
			Pass.extend([objects.Card('S', 12),objects.Card('S', 13)])	#Change all extend and append to this format
			taken_Pass += 2
		elif 14 in decks['S']:
			Pass.extend([object.Card('S', 12),object.Cards('S', 14)])
			taken_Pass += 2
		elif 13 in decks['S'] and 14 in decks['S']:
			Pass.extend([objects.Card('S', 12),objects.Card('S', 13), objects.Card('S', 14)])
			taken_Pass += 3
		elif len(decks['S']) < 3:
			for i in decks['S']:
				Pass.append(objects.Card('S', i))
			taken_Pass += len(decks['S'])


	if 12 not in decks['S']:
		if 13 in decks['S']:
			Pass.append(objects.Card('S', 13))
			taken_Pass += 1
		if 14 in decks['S']:
			Pass.append(objects.Card('S', 14))
			taken_Pass += 1
		for suit in suits:
			deck = decks[suit]
			if len(deck) <= 3 - taken_Pass:
				for i in deck:
					Pass.append(objects.Card(suit,i))
				taken_Pass += len(deck)

		if 2 in decks['C']:
			Pass.append(objects.Card('C', 2))
			taken_Pass += 1

		heart = list(set(decks['H']))
		for x in range(len(heart)-1, 0, -1):
			Pass.append(objects.Card('H', heart[x]))
			taken_Pass += 1
			if taken_Pass >= 3:
				break

		for x in range(14, 2, -1):
			for s in ['D', 'C']:
				if x in decks[s]:
					Pass.append(objects.Card(s, x))
					taken_Pass += 1
					if taken_Pass >=3:
						break
			if taken_Pass >=3:
				break
	print(len(Pass))
	# for i in Pass:
	# 	print(i.suit, i.rank)
	return Pass[0],Pass[1],Pass[2]
