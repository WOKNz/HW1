import math

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
