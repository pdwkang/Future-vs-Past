import pygame;
from pygame.sprite import Sprite;

class Bullet(Sprite):
	def __init__(self,screen,plant,tick):
		super(Bullet, self).__init__();
		self.screen =  screen;
		self.screen_rect = self.screen.get_rect();
		self.image = pygame.image.load('./images/Giant_Pea2.png');
		self.image = pygame.transform.scale(self.image, (40,30));
		self.rect = self.image.get_rect();
		self.rect.centerx = plant.rect.centerx;
		self.rect.top = plant.rect.top + 50;
		self.plant = plant
		self.tick = tick;
		self.name = ''

		self.yard_row = plant.yard_row;

		self.x = self.rect.x+25;
		self.y = self.rect.y;

		if plant.name=='gatling':
			self.image = pygame.image.load('./images/yellow_bullet.png');
			self.image = pygame.transform.scale(self.image, (100,60));
			self.rect.top = plant.rect.top + 40;
		elif plant.name=='gunner3':
			self.image = pygame.image.load('./images/green-bullet.png');
			self.image = pygame.transform.scale(self.image, (100,60));
			self.rect.top = plant.rect.top + 35;		
		elif plant.name=='gunner4':
			self.image = pygame.image.load('./images/pink_bullet.png');
			self.image = pygame.transform.scale(self.image, (60,30));
			self.name='super_bullet'
			# self.x = self.rect.x+25;
			# self.rect.top = plant.rect.top + 35;					
		
		
	def draw_me(self):
		self.screen.blit(self.image,self.rect);


	def update_me(self):
		self.x += 20 * 2;
		self.rect.x = self.x;
		if self.plant.name =='gunner4':
			if self.tick % 3 ==1:
				self.rect.y += 5
			elif self.tick % 3 ==2:
				self.rect.y -= 5
			# elif self.tick % 3 ==0:	
				