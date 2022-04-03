import cv2
import pygame
from win32api import GetMonitorInfo, MonitorFromPoint
from components.Pipes import Pipe

face_detection = cv2.CascadeClassifier(cv2.data.haarcascades +
                                       "haarcascade_frontalface_default.xml")
class Game:
    def __init__(self) -> None:
        pygame.init()

        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        work_area = monitor_info.get("Work")
        self.SCREEN_SIZE = (work_area[2] //2, work_area[3] - 25)

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("Open CV flappy bird")


        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = 0
        self.initialize()
    
    def initialize(self):
        self.all_sprites = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()

        self.pipe1 = Pipe(self.SCREEN_SIZE)
        # pipe2 = PipeDown(self.pipe1)

        self.pipes.add(self.pipe1)
        # self.pipes.add(pipe2)

    
    def run(self) -> None:
        while self.running:
            match self.menu:
                case 0:
                    self.gaming()
        
                    
    def gaming(self) -> None:
        self.playing = True
        # cap = cv2.VideoCapture(0)
        while self.playing:
            # _, img = cap.read()
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # faces = face_detection.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)

            timedelta = self.clock.tick(60) / 1000
            print(self.clock.get_fps())

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
        # cv2.imshow('frame', img)
        self.pipe1.draw(self.screen)
        pygame.display.flip()
        

    def update(self, timedelta) -> None:
        self.pipes.update(timedelta)
        # if pygame.sprite.spritecollide(self.player, self.pipes, False):
        #     self.playing = False

if __name__ == "__main__":
    game = Game()
    game.run()        
                                         
