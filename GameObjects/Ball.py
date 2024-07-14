from GameObjects.PhysicsObject import PhysicsObject
from Utility.Settings import *

class Ball(PhysicsObject):
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.radius = 10
        self.color = (255, 255, 255)
        self.gravity = 0.7
        self.speed_vector = [0, 0]
        self.bounce = 0.85

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def del_x(self):
        del self._x

    def del_y(self):
        del self._y

    x = property(get_x, set_x, del_x)
    y = property(get_y, set_y, del_y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def screen_collision(self):
        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.speed_vector[0] *= -1
        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.speed_vector[1] *= -1
            self.speed_vector[1] *= self.bounce
            self.speed_vector[0] *= self.bounce
            self.y = max(0, min(self.y, SCREEN_HEIGHT))
            self.x = max(0, min(self.x, SCREEN_WIDTH))

    def physics(self, delta_time):
        self.speed_vector[1] += self.gravity * delta_time
        self.x += self.speed_vector[0]
        self.y += self.speed_vector[1]

        self.screen_collision()

    def update(self, delta_time):
        self.physics(delta_time)
