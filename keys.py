import random
from initial import scalar_multiply

def generate_keys(G):
    d = random.randint(1, G.curve.p - 1)
    Q = scalar_multiply(d, G)
    return d, Q