# INITIALIZE
import random
import pygame


# Ghost Class
class Ghost(pygame.sprite.Sprite):

    (SEEK, FLEE, SEPARATE) = range(3)
    moving_frame = []

    def __init__(self, startpos, velocity, startdir):
        super().__init__()
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()

        # Animation of ghost
        image1 = pygame.image.load("images/ghost1.jpg").convert()
        image1 = pygame.transform.scale(image1, (50, 50))
        self.moving_frame.append(image1)
        image = pygame.image.load("images/ghost2.jpg").convert()
        image_c = pygame.transform.scale(image, (50, 50))
        self.moving_frame.append(image_c)
        image = pygame.image.load("images/ghost3.jpg").convert()
        image_c = pygame.transform.scale(image, (50, 50))
        self.moving_frame.append(image_c)
        self.image = image1
        self.rect = self.image.get_rect(
            center=(round(self.pos.x), round(self.pos.y)))
        self.state = Ghost.SEEK

    def update(self):
        if started:
            x, y = pygame.mouse.get_pos()
            # Find direction vector (dx, dy) between enemy and player.
            dirvect = pygame.math.Vector2(x - self.rect.centerx,
                                          y - self.rect.centery)

            try:
                dirvect.normalize_ip()
                if self.state == Ghost.FLEE:
                    dirvect.rotate_ip(180)
            except:
                print("caught player")

            self.dir = dirvect
        if self.state != Ghost.SEPARATE:
            self.pos += self.dir * self.velocity
        else:
            dist = pygame.math.Vector2.distance_to(
                pygame.math.Vector2(x, y), self.pos)
            # arbitrary distance, just be cautious that it includes the whole radius of the circle so it needs to be rather large
            if (dist > 75):
                self.pos += self.dir * self.velocity
            else:
                self.pos += pygame.math.Vector2(0, 0)

        pos = self.rect.x
        frame = (pos // 30) % len(self.moving_frame)
        self.image = self.moving_frame[frame]

        self.rect.center = round(self.pos.x), round(self.pos.y)

# Walls
"""
wall = Wall(200,150,800,2)
wallList.add(wall)
allSpriteList.add(wall)
wall = Wall(200,850,800,2)
wallList.add(wall)
allSpriteList.add(wall)
wall = Wall(0,0,2,1080)
wallList.add(wall)
allSpriteList.add(wall)
wall = Wall(0,1078,1920,2)
wallList.add(wall)
allSpriteList.add(wall)
wall = Wall(1918,0,2,1080)
wallList.add(wall)
allSpriteList.add(wall)
wall = Wall(0,0,1920,2)
wallList.add(wall)
allSpriteList.add(wall)
"""
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

all_groups = pygame.sprite.Group()
start, velocity, direction = (
                                 250, 250), 5, (random.random(), random.random())
ghost = Ghost(start, velocity, direction)
all_groups.add(ghost)
started = False

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                ghost.state = Ghost.SEEK
            if event.key == pygame.K_f:
                ghost.state = Ghost.FLEE
            if event.key == pygame.K_s:
                ghost.state = Ghost.SEPARATE
            if event.key == pygame.K_SPACE:
                print("starting to chase")
                started = True

    all_groups.update()

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), (100, 100, 300, 300), 1)
    all_groups.draw(window)
    pygame.display.flip()
