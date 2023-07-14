import pygame, os

script_dir = os.path.dirname(os.path.abspath(__file__))
yellowbird_downflap_dir = os.path.join(script_dir, "assets", "yellowbird-downflap.png")
yellowbird_midflap = os.path.join(script_dir, "assets", "yellowbird-midflap.png")
yellowbird_upflap = os.path.join(script_dir, "assets", "yellowbird-upflap.png")

class Bird:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.bird_frames = [pygame.transform.scale2x(pygame.image.load(yellowbird_downflap_dir).convert_alpha()),
		                    pygame.transform.scale2x(pygame.image.load(yellowbird_midflap).convert_alpha()),
		                    pygame.transform.scale2x(pygame.image.load(yellowbird_upflap).convert_alpha())]
		self.bird_index = 0
		self.bird_surface = self.bird_frames[self.bird_index]
		self.bird_rectangle = self.bird_surface.get_rect(center=(self.x, self.y))

	def rotacion(self, angle):
		self.bird_surface = pygame.transform.rotozoom(self.bird_frames[self.bird_index], angle, 1)

	def animacion(self):
		self.bird_index = (self.bird_index + 1) % len(self.bird_frames)
		self.bird_surface = self.bird_frames[self.bird_index]

	def movimiento(self, dy):
		self.y += dy
		self.bird_rectangle.centery = self.y

	def dibujo(self, screen):
		screen.blit(self.bird_surface, self.bird_rectangle)
