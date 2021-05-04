import pygame


class GFX:
	def __init__(self):
		self.layer_0 = pygame.sprite.Group()
		self.layer_1 = pygame.sprite.Group()
		self.layer_2 = pygame.sprite.Group()
		self.layer_3 = pygame.sprite.Group()
		self.layer_4 = pygame.sprite.Group()
		self.layer_5 = pygame.sprite.Group()
		self.layer_6 = pygame.sprite.Group()
		self.layer_7 = pygame.sprite.Group()
		self.layers = [
			self.layer_0,
			self.layer_1,
			self.layer_2,
			self.layer_3,
			self.layer_4,
			self.layer_5,
			self.layer_6,
			self.layer_7]
		
	def update(self):
		for layer in self.layers:
			layer.update()
			
	def render(self, display):
		for layer in self.layers:
			layer.draw(display)
