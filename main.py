import pygame
from pygame.locals import *
import sys
import random
from You import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((400, 500))
  pygame.display.set_caption("Rakutan")

  bg = pygame.image.load("./img/stage.jpg").convert_alpha()
  rect_bg = bg.get_rect()

  frame_count = 0

  score = 0

  you = You(screen, 100, 50, 50)

  tannis = []
  hitnum = 0
  rakutan_num = 0

  font = pygame.font.SysFont('meiryomeiryomeiryouimeiryouiitalic', 20)
  h1_font = pygame.font.SysFont('meiryomeiryoboldmeiryouiboldmeiryouibolditalic', 40)

  while(True):
    frame_count += 1
    pygame.time.wait(30)
    pygame.display.update()
    screen.fill((0, 20, 0, 0))  # 画面の背景色
    screen.blit(bg, rect_bg)

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
        if event.key == K_r and (rakutan_num >= 20 or score >= 167):
          frame_count = 0
          score = 0
          tannis = []
          hitnum = 0
          rakutan_num = 0
    you.update()
    you.draw()

    if(score >= 167):
      screen.blit(h1_font.render("卒業!!", True, (255,255,255)), [150, 50])
      continue
    if(rakutan_num >= 20):
      screen.blit(h1_font.render("留年!!", True, (255,255,255)), [150, 50])
      continue

    if(frame_count % 25 == 0):
      tannis.append(Tanni(screen, random.uniform(0,400), 80, True if random.random() >= 0.2 else False))

    num = 0
    rakutan_num = 0
    for i in range(0, len(tannis)):
      if(tannis[i].getIsHit() == False):
        print(str(num))
        tannis[i].update()

        if(hit(you, tannis[i])):
          hitnum += 1
          print("hit")
          if(tannis[i].getIsHalf()):
            score += 2
          else:
            score += 4
          tannis[i].hit()
          continue

        num += 1

        tannis[i].draw()
      if(tannis[i].getIsRakutan() == True):
        if(tannis[i].getIsHalf()):
          rakutan_num += 2
        else:
          rakutan_num += 4

    # print(num)
    screen.blit(font.render("取得単位数：" + str(score), True, (255,255,255)), [0, 0])
    screen.blit(font.render("落単数：" + str(rakutan_num), True, (255,255,255)), [0, 20])

def hit(you, tanni):
  you_t = you.getTop()
  you_l = you.getLeft()
  you_b = you.getBottom()
  you_r = you.getRight()

  tanni_t = you.getTop()
  tanni_l = tanni.getLeft()
  tanni_b = tanni.getBottom()
  tanni_r = tanni.getRight()

  if(tanni_b < you_t):
    return False
  if(tanni_t > you_b):
    return False
  if(tanni_r < you_l):
    return False
  if(tanni_l > you_r):
    return False

  return True


class Tanni:

  def __init__(self, screen, x, speed, isHalf):
    self.screen = screen
    self.x = int(x)
    self.speed = speed
    self.font = pygame.font.SysFont('meiryomeiryomeiryouimeiryouiitalic', 20)
    self.text = self.font.render("単位", True, (255,255,255))   # 描画する文字列の設定
    self.y = 0
    self.isHit = False
    self.isHalf = isHalf
    self.isRakutan = False

  def update(self):
    self.y += 5
    if(self.getBottom() >= 270):
      self.isRakutan = True
      self.hit()

  def draw(self):
    pygame.draw.circle(self.screen,
                       (0,100,0) if self.isHalf else (100, 0, 0),
                       (self.x + 20,self.y + 10),
                       25)
    self.screen.blit(self.text, [self.x, self.y])# 文字列の表示位置

  def hit(self):
    self.isHit = True

  def getIsHit(self):
    return self.isHit

  def getIsRakutan(self):
    return self.isRakutan

  def getTop(self):
    return self.y

  def getBottom(self):
    return self.y + 25

  def getLeft(self):
    return self.x -15

  def getRight(self):
    return self.x + 25


  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def getIsHalf(self):
    return self.isHalf

if __name__ == "__main__":
  main()