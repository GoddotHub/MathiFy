import cmath

def solve_linear(a: float, b: float) -> str:
    """Solve linear equation a*x + b = 0."""
    if a == 0:
        return "Infinite solutions" if b == 0 else "No solution"
    x = -b / a
    return f"x = {x}"

def solve_quadratic(a: float, b: float, c: float) -> str:
    """Solve quadratic equation a*x^2 + b*x + c = 0."""
    if a == 0:
        return solve_linear(b, c)

    D = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)

    if D.real == 0 and D.imag == 0:
        return f"x = {x1.real}"
    return f"x1 = {x1}, x2 = {x2}"