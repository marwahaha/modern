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
#This is a change. Testing git