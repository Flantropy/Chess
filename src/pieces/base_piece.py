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
	
	def draw(self, display):
		display.blit(self.image, self.rect)
	
	def __str__(self):
		return self.name
	
	def move(self, end_cell):
		return True if end_cell in self.list_of_moves else False
	
	def get_moves_list(self, board):
		pass
	
	def add_diagonal_moves(self, board):
		pass
	
	def add_horizontal_moves(self, board):
		self.add_line_of_moves(board, self.col, -1, mode="h")
		self.add_line_of_moves(board, self.col, 1, mode="h")
	
	# for col in range(self.col + 1, 8):
	# 	cell = board[self.row][col]
	# 	# if not isinstance(cell, Piece):
	# 	# 	self.list_of_moves.append((self.row, col))
	# 	# elif cell.color != self.color:
	# 	# 	self.list_of_moves.append((self.row, col))
	# 	# 	break
	# 	# else:
	# 	# 	break
	
	def add_vertical_moves(self, board):
		self.add_line_of_moves(board, self.col, -1, mode="v")
		self.add_line_of_moves(board, self.col, 1, mode="v")
	
	def add_line_of_moves(self, board, start, shift, mode):
		end = 8 if shift == 1 else -1
		
		for i in range(start + shift, end, shift):
			cell = board[self.row][i] if mode == "h" else board[i][self.col]
			add = (self.row, i) if mode == "h" else (i, self.col)
			if not isinstance(cell, Piece):
				self.list_of_moves.append(add)
			elif cell.color != self.color:
				self.list_of_moves.append(add)  # ((self.row, i))
				break
			else:
				break
