from initial import scalar_multiply, Point

def encode_message(msg, G):
    msg = msg.upper()

    lookup = {}
    result = []

    for c in msg:
        if c == ' ':
            result.append(Point(None, None, G.curve))  # ← FIX
            continue

        val = ord(c) - 64

        if val not in lookup:
            lookup[val] = scalar_multiply(val, G)

        result.append(lookup[val])

    return result

def decode_message(points, G):
    lookup = {}

    for i in range(1, 27):
        P = scalar_multiply(i, G)
        lookup[(P.x, P.y)] = chr(i + 64)

    result = ""

    for P in points:
        if P.isInf():
            result += " "
        else:
            result += lookup.get((P.x, P.y), '?')

    return result