import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Gatling(Plant):
	def __init__(self, screen, square,game_settings):
		self.shoot_speed = 1;
		self.health = 6;
		self.image = pygame.image.load('images/gunner2-1.png');
		self.image = pygame.transform.scale(self.image, (73,105));
		self.screen = screen;
		self.square = square;
		self.name = "gatling";
		self.can_shoot = True;
		self.can_make_sun = False;
		super(Gatling, self).__init__();
	def change_image(self, should_shoot):
		if should_shoot:
			self.image = pygame.image.load('images/gunner2-2.png');
			self.image = pygame.transform.scale(self.image, (73,105));
		else:		
			self.image = pygame.image.load('images/gunner2-1.png');
			self.image = pygame.transform.scale(self.image, (73,105));		
