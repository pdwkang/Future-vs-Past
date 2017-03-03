import pygame
from pygame.sprite import Sprite

class Plant_Icon(Sprite):
	def __init__(self,game_settings,icon,slot):
		super(Plant_Icon, self).__init__();		
		self.image = pygame.image.load('./images/'+icon);
		if icon == 'robot-1.png':
			self.image = pygame.transform.scale(self.image,(150,135));
		else: self.image = pygame.transform.scale(self.image,(120,145));	
		self.rect = self.image.get_rect();
		self.rect.left = 300+(130 * slot);
		self.rect.top = 30;
		self.slot = slot;
