import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("./img/background.png")
        self.image = pygame.transform.scale(
            self.image,
            pygame.display.get_surface().get_size()).convert()

            
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rel_x = self.rect.x % self.rect.w

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, (self.rel_x - self.rect.w, 0))
        if self.rel_x < pygame.display.get_surface().get_size()[0]:
            screen.blit(self.image, (self.rel_x, 0))

    def update(self):
        self.rect.x -= 1
        self.rel_x = self.rect.x % self.rect.w
