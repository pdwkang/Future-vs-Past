import pygame;
from pygame.sprite import Sprite;
from random import randint;
# from sounds import sounds
class Zombie(Sprite):
	def __init__(self, screen, game_settings, level):
		super(Zombie,self).__init__();
		self.speed = game_settings.zombie_speed;
		self.health = game_settings.zombie_health;
		self.level = level
		self.image = pygame.image.load('./images/dk1.png')
		self.yard_row = randint(0,4);
		self.name = ''
		if self.level==2:
			self.image = pygame.image.load('./images/wk1.png')
			self.image = pygame.transform.scale(self.image,(180,140));
			self.speed = self.speed + 3
			self.health = 5 * self.health
		elif self.level==3:
			self.image = pygame.image.load('./images/yk1.png')
			self.image = pygame.transform.scale(self.image,(180,130));
			self.speed = self.speed * 4
			self.health = self.health * 10
		elif self.level==4:
			self.image = pygame.image.load('./images/boss1.png')
			self.image = pygame.transform.scale(self.image,(393,414));
			
			self.health = self.health * 170
			temp_tuple=(1,3)
			self.yard_row = temp_tuple[(randint(0,1))]
			temp_tuple2 = (0.5, 0.7, 0.9, 1, 1.1, 1.3, 1.5)
			self.speed = temp_tuple2[(randint(0,6))]
			self.name = 'boss'
		else:
			self.image = pygame.transform.scale(self.image,(110,120));
		# self.image = pygame.transform.scale(self.image,(80,148));
		self.rect = self.image.get_rect();
		self.screen = screen;
		self.screen_rect = screen.get_rect();

		
		self.rect.centery = game_settings.squares["rows"][self.yard_row] + 50
		self.rect.right = self.screen_rect.right;
		game_settings.zombie_in_row[self.yard_row] += 1;
		self.game_settings = game_settings
		self.x = float(self.rect.x);
		self.moving = True;
		self.started_eating = 0;
		self.damage_time = 2;
	def update_me(self):
		if self.level ==4 and self.health <= 300:
			self.image = pygame.image.load('./images/boss1-2.png')
			self.image = pygame.transform.scale(self.image,(393,414));
		if self.health <= 1:
			if self.level==2:
				self.image = pygame.image.load('./images/wk3.png')
				self.image = pygame.transform.scale(self.image,(180,140));
			elif self.level==3:
				self.image = pygame.image.load('./images/yk3.png')
				self.image = pygame.transform.scale(self.image,(180,130));				
			elif self.level==1:
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
					elif self.level==3:
						self.image = pygame.image.load('./images/yk1-2.png')
						self.image = pygame.transform.scale(self.image,(180,130));	
					elif self.level==1:
						self.image = pygame.image.load('./images/dk1-2.png')
						self.image = pygame.transform.scale(self.image,(110,120));
				else:
					if self.level==2:
						self.image = pygame.image.load('./images/wk1.png')
						self.image = pygame.transform.scale(self.image,(180,140));
					elif self.level==3:
						self.image = pygame.image.load('./images/yk1.png')
						self.image = pygame.transform.scale(self.image,(180,130));	
					elif self.level==1:
						self.image = pygame.image.load('./images/dk1.png')
						self.image = pygame.transform.scale(self.image,(110,120));

			else: 
				self.x += 1;
				self.rect.x = self.x;
				if self.x % 3 == 1:
					if self.level==2:
						self.image = pygame.image.load('./images/wk2-2.png')
						self.image = pygame.transform.scale(self.image,(180,140));
					elif self.level==3:
						self.image = pygame.image.load('./images/yk2-2.png')
						self.image = pygame.transform.scale(self.image,(180,130));	
					elif self.level==1:
						self.image = pygame.image.load('./images/dk2-2.png')
						self.image = pygame.transform.scale(self.image,(140,120));
				else:
					# self.image = pygame.image.load('./images/dk1.png')
					# self.image = pygame.transform.scale(self.image,(110,120));			
					if self.level==2:
						self.image = pygame.image.load('./images/wk2.png')
						self.image = pygame.transform.scale(self.image,(180,140));
					elif self.level==3:
						self.image = pygame.image.load('./images/yk2.png')
						self.image = pygame.transform.scale(self.image,(180,130));	
					elif self.level==1:
						self.image = pygame.image.load('./images/dk2.png')
						self.image = pygame.transform.scale(self.image,(140,120));

	def draw_me(self):
		self.screen.blit(self.image, self.rect);

	def hit(self, damage):
		self.health -= damage;
		ouch_sound = pygame.mixer.Sound('./images/attacked.wav')
		ouch_sound.play();
		if self.health == 1:
			bg_music = pygame.mixer.Sound('./images/ouch.wav');
			bg_music.play();
		if self.level == 1 and self.health > 1:
			self.x += 18;
		elif self.level == 2 and self.health > 1:
			self.x += 10;
		if self.level == 4:
			print self.health
