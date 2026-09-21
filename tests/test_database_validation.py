import sqlite3

from src.database_validation import (
    create_orders_table,
    find_duplicate_orders,
    find_invalid_amounts,
    find_invalid_statuses,
)


def create_test_database():
    connection = sqlite3.connect(":memory:")
    create_orders_table(connection)
    return connection


def test_find_duplicate_orders():
    connection = create_test_database()

    connection.executemany(
        """
        INSERT INTO orders (order_id, customer, amount, currency, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (1001, "Ana", 120.0, "USD", "completed"),
            (1001, "Ana", 120.0, "USD", "completed"),
            (1002, "Luis", 80.0, "USD", "pending"),
        ],
    )

    duplicates = find_duplicate_orders(connection)

    assert 1001 in duplicates
    connection.close()


def test_find_invalid_amounts():
    connection = create_test_database()

    connection.executemany(
        """
        INSERT INTO orders (order_id, customer, amount, currency, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (1001, "Ana", 120.0, "USD", "completed"),
            (1002, "Luis", -50.0, "USD", "pending"),
        ],
    )

    invalid_orders = find_invalid_amounts(connection)

    assert 1002 in invalid_orders
    connection
