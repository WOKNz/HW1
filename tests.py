import Geometry
import QuickSort


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

# p1 = Geometry.Point2D(0, 1, 1)
# p2 = Geometry.Point2D(1, 5, 5)
# line1 = Geometry.LineSegment(0, p1, p2)
# print(line1.a)
# print(line1.b)
# print(line1.c)
# print(line1.f(0))


# # Testing regular QuickSort Implementation (without lambda)
# mylist = [6, 7, 8, 4, 6, 6, 5, 3, 6, 2, 4, 2, 5, 7, 7, 5, 3, 2, 1, 4, 8, 9, 7, 7, 8, 2]
# for i in range(0,26):
#     x = random.randint(1,10)
#     mylist.append(x)

# print(mylist)
# QuickSort.quick_sort(mylist)
# print(mylist)


# #Testing QuickSort, sort on x then on y attributes of Point2D
# mylist = []
# for i in range(0, 3):
#     x = random.randint(1, 10)
#     y = random.randint(1, 10)
#     mylist.append(Geometry.Point2D(i, x, y))
#
# for point in mylist:
#     print("P", point.id + 1, "(", point.x, ",", point.y, ") ")
# print("---")
#
# QuickSort.quick_sort(mylist, key=lambda point: point.x)
# for point in mylist:
#     print("P", point.id + 1, "(", point.x, ",", point.y, ") ")
# print("---")
#
# QuickSort.quick_sort(mylist, key=lambda point: point.y)
# for point in mylist:
#     print("P", point.id + 1, "(", point.x, ",", point.y, ") ")
