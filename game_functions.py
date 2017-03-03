import sys;
import pygame;
from peashooter import Peashooter;
from gatling import Gatling;
from bullet import Bullet;
from sunflower import Sunflower;
from robot import Robot;
import time;

def check_events(screen, game_settings,squares,plants,bullets,icons):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if game_settings.game_active:
	 		if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos();
				# print mouse_x;
				# print mouse_y;
				for square in squares:
					if square.rect.collidepoint(mouse_x,mouse_y):
						print "Square: ",square.square_number;
						if(game_settings.chosen_plant == 1):
							plants.add(Peashooter(screen,square,game_settings));
						elif(game_settings.chosen_plant == 2):
							plants.add(Gatling(screen,square,game_settings));
						elif(game_settings.chosen_plant == 3):
							plants.add(Sunflower(screen,square,game_settings));	
						elif(game_settings.chosen_plant == 4):
							plants.add(Robot(screen,square,game_settings));		
				for icon in icons:
					if icon.rect.collidepoint(mouse_x,mouse_y):
						game_settings.chosen_plant = icon.slot
						print "You clicked: ",icon.image;
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


	if game_settings.highlighted_square != 0:
		pygame.draw.rect(screen, (255,215,255), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares['square_width'],game_settings.squares['square_height']),2);
		s = pygame.Surface((game_settings.squares['square_width'],game_settings.squares['square_height']), pygame.SRCALPHA)   # per-pixel alpha
		s.fill((255,215,255,35))                         # notice the alpha value in the color
		screen.blit(s, (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top))
	for plant in plants:
		plant.draw_me();

		# print plant.yard_row;
		# if tick % 20 == 0:
		# is it time to shoot?
		should_shoot = time.time() - plant.last_shot > plant.shoot_speed
		# print time.time() - plant.last_shot;


		in_my_row = game_settings.zombie_in_row[plant.yard_row] > 0
		plant.change_image(in_my_row and should_shoot)
		can_shoot = plant.can_shoot
		can_make_sun = plant.can_make_sun
		should_make_sun = (time.time() - plant.last_sun) > plant.sun_speed;
		if should_shoot and in_my_row and can_shoot:
			bullets.add(Bullet(screen,plant));
			plant.last_shot = time.time();

		if can_make_sun and should_make_sun:
			plant.make_sun(game_settings);
			plant.last_sun = time.time();
	for bullet in bullets.sprites():	
		bullet.update_me();
		bullet.draw_me();

	# draw zombies
	for zombie in zombies.sprites():
		if game_settings.game_active:
			zombie.update_me();
		zombie.draw_me();
		if zombie.rect.left <= zombie.screen_rect.left:
			game_settings.game_active = False;

	score_font = pygame.font.SysFont("monospace",36);
	# render a font takes 3 params:
	# 1. What text.
	# 2. I cant remember
	# 3. Color
	score_render = score_font.render("Kills: "+str(game_settings.zombies_killed),1,(0,0,0));
	screen.blit(score_render,(100,70));

	sun_render = score_font.render("Gold: "+str(game_settings.total_sun),1,(0,0,0));
	screen.blit(sun_render,(100,120));