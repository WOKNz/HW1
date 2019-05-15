class Point2D:
    def __init__(self, id_initial: int, x_initial: float, y_initial: float):
        """
        Class of Point object

        :param id_initial: ID of the point
        :type id_initial: int
        :param x_initial: Ordinate X of the point
        :type x_initial: double
        :param y_initial: Ordinate Y of the point
        :type y_initial: double
        """
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


class LineSegment:
    def __init__(self, id_initial: int, pnt1_initial: Point2D, pnt2_initial: Point2D):
        """
        LineSegment class that represent line segment constructed from
        two point

        :param id_initial: ID of the segment
        :type id_initial: int
        :param pnt1_initial: First point that construct the segment
        :type pnt1_initial: Point2D
        :param pnt2_initial: Second point that construct the segment
        :type pnt2_initial: Point2D
        """
        self.id = id_initial
        self.pnt1 = pnt1_initial
        self.pnt2 = pnt2_initial
        if self.pnt1.y - self.pnt2.y == 0:
            self.a = 0
            self.b = -1 / self.pnt1.y
            self.c = 1
        elif self.pnt1.x - self.pnt2.x == 0:
            self.a = 1
            self.b = 0
            self.c = -self.pnt1.x
        else:
            if self.pnt2.x > self.pnt1.x:
                self.a = (self.pnt2.y - self.pnt1.y) / (self.pnt2.x - self.pnt1.x)
                self.b = self.pnt1.y - self.a * self.pnt1.x
                self.c = -1
            else:
                self.a = (self.pnt1.y - self.pnt2.y) / (self.pnt1.x - self.pnt2.x)
                self.b = self.pnt1.y - self.a * self.pnt1.x
                self.c = -1

    def f(self, x_input):
        return (-(self.a * x_input) / self.b) - self.c

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def pnt1(self):
        return self._pnt1

    @pnt1.setter
    def pnt1(self, value):
        self._pnt1 = value

    @property
    def pnt2(self):
        return self._pnt2

    @pnt2.setter
    def pnt2(self, value):
        self._pnt2 = value

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
