class card_template:
	# init sets things to base values (ie, cmc, mana color requirements)
	def __init__(self, owner):
		# DEBUG
		debug = 1
		# If debug is on, then print helpful info

		######## costs ###########
		# Note that generic mana isn't available since the caster needs
		# to propose how much of each type of mana to pay.
		# colored mana costs
		w = 0
		u = 0
		b = 0
		r = 0
		g = 0
		# colorless mana
		c = 0
		# generic mana
		generic = 0
		# cards (to discard)
		cost_cards = 0
		# life (for phyrexian mana, etc)
		cost_life = 0

 		############## player info ###############
		# Controller and owner are not quite the same (ie, control target 
		# player effects), although they start out the same
		owner = owner
		controller = owner
		
		########### type #################
		is_creature = 0
		is_enchantment = 0
		is_aura = 0
		is_artifact = 0
		is_land = 0
		is_planeswalker = 0

		is_instant = 0
		is_sorcery = 0

		########## casting info ############
		name = ''
		# list of targets in order on the card. If multiple groups of 
		# targets with unknown quantities, then list of lists
		targets = []
		split_sec = 0
		flash = 0
		# The spell itself can never change this info - this is always 
		# changed by player or simulator
		location = 'deck'
		# is_suspended tells you whether or not the spell is currently 
		is_suspended = 0
		time_counters = 0

	def reset(self, debug):
		self.targets = []
		if debug == 1:
			print('spell has been reset')

class bolt(card_template):
	def __init__(self):
		self.cmc = 1
		self.r = 1
		self.name = 'lightning bolt'

	# A spell can only check legality by checking its own targets
	# Overall legality is handled by simulator
	def legal_targets(self):
		if len(self.targets) != 1:
			self.reset(self.debug)
			if self.debug == 1:
				print('incorrect number of targets')
			# 0 = not legal, let player know so they can put the card
			# back where it came from
			return 0
		if self.targets[0].is_creature == 0 and \
		   self.targets[0].is_planeswalker == 0 and \
		   self.targets[0].is_player == 0:
		   	if self.debug == 1:
		   		print('target is not a creature or player or planeswalker')
		   	return 0
		else:
			return 1
	# The function that gets run when this spell is finally resolved
	# Target legality has already been checked, so just add 3 damage
	def resolve(self):
		self.targets[0].damage += 3

