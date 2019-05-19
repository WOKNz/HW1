import Geometry
from Heap import hs as hs


def grscan(pnt_list):
    pnts = hs(pnt_list, 0, 0)  # Sorting list of Point2D by x

    pnts2 = pnts.copy()
    upper = [pnts[0], pnts[1]]  # Initial 2 points
    for i in range(2, len(pnts)):  # Adding and checking points for rotation
        if pnts[i].y >= pnts[0].y:
            upper.append((pnts[i]))
            ccw_list(upper, len(upper)-1)

    pnts2.reverse()  # Reversing the list to run on lower part
    lower = [pnts2[0], pnts2[1]]  # Initial 2 points
    for i in range(2, len(pnts2)):  # Adding and checking points for rotation
        if pnts2[i].y <= pnts[0].y:
            lower.append((pnts2[i]))
            ccw_list(lower, len(lower)-1)
 
    del lower[0]  # Deleting duplicates
    del lower[len(lower)-1]  # Deleting duplicates
    l = upper + lower  # Merging lists
    return l  # Return list of convex hull points


def isccw(a, b, c):  # Rotation check with pyramid volume sign (determinant)
    if ((b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)) > 0:
        return True


def ccw_list(list_points, index):  # Recursive check of rotation
    if index < 2 or len(list_points) < 3:  # Stop case of Index or Size
        return
    if isccw(list_points[index - 2], list_points[index -1], list_points[index]):
        del list_points[index - 1]  # deleting if ccw
    ccw_list(list_points, index - 1)  # recursive call with index moving
