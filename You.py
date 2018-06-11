import pygame
from pygame.locals import *
import sys
import random

class You:

  # 押されている状態を保持する変数
  # 0: 押されていない 1: 右向き 2: 左向き
  pressed = 0
  # 押されているフレーム数をカウント
  pressed_count = 0

  def __init__(self, screen, x, width = 10, height = 10):
    self.screen = screen
    self.x = x
    self.width = width
    self.height = height
    self.player = pygame.image.load("./img/player.png").convert_alpha()
    self.rect_player = self.player.get_rect()
    self.y = 240

  def update(self):
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_LEFT]:
      if(self.pressed != 2):
        self.pressed = 2
        self.pressed_count = 0

      if(self.pressed_count < 15):
        self.move(-5)
      elif(self.pressed_count < 30):
        self.move(-10)
      elif(self.pressed_count >= 30):
        self.move(-10)

      self.pressed_count += 1

    elif pressed_key[K_RIGHT]:
      if(self.pressed != 1):
        self.pressed = 1
        self.pressed_count = 0

      if(self.pressed_count < 15):
        self.move(5)
      elif(self.pressed_count < 30):
        self.move(10)
      elif(self.pressed_count >= 30):
        self.move(10)


      self.pressed_count += 1
    else:
      self.pressed = 0
      self.pressed_count = 0

  def draw(self):
    self.rect_player.center = (self.x, self.y)
    self.screen.blit(self.player, self.rect_player)

  def move(self, px):
    if(self.x + px < 0):
      self.x = 0
    elif(self.x + px > 400):
      self.x = 400
    else:
      self.x += px

  def getTop(self):
    return self.y -50

  def getBottom(self):
    return self.y + 30

  def getLeft(self):
    return self.x - 15

  def getRight(self):
    return self.x + 15