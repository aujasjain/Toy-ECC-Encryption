class Curve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p


class Point:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    def isInf(self):
        return self.x is None

    def __repr__(self):
        if self.isInf():
            return "O"
        return f"({self.x}, {self.y})"


def mod_inv(a, p):
    return pow(a, -1, p)


def point_add(P, Q):
    curve = P.curve
    p = curve.p

    if P.isInf(): return Q
    if Q.isInf(): return P

    if P.x == Q.x and (P.y != Q.y or P.y == 0):
        return Point(None, None, curve)

    if P.x == Q.x:
        lam = (3 * P.x**2 + curve.a) * mod_inv(2 * P.y, p)
    else:
        lam = (Q.y - P.y) * mod_inv(Q.x - P.x, p)

    lam %= p

    x3 = (lam**2 - P.x - Q.x) % p
    y3 = (lam * (P.x - x3) - P.y) % p

    return Point(x3, y3, curve)


def scalar_multiply(k, P):
    if k < 0:
        return scalar_multiply(-k, point_neg(P))

    result = Point(None, None, P.curve)
    cur = P

    while k > 0:
        if k & 1:
            result = point_add(result, cur)
        cur = point_add(cur, cur)
        k >>= 1

    return result

    return result


def point_neg(P):
    if P.isInf():
        return P
    return Point(P.x, (-P.y) % P.curve.p, P.curve)
