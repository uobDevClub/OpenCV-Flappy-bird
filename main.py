import cv2
import pygame
from win32api import GetMonitorInfo, MonitorFromPoint
from components.Backgroud import Background
from components.Pipes import Pipe
from components.Player import Player

face_detection = cv2.CascadeClassifier(cv2.data.haarcascades +
                                       "haarcascade_frontalface_default.xml")
class Game:
    
    MAIN_MENU = 0
    ONGOING = 1
    EXIT_GAME = -1

    def __init__(self) -> None:
        pygame.init()

        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        work_area = monitor_info.get("Work")
        self.SCREEN_SIZE = (work_area[2] //2, work_area[3] - 25)

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("Open CV flappy bird")


        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = self.ONGOING
        self.initialize()
    
    def initialize(self):
        self.pipesGroup = pygame.sprite.Group()

        self.pipes = Pipe()
        self.pipesGroup.add(self.pipes)

        self.player = Player()

        self.background = Background()
    
    def run(self) -> None:
        while self.running:
            match self.menu:
                case self.ONGOING:
                    self.gaming()
                case self.EXIT_GAME:
                    break
        
                    
    def gaming(self) -> None:
        self.playing = True
        # cap = cv2.VideoCapture(0)
        while self.playing:
            # _, img = cap.read()
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # faces = face_detection.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)

            timedelta = self.clock.tick(60) / 1000

            self.events()
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            #     self.update((img.shape[1]-(x + int(w/2) - 20))*2, (y + int(h/2))*2)
            
            self.draw()
            self.update(timedelta)

            # if cv2.waitKey(30) == ord('q'):
                # break
        
        # cap.release()
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
     
    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.background.draw(self.screen)
        # cv2.imshow('frame', img)
        self.pipes.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
        

    def update(self, timedelta) -> None:
        self.background.update()
        self.pipes.update(timedelta)
        self.player.update()
        if self.pipes.isColliding(self.player):
            self.playing = False
            self.menu = self.EXIT_GAME

if __name__ == "__main__":
    game = Game()
    game.run()        
                                         
