"""Core calculator logic (no input/output here, so it is easy to test)."""

from __future__ import annotations

import math
from typing import Callable, Optional


class CalculatorError(Exception):
    """Raised for any calculator-specific error."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise CalculatorError("Division by zero is not allowed.")
    return a / b


def power(a: float, b: float) -> float:
    try:
        result = a ** b
    except OverflowError:
        raise CalculatorError("The result of the power operation is too large.")
    except ZeroDivisionError:
        raise CalculatorError("Zero raised to a negative power is undefined.")
    if isinstance(result, complex):
        raise CalculatorError("The result is a complex number, which is not supported.")
    return result


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise CalculatorError("Modulo by zero is undefined.")
    return a % b


def sqrt(a: float, _: Optional[float] = None) -> float:
    if a < 0:
        raise CalculatorError(
            "Square root of a negative number is undefined for real numbers."
        )
    return math.sqrt(a)


# operator -> (function, number of operands)
OPERATIONS: dict[str, tuple[Callable[..., float], int]] = {
    "+": (add, 2),
    "-": (subtract, 2),
    "*": (multiply, 2),
    "/": (divide, 2),
    "**": (power, 2),
    "%": (modulo, 2),
    "sqrt": (sqrt, 1),
}


def calculate(op: str, a: float, b: Optional[float] = None) -> float:
    """Run an operation and return the result, or raise CalculatorError."""
    if op not in OPERATIONS:
        raise CalculatorError(f"Invalid operator: {op!r}")

    func, arity = OPERATIONS[op]
    if arity == 2 and b is None:
        raise CalculatorError(f"Operator {op!r} needs two numbers.")

    try:
        return func(a, b)
    except CalculatorError:
        raise
    except OverflowError:
        raise CalculatorError("The result is too large to represent.")
    except Exception as e:  # any other unexpected error
        raise CalculatorError(f"Unexpected error: {e}")


def format_result(value: float) -> str:
    """Show whole numbers without a decimal part."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)
