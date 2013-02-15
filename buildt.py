# Author: Kris Knowlton
# Copyright: GPL v2
# Basic newgrf build system. Right now, it just assembles nml and lng data from more logical directories.
# Really, its just to separate out all the feature types to make things more editable. Templating is in progress.
# This is building the english lng file, but it might be better to keep that a single file that's edited directly.
#	This will make it easier to add translations later.

from settings import *

def loadJSON(type, name):
	jsonFile = os.path.join(sourcePath, type, name + '.json')
	with open(jsonFile) as data_file:
		data = json.load(data_file)
	return data

def loadTemplate(type, tmpl, name):
	env = Environment(loader=FileSystemLoader(os.path.join(sourcePath, type)), trim_blocks=True)
	data = loadJSON(type, name)
	return env.get_template(tmpl + '.tnml').render(data)

print loadTemplate('cargo', 'cargo','diat')
print loadTemplate('vehicle', 'trains','diat')
