from pygame import sprite, image, transform


class Piece(sprite.Sprite):
	def __init__(self, name, position=(0, 0), color="w", coordinates=(0, 0)):
		super().__init__()
		self.name = name
		self.color = color
		self.position = position
		self.row, self.col = self.position
		self.list_of_moves = []
		self.image = image.load("images/" + self.color + "_" + self.name + ".png").convert_alpha()
		self.image = transform.scale(self.image, (32, 32))
		self.rect = self.image.get_rect()
		self.rect.center = coordinates
		self.grid_index = self.row * 8 + self.col
	
	def draw(self, display):
		display.blit(self.image, self.rect)
	
	def __str__(self):
		return self.name
	
	def move(self, end_cell):
		return True if end_cell in self.list_of_moves else False
	
	def get_moves_list(self, board):
		self.list_of_moves.clear()
		
	def add_move(self, index, board):
		if not board[index].piece:
			self.list_of_moves.append(index)
		elif board[index].piece.color != self.color:
			self.list_of_moves.append(index)
			return False
		return True
	
	@staticmethod
	def from_index_to_notation(index):
		row = index // 8
		col = index % 8
		return row, col
