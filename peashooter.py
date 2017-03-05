import pygame;
from pygame.sprite import Sprite;
from plant import Plant;
import time
class Peashooter(Plant):
	def __init__(self, screen, square, game_settings):
		self.shoot_speed = 1.5;
		self.health = 3;
		self.image = pygame.image.load('images/gunner1-1.png');
		self.image = pygame.transform.scale(self.image, (73,105));
		self.screen = screen;
		self.square = square;
		self.name = "peashooter";
		self.can_shoot = True;
		self.can_make_sun = False;		
		super(Peashooter, self).__init__();
	def change_image(self, should_shoot):
		if should_shoot:
			self.image = pygame.image.load('images/gunner1-2.png');
			self.image = pygame.transform.scale(self.image, (73,105));
		else:		
			# if int(time.time()) % 2 == 1:
				# self.image = pygame.image.load('images/gunner1-idle1.png');
				# self.image = pygame.transform.scale(self.image, (73,105));
			# elif int(time.time()) % 3 == 2:
				# self.image = pygame.image.load('images/gunner1-idle3.png');
				# self.image = pygame.transform.scale(self.image, (73,105));				
			# else: 
				self.image = pygame.image.load('images/gunner1-idle2.png');
				self.image = pygame.transform.scale(self.image, (73,105));