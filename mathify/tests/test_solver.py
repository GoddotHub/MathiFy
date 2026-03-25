# tests/test_solver.py

import cmath
from core.math_solver import solve_linear, solve_quadratic
from core.parser import solve_equation_auto


# ---------------- Helper Functions ----------------

def is_close_complex(a, b, tol=1e-9):
    """Check if two complex numbers are almost equal."""
    return abs(a.real - b.real) < tol and abs(a.imag - b.imag) < tol


def parse_quadratic_result(result_str):
    """
    Convert a string like 'x1 = (2+0j), x2 = (1+0j)' or 'x1 = 1j, x2 = -1j' into a tuple of complex numbers.
    Handles both real, repeated, and complex roots.
    """
    result_str = result_str.replace(" ", "")  # remove spaces
    if "x=" in result_str:  # repeated root like 'x = -1.0'
        val = result_str.split('=')[1]
        return (complex(val),)

    parts = result_str.split(',')
    roots = []
    for p in parts:
        val_str = p.split('=')[1]
        # remove surrounding parentheses if exist
        val_str = val_str.strip('()')
        # convert to complex
        roots.append(complex(val_str))
    return tuple(roots)


# ---------------- Test Functions ----------------

def test_linear():
    print("Testing linear solver...")
    assert solve_linear(2, -4) == "x = 2.0"
    assert solve_linear(0, 0) == "Infinite solutions"
    assert solve_linear(0, 5) == "No solution"
    print("✅ Linear tests passed")


def test_quadratic():
    print("Testing quadratic solver...")

    # Real roots
    roots = parse_quadratic_result(solve_quadratic(1, -3, 2))
    expected = (2 + 0j, 1 + 0j)
    roots_sorted = sorted(roots, key=lambda z: (z.real, z.imag))
    expected_sorted = sorted(expected, key=lambda z: (z.real, z.imag))
    for r, e in zip(roots_sorted, expected_sorted):
        assert is_close_complex(r, e), f"Mismatch: got {r}, expected {e}"
    print("✅ Real roots test passed")

    # Repeated root
    result = solve_quadratic(1, 2, 1)
    assert result == "x = -1.0", f"Expected repeated root -1.0, got {result}"
    print("✅ Repeated root test passed")

    # Complex roots
    roots = parse_quadratic_result(solve_quadratic(1, 0, 1))
    expected = (1j, -1j)
    roots_sorted = sorted(roots, key=lambda z: (z.real, z.imag))
    expected_sorted = sorted(expected, key=lambda z: (z.real, z.imag))
    for r, e in zip(roots_sorted, expected_sorted):
        assert is_close_complex(r, e), f"Mismatch: got {r}, expected {e}"
    print("✅ Complex roots test passed")
    print("All quadratic tests completed.")


def test_parser_auto():
    print("Testing parser auto...")

    # Linear equations
    result = solve_equation_auto("2x+4=0")
    assert result == "x = -2.0", f"Expected -2.0, got {result}"

    result = solve_equation_auto("x-5=0")
    assert result == "x = 5.0", f"Expected 5.0, got {result}"

    # Quadratic equations
    roots = parse_quadratic_result(solve_equation_auto("x^2-5x+6=0"))
    expected = (3 + 0j, 2 + 0j)
    roots_sorted = sorted(roots, key=lambda z: (z.real, z.imag))
    expected_sorted = sorted(expected, key=lambda z: (z.real, z.imag))
    for r, e in zip(roots_sorted, expected_sorted):
        assert is_close_complex(r, e), f"Mismatch: got {r}, expected {e}"

    result = solve_equation_auto("x^2+2x+1=0")
    assert result == "x = -1.0", f"Expected -1.0, got {result}"

    # parser auto test for x^2 + 1 = 0
    roots = parse_quadratic_result(solve_equation_auto("x^2+1=0"))
    expected = (1j, -1j)  # correct complex roots
    roots_sorted = sorted(roots, key=lambda z: (z.real, z.imag))
    expected_sorted = sorted(expected, key=lambda z: (z.real, z.imag))
    for r, e in zip(roots_sorted, expected_sorted):
        assert is_close_complex(r, e), f"Mismatch: got {r}, expected {e}"
    print("✅ x^2 + 1=0 test passed")

    roots = parse_quadratic_result(solve_equation_auto("x^2+1=0"))
    expected = (1j, -1j)
    roots_sorted = sorted(roots, key=lambda z: (z.real, z.imag))
    expected_sorted = sorted(expected, key=lambda z: (z.real, z.imag))
    for r, e in zip(roots_sorted, expected_sorted):
        assert is_close_complex(r, e), f"Mismatch: got {r}, expected {e}"

    print("✅ All parser auto tests passed")


# ---------------- Main ----------------
if __name__ == "__main__":
    test_linear()
    test_quadratic()
    test_parser_auto()
    print("🎉 All tests passed successfully!")