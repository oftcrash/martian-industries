# Author: Kris Knowlton
# Copyright: GPL v2
# Basic newgrf build system. Right now, it just assembles nml and lng data from more logical directories.
# Really, its just to separate out all the feature types to make things more editable. Templating is in progress.
# This is building the english lng file, but it might be better to keep that a single file that's edited directly.
#	This will make it easier to add translations later.

from settings import *
from src.vehicles.vehicles import *
from src.industries.industries import getIndustries

#pass the grf name as an argument, or ask for a name if the argument isn't passed
try:
	script, name = argv
except:
	print 'Enter a grf name:',
	name = raw_input()

#get the current build number
def getBuildNumber():
	if os.path.isfile(buildCount):
		try:
			file = open(buildCount)
			build = int(file.readline())
			file.close()
		except IOError as e:
			build = 1
	else:
		build = 1
	return build

#set the version by advancing the build by 1
def setVersion():
	build = getBuildNumber() + 1
	ver = str(build)
	file = open(buildCount, 'w')
	file.write(ver)
	file.close()
	return ver

#build the custom_tags file
def customTags():
	version = setVersion()
	ct = open(os.path.join(buildPath, 'custom_tags.txt'), 'w')
	ct.write('VERSION:' + version + '\n')
	ct.write('UPDATEDT:' + str(datetime.now()) + '\n')
	ct.write('TITLE:Martian Industries - build ' + version + '\n')
	ct.write('AUTHOR:Kris Knowlton' + '\n')
	ct.write('COPYRIGHTDT:2013' + '\n')
	ct.write('LICENSE:GPL v2' + '\n')
	ct.close()
	print 'created custom_tag.txt'

#copy any lang files from source to the build.
def lang():
	source = os.path.join(sourcePath, 'lang')
	dest = os.path.join(buildPath, 'lang')
	lngFiles = os.listdir(source)
	for lngFile in lngFiles:
		fileName = os.path.join(source, lngFile)
		if (os.path.isfile(fileName)):
			shutil.copy(fileName, dest)
			print 'copied ' + lngFile
		
#pull in .pnml files that match the name of the section.
def assembleNML(sections):
	ext = '.pnml'
	for s in sections:
		try:
		    source = os.path.join(sourcePath, s)
		    for dirname, dirnames, filenames in os.walk(source):
				for filename in filenames:
					if os.path.splitext(filename)[1] == ext:
						data = open(os.path.join(source, filename))
						content = data.read()
						data.close()
						writeNML(content)
						print 'wrote %s' % s
		except Exception as e:
			print e

#write the nml file
def writeNML(content):
	try:
		dest = os.path.join(buildPath, name + '.nml')
		nml = open(dest, 'a')
		nml.write(content)
		nml.close()
	except Exception as e:
		print e

def loadJSON(type, name):
	jsonFile = os.path.join(sourcePath, type, name + '.json')
	with open(jsonFile) as data_file:
		data = json.load(data_file)
	return data

def loadTemplate(type, name):
	env = Environment(loader=FileSystemLoader(os.path.join(sourcePath, type)), trim_blocks=True)
	data = loadJSON(type, name)
	return env.get_template(type + '.tnml').render(data)


#set up the build directory
def setupBuild():
	subdirs = ['gfx','lang']
	if not os.path.exists(buildPath):
		os.makedirs(buildPath)
		for s in subdirs:
			os.makedirs(os.path.join(buildPath, s))
			print 'created %s directory' % s

#archive any existing builds before starting a new one
def cleanup():
	if os.path.exists(buildPath):
		if not os.path.exists(archivePath):
			os.makedirs(archivePath)
			print '  created archive directory'
		build = str(getBuildNumber())
		os.rename(buildPath, os.path.join(archivePath, build))
		print '  archived build %s' % build

#create the new build
def newBuild():
	print 'Starting build...'
	print 'Clean up:'
	cleanup()
	print 'Set up build:'
	setupBuild()
	customTags()
	lang()
	assembleNML(['core','cargo'])
	writeNML(getIndustries())
	writeNML(getVehicles())
	try:
		os.chdir(buildPath)
		os.system('nmlc ' +  name + '.nml')
		newgrfFile = name + '.grf'
		print 'compiled %s' % newgrfFile
	except:
		print 'error compiling'
	else:
		if os.path.isfile(newgrfFile):
			os.system('mv %s %s' % (newgrfFile,newgrfPath))
			print 'copied %s to %s' % (newgrfFile,newgrfPath)
			print 'SUCCESS!'
newBuild()