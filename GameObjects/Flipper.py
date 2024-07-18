import pygame

from Utility.Settings import *
from GameObjects.PhysicsObject import PhysicsObject
from Core.Polygon import Polygon


class Flipper(PhysicsObject):
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.poly = Polygon(x, y, 100, 20)

        self._angle = 0
        self.color = (255, 255, 255)

        self.active = True
        self.timer = pygame.time.get_ticks()

    # Getters

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_angle(self):
        return self._angle

    # Setters

    def set_x(self, x):
        self._x = x
        self.poly = Polygon(self.x, self.y, self.width, self.height)

    def set_y(self, y):
        self._y = y
        self.poly = Polygon(self.x, self.y, self.width, self.height)

    def set_width(self, width):
        self._width = width
        self.poly = Polygon(self.x, self.y, self.width, self.height)

    def set_height(self, height):
        self._height = height
        self.poly = Polygon(self.x, self.y, self.width, self.height)

    def set_angle(self, angle):
        self._angle = angle
        self.poly.rotate(self.angle)

    # Deleters

    def del_x(self):
        del self._x

    def del_y(self):
        del self._y

    def del_width(self):
        del self._width

    def del_height(self):
        del self._height

    def del_angle(self):
        del self._angle

    # Properties

    x = property(get_x, set_x, del_x)
    y = property(get_y, set_y, del_y)
    width = property(get_width, set_width, del_width)
    height = property(get_height, set_height, del_height)
    angle = property(get_angle, set_angle, del_angle)

    def draw(self, screen):
        self.poly.draw(screen)

    def rotate(self, angle, speed):
        pass

    def debounce(self):
        if pygame.time.get_ticks() - self.timer > 100:
            self.active = True
            self.timer = pygame.time.get_ticks()
        else:
            self.active = False
        return self.active

    def input(self):
        self.debounce()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle = -0.01
        if keys[pygame.K_RIGHT]:
            self.angle = 0.01


    def update(self, delta_time):
        self.input()

