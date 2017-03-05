import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Gunner3(Plant):
	def __init__(self, screen, square,game_settings):
		self.shoot_speed = .2;
		self.health = 15;
		self.image = pygame.image.load('images/gunner3-1.png');
		self.image = pygame.transform.scale(self.image, (73,105));
		self.screen = screen;
		self.square = square;
		self.name = "gunner3";
		self.can_shoot = True;
		self.can_make_sun = False;
		super(Gunner3, self).__init__();
	def change_image(self, should_shoot):
		if should_shoot:
			self.image = pygame.image.load('images/gunner3-2.png');
			self.image = pygame.transform.scale(self.image, (73,105));
		else:		
			self.image = pygame.image.load('images/gunner3-1.png');
			self.image = pygame.transform.scale(self.image, (73,105));		
