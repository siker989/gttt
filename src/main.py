app='Hello Heroes'
print(app)
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooting Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up player
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 5

# Set up bullet
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Set up enemy
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []

# Set up clock
clock = pygame.time.Clock()

# Function to draw player
def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

# Function to draw bullet
def draw_bullet(x, y):
    pygame.draw.rect(screen, white, [x, y, bullet_width, bullet_height])

# Function to draw enemy
def draw_enemy(x, y):
    pygame.draw.rect(screen, red, [x, y, enemy_width, enemy_height])

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed

    # Generate new enemies
    if random.randint(0, 100) < 5:
        enemy_x = random.randint(0, width - enemy_width)
        enemy_y = -enemy_height
        enemies.append([enemy_x, enemy_y])

    # Collision detection
    for bullet in bullets:
        for enemy in enemies:
            if (
                bullet[0] < enemy[0] + enemy_width
                and bullet[0] + bullet_width > enemy[0]
                and bullet[1] < enemy[1] + enemy_height
                and bullet[1] + bullet_height > enemy[1]
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Draw everything
    screen.fill(black)
    draw_player(player_x, player_y)
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])
    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])

    pygame.display.flip()
    clock.tick(60)