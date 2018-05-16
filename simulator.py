from player import *
import card


class simulator:
	''' This class will handle turn phases, check state based actions, check 
	and resolve the stack, pass priority

	Active and nactive will be the players. The players will store
	who was the first and who was the second player. '''

	# These lists are sorted by timestamp (ie, earliest = first)
	# Top of deck = 0
	stack = []
	tapped = []
	# 0 = active player, 1 = not active player
	priority = 0
	

	# Initialize a game (no player decisions made here)
	def __init__(self, player1, player2):

		self.active = player1
		self.nactive = player2
		# Tell players who's going first
		self.active.first = 1
		self.nactive.first = 0
		# Initialize decks
		self.active.shuffle()
		self.nactive.shuffle()

#########################################################################
########################### BEGINNING OF GAME ###########################
#########################################################################

	def begin_game(self):
		mull_act = 1 	# player.should_mull must change this to 1 or 0
		mull_nact = 1	# 1 = mulligan, 0 = no mulligan

		act_handsize = 7
		nact_handsize = 7

		while mull_act == 1 or mull_nact == 1:
		# While at least one player wants to mulligan:

			if mull_act == 1:
			# If active player wants to mulligan:
				# Move cards from hand to deck, if any, then shuffle
				self.move(self.active.lib, self.active.hand)
				self.active.shuffle()
				# Draw a new hand
				self.draw_num(self.active, act_handsize)
				opp_mulls = 7 - nact_handsize
				mull_act = self.active.should_mull(opp_mulls)
				act_handsize -= 1

			if mull_nact == 1:
			# If non active player wants to mulligan:
				# Move cards from hand to deck, if any, then shuffle
				self.move(self.nactive.lib, self.nactive.hand)
				self.nactive.shuffle()
				# Draw a new hand
				self.draw_num(self.nactive, nact_handsize)
				opp_mulls = 7 - act_handsize
				mull_nact = self.nactive.should_mull(opp_mulls)
				nact_handsize -= 1

		# If handsize < 7, then scry 1
		if act_handsize < 7:
			top = self.active.scry(self.nactive.pub, \
				  self.active.lib[0])
			if not top:
				move(self.active.deck, self.active.deck[0])
		if nact_handsize < 7:
			top = self.nactive.scry(self.active.pub, \
				  self.nactive.lib[0])
			if not top:
				move(self.nactive.deck, self.nactive.deck[0])

		# After mulligans, determine pre game actions (ie. leyline, etc)
		stack.append(self.active.pre_game_actions(self.nactive.pub))
		while len(stack) > 0:
			resolve()
		stack.append(self.nactive.pre_game_actions(self.active.pub))
		while len(stack) > 0:
			resolve()

#########################################################################
############# UTILITY FUNCTIONS #########################################
#########################################################################

	def draw_num(self, drawer, num):
	# drawer = drawing player (active or nactive)
	# This is way more complicated than just moving
	# Required functionality:
	# 	Draw 3 = draw, draw, draw means you need to check to see if these
	#		need to be revealed
	# 	Need to change known deck information - player is responsible
	# 		for this, so need to tell both players that we've drawn

		# Check who the other player is
		if drawer == self.active:
			other = self.nactive
		else:
			other = self.active

		for i in range(num):
			# drawing player draws, check if top card revealed
			# tell other player that drawing player drew
			drawer.draw_one()
			if drawer.top_reveal:
				drawn_card = drawer.lib[0]
			else:
				drawn_card = '?'
			other.opp_drew(drawn_card)

	

	def move(self, moveTo, beingMoved):
	# Move beingMoved to moveTo. Always move to the end of the 
	# list (ie, moveTo + beingMoved)
	# MOVES TO BOTTOM OF LIBRARY (ie, top = 0)
		moveTo += beingMoved
		beingMoved = []
		return moveTo

	def move_top(self, moveTo, beingMoved):
	# Move to the front of moveFrom (ie, tutor to top of library)
	# MOVES TO TOP OF LIBRARY (ie, top = 0)
		moveTo = beingMoved + moveTo

#########################################################################
####################### TURN PHASES #####################################
#########################################################################
	def untap(self):
		pass

	def upkeep(self):
		pass

	def draw(self):
		draw_num(self, self.active, 1)
		# Now give priority to active player and repeat until stack
		# is empty

	def first_main(self):
		pass

	def combat(self):
		pass

	def attackers(self):
		pass

	def blockers(self):
		pass 

	def damage_first(self):
		pass

	def damage(self):
		pass

	def sec_main(self):
		pass

	def end_step():
		pass


#########################################################################
################### THE STACK AND STATE BASED ACTIONS ###################
#########################################################################
	def resolve(self):
	# Resolve the top of the stack, check for triggered abilities, then
	# pass priority to other player
		pass

	def pass_priority(self):
	# Check for state based actions, then triggered abilities
	# If an ability was triggered, then check state based actions again
	# If no abilities were triggered, then pass priority
		pass

	def triggered_abilities(self):
	# Check for triggered abilities
		pass

	def state_based_actions(self):
	# Check for state based actions
		pass