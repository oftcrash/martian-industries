import os
from sys import argv #accept arguments passed from the command line
from datetime import datetime #formatting timecodes
import shutil
import json
from pprint import pprint
from jinja2 import Environment, FileSystemLoader

projectName = 'martian-industries'
basePath = os.getcwd()
newgrfPath = os.path.join('/Users/knowltk/Documents/OpenTTD/', 'newgrf')
projectPath = basePath
buildPath = os.path.join(projectPath, 'build')
releasePath = os.path.join(projectPath, 'release')
sourcePath = os.path.join(projectPath, 'src')
archivePath = os.path.join(projectPath, 'archive')
buildCount = 'buildcount.txt'
sections = ['core','cargo','industries','vehicles','houses','towns','objects']
templatePath = os.path.join(sourcePath, 'templates')
