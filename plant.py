import pygame;
from pygame.sprite import Sprite;

class Plant(Sprite):
	def __init__(self):
		super(Plant,self).__init__();
		self.screen_rect = self.screen.get_rect();
		# self.image =  pygame.image.load(self.image_file);
		# self.image = pygame.transform.scale(self.image, (99,96));
		self.rect = self.image.get_rect();

		self.rect.left = self.square.rect.left + 10;
		self.rect.top = self.square.rect.top;
		self.yard_row = self.square.row_number;

		self.last_shot = 0;
		self.last_sun = 0;
		self.sun_speed = 5;
	def draw_me(self):
		self.screen.blit(self.image, self.rect);

	def zombie_chomp(self):
		self.health -= 1;		