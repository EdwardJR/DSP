

# NOTE: A simple integral calculator using midpoint

def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2)+i*h)
    result *= h
    return result
