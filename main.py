from initial import Curve, Point
from keys import generate_keys
from encrypt_decrypt import encrypt, decrypt, point_order

def predefined_setup():
    p = 307
    a = 2
    b = 3

    curve = Curve(a, b, p)
    G = Point(3, 6, curve)

    print("\nUsing predefined curve:")
    print(f"y^2 = x^3 + {a}x + {b} mod {p}")
    print(f"G = {G}")
    print(f"Order of G = {point_order(G)}\n")

    return curve, G

def custom_setup():

    def is_on_curve(P):
        x, y = P.x, P.y
        c = P.curve
        return (y * y - (x * x * x + c.a * x + c.b)) % c.p == 0

    print("\nEnter curve parameters:")

    p = int(input("p (must be prime): "))
    a = int(input("a: "))
    b = int(input("b: "))

    curve = Curve(a, b, p)

    print("\nEnter base point G:")
    print("\nA small order of G (less than 26) is almost guaranteed to fail encryption!")

    x = int(input("G.x: "))
    y = int(input("G.y: "))

    G = Point(x, y, curve)

    if not is_on_curve(G):
        print("Point is not on the curve!")
        return

    print(f"\nOrder of G = {point_order(G)}\n")

    return curve, G


def main():
    print("1. Predefined curve (recommended)")
    print("2. Custom")

    choice = input("Choice: ")

    if choice == "1":
        curve, G = predefined_setup()
    else:
        curve, G = custom_setup()

    # Generate keys
    d, Q = generate_keys(G)

    print("Private key:", d)
    print("Public key:", Q)

    # Message
    msg = input("\nEnter message: ")

    cipher = encrypt(msg, G, Q)

    print("\nEncrypted:")
    for c1, c2 in cipher:
        print(f"{c1}, {c2}")

    decrypted = decrypt(cipher, d, G)

    print("\nDecrypted:")
    print(decrypted)

main()