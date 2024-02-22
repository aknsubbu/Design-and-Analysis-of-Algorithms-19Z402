import matplotlib.pyplot as plt

# Function to find the cross product of three points
def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

# Function to find the points on the convex hull using the divide and conquer algorithm
def convex_hull(points):
    def divide_and_conquer(points):
        if len(points) <= 3:
            return points
        
        # Sort the points by x-coordinate
        points.sort()
        
        # Divide the set of points into two halves
        left_half = divide_and_conquer(points[:len(points)//2])
        right_half = divide_and_conquer(points[len(points)//2:])
        
        return merge_convex_hulls(left_half, right_half)
    
    def merge_convex_hulls(left_half, right_half):
        def get_tangent(points1, points2, direction):
            start = points1[-1]
            while True:
                best_angle = None
                for point in points1:
                    while cross_product(start, point, points2[direction]) < 0:
                        direction = (direction + 1) % len(points2)
                    angle = cross_product(start, point, points2[direction])
                    if best_angle is None or angle < best_angle:
                        best_angle = angle
                        best_point = point
                if best_point == points1[-1]:
                    return best_point
                points1 = points1[:-1]
                start = best_point
            
        # Removed unused variables upper_tangent and lower_tangent
        get_tangent(left_half, right_half, 0)
        get_tangent(right_half, left_half, -1)
        
        return left_half + right_half[1:-1]
    
    return divide_and_conquer(points)

# Example usage:
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull_points = convex_hull(points)

# Plotting the points and convex hull
x, y = zip(*points)
hull_x, hull_y = zip(*convex_hull_points)
plt.plot(x, y, 'ro')
plt.plot(hull_x, hull_y, 'g-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Convex Hull using Divide and Conquer')
plt.show()