import math


class Point2D:
    def __init__(self, id_initial, x_initial, y_initial):
        self.id = id_initial
        self.x = x_initial
        self.y = y_initial

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
