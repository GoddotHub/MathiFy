import math
from core.constants import PI, E

def clean_input(expr: str) -> str:
    """Remove unnecessary spaces and normalize symbols."""
    return expr.replace(" ", "").replace("π", "pi").replace("√", "sqrt")

def is_number(s: str) -> bool:
    """Check if string can be converted to float."""
    try:
        float(s)
        return True
    except ValueError:
        return False

def clean_input(expr: str) -> str:
    expr = expr.replace("π", str(math.pi))
    expr = expr.replace("e", str(math.e))
    expr = expr.replace("^", "**")
    return expr