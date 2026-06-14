import pygame, sys, random, time
from pygame.locals import *

pygame.init()

# Colors
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
WORLD_WIDTH = 3000
WORLD_HEIGHT = 3000

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dungeon Chef')

# Variables
spawn_points = [(500-25, 75), (50, WINDOW_HEIGHT//2), (950-50, 300)]
last_spawn_time = 0
spawn_interval = 3000  # 2.3 seconds in milliseconds
fading_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
fading_surface.fill((255, 0, 0))  # Red color
fade_alpha = 0
game_over = False
camera_x = 0
camera_y = 0

# Images
background = pygame.image.load('floor.png').convert_alpha()
background = pygame.transform.scale(background, (3000, 3000))



class Player():
    def __init__(self):
        self.x = 300
        self.y = 500
        self.width = 50
        self.height = 50
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.health = 10
        self.max_health = 10
        self.last_hit = 0
        #self.healthbar = Healthbar()

    def draw(self, camera_x, camera_y):
        pygame.draw.rect(WINDOW, (50, 5, 50), (self.x - camera_x, self.y - camera_y, self.width, self.height))

    def monster_collisions(self, monster):
        if self.hitbox.colliderect(monster.hitbox):
            start_time = pygame.time.get_ticks()
            if start_time - self.last_hit > 2000:
                player.health -= 1

    def movement(self):
        speed = 2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= speed
            self.update()
            if station1.collisions(self):
                self.hitbox.left = station1.hitbox.right
                self.x = self.hitbox.x
            elif boundary1.collisions(self):
                if boundary1.left.colliderect(self.hitbox):
                    self.hitbox.left = boundary1.left.right
                    self.x = self.hitbox.x
        if keys[pygame.K_RIGHT]:
            self.x += speed
            self.update()
            if station1.collisions(self):
                self.hitbox.right = station1.hitbox.left
                self.x = self.hitbox.x
            elif boundary1.collisions(self):
                if boundary1.right.colliderect(self.hitbox):
                    self.hitbox.right = boundary1.right.left
                    self.x = self.hitbox.x
        if keys[pygame.K_UP]:
            self.y -= speed
            self.update()
            if station1.collisions(self):
                self.hitbox.top = station1.hitbox.bottom
                self.y = self.hitbox.y
            elif boundary1.collisions(self):
                if boundary1.top.colliderect(self.hitbox):
                    self.hitbox.top = boundary1.top.bottom
                    self.y = self.hitbox.y
        if keys[pygame.K_DOWN]:
            self.y += speed
            self.update()
            if station1.collisions(self):
                self.hitbox.bottom = station1.hitbox.top
                self.y = self.hitbox.y
            elif boundary1.collisions(self):
                if boundary1.bottom.colliderect(self.hitbox):
                    self.hitbox.bottom = boundary1.bottom.top
                    self.y = self.hitbox.y

        if self.x < 0:
            self.x = 0

        if self.x > WORLD_WIDTH - self.width:
            self.x = WORLD_WIDTH - self.width

        if self.y < 0:
            self.y = 0

        if self.y > WORLD_HEIGHT - self.height:
            self.y = WORLD_HEIGHT - self.height

    def update(self):
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def magic(self):
        pass

    def camera(self):
        pass

    def animation(self):
        pass

class boundary(): # boundaries for the dungeon background so it feels like a room
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.top = pygame.Rect(self.x, self.y, self.width, 10)
        self.bottom = pygame.Rect(self.x, self.y + self.height - 10, self.width, 10)
        self.left = pygame.Rect(self.x, self.y, 10, self.height)
        self.right = pygame.Rect(self.x + self.width - 10, self.y, 10, self.height)

    def draw(self):
        pygame.draw.rect(WINDOW, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)

    def collisions(self, player):
        return (
                self.top.colliderect(player.hitbox)
                or self.bottom.colliderect(player.hitbox)
                or self.left.colliderect(player.hitbox)
                or self.right.colliderect(player.hitbox)
        )

# Boundary Objects
boundary1 = boundary(0, 0, WORLD_WIDTH, WORLD_HEIGHT)


class slot():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(WINDOW, (255, 255, 255), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(WINDOW, (0, 0, 0), (self.x, self.y, self.width, self.height), 5)


class Monster():
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 35
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 1

    def draw(self, camera_x, camera_y):
        pygame.draw.rect(WINDOW, (255, 0, 0), (self.x - camera_x, self.y - camera_y, self.width, self.height))

    def update(self):
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def drop_item(self):
        pass

    def attack(self):
        pass

    def defense(self):
        pass

    def collisions(self):
        if player.hitbox.colliderect(self.hitbox):
            current_time = pygame.time.get_ticks()
            # Only deal damage if enough time has passed since last hit (2 seconds = 2000ms)
            if current_time - player.last_hit > 2000:
                player.health -= 1
                player.health = max(0, player.health)
                player.last_hit = current_time  # Reset the timer
                return True
        return False

    def movement(self, player):
        if player.x > self.x:
            self.x += self.speed
            self.update()
        if player.x < self.x:
            self.x -= self.speed
            self.update()
        if player.y < self.y:
            self.y -= self.speed
            self.update()
        if player.y > self.y:
            self.y += self.speed
            self.update()

# cooking station class
class station():
    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, camera_x, camera_y):
        pygame.draw.rect(WINDOW, self.color, (self.x - camera_x, self.y - camera_y, self.width, self.height))

    def collisions(self, player):
        return self.hitbox.colliderect(player.hitbox)

    def cooking(self):
        pass


# Player Object
player = Player()

class Healthbar():
    def __init__(self):
        self.x = 20
        self.y = 20
        self.width = 200+75
        self.height = 40
        self.main_color = (46, 204, 113)

    def draw(self):
        pygame.draw.rect(WINDOW, (100, 100, 100), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(WINDOW, (self.main_color), (self.x, self.y, self.current_width, self.height))
        pygame.draw.rect(WINDOW, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)

    def update(self, player):
        self.health_percent = player.health / player.max_health
        self.current_width = self.width * self.health_percent
        player.health = max(0, player.health)
        if player.health > 6:
            self.main_color = (46, 204, 113)
        elif player.health > 3:
            self.main_color = (255, 215, 0)
        else:
            self.main_color = (255, 0, 0)
        pygame.draw.rect(WINDOW, (self.main_color), (self.x, self.y, self.current_width, self.height))

# Objects
healthbar = Healthbar()
station1 = station(300, 100, 100, 100, (205, 133, 63))
slot1 = slot(WINDOW_WIDTH - 450, WINDOW_HEIGHT - 80)
slot2 = slot(slot1.x + slot1.width, WINDOW_HEIGHT - 80)
slot3 = slot(slot2.x + slot2.width, WINDOW_HEIGHT - 80)
slot4 = slot(slot3.x + slot3.width, WINDOW_HEIGHT - 80)
slot5 = slot(slot4.x + slot4.width, WINDOW_HEIGHT - 80)
slot6 = slot(slot5.x + slot5.width, WINDOW_HEIGHT - 80)
slot7 = slot(slot6.x + slot6.width, WINDOW_HEIGHT - 80)
slot_list = [slot1, slot2, slot3, slot4, slot5, slot6, slot7]
monsters = []


# The main function that controls the game
def main():
    global last_spawn_time, fade_alpha, game_over
    looping = True

    # The main game loop
    while looping:

        # Check if player died
        if player.health <= 0:
            game_over = True

        # Only update game logic if not game over
        if not game_over:
            player.movement()
            player.update()
            # Clamp camera to world boundaries
            camera_x = player.x - WINDOW_WIDTH // 2
            camera_y = player.y - WINDOW_HEIGHT // 2
            camera_x = max(0, min(camera_x, WORLD_WIDTH - WINDOW_WIDTH))
            camera_y = max(0, min(camera_y, WORLD_HEIGHT - WINDOW_HEIGHT))
            # Get inputs
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Processing
            # Get current time for spawning

            # Render elements of the game
            WINDOW.blit(background, (-camera_x, -camera_y))

            current_time = pygame.time.get_ticks()
            
            # Check if it's time to spawn a new monster
            if current_time - last_spawn_time > spawn_interval:
                spawn_x, spawn_y = random.choice(spawn_points)
                new_monster = Monster(spawn_x, spawn_y)
                monsters.append(new_monster)
                last_spawn_time = current_time
                print(f"Monster spawned at ({spawn_x}, {spawn_y})")

            for monster in monsters:
                monster.movement(player)
                monster.collisions()
                monster.draw(camera_x, camera_y)

            # Objects made from class
            player.draw(camera_x, camera_y)
            station1.draw(camera_x, camera_y)
            healthbar.update(player)
            healthbar.draw()
            #boundary1.draw()
            station1.collisions(player)
            for x in slot_list:
                x.draw()
        else:
            # Game over - handle fade effect
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Still draw the game state behind the fade
            WINDOW.blit(background, (-camera_x, -camera_y))
            for monster in monsters:
                monster.draw(camera_x, camera_y)
            player.draw(camera_x, camera_y)
            station1.draw(camera_x, camera_y)
            healthbar.draw()
            for x in slot_list:
                x.draw()

            # Gradually increase fade alpha
            if fade_alpha < 255:
                fade_alpha += 2  # Adjust this value to change fade speed
                fading_surface.set_alpha(fade_alpha)
                WINDOW.blit(fading_surface, (0, 0))

        pygame.display.update()
        fpsClock.tick(FPS)

main()
