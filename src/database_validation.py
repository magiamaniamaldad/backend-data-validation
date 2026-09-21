import csv
import sqlite3
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "orders.csv"


def create_database():
    connection = sqlite3.connect(":memory:")

    connection.execute(
        """
        CREATE TABLE orders (
            order_id TEXT,
            customer_id TEXT,
            amount REAL,
            currency TEXT,
            status TEXT,
            created_at TEXT
        )
        """
    )

    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            connection.execute(
                """
                INSERT INTO orders (
                    order_id,
                    customer_id,
                    amount,
                    currency,
                    status,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    row["order_id"],
                    row["customer_id"],
                    float(row["amount"]) if row["amount"] else None,
                    row["currency"],
                    row["status"],
                    row["created_at"],
                ),
            )

    connection.commit()
    return connection


def find_duplicate_orders(connection):
    return connection.execute(
        """
        SELECT order_id, COUNT(*)
        FROM orders
        GROUP BY order_id
        HAVING COUNT(*) > 1
        """
    ).fetchall()


def find_invalid_amounts(connection):
    return connection.execute(
        """
        SELECT order_id
        FROM orders
        WHERE amount IS NULL OR amount <= 0
        """
    ).fetchall()


def find_invalid_currencies(connection):
    return connection.execute(
        """
        SELECT order_id
        FROM orders
        WHERE currency NOT IN ('USD', 'EUR', 'ARS')
           OR currency IS NULL
        """
    ).fetchall()


def find_invalid_statuses(connection):
    return connection.execute(
        """
        SELECT order_id
        FROM orders
        WHERE status NOT IN ('completed', 'pending', 'cancelled')
           OR status IS NULL
        """
    ).fetchall()


if __name__ == "__main__":
    db = create_database()

    print("Duplicate orders:", find_duplicate_orders(db))
    print("Invalid amounts:", find_invalid_amounts(db))
    print("Invalid currencies:", find_invalid_currencies(db))
    print("Invalid statuses:", find_invalid_statuses(db))

    db.close()
