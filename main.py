import pygame as pg
from mazeMap import maze
import createMaze
#import tilt

#maze = createMaze.load_maze(50, 50)
print(maze)

pg.init()
screenSize = (800,800)

bgColour = (255,255,255)
wallColour = (0,255,0)
playerColour = (255,0,0)
screen = pg.display.set_mode(screenSize)
clock = pg.time.Clock()
playerCoord = [10, 14]
lines = []
cell_size = 24

def draw_lines(maze):
	for (x, y), neighbours in maze.items():
		if (x,y-1) not in neighbours:
			line = pg.Rect(x*cell_size, y*cell_size, cell_size, 5)
			pg.draw.rect(screen, wallColour, line)
			lines.append(line)

		if (x,y+1) not in neighbours:
			line = pg.Rect(x*cell_size, (y+1)*cell_size, cell_size, 5)
			pg.draw.rect(screen, wallColour, line)
			lines.append(line)

		if (x-1,y) not in neighbours:
			line = pg.Rect(x*cell_size, y*cell_size, 5, cell_size+5)
			pg.draw.rect(screen, wallColour, line)
			lines.append(line)

		if (x+1,y) not in neighbours:
			line = pg.Rect((x+1)*cell_size, y*cell_size, 5, cell_size+5)
			pg.draw.rect(screen, wallColour, line)
			lines.append(line)

def mtCollide():
	for line in lines:
		if line.collidepoint(playerRect.midtop):
			return True
	return False

def mlCollide():
	for line in lines:
		if line.collidepoint(playerRect.midleft):
			return True
	return False

def mbCollide():
	for line in lines:
		if line.collidepoint(playerRect.midbottom):
			return True
	return False

def mrCollide():
	for line in lines:
		if line.collidepoint(playerRect.midright):
			return True
	return False

running = True
while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

	screen.fill(bgColour)

	playerRect = pg.Rect(playerCoord[0], playerCoord[1], 10, 10)
	player = pg.draw.rect(screen, playerColour, playerRect)
	lines = []
	draw_lines(maze)
		
	inputBuffer = 0
	keys = pg.key.get_pressed()
	"""
	x, y, z = tilt.get_tilt_data() # No use for z

	if not mlCollide():
		playerCoord[0] += x/100

	if not mrCollide():
		playerCoord[0] += x/100

	if not mtCollide():
		playerCoord[1] += y/100

	if not mbCollide():
		playerCoord[1] += y/100
	"""
	if keys[pg.K_w]:
		if not mtCollide():
			if inputBuffer == 0:
				inputBuffer = 10
				playerCoord[1] -= 3

	if keys[pg.K_a]:
		if not mlCollide():
			if inputBuffer == 0:
				inputBuffer = 10
				playerCoord[0] -= 3

	if keys[pg.K_s]:
		if not mbCollide():
			if inputBuffer == 0:
				inputBuffer = 10
				playerCoord[1] += 3
		
	if keys[pg.K_d]:
		if not mrCollide():
			if inputBuffer == 0:
				inputBuffer = 10
				playerCoord[0] += 3
		
	if inputBuffer > 0:
		inputBuffer -= 1

	clock.tick(120)
	pg.display.flip()
pg.quit()
