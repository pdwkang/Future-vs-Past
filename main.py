import pygame;
from settings import Settings;
from background import Background;
import game_functions as gf;
from pygame.sprite import Group, groupcollide
from zombie import Zombie;
from square import Square;
from plant_icon import Plant_Icon;
import time
from sunflower import Sunflower;

pygame.init();
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("DC PvZ clone");
background = Background(game_settings);
peashooter_icon = Plant_Icon(game_settings,'gunner1-icon.png',1, True);
gatling_icon = Plant_Icon(game_settings,'gunner2-icon.png',2, False);
gunner3_icon = Plant_Icon(game_settings, 'gunner3-icon.png', 3, False)
gunner4_icon = Plant_Icon(game_settings, 'gunner4-icon.png', 4, False)
sunfolwer_icon = Plant_Icon(game_settings, 'gold-gatherer.png', 5, False)
robot_icon = Plant_Icon(game_settings, 'robot-1.png', 6, False)

icons = [peashooter_icon,gatling_icon,gunner3_icon,gunner4_icon,sunfolwer_icon,robot_icon];

# All our groups
zombies = Group();
plants = Group();
squares = Group();
bullets = Group()

# Load up squares with our vars
for i in range(0,5):
	for j in range(0,9):
		squares.add(Square(screen,game_settings,i, j));
		if i==0 and j==0:
			for square in squares:
				plants.add(Sunflower(screen,square,game_settings));								


def run_game():
	tick = 0;
	bg_sound = pygame.mixer.Sound('./images/bg.wav')
	bg_sound.play(-1);	
	# zombies.add(Zombie(screen,game_settings,4));
	while 1:
		gf.check_events(screen,game_settings, squares, plants,bullets,icons,tick);
		if game_settings.game_active:
			tick += 1;
			if tick > 6200:
				if tick % 300 ==0:
					zombies.add(Zombie(screen,game_settings,4));
				if tick % 400 ==0:
					zombies.add(Zombie(screen,game_settings,4));
				if tick % 1000 ==0:
					zombies.add(Zombie(screen,game_settings,4));	
				if tick % 5 == 0:
					zombies.add(Zombie(screen,game_settings,3));				
				if tick % 4 == 0:
					zombies.add(Zombie(screen,game_settings,2));									
				if tick % 3 == 0:
					zombies.add(Zombie(screen,game_settings,1));	

			elif tick > 5450:
				if tick % 5500 == 0:
					zombies.add(Zombie(screen,game_settings,4));
					zombies.add(Zombie(screen,game_settings,4));
				if tick % 10 == 0:
					zombies.add(Zombie(screen,game_settings,3));				
				if tick % 30 == 0:
					zombies.add(Zombie(screen,game_settings,2));									
				if tick % 20 == 0:
					zombies.add(Zombie(screen,game_settings,1));	
			elif tick > 4500:
				if tick % 5 == 0:
					zombies.add(Zombie(screen,game_settings,3));
			elif tick > 3300:
				# if tick % 5 == 0:
					# zombies.add(Zombie(screen,game_settings,1));				
				if tick % 20 == 0:
					zombies.add(Zombie(screen,game_settings,2));
				if tick % 15 == 0:
					zombies.add(Zombie(screen,game_settings,3));				
			elif tick > 2300:
				if tick % 10 == 0:
					zombies.add(Zombie(screen,game_settings,1));
				if tick % 50 == 0:
					zombies.add(Zombie(screen,game_settings,2));				
				if tick % 100 == 0:
					zombies.add(Zombie(screen,game_settings,3));					
			elif tick > 1500:
				if tick % 20 == 0:
					zombies.add(Zombie(screen,game_settings,1));
				if tick % 50 == 0:
					zombies.add(Zombie(screen,game_settings,2));				
				# if tick % 250 == 0:
					# zombies.add(Zombie(screen,game_settings,3));					
			elif tick > 600:
				if tick % 30 == 0:
					zombies.add(Zombie(screen,game_settings,1));
				if tick % 150 == 0:
					zombies.add(Zombie(screen,game_settings,2));	
			else:
				if tick % 60 == 0:
					zombies.add(Zombie(screen,game_settings,1));
				
					

			zombies_hit = groupcollide(zombies, bullets, False, False);
			# print zombies_hit;
			if tick % 1000 == 0:
				for bullet in bullets:
					bullets.remove(bullet);
			for zombie in zombies_hit:
				# print zombie;
				# print zombies_hit[zombie];
				if zombie.yard_row == zombies_hit[zombie][0].yard_row or zombies_hit[zombie][0].name == "super_bullet" or zombie.name=='boss':
					# print "Same row!!!";
					bullets.remove(zombies_hit[zombie][0]);
					if zombies_hit[zombie][0].name=='super_bullet':
						zombie.hit(3);
					else: zombie.hit(1);
					if(zombie.health <= 0):
						zombies.remove(zombie);
						game_settings.total_sun += 25;
						game_settings.zombie_in_row[zombie.yard_row] -= 1;
						game_settings.zombies_killed += 1;

			# create a dictionary a key of zombie and a vlaue of a list 
			for zombie in zombies:
				zombie.moving = True;
			zombies_eating = groupcollide(plants, zombies, False, False);
			# loop through dictionary
			for plant in  zombies_eating:
				# each plant being eaten
				feeding_zombies = zombies_eating[plant]
				for zombie in feeding_zombies:
				# check to see if zombie/plant are on same row
					if not zombie.name == 'boss' and zombie.yard_row == plant.yard_row:
						# Zombie has run into a plant in its row
						# start and continue eating /stop moving
						zombie.moving = False;
						# check to see if zombie takes a bite
						if time.time() - zombie.started_eating > zombie.damage_time:
							# run chomp
							plant.zombie_chomp();
							# zombie the plant if its 0 or below
							zombie.started_eating = time.time();
							# print "started eating"
							if plant.health <= 0:
								plants.remove(plant);
							# start the zombie march again
					elif zombie.name =='boss':
						plants.remove(plant);
			gf.update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick,icons);		
		pygame.display.flip();



run_game();
# zombies_eating = {
# 	key : 2,
# 	zombie [plant,plantplant]
# }