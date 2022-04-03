import random
import pygame
from util import *

class Pipe(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("./img/pipe.png")
        self.image = pygame.transform.scale2x(self.image).convert()

        self.image_2 = pygame.transform.flip(self.image, False, True).convert()

        self.screenSize = pygame.display.get_surface().get_size()

        self.rect = self.image.get_rect()
        self.rect.x = self.screenSize[0] - self.rect.w // 2
        self.rect.y = self.screenSize[1] - random.randint(30, self.rect.h)

        self.rect_2 = self.image_2.get_rect()
        self.rect_2.x = self.rect.x
        self.rect_2.bottom = self.rect.y - random.randint(75, 125)

        self.mask = pygame.mask.from_surface(self.image)
        self.mask_2 = pygame.mask.from_surface(self.image_2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image_2, self.rect_2)

    def update(self, tick: float) -> None:
        if self.rect.x <= 0:
            self.rect.x = self.screenSize[0]
            self.rect_2.x = self.rect.x

            self.rect.y = self.screenSize[1] - random.randint(30, self.rect.h)
            self.rect_2.bottom = self.rect.y - random.randint(75, 125)
        else:
            self.rect.x -= 100 * min(tick, 1 / 60)
            self.rect_2.x = self.rect.x

    def isColliding(self, other: pygame.sprite.Sprite) -> bool:
        return collide_mask(other.mask, self.mask, other.rect ,self.rect) or collide_mask(other.mask, self.mask_2, other.rect ,self.rect_2)