import re
from core.math_solver import solve_linear, solve_quadratic

def solve_equation_auto(expr):
    expr = expr.replace(" ", "").replace("=0", "")

    # ================= QUADRATIC =================
    if "x^2" in expr or "x²" in expr:
        # Normalize x² → x^2
        expr = expr.replace("x²", "x^2")

        # Default coefficients
        a, b, c = 0, 0, 0

        # Extract a
        a_match = re.search(r'([+-]?\d*)x\^2', expr)
        if a_match:
            a_str = a_match.group(1)
            if a_str in ("", "+"):
                a = 1
            elif a_str == "-":
                a = -1
            else:
                a = float(a_str)

        # Extract b
        b_match = re.search(r'([+-]?\d*)x(?!\^)', expr)
        if b_match:
            b_str = b_match.group(1)
            if b_str in ("", "+"):
                b = 1
            elif b_str == "-":
                b = -1
            else:
                b = float(b_str)

        # Extract c (constant)
        c_match = re.findall(r'([+-]?\d+)(?![x^])', expr)
        if c_match:
            c = float(c_match[-1])

        return solve_quadratic(a, b, c)

    # ================= LINEAR =================
    elif "x" in expr:
        a, b = 0, 0

        a_match = re.search(r'([+-]?\d*)x', expr)
        if a_match:
            a_str = a_match.group(1)
            if a_str in ("", "+"):
                a = 1
            elif a_str == "-":
                a = -1
            else:
                a = float(a_str)

        b_match = re.findall(r'([+-]?\d+)(?!x)', expr)
        if b_match:
            b = float(b_match[-1])

        return solve_linear(a, b)

    else:
        return "Equation not recognized"