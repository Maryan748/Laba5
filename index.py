import math

def required_terms(epsilon):
    n = 1
    pi_approx = 0
    while True:
        term = ((-1) ** (n + 1)) * (4 / (2 * n - 1))
        pi_approx += term
        if abs(math.pi - pi_approx) < epsilon:
            break
        n += 1
    return n

epsilon = 0.0001
n = required_terms(epsilon)
print(n)
