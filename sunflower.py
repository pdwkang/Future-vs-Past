import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Sunflower(Plant):
	def __init__(self, screen, square,game_settings):
		self.shoot_speed = 0;
		self.health = 5;
		
		self.image = pygame.image.load('images/gold-gatherer.png');
		self.image = pygame.transform.scale(self.image, (73,105));
		self.screen = screen;
		self.square = square;
		self.name = "sunflower";
		self.can_shoot = False;
		self.can_make_sun = True;
		self.last_sun = 0;
		self.sun_speed = 5;
		self.sun_cost = 50;
		super(Sunflower, self).__init__();

	def make_sun(self,game_settings):
		game_settings.total_sun += 25;
	def change_image(self, should_shoot):
		if self.can_shoot:
			self.image = pygame.image.load('images/gunner1-2.png');	