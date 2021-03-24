import pygame
import sys
import constants as c
from board import Board
from player import Player

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode(c.DISPLAY_SIZE)

# Sprites
layer_board = pygame.sprite.Group()
layer_pieces = pygame.sprite.Group()
background = pygame.image.load("bg.jpg").convert()
background = pygame.transform.scale(background, c.DISPLAY_SIZE)

# Board
board = Board(
	top_right=(
		c.DISPLAY_WIDTH_CENTER - int(4 * 32 * c.SCALE),
		c.DISPLAY_HEIGHT_CENTER - int(4 * 32 * c.SCALE)
	)
)
for cell in board.grid:
	layer_board.add(cell)

# Players
wp = Player("w", layer=layer_pieces, board=board)
bp = Player("b", layer=layer_pieces, board=board)
current_player = wp
selected_piece = None
start_cell = None

# Init surfaces
display.blit(background, (0, 0))

while True:
	# Tick
	clock.tick(c.FPS)
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			board.clear_selection()
			x, y = event.pos
			for cell in board.grid:
				if cell.rect.collidepoint(x, y):
					if cell.piece:
						if cell.piece.color == current_player.side:
							cell.is_selected = True
							selected_piece = cell.piece
							# cell.piece = None
							start_cell = cell
							break
					if selected_piece:
						if selected_piece.move(start_cell, cell, current_player):
							if cell.piece and (cell.piece.color != current_player.side):
								print("capture")
								cell.piece.kill()
							selected_piece.rect.center = cell.rect.center
							cell.piece = selected_piece
							# print(f"{current_player.side} move {selected_piece.name} {start_cell} to {cell}")
							selected_piece = None
							start_cell.piece = None
							current_player = wp if current_player == bp else bp
						else:
							selected_piece = None
							
	# Update
	layer_board.update()
	layer_pieces.update()
	
	# Draw
	layer_board.draw(display)
	layer_pieces.draw(display)
	
	# Render
	pygame.display.update()
