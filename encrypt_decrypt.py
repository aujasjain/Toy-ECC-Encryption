import random
from initial import scalar_multiply, point_add, point_neg
from conversion import encode_message, decode_message

def point_order(G):
    P = G
    count = 1

    while not P.isInf():
        P = point_add(P, G)
        count += 1

    return count

def encrypt(msg, G, Q):
    encoded = encode_message(msg, G)
    ciphertext = []

    order = point_order(G)

    for M in encoded:
        # pick k PER CHARACTER
        k = random.randint(1, order - 1)

        C1 = scalar_multiply(k, G)
        kQ = scalar_multiply(k, Q)

        C2 = point_add(M, kQ)

        ciphertext.append((C1, C2))

    return ciphertext

def decrypt(ciphertext, d, G):
    decoded_points = []

    for C1, C2 in ciphertext:
        dC1 = scalar_multiply(d, C1)
        neg = point_neg(dC1)

        M = point_add(C2, neg)
        decoded_points.append(M)

    return decode_message(decoded_points, G)