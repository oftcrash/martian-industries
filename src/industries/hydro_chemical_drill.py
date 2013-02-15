def getInd():
	out = {
		"full" : "hydrochemical drill",
		"abbr" : "hcd",
		"number" : "32",
		"prod_cargo_types" : "HYCH",
		"accept_cargo_types" : "",
		"prod_multiplier" : "15",
		"min_cargo_distr" : "5",
		"life_type" : "EXTRACTIVE",
		"random_sound_effects" : "",
		"conflicting_ind_types" : "",
		"input_multiplier_1" : "0",
		"input_multiplier_2" : "0",
		"input_multiplier_3" : "0",
		"spec_flags" : "",
		"prob_random" : "3",
		"prob_in_game" : "2",
		"prospect_chance" : "0",
		"fund_cost_multiplier" : "100",
		"remove_cost_multiplier" : "0",
		"tiles" : ["148","149","150","151","152","153","154","155"],
		"tile_cargos" : "",
		"layouts" : {
			'1' : '''
			 	0, 0: 148;
			 	0, 1: 151;
			 	0, 2: 154;
			 	0, 3: 151;
			 	0, 4: 148;''',
			'2' : '''
			 	0, 2: 148;
			 	1, 2: 151;
			 	2, 2: 154;
			 	3, 2: 151;
			 	4, 2: 148;
			 	2, 0: 148;
			 	2, 1: 151;
			 	2, 3: 151;
			 	2, 4: 148;''',
			'3' : '''
			 	0, 0: 148;
			 	1, 0: 151;
			 	2, 0: 154;
			 	3, 0: 151;
			 	4, 0: 148;
			 	4, 1: 151;
			 	4, 2: 154;
			 	4, 3: 151;
			 	4, 4: 148;'''
		}
	}
	return out
