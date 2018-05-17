import card
import random
from strategy import *

class player(strategy):
	''' player is a trusted program - it stores the deck and modifies
	some of the zones (ie, drawing). It's not allowed to do anything 
	unless explicitly told to by simulator.'''

	def __init__(self, cards):
		# first stores whether or not you're going first
		self.first = -1
		# active stores whether or not we're the active player
		self.active = -1

		# lib is the actual order of the deck
		self.lib = []

		# Is the top card of my library revealed?
		self.top_reveal = 0

		# cards = decklist
		self.decklist = cards
		# Fill out information about your deck as you go
		for card in self.decklist:
			self.lib.append(card)

	def should_mull(self, opp_mulls):
		pass

	def pre_game_actions(self, state):
		# We can tell if we're the first player or not by checking 
		# self.first
		if self.first == 1:
			pass
		pass

	def scry(self, opp_state, cards):
	# Return 1 if top, 0 if bottom
		top = self.scry_strat(opp_state, cards)
		return top

	def shuffle(self):
		random.shuffle(self.lib)

	def draw_one(self):
		pass


