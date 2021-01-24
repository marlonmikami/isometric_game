import pygame

import assets
import colors
import config
import screen

# Initialize pygame
pygame.init()

WIN = pygame.display.set_mode((config.width, config.height))
MAP = open('Maps/map1.txt')
LINES = MAP.readlines()
pygame.display.set_caption("Mouse test")
previous_positions = []
tiles = []
tiles2 = []
cells = []

tile = assets.tile_short

position = (2, 2)

myfont = pygame.font.SysFont('Consolas', 16)

padding_x = 350
padding_y = 0

pos_x = 0
pos_y = 0


# Main game logic
def main():
    global pos_x
    global pos_y
    global tile

    WIN.fill(colors.black)

    key_down_pressed = False
    key_up_pressed = False
    key_right_pressed = False
    key_left_pressed = False

    clock = pygame.time.Clock()
    # pygame.mouse.set_visible(False)
    pygame.font.init()

    sphere = assets.sphere
    sphere.set_colorkey(colors.black)
    sphere.set_alpha(255)
    # crosshair = assets.crosshair
    # text_cell_surface = myfont.render("", False, (0, 0, 0))

    # background_color = (50, 50, 50)

    define_tiles_positions()

    tile.set_colorkey(colors.black)
    tile.set_alpha(255)

    # Make the buffers that are used several times
    buffer_scanlines = draw_scanlines()

    buffer_full_map = draw_tile_grid()
    buffer_visible_map = pygame.Surface((config.game_area_width, config.game_area_height))
    buffer_visible_map.blit(buffer_full_map, (0, 0), (pos_x, pos_y, config.game_area_width, config.game_area_height))

    buffer_play_area = pygame.Surface((config.game_area_width, config.game_area_height))

    buffer_full_screen = pygame.Surface((config.width, config.height))

    run = True
    while run:
        clock.tick(config.fps)

        buffer_full_screen.fill(colors.black)
        # Load the map
        buffer_visible_map.blit(buffer_full_map, (0, 0), (pos_x, pos_y, config.game_area_width, config.game_area_height))
        buffer_visible_map = assets.pallet_swap(buffer_visible_map, colors.magenta, screen.get_color())
        buffer_play_area.blit(buffer_visible_map, (0, 0))

        # Load the sprites
        buffer_play_area.blit(sphere, (200 - 16, 250 - 16))
        text_surface = myfont.render("FPS: % s" % clock.get_fps(), False, (255, 255, 255))
        buffer_full_screen.blit(buffer_play_area, (50, 50))

        # Post Processing
        buffer_full_screen.blit(buffer_scanlines, (0, 0))
        buffer_full_screen.blit(text_surface, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    key_up_pressed = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    key_down_pressed = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    key_right_pressed = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    key_left_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    key_up_pressed = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    key_down_pressed = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    key_right_pressed = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    key_left_pressed = False

        if key_up_pressed:
            pos_y -= 1
            pos_x += 2
        if key_down_pressed:
            pos_y += 1
            pos_x -= 2
        if key_right_pressed:
            pos_x += 2
            pos_y += 1
        if key_left_pressed:
            pos_x -= 2
            pos_y -= 1

        # Prints the crosshair and it's trail
        pos = pygame.mouse.get_pos()
        if config.mouse_trail_size > 0:
            draw_crosshair_trail(buffer_full_screen, assets.crosshair, pos)
        buffer_full_screen.blit(assets.crosshair, pos)

        # Update the window
        WIN.blit(buffer_full_screen, (0, 0))

        pygame.display.update()
    pygame.quit()


def draw_scanlines():
    buffer = pygame.Surface((config.width, config.height))
    buffer.fill((255, 255, 255))
    for i in range(config.height):
        if i % 2 > 0:
            pygame.draw.line(buffer, (0, 0, 0), (0, i), (1000, i))
    buffer.set_colorkey((255, 255, 255))
    buffer.set_alpha(30)
    return buffer


def draw_crosshair_trail(buffer, crosshair, pos):
    alpha_multiplier = 100 / config.mouse_trail_size
    for i in range(0, len(previous_positions)):
        crosshair.set_alpha((i + 1) * alpha_multiplier)
        buffer.blit(crosshair, previous_positions[i])

    previous_positions.append(pos)
    if len(previous_positions) > config.mouse_trail_size:
        previous_positions.pop(0)
    crosshair.set_alpha(255)


def define_tiles_positions():
    file_lines = LINES.copy()
    line_count = 0
    for line in file_lines:
        line_count += 1
        char_count = 0
        for element in line[::-1]:
            char_count += 1
            if element != "." and element != "\n":
                pos_x = (padding_x + (line_count * 16) - (char_count * 16))
                pos_y = (padding_y + (char_count * 8) + (line_count * 8))
                tiles.append((pos_x, pos_y, element))
                if element == "1":
                    pos_y = (padding_y + (char_count * 8) + (line_count * 8) - 16)
                    tiles2.append((pos_x, pos_y, element))


def draw_tile_grid():
    buffer = pygame.Surface((1500, 1500))
    for i in range(len(tiles)):
        buffer.blit(tile, (300 + tiles[i][0] + pos_x, tiles[i][1] + pos_y))
    for j in range(len(tiles2)):
        buffer.blit(tile, (300 + tiles2[j][0] + pos_x, tiles2[j][1] + pos_y))
    return buffer


# Starts the program
if __name__ == '__main__':
    main()
