# Elliptic Curve Encryption in Python

This project is a simple implementation of elliptic curve cryptography (ECC) in Python. It shows how messages can be encrypted and decrypted using points on a mathematical curve.

---

## What it does

* Defines an elliptic curve over a finite field (predefined or custom values, depending on user)
* Performs point addition and scalar multiplication
* Generates a public/private key pair
* Encodes text messages as points on the curve
* Encrypts each character using a random value
* Decrypts the message back to readable text

---

## How it works (basic idea)

1. A curve is defined using an equation of the form:

   y² = x³ + ax + b (mod p)

2. A base point `G` is chosen on the curve.

3. A private key `d` is randomly generated.

4. The public key `Q` is computed as:

   Q = d × G

5. Each character in the message is converted into a point on the curve.

6. For encryption:

   * A random number `k` is chosen
   * Two values are generated:

     * C1 = k × G
     * C2 = M + k × Q

7. For decryption:

   * The receiver uses their private key to recover the original point:

     * M = C2 - d × C1

8. The points are converted back into characters.

---

## Running the program
Just run main.py.

## Note
This is a just a project I made to understand and implement ECC, it is not secure for real applications at all. Small curves
are used, which are easy to break.

---
