import sys
import pygame
from pygame.locals import USEREVENT
import dashboard

pygame.init()
pygame.font.init()

size   = width, height = 480, 320
screen = pygame.display.set_mode(size)

UPDATE_WEATHER_EVENT = USEREVENT + 1
UPDATE_BUS_EVENT     = USEREVENT + 2

pygame.time.set_timer(UPDATE_WEATHER_EVENT, 600000)
pygame.time.set_timer(UPDATE_BUS_EVENT,     60000)

def draw_background():
  background_color = pygame.Color("white")
  screen.fill(background_color)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  key = pygame.key.get_pressed()
  if key[pygame.K_q]:
    sys.exit()
  draw_background()
  dashboard.draw(screen)
