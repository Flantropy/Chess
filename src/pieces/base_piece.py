from pygame import sprite, image, transform


class Piece(sprite.Sprite):
	def __init__(self, name, position=(0, 0), color="tr_pos", coordinates=(0, 0)):
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
		self.move_offsets = ()
		
	def draw(self, display):
		display.blit(self.image, self.rect)
	
	def __str__(self):
		return self.name
	
	def move(self, end_cell):
		return True if end_cell in self.list_of_moves else False
	
	def get_moves_list(self, board):
		self.list_of_moves.clear()
		for offset in self.move_offsets:
			self.add_moves_by_offset(board, offset)

	def add_moves_by_offset(self, board, offset):
		row_shift, col_shift = offset
		new_row = self.row + row_shift
		new_row = min(new_row, 7) if row_shift > 0 else max(new_row, 0)
		new_col = self.col + col_shift
		new_col = min(new_col, 7) if col_shift > 0 else max(new_col, 0)
		
		try:
			if new_col + new_row != self.row + self.col:
				print(board[new_row][new_col].piece.name)
		except:
			pass
