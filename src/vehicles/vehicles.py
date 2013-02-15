from trains import *
from rvs import *
from ships import *

def getVehicles():
	out = '/* Vehicles */'
	out += getTrains()
	print 'wrote Trains'
	out += getRVs()
	print 'wrote RVs'
	out += getShips()
	print 'wrote Ships'
	return out
