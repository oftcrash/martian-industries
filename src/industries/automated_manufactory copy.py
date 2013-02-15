from jinja2 import Environment

def getInd():
	out = {
		"full" : "automated manufactory",
		"abbr" : "am",
		"number" : "31",
		"prod_cargo_types" : "SUPP",
		"accept_cargo_types" : "ALOY, CHEM, PLST",
		"prod_multiplier" : "15",
		"min_cargo_distr" : "5",
		"life_type" : "PROCESSING",
		"random_sound_effects" : "0x03, 0x27",
		"conflicting_ind_types" : "31",
		"input_multiplier_1" : "0",
		"input_multiplier_2" : "0",
		"input_multiplier_3" : "0",
		"spec_flags" : "IND_FLAG_BUILT_NEAR_TOWN",
		"prob_random" : "3",
		"prob_in_game" : "2",
		"prospect_chance" : "0",
		"fund_cost_multiplier" : "100",
		"remove_cost_multiplier" : "0"
	}
	return out

def renderNML(nml):
	ind = getInd()
	return Environment().from_string(nml).render(ind)

# automated manufactory
def industry():
	nml = '''
/* {{ full }} */

produce(am_cargo_arrive_produce, 4, 4, 4, 3, 3, 1);

item(FEAT_INDUSTRIES, industry_{{ abbr }}, {{ number }}) {
	graphics {
		produce_cargo_arrival: {{ abbr }}_cargo_arrive_produce;
	}
	property {
		substitute: {{ number }};
		override: {{ number }};
		prod_cargo_types: [{{ prod_cargo_types }}];
		accept_cargo_types: [{{ accept_cargo_types }}];
		prod_multiplier: [{{ prod_multiplier }}];
		min_cargo_distr: {{ min_cargo_distr }};
		name: string(STR_IND_NAME_{{ abbr|upper }});
		nearby_station_name: string(STR_STATION, string(STR_TOWN), string(STR_IND_NAME_{{ abbr|upper }}));
		life_type: IND_LIFE_TYPE_{{ life_type }};
		closure_msg: TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS;
		prod_increase_msg: TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL;
		prod_decrease_msg: TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL;
		new_ind_msg: TTD_STR_NEWS_INDUSTRY_CONSTRUCTION;
		random_sound_effects: [{{ random_sound_effects }}];
		conflicting_ind_types: [{{ conflicting_ind_types }}];
		input_multiplier_1: [{{ input_multiplier_1 }}];
		input_multiplier_2: [{{ input_multiplier_2 }}];
		input_multiplier_3: [{{ input_multiplier_3 }}];
		spec_flags: bitmask({{ spec_flags }});
		prob_random: {{ prob_random }};
		prob_in_game: {{ prob_in_game }};
		prospect_chance: {{ prospect_chance }};
		fund_cost_multiplier: {{ fund_cost_multiplier }};
		remove_cost_multiplier: {{ remove_cost_multiplier }};
	}
}

item(FEAT_INDUSTRYTILES, industry_{{ abbr }}_tile_142, 142) {
	property {
		substitute:					142;
		override:					142;
		accepted_cargos:			[[ALOY,8],[CHEM,8],[PLST,8]];
	}
}
item(FEAT_INDUSTRYTILES, industry_{{ abbr }}_tile_143, 143) {
	property {
		substitute:					143;
		override:					143;
		accepted_cargos:			[[ALOY,8],[CHEM,8],[PLST,8]];
	}
}
item(FEAT_INDUSTRYTILES, industry_{{ abbr }}_tile_144, 144) {
	property {
		substitute:					144;
		override:					144;
		accepted_cargos:			[[ALOY,8],[CHEM,8],[PLST,8]];
	}
}
item(FEAT_INDUSTRYTILES, industry_{{ abbr }}_tile_145, 145) {
	property {
		substitute:					145;
		override:					145;
		accepted_cargos:			[[ALOY,8],[CHEM,8],[PLST,8]];
	}
}
item(FEAT_INDUSTRYTILES, industry_{{ abbr }}_tile_146, 146) {
	property {
		substitute:					146;
		override:					146;
		accepted_cargos:			[[ALOY,8],[CHEM,8],[PLST,8]];
	}
}
item(FEAT_INDUSTRYTILES, industry_{{ abbr }}_tile_147, 147) {
	property {
		substitute:					147;
		override:					147;
		accepted_cargos:			[[ALOY,8],[CHEM,8],[PLST,8]];
	}
}
'''
	out = renderNML(nml)
	return out