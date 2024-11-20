import pygame as pg
import createMaze
import tilt
maze_size = 30
maze = createMaze.load_maze(maze_size, maze_size)

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
		if line.collidepoint(future_rect.midtop):
			return True
	return False

def mlCollide():
	for line in lines:
		if line.collidepoint(future_rect.midleft):
			return True
	return False

def mbCollide():
	for line in lines:
		if line.collidepoint(future_rect.midbottom):
			return True
	return False

def mrCollide():
	for line in lines:
		if line.collidepoint(future_rect.midright):
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

	x, y, z = tilt.get_tilt_data() # No use for z
	y = y*-1 # flip the y axis (maybe)
	print(f" {x}\t {y}")
	future_pos = [playerCoord[0] + x/maze_size, playerCoord + y/maze_size]
	future_rect = pg.Rect(future_pos[0], future_pos[1])

	if mlCollide() or mrCollide() or mtCollide() or mbCollide():
		while mlCollide():
			future_pos[0] += 1

		while mrCollide():
			future_pos[0] -= 1

		while mtCollide():
			future_pos[1] += 1

		while mbCollide():
			future_pos[1] -= 1
	playerCoord = future_pos


#if not mlCollide():
	playerCoord[0] += x/maze_size

#if not mrCollide():
	#playerCoord[0] += x/maze_size

#if not mtCollide():
	playerCoord[1] += y/maze_size

#if not mbCollide():
	#playerCoord[1] += y/maze_size

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

	clock.tick(10)
	pg.display.flip()
pg.quit()
