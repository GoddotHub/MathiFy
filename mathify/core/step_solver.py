# core/step_solver.py

import sympy as sp

x = sp.symbols('x')


def get_solution_steps(expr: str):
    """
    Returns step-by-step solution (basic version)
    """
    steps = []

    try:
        if "=" not in expr:
            return ["Only equations supported for steps"]

        left, right = expr.split("=")

        eq = sp.Eq(sp.sympify(left), sp.sympify(right))

        steps.append(f"Start: {eq}")

        # Move everything to one side
        simplified = sp.simplify(left + "-(" + right + ")")
        steps.append(f"Simplify: {simplified} = 0")

        # Solve equation
        solution = sp.solve(eq, x)
        steps.append(f"Solve: x = {solution}")

        return steps

    except Exception as e:
        return [f"Error: {e}"]