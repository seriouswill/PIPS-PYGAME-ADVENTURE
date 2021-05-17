import pygame

pygame.init()
screen_width = 500
screen_height = 480
win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("PIPS PYGAME IN INGERLAND")

# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


clock = pygame.time.Clock()
bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
# classes


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load(
        'R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load(
        'L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        # This will define where our enemy starts and finishes their path.
        self.path = [x, end]
        self.walk_count = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 60)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.vel > 0:
                win.blit(
                    self.walkRight[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.walkLeft[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        if self.health > 0:
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(
            win, (0, 230, 0), (self.hitbox[0], self.hitbox[1] - 20,  50 - (5*(10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31, 60)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        global hit_count
        hit_count += 1


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.jump_count = 10
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.life_count = 10

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(walkRight[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(win, (255, 0, 0),
                         (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(
            win, (0, 230, 0), (self.hitbox[0], self.hitbox[1] - 20,  50 - (5*(10 - self.life_count)), 10))
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.is_jump = False
        self.jump_count = 10
        self.x = 60
        self.y = 410
        self.walk_count = 0

        font1 = pygame.font.SysFont('comicsans', 30)
        hit_text = font1.render(
            'SAMMATRON USED LANGOS!', 1, (255, 0, 0))
        hit_text2 = font1.render('-5 points, and -1 life.', 1, (255, 0, 0))
        win.blit(hit_text2, (screen_width/2 -
                 (hit_text2.get_width()/2), screen_height/2))
        win.blit(hit_text, (screen_width/2 -
                 (hit_text.get_width()/2), screen_height/2 - 20))
        pygame.display.update()
        i = 0
        while i < 150:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 151
                    pygame.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 30)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)


# functions
def redrawGameWindow():
    global walk_count
    global hit_count
    win.blit(bg, (0, 0))
    goblin.draw(win)

    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    text = TITLE_FONT.render("BERKPOCALYPSE", 1, BLACK)
    win.blit(text, (screen_width/2 - text.get_width()/2, 20))

    score = WORD_FONT.render(
        f"You Swangled him {hit_count} times!", 1, BLUE)
    win.blit(score, (screen_width/2 - text.get_width()/2, 60))
    pygame.display.update()


def display_message(colour, message):
    pygame.time.delay(2000)
    win.fill(colour)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (screen_width/2 - text.get_width() /
             2, screen_height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


# game loop
man = player(300, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
run = True
bullets = []
hit_count = 0
lives = 5

# WHOLE GAME FUNCTION


def run_game():
    global run
    global shootLoop
    global bullets
    global hit_count
    global lives
    global life_count

    while run:
        clock.tick(27)
        # collision
        if goblin.visible == True:
            if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:

                    man.hit()
                    hit_count -= 5
                    man.life_count -= 1

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        # quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # bullets
        for bullet in bullets:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    if goblin.health != 0:
                        hitSound.play()

                    goblin.hit()
                    bullets.pop(bullets.index(bullet))

            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        # key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and shootLoop == 0:
            bulletSound.play()
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 7:
                bullets.append(projectile(round(man.x + man.width // 2),
                               round(man.y + man.height // 2), 6, (RED), facing))
            shootLoop = 1
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
            man.x += man.vel
            man.left = False
            man.right = True
            man.standing = False
        else:
            man.standing = True
            man.walk_count = 0

        if not(man.is_jump):
            if keys[pygame.K_UP]:
                man.is_jump = True
                man.right = False
                man.left = False
                man.walk_count = 0
        else:
            if man.jump_count >= -10:
                neg = 1
                if man.jump_count < 0:
                    neg = -1
                man.y -= (man.jump_count ** 2) * 0.5 * neg
                man.jump_count -= 1
            else:
                man.is_jump = False
                man.jump_count = 10

        if man.life_count == 0:
            display_message(RED, "YOU FUCKING LOST")
            pygame.quit()
        redrawGameWindow()

    pygame.quit()


run_game()
