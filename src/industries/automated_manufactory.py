def getInd():
	out = {
		"full" : "automated manufactory",
		"abbr" : "am",
		"number" : "31",
		"prod_cargo_types" : "SUPP",
		"accept_cargo_types" : "ALOY, CHEM, PLST",
		"prod_multiplier" : "0,0",
		"min_cargo_distr" : "5",
		"life_type" : "PROCESSING",
		"random_sound_effects" : "0x03, 0x27",
		"conflicting_ind_types" : "31",
		"input_multiplier_1" : "1,1",
		"input_multiplier_2" : "1,1",
		"input_multiplier_3" : "1,1",
		"spec_flags" : "IND_FLAG_BUILT_NEAR_TOWN",
		"prob_random" : "3",
		"prob_in_game" : "2",
		"prospect_chance" : "0",
		"fund_cost_multiplier" : "100",
		"remove_cost_multiplier" : "0",
		"tiles" : ["142", "143", "144", "145", "146", "147"],
		"tile_cargos" : "[ALOY, 8],[CHEM, 8], [PLST, 8]",
		"graphics" : '''
			produce_cargo_arrival: am_produce;
			produce_256_ticks: am_produce_256;
			''',
		"pre" : '''
			produce (am_produce, waiting_cargo_1, waiting_cargo_2, waiting_cargo_3, 16, 16, 0);
			produce (am_produce_256, 0, 0, 0, 0, 0, 0);
			'''
	}
	return out