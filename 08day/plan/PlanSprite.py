import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)

FRAME_PER_SEC = 60

#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y += self.speed	




class Background(GameSprite):

	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height

	
	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height





					
		