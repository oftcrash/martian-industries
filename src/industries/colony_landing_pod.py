def getInd():
	out = {
		"full" : "colony landing pod",
		"abbr" : "clp",
		"number" : "29",
		"prod_cargo_types" : "SUPP, PASS",
		"accept_cargo_types" : "DEUT",
		"prod_multiplier" : "15, 15",
		"min_cargo_distr" : "5",
		"life_type" : "PROCESSING",
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
		"tiles" : ["137"],
		"tile_cargos" : "[DEUT, 8]",
		"tile_cargo_amount" : ["8"],
		"layouts" : {
			'1' : '''
				0, 0: 137;
		 		2, 1: 137;
	 			5, 3: 137;
	 			1, 5: 137;
	 			4, 4: 137;''',
	 		'2' : '''
	 			0, 0: 137;''',
	 		'3' : '''
	 			1, 1: 137;
				4, 3: 137;
				0, 2: 137;'''
		},
		"graphics" : '''
			produce_cargo_arrival: clp_produce;
		''',
		"pre" : '''
			produce (clp_produce, waiting_cargo_1, 0, 0, waiting_cargo_1, waiting_cargo_1);
		'''
	}
	return out