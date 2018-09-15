import pygame
from datetime import datetime

def draw(screen):
  draw_date()
  draw_weather()
  draw_bus()
  pygame.display.flip()

def draw_text(text, size, left, top):
  font_color = pygame.Color("black")
  font = pygame.font.Font(None, size)
  rendered_text = font.render(text, 1, font_color)
  size = rendered_text.get_size()
  rect = pygame.Rect(left, top, size[0], size[1])

  screen = pygame.display.get_surface()
  screen.blit(rendered_text, rect)


def draw_date():
  today = datetime.today()
  date = today.strftime('%B %d, %Y')
  day = today.strftime('%A')

  left = 200
  top = 15

  draw_text(date, 32, left, top)
  draw_text(day, 28, left + 60, top + 30)

def draw_weather():
  pass

def draw_bus():
  pass
