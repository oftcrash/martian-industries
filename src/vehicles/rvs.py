from settings import *

def writeRV(data):
	rv = '''
item(FEAT_ROADVEHS, rv_{{ id }}, {{ id }}) {
	property {
		{% if name %}name: {{ name }};{% endif %}
		{% if refittable_cargo_classes %}refittable_cargo_classes: {{ refittable_cargo_classes }};{% endif %}
		{% if default_cargo_type %}default_cargo_type: {{ default_cargo_type }};{% endif %}
	}
}'''
	return Environment().from_string(rv).render(data)

def getRVs():
	out = ''

	#hoppers
	cars = []
	diat = [58,59,60]
	plst = [67,68,69]
	basicHopper = [64,65,66]
	cars.extend(diat)
	cars.extend(plst)
	cars.extend(basicHopper)
	dCt = 1
	pCt = 1
	bCt = 1
	for car in cars:
		types = 'CC_BULK, CC_POWDERIZED'
		if car in diat:
			dSt = str(dCt)
			dCt += 1
			name = 'DIAT_' + dSt
			cargo = 'DIAT'
		elif car in plst:
			pSt = str(pCt)
			pCt += 1
			name = 'PLST_' + pSt
			cargo = 'PLST'
		else:
			bSt = str(bCt)
			bCt += 1
			name = 'HOPPER_' + bSt
			cargo = 'DIAT'
		v = {
			'id': car,
			'name': 'string(STR_RV_NAME_' + name + ')',
			'refittable_cargo_classes': 'bitmask(' + types + ')',
			'default_cargo_type': cargo
		}
		out += writeRV(v)

	#tankers
	cars = []
	deut = [61,62,63]
	hych = [82,83,84]
	cars.extend(deut)
	cars.extend(hych)
	dCt = 1
	hCt = 1
	for car in cars:
		types = 'CC_LIQUID'
		if car in deut:
			dSt = str(dCt)
			dCt += 1
			name = 'DEUT_' + dSt
			cargo = 'DEUT'
		else:
			hSt = str(hCt)
			hCt += 1
			name = 'HYCH_' + hSt
			cargo = 'HYCH'
		v = {
			'id': car,
			'name': 'string(STR_RV_NAME_' + name + ')',
			'refittable_cargo_classes': 'bitmask(' + types + ')',
			'default_cargo_type': cargo
		}
		out += writeRV(v)

	#vans
	cars = []
	chem = [85,86,87]
	supp = [73,74,75]
	lumb = [70,71,72]
	cars.extend(chem)
	cars.extend(supp)
	cars.extend(lumb)
	cCt = 1
	sCt = 1
	lCt = 1
	for car in cars:
		types = 'CC_BULK, CC_PIECE_GOODS, CC_COVERED, CC_NEO_BULK, CC_ARMOURED'
		if car in chem:
			cSt = str(cCt)
			cCt += 1
			name = 'CHEM_' + cSt
			cargo = 'CHEM'
			types += ', CC_HAZARDOUS'
		elif car in supp:
			sSt = str(sCt)
			sCt += 1
			name = 'SUPP_' + sSt
			cargo = 'SUPP'
			types += ', CC_EXPRESS, CC_REFRIGERATED'
		else:
			lSt = str(lCt)
			lCt += 1
			name = 'LUMB_' + lSt
			cargo = 'LUMB'
		v = {
			'id': car,
			'name': 'string(STR_RV_NAME_' + name + ')',
			'refittable_cargo_classes': 'bitmask(' + types + ')',
			'default_cargo_type': cargo
		}
		out += writeRV(v)
	
	#flatbeds
	cars = []
	wood = [76,77,78]
	cars.extend(wood)
	wCt = 1
	for car in cars:
		wSt = str(wCt)
		wCt += 1
		name = 'WOOD_' + wSt
		cargo = 'WOOD'
		types = 'CC_PIECE_GOODS, CC_OVERSIZED, CC_NEO_BULK'
		v = {
			'id': car,
			'name': 'string(STR_RV_NAME_' + name + ')',
			'refittable_cargo_classes': 'bitmask(' + types + ')',
			'default_cargo_type': cargo
		}
		out += writeRV(v)

	return out
