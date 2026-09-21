from src.database_validation import (
    create_database,
    find_duplicate_orders,
    find_invalid_amounts,
    find_invalid_currencies,
    find_invalid_statuses,
)


def test_find_duplicate_orders():
    connection = create_database()

    duplicates = find_duplicate_orders(connection)

    assert len(duplicates) > 0
    assert any(order_id == "1008" for order_id, count in duplicates)

    connection.close()


def test_find_invalid_amounts():
    connection = create_database()

    invalid_orders = find_invalid_amounts(connection)
    invalid_ids = [row[0] for row in invalid_orders]

    assert "1003" in invalid_ids
    assert "1005" in invalid_ids

    connection.close()


def test_find_invalid_currencies():
    connection = create_database()

    invalid_orders = find_invalid_currencies(connection)
    invalid_ids = [row[0] for row in invalid_orders]

    assert "1007" in invalid_ids

    connection.close()


def test_find_invalid_statuses():
    connection = create_database()

    invalid_orders = find_invalid_statuses(connection)
    invalid_ids = [row[0] for row in invalid_orders]

    assert "1008" in invalid_ids

    connection.close()
