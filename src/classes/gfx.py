import pygame


class GFX:
	def __init__(self):
		self.layer_0 = pygame.sprite.Group()
		self.layer_1 = pygame.sprite.Group()
		self.layer_2 = pygame.sprite.Group()
		self.layers = [
			self.layer_0,
			self.layer_1,
			self.layer_2]
		
	def update(self):
		for layer in self.layers:
			layer.update()
			
	def render(self, display):
		for layer in self.layers:
			layer.draw(display)
