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
	sim = setup()
	sim.bei

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

