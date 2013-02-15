from settings import *
from jinja2 import Environment, FileSystemLoader
import automated_manufactory as af
import bio_plastic_extractor as bpe
import ceramic_kiln as ck
import colony_landing_pod as clp
import diatomaceous_soil_mine as dsm
import fusion_reactor as fr
import hydro_chemical_drill as hcd
import hydro_chemical_refinery as hcr
import terran_food_plantation as tfp
import xeno_arboretum as xa
import xeno_flora_processor as xfp

indList = [af, bpe, ck, clp, dsm, fr, hcd, hcr, tfp, xa, xfp]
env = Environment(loader=FileSystemLoader(templatePath), trim_blocks=True)

def getIndustries():
	out = ''
	print 'starting industries'
	for i in indList:
		try:
			ind = i.getInd()
			if "pre" in ind:
				out += ind["pre"]
			out += env.get_template('industries.tnml').render(ind)
			out += env.get_template('industrytiles.tnml').render(ind)
			if "layouts" in ind:
				for l in ind["layouts"]:
					lo = ind["layouts"].get(l)
					out += env.get_template('industry_tilelayout.tnml').render(tile=l, layout=lo, abbr=ind["abbr"])
			if "post" in ind:
				out += ind["post"]
			print 'wrote industry: %s' % ind["full"]
		except Exception as e:
			print e
			pass
	print 'finished industries'
	return out
