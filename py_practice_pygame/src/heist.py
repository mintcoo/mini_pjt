import pygame


class Heist:

    falling_speed = 10
    is_dead = False

    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.size = image.get_rect()

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def on_collision_bottom(self):
        self.is_dead = True
        print("바닥과 충돌함")
