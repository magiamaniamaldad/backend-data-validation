import csv
from collections import Counter
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "orders.csv"

VALID_CURRENCIES = {"USD", "EUR", "ARS"}
VALID_STATUSES = {"completed", "pending", "cancelled"}


def load_orders():
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def validate_orders(orders):
    errors = []

    order_ids = [order["order_id"] for order in orders]
    duplicate_ids = {
        order_id
        for order_id, count in Counter(order_ids).items()
        if count > 1
    }

    for row_number, order in enumerate(orders, start=2):
        order_id = order["order_id"]

        if order_id in duplicate_ids:
            errors.append(
                f"Row {row_number}: duplicate order_id '{order_id}'"
            )

        if not order["amount"]:
            errors.append(
                f"Row {row_number}: amount is required"
            )
        else:
            try:
                amount = float(order["amount"])
                if amount <= 0:
                    errors.append(
                        f"Row {row_number}: amount must be greater than 0"
                    )
            except ValueError:
                errors.append(
                    f"Row {row_number}: amount must be numeric"
                )

        if order["currency"] not in VALID_CURRENCIES:
            errors.append(
                f"Row {row_number}: invalid currency '{order['currency']}'"
            )

        if order["status"] not in VALID_STATUSES:
            errors.append(
                f"Row {row_number}: invalid status '{order['status']}'"
            )

    return errors


if __name__ == "__main__":
    orders = load_orders()
    errors = validate_orders(orders)

    print(f"Validated {len(orders)} orders.")

    if errors:
        print(f"Found {len(errors)} validation issue(s):")
        for error in errors:
            print(f"- {error}")
    else:
        print("All orders passed validation.")
