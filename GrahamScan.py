import Geometry
from Heap import hs as hs


def grscan(pnt_list):
    pnts = hs(pnt_list, 0, 0)

    pnts2 = pnts.copy()
    upper = [pnts[0], pnts[1]]
    for i in range(2, len(pnts)):
        if pnts[i].y >= pnts[0].y:
            upper.append((pnts[i]))
            ccw_list(upper, len(upper)-1)

    pnts2.reverse()
    lower = [pnts2[0], pnts2[1]]
    for i in range(2, len(pnts2)):
        if pnts2[i].y <= pnts[0].y:
            lower.append((pnts2[i]))
            ccw_list(lower, len(lower)-1)
 
    del lower[0]
    del lower[len(lower)-1]
    l = upper + lower
    return l


def isccw(a, b, c):
    if ((b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)) > 0:
        return True


def ccw_list(list_points, index):
    if index < 2 or len(list_points) < 3:
        return
    if isccw(list_points[index - 2], list_points[index -1], list_points[index]):
        del list_points[index - 1]
    ccw_list(list_points, index - 1)