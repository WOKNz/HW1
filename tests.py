import Geometry

if __name__ == '__main__':
    # # Testing vertical line
    # p1 = Geometry.Point2D(0, 1, 4)
    # p2 = Geometry.Point2D(1, 1, 5)
    # line1 = Geometry.LineSegment(0, p1, p2)
    # print(line1.a)
    # print(line1.b)
    # print(line1.c)
    #
    # # Testing vertical line pnt1 above pnt2
    # p3 = Geometry.Point2D(0, 1, 6)
    # p4 = Geometry.Point2D(1, 1, 5)
    # line1 = Geometry.LineSegment(0, p1, p2)
    # print(line1.a)
    # print(line1.b)
    # print(line1.c)
    #
    # # Testing horizontal line pnt1 before pnt2
    # p1 = Geometry.Point2D(0, 1, 5)
    # p2 = Geometry.Point2D(1, 3, 5)
    # line1 = Geometry.LineSegment(0, p1, p2)
    # print(line1.a)
    # print(line1.b)
    # print(line1.c)
    #
    # # Testing horizontal line pnt1 after pnt2
    # p1 = Geometry.Point2D(0, 4, 5)
    # p2 = Geometry.Point2D(1, 3, 5)
    # line1 = Geometry.LineSegment(0, p1, p2)
    # print(line1.a)
    # print(line1.b)
    # print(line1.c)

    p1 = Geometry.Point2D(0, 1, 1)
    p2 = Geometry.Point2D(1, 5, 5)
    line1 = Geometry.LineSegment(0, p1, p2)
    print(line1.a)
    print(line1.b)
    print(line1.c)
    # print(line1.f(0))
