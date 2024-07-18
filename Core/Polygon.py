from Utility.Settings import *

class Polygon:
    @dispatch(list)
    def __init__(self, points):
        self.points = points
        self._color = (255, 255, 255)

        self.calculate_rotate_point()

    @dispatch(int, int, int, int)
    def __init__(self, x, y, width, height):
        self.points = [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]
        self._color = (255, 255, 255)

        self.calculate_rotate_point()

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def del_color(self):
        del self._color

    color = property(get_color, set_color, del_color)

    def calculate_rotate_point(self):
        self.left_rotate_point = ((self.points[0][0] + self.points[3][0]) / 2,
                                  (self.points[0][1] + self.points[3][1]) / 2)

        self.right_rotate_point = ((self.points[1][0] + self.points[2][0]) / 2,
                                   (self.points[1][1] + self.points[2][1]) / 2)

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)

    def rotate(self, angle):
        for i in range(len(self.points)):
            x = self.points[i][0] - self.left_rotate_point[0]
            y = self.points[i][1] - self.left_rotate_point[1]

            new_x = x * math.cos(angle) - y * math.sin(angle)
            new_y = x * math.sin(angle) + y * math.cos(angle)

            self.points[i] = (new_x + self.left_rotate_point[0], new_y + self.left_rotate_point[1])

