from pygame import sprite, image, transform


class Piece(sprite.Sprite):
	def __init__(self, name, color, pos):
		super().__init__()
		self.name = name
		self.color = color
		self.grid_index = pos
		self.image = image.load("images/" + self.color + "_" + self.name + ".png").convert_alpha()
		self.image = transform.scale(self.image, (32, 32))
		self.rect = self.image.get_rect()
		self.list_of_moves = []
	
	def __str__(self):
		return str(self.name) + str(self.grid_index)
	
	def get_moves_list(self, board):
		pass
	
	@staticmethod
	def from_index_to_notation(index):
		row = index // 8
		col = index % 8
		return row, col
