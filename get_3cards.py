from objects import *

def get_3_init(player,to_pass):
	# to_pass can be left , right or across
	suits = ['H', 'C', 'D', 'S']
	decks = {'C': [], 'H': [], 'D':[], 'S':[]}

	to_pass = []
	taken_to_pass = 0
	for hand in player.hand:
		decks[hand.suit].append(hand.rank)

	if 12 in decks['S']:
		if 13 in decks['S']:
			to_pass.extend([Card('S', 12),Card('S', 13)])	#Change all extend and append to this format
			taken_to_pass += 2
		elif 14 in decks['S']:
			to_pass.extend([12,14])
			taken_to_pass += 2
		elif 13 in decks['S'] and 14 in decks['S']:
			to_pass.extend([12,13,14])
			taken_to_pass += 3
		elif len(decks['S']) < 3:
			to_pass.extend(decks['S'])
			taken_to_pass += len(decks['S'])


	if 12 not in decks['S']:
		if 13 in decks['S']:
			to_pass.append(13)
			taken_to_pass += 1
		if 14 in decks['S']:
			to_pass.append(14)
			taken_to_pass += 1
		for suit in suits:
			deck = decks[suit]
			if len(deck) <= 3 - taken_to_pass:
				to_pass.extend(deck)
				taken_to_pass += len(deck)

		if 2 in decks['C']:
			to_pass.append(2)
			taken_to_pass += 1

		heart = list(set(deck['H']))
		for x in range(len(heart)-1, 0, -1):
			to_pass.append(heart[x])
			taken_to_pass += 1
			if taken_to_pass == 3:
				break

		for x in range(14,2, -1):
			for s in ['D', 'C']:
				to_pass.append(Card(s,x))
				taken_to_pass += 1
				if taken_to_pass ==3:
					break
			if taken_to_pass ==3:
				break

	return to_pass[0],to_pass[1],to_pass[2]
