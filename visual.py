from re import A
import pygame as pg

_WHITE=(255, 255, 255)
_BLACK=(0, 0, 0)

grid_block_size = 15
draw_speed = 60
render_speed = 10
clock = pg.time.Clock()

def init_pygame(board):
    display_width = grid_block_size * board.bounds[0]
    display_height = grid_block_size * board.bounds[1]

    pg.init()
    dis = pg.display.set_mode((display_width, display_height))
    pg.display.set_caption('Conway\'s Game of Life')

    dis.fill(_WHITE)
    pg.display.update()

    loop(board, dis)

def loop(board, dis):
    running = True

    spaceHeld = False
    boardRunning = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False

        if pg.mouse.get_pressed()[0]:   #event.type==pygame.MOUSEBUTTONDOWN
            pos = pg.mouse.get_pos()
            col = pos[0] // grid_block_size
            row = pos[1] // grid_block_size
            draw_grid_block(board, dis, col, row, 1)
        elif pg.mouse.get_pressed()[2]:   #event.type==pygame.MOUSEBUTTONDOWN
            pos = pg.mouse.get_pos()
            col = pos[0] // grid_block_size
            row = pos[1] // grid_block_size
            draw_grid_block(board, dis, col, row, 0)

        pressed = pg.key.get_pressed()
        if pressed[pg.K_SPACE]:
            if not spaceHeld:
                boardRunning = not boardRunning
            spaceHeld = True
        else:
            spaceHeld = False

        if boardRunning:
            board.next_frame()
            render_grid(board, dis)
            clock.tick(render_speed)
        else:
            clock.tick(draw_speed)

        pg.display.flip()
    pg.quit()
    quit()

def render_grid(board, dis):
    dis.fill(_WHITE)
    for x in range(board.bounds[0]):
        for y in range(board.bounds[1]):
            render_cell(dis, x, y, board.get_cell(x, y).alive)
    pg.display.flip()

def render_cell(dis, x, y, alive):
    if alive:
        pg.draw.rect(dis, _BLACK, [x * grid_block_size, y * grid_block_size, grid_block_size, grid_block_size])

def draw_grid_block(board, dis, x, y, set_value):
    if set_value == 0:
        pg.draw.rect(dis, _WHITE, [x * grid_block_size, y * grid_block_size, grid_block_size, grid_block_size])
        board.kill_cell(x, y)
    elif set_value == 1:
        pg.draw.rect(dis, _BLACK, [x * grid_block_size, y * grid_block_size, grid_block_size, grid_block_size])
        board.wake_up_cell(x, y)
    pg.display.flip()
