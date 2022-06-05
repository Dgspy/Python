# Roots of a quadratic equation
import math
def quadraticequation(a, b, c):
    try:
        assert a != 0, "Not a quadratic equation as coefficient of x ^ 2 can't be 0"
        D = (b * b - 4 * a*c)
        assert D>= 0, "Roots are imaginary"
        r1 = (-b + math.sqrt(D))/(2 * a)
        r2 = (-b - math.sqrt(D))/(2 * a)
        print("Roots of the quadratic equation are :", r1, "", r2)
    except AssertionError as msg:
        print(msg)
quadraticequation(-1, 5, -6)
quadraticequation(1, 1, 6)
quadraticequation(2, 12, 18)