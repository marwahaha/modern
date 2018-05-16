import card

class strategy:
	known_deck = []
	opponent_hand = []

	battle = []
	grave = []
	exile = []

	hand = []

	pub = {'bf': battle, 'gy': grave, 'ex': exile}
	priv = {'hand': hand}

	def __init__(self):
		self.known_deck = []
		self.opponent_hand = []

		self.battle = []
		self.grave = []
		self.exile = []

	def scry_strat(self, opp_state, cards):
		# 1 = top, 0 = bottom
		return 1

	def opp_drew(self, drawn_card):
		self.opponent_hand += [drawn_card]
		