import os
import pygame

#Initializing Pygame
pygame.init()

#Setting up screen
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")
isPlaying = True

# Background
background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Background.jpg'))

#Player Setup
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        playerImg = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Ship.jpg'))
        screen.blit(playerImg, (self.x, self.y))

#Enemy Setup
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        enemyImg = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Alien.png'))
        screen.blit(enemyImg, (self.x, self.y))
        self.y += 0.1

    def detectCollision(self):
        for laser in lasers:
            if (laser.x > self.x and
                    laser.x < self.x + 64 and
                    laser.y > self.y and
                    laser.y < self.y + 64):
                lasers.remove(laser)
                enemies.remove(self)

#Laser/Bullet Setup
class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (254, 71, 110), pygame.Rect(self.x, self.y, 2, 5))
        self.y -= 4

# Create Player object
player = Player(width/2, height - 50)

# Enemies list
enemies = []

#lasers list
lasers = []

# Spawn enemies
for x in range(1, 11):
    for y in range(1, 4):
        enemies.append(Enemy(x * 50, y * 50))

def displayText(text):
    font = pygame.font.SysFont('', 50)
    message = font.render(text, False, (255, 255, 255))
    screen.blit(message, (200, 160))

#Game Loop
while isPlaying:
    screen.blit(background, (0, 0))
    player.draw()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if player.x > 20:
            player.x -= 2
    elif pressed[pygame.K_RIGHT]:
        if player.x < width - 40:
            player.x += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlaying = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            lasers.append(Laser(player.x, player.y))

    for enemy in enemies:
        enemy.draw()
        enemy.detectCollision()
        if enemy.y > height-32:
            displayText("GAME OVER")

    for laser in lasers:
        laser.draw()

    if len(enemies) <= 10:
      enemy.y += 0.5

    if len(enemies) <= 0:
        displayText("YOU WIN")

    pygame.display.update()
