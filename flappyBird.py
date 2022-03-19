import pygame
from win32api import GetMonitorInfo, MonitorFromPoint

monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
work_area = monitor_info.get("Work")

pygame.init()

SCREEN_SIZE = (WIDTH, HEIGHT) = (work_area[2] // 2, work_area[3] - 25)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("OpenCV Flappy Bird")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    screen.fill((0, 0, 0))

    pygame.display.flip()
