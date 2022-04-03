import pygame


class Player(pygame.sprite.Sprite):
	def __init__(self) -> None:
		super().__init__()
		self.image = pygame.image.load("./img/bird.png")
		self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
	
	def draw(self, screen: pygame.Surface) -> None:
		screen.blit(self.image, self.rect)

	def update(self) -> None:
		self.rect.center = pygame.mouse.get_pos()