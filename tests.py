from simulator import *

def setup():
	p1 = player([1, 2, 3, 4, 5, 6, 7, 8, 9])
	p2 = player(['a', 'b', 'b', 'c', 'd', 'e', 'e', 'f', 'f', 'f'])

	sim = simulator(p1, p2)

	print(p1.lib)
	print(p2.lib)
	return sim

def mulligan():
	sim = setup()
	sim.begin_game()
	return

def leyline():
	# It would be great to check pre game actions actually work right now, but
	# they're a low priority since they're not super frequent
	# Before testing can occur, we'd need to implement the leyline cards 
	# and ask players if they have a leyline in hand 
	# (since there's no reason to not play one)
	pass


def setup_bolt():
	# make an instance of lightning bolt
	bolt = card.bolt()

	# put the bolt in player 1's hand
	p1 = player([bolt])
	# Initialize player 2 with 0's because that's equal to just passing priority
	p2 = player([0, 0, 0])
	sim = simulator(p1, p2)
	return sim

# initialize 
def bolt1():
	sim = setup_bolt()
	# begin game actually doesn't do anything here. It just shuffles.
	sim.begin_game()
	# Check that p1 and p2 both start with 0 damage
	print(sim.state.p1.damage)
	print(sim.state.p2.damage)
	# Give player 1 (the player with bolts) priority
	sim.has_priority(sim.state.p1)
	# p2 should now have 3 points of damage
	print(sim.state.p1.damage)
	print(sim.state.p2.damage)

