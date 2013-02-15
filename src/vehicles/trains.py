from settings import *

def writeTrain(data):
	train = '''
item(FEAT_TRAINS, train_{{ id }}, {{ id }}) {
	property {
		{% if name %}name: {{ name }};{% endif %}
		{% if refittable_cargo_classes %}refittable_cargo_classes: {{ refittable_cargo_classes }};{% endif %}
		{% if default_cargo_type %}default_cargo_type: {{ default_cargo_type }};{% endif %}
	}
}'''
	return Environment().from_string(train).render(data)

def getTrains():
	out = ''
#	enginesRail = [0,2,3,4,5,6,11,12,22,25,26]
#	enginesMono = [56]
#	enginesMlev = [88]
	#engines
#	for n in enginesRail:
#		out += buildTrain('rail', n, 'eng', 'NO_CARGO_CLASS')
#	for n in enginesMono:
#		out += buildTrain('mono', n, 'eng', 'NO_CARGO_CLASS')
#	for n in enginesMlev:
#		out += buildTrain('mlev', n, 'eng', 'NO_CARGO_CLASS')

	#hoppers
	hoppers = []
	diat = [44,74,106]
	plst = [46,76,108]
	basicHopper = [45,75,107]
	hoppers.extend(diat)
	hoppers.extend(plst)
	hoppers.extend(basicHopper)
	for hopper in hoppers:
		types = 'CC_BULK, CC_POWDERIZED'
		if hopper in diat:
			name = 'DIAT'
			cargo = 'DIAT'
		elif hopper in plst:
			name = 'PLST'
			cargo = 'PLST'
		else:
			name = 'HOPPER'
			cargo = 'DIAT'
		car = {
			'id': hopper,
			'name': 'string(STR_TRAIN_NAME_' + name + ')',
			'refittable_cargo_classes': 'bitmask(' + types + ')',
			'default_cargo_type': cargo
		}
		out += writeTrain(car)

	#tankers
	tankers = []
	deut = [48,78,110]
	hych = [53,83,115]
	tankers.extend(deut)
	tankers.extend(hych)
	for tanker in tankers:
		types = 'CC_LIQUID'
		if tanker in deut:
			name = 'DEUT'
			cargo = 'DEUT'
		else:
			name = 'HYCH'
			cargo = 'HYCH'
		car = {
			'id': tanker,
			'name': 'string(STR_TRAIN_NAME_' + name + ')',
			'refittable_cargo_classes': 'bitmask(' + types + ')',
			'default_cargo_type': cargo
		}
		out += writeTrain(car)

	#vans
	vans = []
	chem = [47,77,109]
	supp = [49,79,111]
	lumb = [50,80,112]
	vans.extend(chem)
	vans.extend(supp)
	vans.extend(lumb)
	for van in vans:
		types = 'CC_BULK, CC_PIECE_GOODS, CC_COVERED, CC_NEO_BULK, CC_ARMOURED'
		if van in chem:
			name = 'CHEM'
			cargo = 'CHEM'
			types += ', CC_HAZARDOUS'
		elif van in supp:
			name = 'SUPP'
			cargo = 'SUPP'
			types += ', CC_EXPRESS, CC_REFRIGERATED'
		else:
			name = 'LUMB'
			cargo = 'LUMB'
		car = {
			'id': van,
			'name': 'string(STR_TRAIN_NAME_' + name + ')',
			'refittable_cargo_classes': 'bitmask(' + types + ')',
			'default_cargo_type': cargo
		}
		out += writeTrain(car)
	
	#trucks
	trucks = []
	wood = [51,81,113]
	trucks.extend(wood)
	for truck in trucks:
		types = 'CC_PIECE_GOODS, CC_OVERSIZED, CC_NEO_BULK'
		name = 'WOOD'
		cargo = 'WOOD'
		car = {
			'id': truck,
			'name': 'string(STR_TRAIN_NAME_' + name + ')',
			'refittable_cargo_classes': 'bitmask(' + types + ')',
			'default_cargo_type': cargo
		}
		out += writeTrain(car)
	
		
	
#	for n in range(45,54):
#		out += buildTrain('rail', n, 'car', 'ALL_CARGO_CLASSES')
#	for n in range(75,84):
#		out += buildTrain('mono', n, 'car', 'ALL_CARGO_CLASSES')
#	for n in range(107,116):
#		out += buildTrain('mlev', n, 'car', 'ALL_CARGO_CLASSES')
	
	return out
