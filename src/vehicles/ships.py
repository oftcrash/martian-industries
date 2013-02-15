from settings import *

def writeShip(data):
	ship = '''
item(FEAT_SHIPS, ship_{{ id }}, {{ id }}) {
	property {
		{% if name %}name: {{ name }};{% endif %}
		{% if refittable_cargo_classes %}refittable_cargo_classes: {{ refittable_cargo_classes }};{% endif %}
		{% if default_cargo_type %}default_cargo_type: {{ default_cargo_type }};{% endif %}
	}
}'''
	return Environment().from_string(ship).render(data)

def getShips():
	ship = {
		'id': 10,
		'refittable_cargo_classes': 'ALL_NORMAL_CARGO_CLASSES',
		'default_cargo_type': 'SUPP'
	}
	return writeShip(ship)