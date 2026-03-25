import sympy as sp
from core.helpers import clean_input

x = sp.symbols('x')

def solve_expression(expr: str) -> str:
    try:
        expr = clean_input(expr)

        # Convert trig to degrees
        expr = convert_trig(expr)

        if "=" in expr:
            left, right = expr.split("=")
            eq = sp.Eq(sp.sympify(left), sp.sympify(right))
            sol = sp.solve(eq, x)
            return f"x = {sol}"

        result = sp.sympify(expr)
        return str(result.evalf())

    except Exception as e:
        return f"Error: {e}"


def convert_trig(expr: str) -> str:
    """
    Converts sin(30) → sin(30*pi/180)
    """
    import re

    def repl(match):
        func = match.group(1)
        angle = match.group(2)
        return f"{func}(({angle})*pi/180)"

    pattern = r"(sin|cos|tan)\(([^)]+)\)"
    return re.sub(pattern, repl, expr)