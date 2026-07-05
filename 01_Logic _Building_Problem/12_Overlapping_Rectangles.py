# Given two rectangles, find if the given two rectangles overlap or not.
# Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates. 
# l1: Top Left coordinate of first rectangle. 
# r1: Bottom Right coordinate of first rectangle. 
# l2: Top Left coordinate of second rectangle. 
# r2: Bottom Right coordinate of second rectangle.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def overlap(l1, r1, l2, r2):

    # Rectangle 1 is left of Rectangle 2
    if r1.x < l2.x:
        return False

    # Rectangle 1 is right of Rectangle 2
    if l1.x > r2.x:
        return False

    # Rectangle 1 is above Rectangle 2
    if r1.y > l2.y:
        return False

    # Rectangle 1 is below Rectangle 2
    if l1.y < r2.y:
        return False

    return True


l1 = Point(0, 10)
r1 = Point(10, 0)

l2 = Point(5, 5)
r2 = Point(15, 0)

print(overlap(l1, r1, l2, r2))