import pygame
from random import randint
# Varieable

HEIGHT = 1000
WIDTH = 1500
BORDER = 20
VELOCITY = 1

# Define Class


class Ball:

    RADIUS = 20

    def __init__(self, x, y, vx, vy, color, bg_color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.bg_color = bg_color

    def show(self, color):

        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)

    def is_on_paddle(self):
        global rumpesprett
        if (self.x + self.RADIUS > WIDTH - Paddle.WIDTH and
                rumpesprett.y - Paddle.HEIGHT//2 < self.y < rumpesprett.y + Paddle.HEIGHT//2):
            return True
        return False

    def update(self):
        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx <= BORDER + self.RADIUS:
            self.vx = -self.vx
            self.color = make_random_color()
        elif self.is_on_paddle():
            self.vx = -abs(self.vx)
            self.color = make_random_color()
        elif newy < BORDER + self.RADIUS or newy > HEIGHT - BORDER - self.RADIUS:
            self.vy = -self.vy
            self.color = make_random_color()

        self.show(self.bg_color)
        self.x = newx
        self.y = newy
        self.show(self.color)


class Paddle:
    WIDTH = 20
    HEIGHT = 400

    def __init__(self, y):
        self.y = y

    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect(
            WIDTH-self.WIDTH, self.y-self.HEIGHT//2, Paddle.WIDTH, Paddle.HEIGHT))

    def update(self):
        global fgColor, bgColor
        self.show(bgColor)
        self.y = pygame.mouse.get_pos()[1]
        self.show(fgColor)


# Create objects
def make_random_color():
    """
    returns a random pygame.color
    """
    R = randint(50,255)
    B = randint(50,255)
    G = randint(50,255)

    return pygame.Color(R,B,G)
    

my_color = pygame.Color(0,255,255)

rumpesprett = Paddle(HEIGHT//2)
ballplay = Ball(3*WIDTH//5 - Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY, make_random_color(), pygame.Color("black"))
ballplay2 = Ball(3*WIDTH//4 - Ball.RADIUS, 3*HEIGHT//4, -VELOCITY, -VELOCITY, make_random_color() , pygame.Color("black"))
# Draw scenario
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgColor = pygame.Color("black")
fgColor = pygame.Color("magenta")

pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, WIDTH, BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, BORDER, HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0, HEIGHT - BORDER, WIDTH, BORDER))


ballplay.show(fgColor)
ballplay2.show(fgColor)
rumpesprett.show(fgColor)

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    pygame.display.flip()
    ballplay.update()
    ballplay2.update()
    rumpesprett.update()


pygame.quit()
