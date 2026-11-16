import math


def parse_order(text):
    """Parse 'garment:kg' (e.g. 'regular:6') into ('Regular', 6.0).

    Returns None for invalid input (non-string, wrong number of ':',
    empty garment, non-numeric / non-finite / non-positive weight).
    """
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    garment = parts[0].strip()
    if not garment:
        return None
    try:
        kg = float(parts[1].strip())
    except (ValueError, OverflowError):
        return None
    if not math.isfinite(kg) or kg <= 0:
        return None
    return garment.title(), kg


def weight_average(weights_csv):
    """Average of comma-separated whole-number weights (e.g. '3,5,8' -> 5.333...).

    Returns None for invalid input (non-string, empty, non-integer or negative item).
    """
    if not isinstance(weights_csv, str) or not weights_csv.strip():
        return None
    values = []
    for item in weights_csv.split(','):
        try:
            value = int(item.strip())
        except (ValueError, OverflowError):
            return None
        if value < 0:
            return None
        values.append(value)
    try:
        return sum(values) / len(values)
    except OverflowError:
        return None


def payable_charge(text):
    """Parse 'charge|discount' and return charge * 1.18 - discount (never below 0).

    Returns None for invalid input (non-string, wrong number of '|',
    non-numeric / non-finite / negative values).
    """
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    try:
        charge = float(parts[0].strip())
        discount = float(parts[1].strip())
    except (ValueError, OverflowError):
        return None
    if not (math.isfinite(charge) and math.isfinite(discount)):
        return None
    if charge < 0 or discount < 0:
        return None
    total = charge * 1.18 - discount
    if not math.isfinite(total):
        return None
    return max(total, 0)


def _ask(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None


def main():
    print("==== Running parse_order ====")
    result = parse_order(_ask("Enter garment:weight in kg (e.g. regular:6): "))
    print("Garment and Weight:", result if result is not None else "Invalid input")

    print("\n==== Running weight_average ====")
    result = weight_average(_ask("Enter garment weights as CSV (e.g. 3,5,8): "))
    print("Average Weight:", result if result is not None else "Invalid input")

    print("\n==== Running payable_charge ====")
    result = payable_charge(_ask("Enter charge|discount (e.g. 300|40): "))
    print("Payable Charge:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()
