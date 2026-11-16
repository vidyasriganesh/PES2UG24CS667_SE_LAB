
"""Library catalog management module."""

import hashlib
import json
import secrets
from pathlib import Path

CATALOG = {
    "B01": {"title": "Clean Code", "copies": 3},
    "B02": {"title": "The Pragmatic Programmer", "copies": 1},
    "B03": {"title": "Design Patterns", "copies": 2},
}


def issue_book(book_id, patron, active_issues=None):
    """Issue a book when copies are available."""
    if active_issues is None:
        active_issues = []

    if book_id not in CATALOG or CATALOG[book_id]["copies"] <= 0:
        return False

    CATALOG[book_id]["copies"] -= 1
    active_issues.append(f"Issued book {book_id} to patron {patron}")
    return True


def return_book(book_id):
    """Return a book, reporting whether the book ID exists."""
    if book_id not in CATALOG:
        return False

    CATALOG[book_id]["copies"] += 1
    return True


def check_availability(book_id):
    """Check whether a book exists and has available copies."""
    book = CATALOG.get(book_id)
    return book is not None and book["copies"] > 0


def calculate_fine(days_overdue, daily_rate=2.0):
    """Calculate a fine using a fixed daily rate."""
    if days_overdue < 0 or daily_rate < 0:
        raise ValueError("Days overdue and daily rate must be non-negative")

    return days_overdue * daily_rate


def generate_patron_hash(patron_id):
    """Generate a SHA-256 digest for a patron identifier."""
    return hashlib.sha256(patron_id.encode("utf-8")).hexdigest()


def generate_temp_patron_pin():
    """Generate a cryptographically secure four-digit PIN."""
    return f"{secrets.randbelow(9000) + 1000}"


def export_catalog(filename="catalog_export.json"):
    """Export the catalog as JSON."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(CATALOG, file, indent=4)
    return output_path


def main():
    """Demonstrate the library catalog functions."""
    issue_book("B01", "P101")
    return_book("B02")

    print("Is B01 available:", check_availability("B01"))
    print("Fine accrued:", calculate_fine(4))
    print("Patron Hash:", generate_patron_hash("P101"))
    print("Temp PIN:", generate_temp_patron_pin())
    print("Catalog exported to:", export_catalog())


if __name__ == "__main__":
    main()
