# controllers/app_controller.py

from core.sympy_solver import solve_expression as sympy_solve
from core.parser import solve_equation_auto
from core.helpers import clean_input
from core.step_solver import get_solution_steps


class AppController:
    """Handles math solving logic for the Mathify app (v2)."""

    def solve_expression(self, expression: str) -> str:
        """
        Solve a math expression or equation using Sympy first,
        then fallback to custom parser if needed.
        """

        expression = expression.strip()

        if not expression:
            return "No expression provided"

        try:
            # Step 1: Clean input
            cleaned_expr = clean_input(expression)

            # Step 2: Try Sympy (powerful engine)
            result = sympy_solve(cleaned_expr)

            # If Sympy gives a valid result, return it
            if result and not str(result).startswith("Error"):
                return str(result)

            # Step 3: Fallback to your parser (safety backup)
            fallback_result = solve_equation_auto(expression)
            return str(fallback_result)

        except Exception as e:
            return f"Error: {e}"

    def get_steps(self, expression: str):
        return get_solution_steps(expression)