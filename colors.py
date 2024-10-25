class Colors:
	dark_grey = (26, 31, 40)
	green = (170, 219, 161)
	red = (241, 177, 202)
	orange = (255, 183, 145)
	yellow = (238, 214, 95)
	purple = (203, 195, 232)
	cyan = (86, 177, 228)
	blue = (156, 208, 224)
	trang = (231, 201, 213)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]