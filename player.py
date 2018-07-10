import card
import random
from strategy import *

class player(strategy):
	''' player is a trusted program - it stores the deck and modifies
	some of the zones (ie, drawing). It's not allowed to do anything 
	unless explicitly told to by simulator.'''

	def __init__(self, cards):

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

		######## info for other classes/functions #######
		self.is_player = 1
		self.damage = 0
		self.life = 20

	def should_mull(self, opp_mulls):
		pass

	def pre_game_actions(self, state):
		# We can tell if we're the first player or not by checking 
		# self.first
		pre_game_perms = []
		if self.first == 1:
			pass
		return pre_game_perms

	def init_spell(self, state):
		spell = self.init_spell_strat(state)
		if spell == 0:
			return 0
		else:
			# costs are stored in spell object, find_cost_modes doesn't
			# return anything, just alters the spell object
			# Note: costs and modes need to happen at same time because 
			# of Collective Brutality
			spell = self.find_cost_modes(spell, state)
			
			# Update spell again, this time with targets
			spell = self.choose_targets(spell, state)
			# Update spell to distribute effects
			spell = self.distr_effects(spell, state)

			# Return the spell to check legality (hexproof, shroud, flash)
			return spell

	def pay_cost(self, state, spell):
		pass


	def scry(self, opp_state, cards):
	# Return 1 if top, 0 if bottom
		top = self.scry_strat(opp_state, cards)
		return top

	def shuffle(self):
		random.shuffle(self.lib)
		return

	def draw_one(self):
		pass


