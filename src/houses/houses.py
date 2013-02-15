def getHouses():
	houses = ''
	for n in range(91, 109):
		try:
			houses += '''
item(FEAT_HOUSES, house_%d, %d) {
    property {
		substitute: %d;
		override: %d;
		accepted_cargos: [[PASS,8],[MAIL,8],[SUPP,8]];
		watched_cargo_types: [PASS, MAIL, SUPP];
	}
}''' % (n, n, n, n)
		except Exception as e:
			print e
	return houses
