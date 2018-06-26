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
		# first stores whether or not you're going first
		self.first = -1

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

	def init_spell_strat(self, state):
		# This is the just filler right now - always try to cast the first
		# spell in your hand.
		if len(hand > 0):
			return hand[0]
		else:
			return 0

	def find_cost_modes(self, spell, state):
		
		return spell

	def choose_targets(spell, state):
		## TODO: pick an appropriate target. ##
		if first == 0:
			spell.targets[0] = state.p1
		else:
			spell.targets[0] = state.p2
		return spell

	def distr_effects(spell, state):
		## TODO: fill this in later with something trivial.
		return spell