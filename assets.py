import pygame
import os

cell = pygame.image.load(os.path.join("Assets", "cell.png"))
tile_flat = pygame.image.load(os.path.join("Assets", "tile_flat.png"))
tile_short = pygame.image.load(os.path.join("Assets", "tile_short.png"))
tile_long = pygame.image.load(os.path.join("Assets", "tile_long.png"))
# tile_long = pygame.transform.scale(tile_long, (32 * configuration.scale, 64 * configuration.scale))
sphere = pygame.image.load(os.path.join("Assets", "sphere.png"))

crosshair = pygame.image.load(os.path.join("Assets", "crosshair2.png"))

def pallet_swap(surface, old_color, new_color):
    image_copy = surface.copy()
    image_copy.fill(new_color)
    surface.set_colorkey(old_color)
    image_copy.blit(surface, (0, 0))
    return image_copy