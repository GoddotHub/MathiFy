from core.constants import SUPPORTED_OPERATORS, SUPPORTED_FUNCTIONS

def validate_expression(expr: str) -> bool:
    """Check if the expression contains only supported characters/functions."""
    for char in expr:
        if char.isalpha() and char not in SUPPORTED_FUNCTIONS:
            if char not in ("x", "y"):
                return False
    return True