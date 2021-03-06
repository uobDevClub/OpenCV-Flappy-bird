import cv2
import pygame
from win32api import GetMonitorInfo, MonitorFromPoint
from components.Backgroud import Background
from components.Pipes import Pipe
from components.Player import Player
from threading import Thread

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

        self.score = 0

        self.font = pygame.font.SysFont("Impact", 60)
        self.text = self.font.render(f"{self.score}", True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.SCREEN_SIZE[0] // 2, self.SCREEN_SIZE[1] - self.textRect.h)
    
    def run(self) -> None:
        while self.running:
            match self.menu:
                case self.ONGOING:
                    self.gaming()
                case self.EXIT_GAME:
                    break
        
                    
    def gaming(self) -> None:
        self.playing = True
        self.cap = cv2.VideoCapture(0)
        while self.playing:

            self.timedelta = self.clock.tick(120) / 1000

            self.events()
            
            self.draw()
            self.update()
            # print(self.clock.get_fps())

    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
     
    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.background.draw(self.screen)
        
        self.pipes.draw(self.screen)
        self.player.draw(self.screen)

        self.screen.blit(self.text, self.textRect)
        pygame.display.flip()
        

    def update(self) -> None:
        self.background.update()
        self.pipes.update(self.timedelta, self.score)

        self.player.update(self.cap)
        
        if self.pipes.isColliding(self.player):
            self.playing = False
            self.menu = self.EXIT_GAME
        
        if self.pipes.isPassed(self.player) and not self.pipes.done:
            self.pipes.done = True
            self.score += 1
            self.text = self.font.render(f"{self.score}", True, (255, 255, 255))

if __name__ == "__main__":
    game = Game()
    game.run()        
                                         
