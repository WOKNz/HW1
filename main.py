import Geometry
import QuickSort
import random


# if __name__ == '__main__':
#     # Testing parallel line vertical pnt1 below pnt2
#     p1 = Geometry.Point2D(0, 1, 4)
#     p2 = Geometry.Point2D(1, 1, 5)
#     line1 = Geometry.LineSegment(0, p1, p2)
#     print(line1.a)
#     print(line1.b)
#     print(line1.c)


mylist = [6, 7, 8, 4, 6, 6, 5, 3, 6, 2, 4, 2, 5, 7, 7, 5, 3, 2, 1, 4, 8, 9, 7, 7, 8, 2]

# for i in range(0,26):
#     x = random.randint(1,10)
#     mylist.append(x)

print(mylist)
QuickSort.quick_sort(mylist)
print(mylist)
