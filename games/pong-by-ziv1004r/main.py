import pygame, sys, random, os


def anime():
	global ball_speed_x, ball_speed_y, player_score, opponent_score
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	
	if ball.left <= 0: 
		ball_start()
		player_score += 1

	if ball.right >= screen_width:
		ball_start()
		opponent_score += 1		

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

def p_anime():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opp_anime():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))


pygame.init()
clock = pygame.time.Clock()


screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Z-pong')


light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)
playing = True

while playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -= 6
			if event.key == pygame.K_DOWN:
				player_speed += 6
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed += 6
			if event.key == pygame.K_DOWN:
				player_speed -= 6
	
	
	anime()
	p_anime()
	opp_anime()
	screen.fill(bg_color)
	pygame.draw.rect(screen, light_grey, player)
	pygame.draw.rect(screen, light_grey, opponent)
	pygame.draw.ellipse(screen, light_grey, ball)
	pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))
	player_text = basic_font.render(f'{player_score}',False,light_grey)
	screen.blit(player_text,(660,470))
	opponent_text = basic_font.render(f'{opponent_score}',False,light_grey)
	screen.blit(opponent_text,(600,470))


	pygame.display.flip()
	clock.tick(60)
pygame.quit()