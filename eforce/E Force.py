import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 1000

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("E Force")

white = (255, 255, 255)
black = (0, 0, 0)

class Player:
	def __init__(self, win, x, y, width, height, color, vel):
		self.win = win
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.vel = vel
		
	def draw(self):
		pygame.draw.rect(self.win, self.color, [self.x, self.y, self.width, self.height])
		
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.y -= vel
			
		pygame.display.update()

#class Bullet:
	
	
#class Target:

playing = True

while playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False
			
	win.fill((white))
	
	player = Player(win, 10, 500, 50, 50, black, 1)
	player.draw()
	
	pygame.display.update()
