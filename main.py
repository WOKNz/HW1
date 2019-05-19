import matplotlib.pyplot as plt
from Heap import hs as hs
import Geometry
from GrahamScan import grscan as gr

if __name__ == '__main__':
    file = open("Points.txt", "r")  # Opening txt file
    pnt_list = []
    for i, row in enumerate(file):  # Creating list of Point2D for txt file
        if i == 0:
            continue
        a, b, c = row.split()
        pnt_list.append(Geometry.Point2D(int(a), int(b), int(c)))

    convex = gr(pnt_list)  # Receiving convex hull list of Point2D
    x_cnvx = []
    y_cnvx = []
    x_pnt = []
    y_pnt = []
    for point in convex:  # Separating convex list to x,y lists
        x_cnvx.append(point.x)
        y_cnvx.append(point.y)
    for point in pnt_list:  # Separating original input list to x,y lists
        x_pnt.append(point.x)
        y_pnt.append(point.y)

    plt.fill(x_cnvx, y_cnvx, edgecolor='b', fill=False)  # Plotting Convex hull
    plt.plot(x_pnt, y_pnt, 'ro')  # Plotting original points
    plt.axis(
        [min(x_cnvx) - abs(max(x_cnvx)) // 10, max(x_cnvx) + max(x_cnvx) // 10, min(y_cnvx) - abs(max(y_cnvx)) // 10,
         max(y_cnvx) + max(y_cnvx) // 10])  # Increasing plot gaps by 10%
    plt.show()


