from pygame import image, sprite, transform

from constants import LARGE_TILE_SIZE


class BasePiece(sprite.Sprite):
	def __init__(self, layer, pos=(0, 0), name="pawn", color="w"):
		super(BasePiece, self).__init__()
		self.image = image.load("images/" + color + "_" + name + ".png").convert_alpha()
		self.image = transform.scale(self.image, LARGE_TILE_SIZE)
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.layer = layer
		self.visible = True
		self.color = color
		self.name = name
		self.add_to_layer(layer)
	
	def add_to_layer(self, layer):
		layer.add(self)
	
	def move(self, start, end, player):
		# print(start, end, player.side)
		if start == end:
			print("Not today")
			return False
		
		return True
	
	def update(self, *args, **kwargs):
		if self.visible:
			pass
		else:
			self.remove(self.layer)
			print(f"remove {self.name}:{self.rect.center}")
