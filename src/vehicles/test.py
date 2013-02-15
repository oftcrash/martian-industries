import json
from jinja2 import Environment

def loadJSON():
	try:
		with open('rvs.json') as data_file:
			data = json.load(data_file)
	except Exception as e:
		data = e
	return data

rv = '''
item(FEAT_ROADVEHS, rv_{{ id }}, {{ id }}) {
	property {
		{% if name %}name: {{ name }};{% endif %}
		{% if refittable_cargo_classes %}refittable_cargo_classes: {{ refittable_cargo_classes }};{% endif %}
		{% if default_cargo_type %}default_cargo_type: {{ default_cargo_type }};{% endif %}
	}
}'''

data = loadJSON()
for vehicle in data.iteritems():
	print vehicle

#	print Environment().from_string(rv).render(d)
