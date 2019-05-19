import matplotlib.pyplot as plt
from Heap import hs as hs
import Geometry
from GrahamScan import grscan as gr

if __name__ == '__main__':
    file = open("Points.txt", "r")
    pnt_list = []
    for i, row in enumerate(file):
        if i == 0:
            continue
        a, b, c = row.split()
        pnt_list.append(Geometry.Point2D(int(a), int(b), int(c)))

    convex = gr(pnt_list)
    x_cnvx = []
    y_cnvx = []
    x_pnt = []
    y_pnt = []
    for point in convex:
        x_cnvx.append(point.x)
        y_cnvx.append(point.y)
    for point in pnt_list:
        x_pnt.append(point.x)
        y_pnt.append(point.y)

    plt.fill(x_cnvx, y_cnvx, edgecolor='b', fill=False)
    plt.plot(x_pnt, y_pnt, 'ro')
    plt.axis(
        [min(x_cnvx) - abs(max(x_cnvx)) // 10, max(x_cnvx) + max(x_cnvx) // 10, min(y_cnvx) - abs(max(y_cnvx)) // 10,
         max(y_cnvx) + max(y_cnvx) // 10])
    plt.show()


