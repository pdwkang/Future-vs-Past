import pygame
from pygame.sprite import Sprite

class Shovel_Icon(Sprite):
	def __init__(self,game_settings,icon,slot):
		super(Plant_Icon, self).__init__();		
		self.image = pygame.image.load('./images/'+icon);
		self.image = pygame.transform.scale(self.image,(90,135));
		self.rect = self.image.get_rect();
		self.rect.left = 300+(100 * slot);
		self.rect.top = 30;
		self.slot = slot;
		
