import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Robot(Plant):
	def __init__(self, screen, square,game_settings):
		self.shoot_speed = 0;
		self.health = 10;
		
		self.image = pygame.image.load('images/robot-1.png');
		self.image = pygame.transform.scale(self.image, (140,105));
		self.screen = screen;
		self.square = square;
		self.name = "robot";
		self.can_shoot = False;
		self.can_make_sun = True;
		self.last_sun = 0;
		self.sun_speed = 5;
		self.sun_cost = 50;
		self.rect = self.image.get_rect();
		super(Robot, self).__init__();
	def make_sun(self,game_settings):
		game_settings.total_sun += 0;

	def change_image(self, should_shoot):
		if self.health <= 1:
			self.image = pygame.image.load('./images/robot-3.png')
			self.image = pygame.transform.scale(self.image, (130,105));		
		else: 
			self.rect.x += 2
			if self.rect.x % 3 == 1:
				self.image = pygame.image.load('./images/robot-2.png')
				self.image = pygame.transform.scale(self.image, (130,105));		
			else:
				self.image = pygame.image.load('./images/robot-4.png')
				self.image = pygame.transform.scale(self.image, (130,105));		
		# elif self.health < 9:
			# self.image = pygame.image.load('./images/robot-2.png')
			# self.image = pygame.transform.scale(self.image, (130,105));			
		# else: 
		# 	self.image = pygame.image.load('./images/robot-1.png')
		# 	self.image = pygame.transform.scale(self.image, (120,105));		
	def zombie_chomp(self):
		self.health -= 1;			
		# self.image = pygame.image.load('images/robot-2.png');	
		# self.image = pygame.transform.scale(self.image, (120,105));					