import pygame
from datetime import datetime

def draw(screen):
  draw_date(screen)
  draw_weather(screen)
  draw_bus(screen)
  pygame.display.flip()

def draw_date(screen):
  today = datetime.today()
  date = today.strftime('%B %d, %Y')
  day = today.strftime('%A')

  font_color = (255, 255, 255)
  left = 200
  top = 15
  full_date_rect = pygame.Rect(left, top, 200, 130)
  date_rect = pygame.Rect(left, top, 200, 130)
  day_rect = pygame.Rect(left, top + 30, 200, 130)
  #pygame.draw.rect(screen, (0, 0, 255), full_date_rect)

  font = pygame.font.Font(None, 30)
  date_text = font.render(date, 1, font_color)
  screen.blit(date_text, date_rect)

  day_text = font.render(day, 1, font_color)
  screen.blit(day_text, day_rect)


def draw_weather(screen):
  pass

def draw_bus(screen):
  pass
