import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Sunflower(Plant):
	def __init__(self, screen, square,game_settings):
		self.shoot_speed = 0;
		self.health = 5;
		
		self.image = pygame.image.load('images/gold-gatherer.png');
		self.width = 75;
		self.height = 100
		
		self.image = pygame.transform.scale(self.image, (self.width,self.height));
		self.screen = screen;
		self.square = square;
		self.name = "sunflower";
		self.can_shoot = False;
		self.can_make_sun = True;
		self.last_sun = 0;
		self.sun_speed = 5;
		self.sun_cost = 50;
		super(Sunflower, self).__init__();
	# def get_bigger(self):
	# 	if self.height >= 90:
	# 		self.height -= 1;
	# 	# self.width += 1;
	# 	self.image = pygame.image.load('images/gold-gatherer.png');
	# 	self.image = pygame.transform.scale(self.image, (int(self.width),int(self.height)));
	# 	self.rect = self.image.get_rect();
	# 	self.rect.centerx = self.square.rect.centerx;
	# 	self.rect.bottom = self.square.rect.bottom;				
	# 	self.screen.blit(self.image, self.rect);
	def make_sun(self,game_settings):
		game_settings.total_sun += 50;
		# self.height = 110
	def change_image(self, should_shoot):
		if self.can_shoot:
			self.image = pygame.image.load('images/gunner1-2.png');	