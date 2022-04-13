from util import translate
from threading import Thread
import pygame
import cv2

face_detection = cv2.CascadeClassifier(cv2.data.haarcascades +
                                       "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("./img/bird.png")
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() * 2,
                         self.image.get_height() * 2)).convert()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def update(self, cap) -> None:
        t1 = Thread(target=self.readVideo, args=(cap, ))
        t1.start()
        t1.join()

        t2 = Thread(target=self.processVideo, args=())
        t2.start()
        t2.join()

        cv2.imshow('frame', self.img)
        # self.rect.center = pygame.mouse.get_pos()
        return

    def readVideo(self, cap):
        _, self.img = cap.read()

    def processVideo(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.faces = face_detection.detectMultiScale(gray,
                                                     scaleFactor=1.2,
                                                     minNeighbors=5)
        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            vw, vh = self.img.shape[:2]
            self.rect.center = self.mapCoord(x, y, vw, vh)

    def mapCoord(self, x, y, w, h):
        windowWidth, windowHeight = pygame.display.get_surface().get_size()
        return (translate(x, 0, w, 0,
                          windowWidth), translate(y, 0, h, 0, windowHeight))
