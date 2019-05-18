import Geometry
import QuickSort
import Heap
import random

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


# # Testing regular heapsort
# mylist = [24, 6, 73, 8, 42, 82, 76, 23, 8, 65, 98, 96, 88, 98, 95, 76, 66, 86, 21, 87]
# mylist = []
# for i in range(0, 20):
#     mylist.append(random.randint(1, 100))
# a = Heap.Heap(mylist, "max")
#
# print(str(a.heap[0:len(a.heap)]))
#
# k = []
# while len(a.heap) > 0:
#     k.append(a.pull())
#
# print(str(k[0:len(k)]))

# # Testing object's atribute heapsort
# mylist = []
# for i in range(0, 10):
#     x = random.randint(1, 10)
#     y = random.randint(1, 10)
#     mylist.append(Geometry.Point2D(i, x, y))
#
# for point in mylist:
#     print("P", point.id + 1, "(", point.x, ",", point.y, ") ")
# print("---")
#
# a = Heap.Heap(mylist, "min", key=lambda point: point.x)
# sorted_a = a.sort(key=lambda point: point.x)
# for point in sorted_a:
#     print("P", point.id + 1, "(", point.x, ",", point.y, ") ")
# print("---")
