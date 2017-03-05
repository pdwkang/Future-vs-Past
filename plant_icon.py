import pygame
from pygame.sprite import Sprite

class Plant_Icon(Sprite):
	def __init__(self,game_settings,icon,slot,chosen):
		super(Plant_Icon, self).__init__();		
		self.image = pygame.image.load('./images/'+icon);
		# if icon == 'gunner1-icon.png':
			# self.image = pygame.transform.scale(self.image,(120,125));
		if icon == 'robot-1.png':
			self.image = pygame.transform.scale(self.image,(150,125));
		elif icon == 'gold-gatherer.png':
			self.image = pygame.transform.scale(self.image,(120,125));			
		else: self.image = pygame.transform.scale(self.image,(120,135));	
		self.rect = self.image.get_rect();
		self.rect.left = 300+(130 * slot);
		self.rect.top = 40;
		self.slot = slot;
		self.chosen = chosen;
