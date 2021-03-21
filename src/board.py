from cell import Cell
from constants import LARGE_TILE_SIZE, BLACK, WHITE


class Board(Cell):
	def __init__(self, top_right):
		super(Board, self).__init__(pos=top_right)
		self.grid = []
		self.create()
	
	def create(self):
		for col in range(0, 8):
			for row in range(0, 8):
				color = BLACK if (col + row) % 2 != 0 else WHITE
				cell = Cell(
					color=color,
					pos=(self.x + LARGE_TILE_SIZE[0] * col, self.y + LARGE_TILE_SIZE[1] * row),
					notation=(col, row)
				)
				self.grid.append(cell)
				
	def clear_selection(self):
		for cell in self.grid:
			cell.is_selected = False
