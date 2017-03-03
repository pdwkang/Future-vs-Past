import pygame;
from pygame.sprite import Sprite;
from random import randint;

class Zombie(Sprite):
	def __init__(self, screen, game_settings, level):
		super(Zombie,self).__init__();
		self.speed = game_settings.zombie_speed;
		self.health = game_settings.zombie_health;
		self.level = level
		self.image = pygame.image.load('./images/dk1.png')
		if self.level==2:
			self.image = pygame.image.load('./images/wk1.png')
			self.image = pygame.transform.scale(self.image,(180,140));
			self.speed = 8
			self.health = 10
		else:
			self.image = pygame.transform.scale(self.image,(110,120));
		# self.image = pygame.transform.scale(self.image,(80,148));
		self.rect = self.image.get_rect();
		self.screen = screen;
		self.screen_rect = screen.get_rect();

		self.yard_row = randint(0,4);
		self.rect.centery = game_settings.squares["rows"][self.yard_row] + 50
		self.rect.right = self.screen_rect.right;
		game_settings.zombie_in_row[self.yard_row] += 1;
		self.game_settings = game_settings
		self.x = float(self.rect.x);
		self.moving = True;
		self.started_eating = 0;
		self.damage_time = 2;
	def update_me(self):
		if self.health <= 1:
			if self.level==2:
				self.image = pygame.image.load('./images/wk3.png')
				self.image = pygame.transform.scale(self.image,(180,140));
			else:
				self.image = pygame.image.load('./images/dk3.png')
				self.image = pygame.transform.scale(self.image,(180,140));
				self.rect.centery = self.game_settings.squares["rows"][self.yard_row] + 20
		else:
			if self.moving:
				self.x -= self.speed * 1;
				self.rect.x = self.x;			
				if self.x % 3 == 1:
					if self.level==2:
						self.image = pygame.image.load('./images/wk1-2.png')
						self.image = pygame.transform.scale(self.image,(180,140));
					else:
						self.image = pygame.image.load('./images/dk1-2.png')
						self.image = pygame.transform.scale(self.image,(110,120));
				else:
					if self.level==2:
						self.image = pygame.image.load('./images/wk1.png')
						self.image = pygame.transform.scale(self.image,(180,140));
					else:
						self.image = pygame.image.load('./images/dk1.png')
						self.image = pygame.transform.scale(self.image,(110,120));

			else: 
				self.x += 1;
				self.rect.x = self.x;
				if self.x % 3 == 1:
					if self.level==2:
						self.image = pygame.image.load('./images/wk2-2.png')
						self.image = pygame.transform.scale(self.image,(180,140));
					else:
						self.image = pygame.image.load('./images/dk2-2.png')
						self.image = pygame.transform.scale(self.image,(140,120));
				else:
					# self.image = pygame.image.load('./images/dk1.png')
					# self.image = pygame.transform.scale(self.image,(110,120));			
					if self.level==2:
						self.image = pygame.image.load('./images/wk2.png')
						self.image = pygame.transform.scale(self.image,(180,140));
					else:
						self.image = pygame.image.load('./images/dk2.png')
						self.image = pygame.transform.scale(self.image,(140,120));

	def draw_me(self):
		self.screen.blit(self.image, self.rect);

	def hit(self, damage):
		self.health -= damage;
		if self.level == 1 and self.health > 1:
			self.x += 18;
		elif self.health > 1:
			self.x += 28;
