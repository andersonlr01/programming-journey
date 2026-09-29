from __future__ import annotations

import math

from calculator import OPERATIONS, CalculatorError, calculate, format_result


def read_number(prompt: str) -> float:
    """Ask the user for a number until a valid one is entered."""
    while True:
        raw = input(prompt).strip().replace(",", "")
        try:
            value = float(raw)
        except ValueError:
            print("Error: please enter a valid number.")
            continue
        if math.isnan(value) or math.isinf(value):
            print("Error: 'nan' and 'inf' are not allowed.")
            continue
        return value


def read_operator() -> str:
    """Ask the user for a valid operator."""
    while True:
        op = input(f"Operator ({' '.join(OPERATIONS)}): ").strip().lower()
        if op in OPERATIONS:
            return op
        print("Error: invalid operator.")


def calculate_once() -> None:
    op = read_operator()
    _, arity = OPERATIONS[op]

    a = read_number("First number: ")
    b = read_number("Second number: ") if arity == 2 else None

    try:
        result = calculate(op, a, b)
    except CalculatorError as e:
        print(f"Error: {e}")
    else:
        print(f"Result: {format_result(result)}")


def main() -> None:
    print("=== Calculator ===")
    print("Press Ctrl+C at any time, or answer 'n' when asked to continue, to quit.\n")

    while True:
        try:
            calculate_once()
            again = input("\nNew calculation? (y/n): ").strip().lower()
            if again not in ("y", "yes", ""):
                break
            print()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()
