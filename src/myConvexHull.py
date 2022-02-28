import math
import numpy as np
import matplotlib.pyplot as plt

def myConvexHull(bucket):
    p_l, p_r = min_max_X(bucket)

    leftPart    = myConvexHullPart(p_l, p_r, bucket, True)
    rightPart   = myConvexHullPart(p_l, p_r, bucket, False)

    return np.unique(leftPart + rightPart, axis = 0)

def myConvexHullPart(p_l, p_r, points, is_left):
    pointsLeft, pointsRight = filterPart(p_l, p_r, points)

    if(is_left):
        pointsPart = pointsLeft
    else:
        pointsPart = pointsRight

    if(pointsPart.size == 0): 
        return [[p_l, p_r]]
    else:
        p_x = maxDistPointLine(p_l, p_r, pointsPart)
        firstPart   = myConvexHullPart(p_l, p_x, pointsPart, is_left) 
        secondPart  = myConvexHullPart(p_x, p_r, pointsPart, is_left)
        return firstPart + secondPart

def maxDistPointLine(p_l, p_r, points):
    maxPoint = points[0]
    maxDist, maxTheta = PLdist(p_l, p_r, maxPoint)
    for point in points:
        tmpDist, tmpTheta = PLdist(p_l, p_r, point)
        if (tmpDist > maxDist or (tmpDist == maxDist and tmpTheta > maxTheta)):
            maxTheta = tmpTheta
            maxDist = tmpDist
            maxPoint = point

    return maxPoint

def PLdist(p_l, p_r, p_x):

    v1 = [p_r[0] - p_l[0], p_r[1] - p_l[1]]
    v1_len = pythDist(v1)

    v2 = [p_x[0] - p_l[0], p_x[1] - p_l[1]]
    v2_len = pythDist(v2)

    theta = math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (v1_len * v2_len))

    return abs(v2_len * math.sin(theta)), abs(theta)

def pythDist(v):
    return (v[0] ** 2 + v[1] ** 2) ** 0.5

def min_max_X(bucket):
    minPoint = bucket[0]
    maxPoint = bucket[0]

    for point in bucket:
        if point[0] > maxPoint[0]:
            maxPoint = point
        if point[0] < minPoint[0]:
            minPoint = point

    return minPoint, maxPoint

def LRPoint(p_l, p_r, p_x):

    x1, y1 = p_l[0], p_l[1]
    x2, y2 = p_r[0], p_r[1]
    x3, y3 = p_x[0], p_x[1]

    return x1 * y2 + x3 * y1 + x2 * y3 - x3 * y2 - x2 * y1 - x1 * y3

def filterPart(p_l, p_r, bucket):

    pointsLeft  = []
    pointsRight = []

    for point in bucket:
        det = LRPoint(p_l, p_r, point)
        is_zero = math.isclose(det, 0, abs_tol=1e-5)
        if (det > 0 and not is_zero):
            pointsLeft += [point]
        elif (det < 0 and not is_zero):
            pointsRight += [point]

    return np.array(pointsLeft), np.array(pointsRight)

if __name__ == "__main__":
    arr = np.array([
        [4.7, 3.2],
        [4.6, 3.1],
        [4.6, 3.4],
        [4.8, 3.4],
        [4.6, 3.6],
        [4.8, 3.4],
        [4.7, 3.2],
        [4.9, 3.6],
        [4.6, 3.2]
    ])

    hull = myConvexHull(arr)
    plt.scatter(arr[:, 0], arr[:, 1])
    for simpul in hull:
        x = [simpul[0][0], simpul[1][0]]
        y = [simpul[0][1], simpul[1][1]]
        plt.plot(x, y, "b")

    plt.show()
