import math

def polar_angle(p0, p):
    dy = p[1] - p0[1]
    dx = p[0] - p0[0]
    return math.atan2(dy, dx)

def dist(p0, p):
    return math.sqrt((p[0] - p0[0])**2 + (p[1] - p0[1])**2)


def graham_scan(points:list)->list:
    p0=min(points,key=lambda p:(p[1],p[0]))
    points.sort(key=lambda p:(polar_angle(p0,p),dist(p0,p)))