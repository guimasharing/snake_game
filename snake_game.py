import pygame
import random

GRIDS_WIDTH = 30
GRIDS_HEIGHT = 20
BLOCK = 40
BG_COLOR = (23, 126, 137)
GAME_RUNNING = True
FOOD_COLOR = (219, 58, 52)
OUTLINE_COLOR = (8, 76, 97)
SNAKE_COLOR = (255, 200, 87)
FONT_COLOR = (8, 76, 9)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
TICK = 5


class Snake(object):
    def __init__(self):
        self.length = 3
        self.positions = [(12, 4), (12, 5), (12, 6)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = SNAKE_COLOR
        self.scores = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, direction):
        if (direction[0]*-1, direction[1]*-1) == self.direction:
            return
        else:
            self.direction = direction

    def move(self):
        a, b = self.direction
        head_position = self.get_head_position()
        a2 = head_position[0]+a
        b2 = head_position[1]+b
        new_head_position = (a2, b2)
        if new_head_position in self.positions:
            quit()
        elif a2 < 0 or a2 > GRIDS_WIDTH-1 or b2 < 0 or b2 > GRIDS_HEIGHT-1:
            quit()
        else:
            self.positions.insert(0, new_head_position)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, screen):
        for p in self.positions:
            r = pygame.Rect(p[0]*BLOCK, p[1]*BLOCK, BLOCK, BLOCK)
            pygame.draw.rect(screen, SNAKE_COLOR, r)
            pygame.draw.rect(screen, OUTLINE_COLOR, r, 3)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = FOOD_COLOR
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRIDS_WIDTH-1),
                         random.randint(0, GRIDS_HEIGHT-1))

    def draw(self, screen):
        r = pygame.Rect(self.position[0]*BLOCK,
                        self.position[1]*BLOCK, BLOCK, BLOCK)
        pygame.draw.rect(screen, self.color, r)
        pygame.draw.rect(screen, OUTLINE_COLOR, r, 3)


def main():
    pygame.init()
    screen = pygame.display.set_mode([GRIDS_WIDTH*BLOCK, GRIDS_HEIGHT*BLOCK])
    pygame.display.set_caption("喂饱贪吃的蛇")
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont('STSong', 20)
    food = Food()
    snake = Snake()
    while GAME_RUNNING:
        clock.tick(TICK)
        snake.handle_keys()
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.scores += 1
            food.randomize_position()
        screen.fill(BG_COLOR)
        snake.draw(screen)
        food.draw(screen)
        scores_text = myfont.render(
            "分数：{0}".format(snake.scores), 1, FONT_COLOR)
        screen.blit(scores_text, (8, 10))
        pygame.display.update()
    pygame.quit()


main()
