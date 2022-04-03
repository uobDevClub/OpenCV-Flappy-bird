import random
import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, screenSize) -> None:
        super().__init__()
        self.image = pygame.image.load("./img/pipe.png")
        self.image = pygame.transform.scale2x(self.image)
        # self.image_2 = pygame.transform.flip(self.image, False, True)

        self.screenSize = screenSize

        self.rect = self.image.get_rect()
        self.rect.x = self.screenSize[0] - self.rect.w // 2
        self.rect.y = self.screenSize[1] - random.randint(30, self.rect.h)

        # self.rect_2 = self.image_2.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, tick) -> None:
        if self.rect.x <= 0:
            self.rect.x = self.screenSize[0]
            self.rect.y = self.screenSize[1] - random.randint(30, self.rect.h)
        else:
            self.rect.x -= 100 * min(tick, 1 / 60)
            print(f"{self.rect.x = }")
