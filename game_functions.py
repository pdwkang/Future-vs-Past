import sys;
import pygame;
from peashooter import Peashooter;
from gatling import Gatling;
from bullet import Bullet;
from sunflower import Sunflower;
from robot import Robot;
from gunner3 import Gunner3;
from gunner4 import Gunner4;
import time;

def remove_plant_in_square(square, plants):
	for plant in plants:
		if plant.square == square:
			# if plant.name=='peashooter':
			plants.remove(plant);
game_log = ''
def check_events(screen, game_settings,squares,plants,bullets,icons,tick):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if game_settings.game_active:
			# plants.add(Sunflower(screen,1,game_settings));
	 		if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos();
				# print mouse_x;
				# print mouse_y;
				for square in squares:
					
					if square.rect.collidepoint(mouse_x,mouse_y):
						# print "Square: ",square.square_number;
						if(game_settings.chosen_plant == 1 and game_settings.total_sun >= 50):
							# for plant in plants:
								# if plant.square == square and (plant.name=='gatling' or plant.name=='gunner3' or plant.name=='peashooter'):
								# 	game_log = 'You can\'t downgrade your hero'
								# else:
								# 	plants.remove(plant);
								# 	plants.add(Peashooter(screen,square,game_settings));
								# 	game_settings.total_sun -= 50							
							remove_plant_in_square(square, plants)
							plants.add(Peashooter(screen,square,game_settings));
							game_settings.total_sun -= 50
						elif(game_settings.chosen_plant == 2 and game_settings.total_sun >= 200):
							for plant in plants:
								if plant.square == square:
									if plant.name=='peashooter':
										plants.remove(plant);
										plants.add(Gatling(screen,square,game_settings));
										game_settings.total_sun -= 200
						elif(game_settings.chosen_plant == 3 and game_settings.total_sun >= 1000):
							for plant in plants:
								if plant.square == square:
									if plant.name=='gatling':
										plants.remove(plant);
										plants.add(Gunner3(screen,square,game_settings));
										game_settings.total_sun -= 1000							
						elif(game_settings.chosen_plant == 4 and game_settings.total_sun >= 5200):
							for plant in plants:
								if plant.square == square:
									if plant.name=='gunner3':
										plants.remove(plant);
										plants.add(Gunner4(screen,square,game_settings));
										game_settings.total_sun -= 5200																	
						elif(game_settings.chosen_plant == 5 and game_settings.total_sun >= 500):
							remove_plant_in_square(square, plants)
							plants.add(Sunflower(screen,square,game_settings));	
							game_settings.total_sun -= 500
						elif(game_settings.chosen_plant == 6 and game_settings.total_sun >= (30+int(tick/50))):
							plants.add(Robot(screen,square,game_settings));		
							game_settings.total_sun -= (30+int(tick/50))

				for icon in icons:
					if icon.rect.collidepoint(mouse_x,mouse_y):
						game_settings.chosen_plant = icon.slot
						# print "You clicked: ",icon.image;
						icon.chosen = True;
					else:
						icon.chosen = False;
						# plants.add(Peashooter(screen,square));		
			elif event.type == pygame.MOUSEMOTION:
				# print event.pos
				for square in squares:
					if square.rect.collidepoint(event.pos):
						game_settings.highlighted_square = square;
						# print game_settings.highlighted_square;

def update_screen(screen,game_settings,background,zombies,squares,plants,bullets,tick,icons):
	screen.blit(background.image, background.rect);

	for icon in icons:
		screen.blit(icon.image, icon.rect);
		if icon.slot == game_settings.chosen_plant:
			pygame.draw.rect(screen, (180,180,255), (icon.rect.left, icon.rect.top,int(115),int(145)),2);
			s = pygame.Surface((int(115),int(145)), pygame.SRCALPHA)   # per-pixel alpha
			s.fill((0,0,200,35))                        
			screen.blit(s, (icon.rect.left, icon.rect.top))


	if game_settings.highlighted_square != 0:
		pygame.draw.rect(screen, (255,215,255), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares['square_width'],game_settings.squares['square_height']),2);
		s = pygame.Surface((game_settings.squares['square_width'],game_settings.squares['square_height']), pygame.SRCALPHA)   # per-pixel alpha
		s.fill((255,215,255,35))                        
		screen.blit(s, (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top))
	for plant in plants:
		plant.draw_me();
		# if plant.name == 'sunflower':
			# plant.get_bigger();
		# else: plant.draw_me();
		# print plant.yard_row;
		# if tick % 20 == 0:
		# is it time to shoot?
		should_shoot = time.time() - plant.last_shot > plant.shoot_speed
		# print time.time() - plant.last_shot;


		in_my_row = game_settings.zombie_in_row[plant.yard_row] > 0
		if plant.name == 'gunner4':
			in_my_row = True;
		plant.change_image(in_my_row and should_shoot)
		can_shoot = plant.can_shoot
		can_make_sun = plant.can_make_sun
		should_make_sun = (time.time() - plant.last_sun) > plant.sun_speed;
		if should_shoot and in_my_row and can_shoot:
			bullets.add(Bullet(screen,plant,tick));
			plant.last_shot = time.time();

		if can_make_sun and should_make_sun:
			plant.make_sun(game_settings);
			plant.last_sun = time.time();

	for zombie in zombies.sprites():
		if game_settings.game_active:
			zombie.update_me();
		zombie.draw_me();
		if zombie.rect.left <= zombie.screen_rect.left:
			game_settings.game_active = False;


	for bullet in bullets.sprites():	
		bullet.update_me();
		bullet.draw_me();



	score_font = pygame.font.SysFont("monospace",36);
	# render font takes 3 params:
	# 1. What text.
	# 2. 
	# 3. Color
	sun_render = score_font.render("Score: " + str((tick*3)),1,(0,0,0));
	screen.blit(sun_render,(100,50));

	score_render = score_font.render("Kills: "+str(game_settings.zombies_killed),1,(0,0,0));
	screen.blit(score_render,(100,90));

	sun_render = score_font.render("Minerals: "+str(game_settings.total_sun),1,(0,0,0));
	screen.blit(sun_render,(100,130));

	cost_font = pygame.font.SysFont("Arial",20);
	sun_render = cost_font.render("50                            200                           1050                         5200                           500                            "+str(30 + int(tick/50)),1,(0,0,0));
	screen.blit(sun_render,(475,170));

	sun_render = cost_font.render("                           upgrade        >>>       upgrade       >>>       upgrade",1,(0,0,0));
	screen.blit(sun_render,(475,22));