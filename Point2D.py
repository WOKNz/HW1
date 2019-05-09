import math


class Point2D:

    def __init__(self, id_initial, x_initial, y_initial):
        self.id = id_initial
        self.x = x_initial
        self.y = y_initial

    @property
    def x(self):
        return self.x

    def y(self):
        return self.y

    @x.setter
    def x(self, x):
        self.x = x

    def y(self, y):
        self.y = y
