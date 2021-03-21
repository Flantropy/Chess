from pygame import sprite, image, transform
from constants import LARGE_TILE_SIZE


class BasePiece(sprite.Sprite):
	def __init__(self, layer, pos=(0, 0), name="pawn", color="w"):
		super(BasePiece, self).__init__()
		self.image = image.load("images/" + color + "_" + name + ".png").convert_alpha()
		self.image = transform.scale(self.image, LARGE_TILE_SIZE)
		self.rect = self.image.get_rect()
		self.rect.center = pos
		# self.center = self.rect.center
		# self.x, self.y = pos
		self.layer = layer
		self.visible = False
		self.add_to_layer(layer)
	
	def add_to_layer(self, layer):
		layer.add(self)
		
	def update(self, *args, **kwargs):
		print("update")
