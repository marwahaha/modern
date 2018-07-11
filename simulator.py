from player import *
import card


class ability:
	''' Stack objects are spells, activated abilities, or triggered 
	abilities. This will just handle abilities. This object needs to
	be able to check its legality, enforce cost payment, and announce
	its presence to opponents.
	'''
	def __init__(self, controller, effect, targets):
		self.controller = controller
		# effect is a function that permanents or the delayed
		# trigger handler produces.
		self.effect = effect
		# Targets is a list, listed in order the ability specifies
		self.targets = targets

class stack_object:
	''' This is what lives on the stack. They all get put in a list, so we
	can pop/append as necessary.

	NOTE: spell here refers to spell OR ability!
	'''
	def __init__(self, spell):
		self.spell = spell

		# num_passed is the number of times priority has been passed on it 
		# while it has been the top of the stack.
		# Note that the stack_object can't change this itself. Instead, it
		# gets changed by priority handlers (probably has_priority?)
		self.num_passed = 0

class state_obj:
	''' This is the object that gets passed around to player/strategy. This
	also stores the public states for simulator to access. Note that private
	states (exile face down, morph, etc) can't be stored here because this is
	passed to strategy who will use this info to make decisions. However, we 
	do need a way to mark exiled facedown cards... (TODO)
	'''

	p1 = None
	p2 = None

	def __init__(self):
		# These lists are sorted by timestamp (ie, earliest = first = 0)
		# Store info about tapped, etc in the permanent itself
		self.stack = []

		self.p1_grave = []
		self.p2_grave = []

		self.p1_battle = []
		self.p2_battle = []

		self.p1_exile = []
		self.p2_exile = []


class simulator:
	''' This class will handle turn phases, check state based actions, 
	check and resolve the stack, and pass priority

	Active and nactive will be the players. The players will store
	who was the first and who was the second player.

	Actions like drawing cards will start in the simulator, but the 
	actual moving of the list elements will occur in player
	 '''

	# Top of deck = 0

	# 0 = active player, 1 = not active player
	priority = 0

	# state is the object that gets passed around to player/strategy to help
	# in making strategy decisions.
	

	# Initialize a game (no strategy decisions made here)
	def __init__(self, player1, player2):
		self.active = player1
		self.nactive = player2
		# Tell players who's going first
		self.active.first = 1
		self.nactive.first = 0
		# Initialize decks
		self.active.shuffle()
		self.nactive.shuffle()

		self.state = state_obj()
		self.state.p1 = player1
		self.state.p2 = player2

		self.debug = 1

#########################################################################
########################### BEGINNING OF GAME ###########################
#########################################################################

	def begin_game(self):
		mull_act = 1 	# player.should_mull must change this to 1 or 0
		mull_nact = 1	# 1 = mulligan, 0 = no mulligan

		act_handsize = 7
		nact_handsize = 7

		################# Mulligans ##################
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

		############ Scrying ##############
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

		############# Pre game effects #############
		# After mulligans, determine pre game actions (ie. leyline, etc)
		self.state.p1_battle += self.state.p1.pre_game_actions(self.state)
		self.state.p2_battle += self.state.p2.pre_game_actions(self.state)
		return

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

	def clean_up():
		pass

	def pass_turn():
		former_active = self.active
		self.active = self.nactive
		self.nactive = former_active

#########################################################################
################### THE STACK AND STATE BASED ACTIONS ###################
#########################################################################
	def resolve(self):
	# Resolve the top of the stack, check for state based actions,
	# check for triggered abilities, then
	# pass priority to active player
		resolve_me = self.state.stack.pop()
		if resolve_me.check_legality() == 1:
			########### TODO: Check for replacement effects #############
			resolve_me.resolve()



	def pass_priority(self, player):
	# Check for state based actions, then triggered abilities
	# If an ability was triggered, then check state based actions again
	# If no abilities were triggered, 
	# call has_priority to prompt activated abilities
	# or spell casting

		# Check for SBA's and triggered abilities until there are no more
		# changes
		acted = 1
		while acted == 1:
			acted = self.state_based_actions()

		triggered = 1
		while triggered == 1:
			triggered = self.triggered_abilities()

		resolve = 0
		if self.state.stack != []:
			if self.debug == 1:
				print(self.state.stack)


			# Tell the stack object that priority is being passed one
			# more time while they're on top 
			self.state.stack[-1].times_passed += 1
			resolve = self.state.stack[-1].times_passed

		if resolve > 1: 
			# If priority has been passed on this more than once (ie,
			# both players have passed priority), then resolve it
			resolve()
			if self.debug == 1:
				print('here')
				return
			self.has_priority(self.active)
		else:
			self.has_priority(player)

	def triggered_abilities(self):
	# Check for triggered abilities
		# No triggered abilities yet, so we just continue 
		return 0

	def state_based_actions(self):
	# Check for state based actions
	# Return 1 if any state based actions occured (eg, damage is now lethal,
	# so another creature dies, etc)
		# No SBA's yet, so we just continue 
		return 0

	def has_priority(self, player):
	# 	if self.debug == 1:
	# 		if player == self.state.p1:
	# 			print('Player 1 has priority')
	# 		else:
	# 			print('Player 2 has priority')
		
		spell = self.cast_spell(player)	
		if spell != 0:
			stack_spell = stack_object(spell)
			self.state.stack.append(stack_spell)

			if self.debug == 1:
				print('spell added to stack ' + str(spell.name))

		# For clarity, this will probably get merged with spell
		# Also, right now, you get to cast a spell and activate an ability
		# and that's not how the rules work.
		ability = self.activate_ability(player)			
		if ability != 0:
				stack_ability = stack_object(ability)
				self.state.stack.append(stack_ability)

				if self.debug == 1:
					print('ability added to stack ' + str(ability.name))


		# If the player wants to hold priority, then return 1
		hold = 0
		hold = player.hold_priority()
		if hold == 1:
			priority = self.pass_priority(player)
		else:
			if player == self.state.p1:
				other_player = self.state.p2
			else:
				other_player = self.state.p1
			priority = self.pass_priority(other_player)

		 



#########################################################################
################ SPELLS + ABILITIES (RESOLUTION, ETC) ###################
#########################################################################
	def activate_ability(self,player):
		# This is the activated ability version of spells.
		# Perhaps they'll even end up being the same function,
		# since there are lots of similarites 
		# Although probably not, since they'll probably have different
		# check_legality's
		return 0

	def cast_spell(self, player):
		spell = player.init_spell(self.state)
		if spell == 0:
			return 0
		if self.check_legality(spell) == 0:
			spell.reset()
			return 0
		if self.paid_cost(spell) == 0:
			spell.reset()
			return 0
		return spell

	def check_legality(self, spell):
		legal = 1
		# First, check if targets are the right type and number
		legal = self.spell.legal()

		######### TODO: Check permanents for legality effects ###########
		## Ie, flash, hexproof, shroud, protection ##
		
		return legal

	def paid_cost(self, spell):
		# Prompt player to pay appropriate costs
		# 1 = paid, 0 = did not pay
		paid = player.pay_cost(self.state, spell)
		return paid

