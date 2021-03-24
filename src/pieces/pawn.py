from pieces.base_piece import BasePiece


class Pawn(BasePiece):
	def __init__(self, layer, pos, color):
		super(Pawn, self).__init__(layer=layer, pos=pos, name="pawn", color=color)
		self.direction = 1
		self.base_row = 1 if color == "w" else 6
	
	def move(self, start, end, player):
		if super().move(start, end, player):
			self.direction = 1 if player.side == "w" else -1
			print(f"base row{self.base_row}")
			print(f"{start.row_int} to {end.row_int}")
			print(f"direction {self.direction}")
			if not end.piece:
				if end.row == 8 or end.row == 1:
					print("magic")
			else:
				if abs(end.col_int - start.col_int) == 1 and abs(end.row_int - start.row_int) == 1:
					return True
				# else:
				# 	return False
			if end.row_int - self.direction == start.row_int and start.col == end.col:
				return True
			if start.row_int == self.base_row and end.row_int - self.direction*2 == start.row_int and start.col == end.col:
				return True
			return False
