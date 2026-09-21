from src.validate_orders import validate_orders


def test_valid_order_has_no_errors():
    orders = [
        {
            "order_id": "1001",
            "customer_id": "C001",
            "amount": "1250.50",
            "currency": "USD",
            "status": "completed",
            "created_at": "2026-09-01",
        }
    ]

    assert validate_orders(orders) == []


def test_negative_amount_is_detected():
    orders = [
        {
            "order_id": "1001",
            "customer_id": "C001",
            "amount": "-100",
            "currency": "USD",
            "status": "completed",
            "created_at": "2026-09-01",
        }
    ]

    errors = validate_orders(orders)

    assert any("amount must be greater than 0" in error for error in errors)


def test_invalid_currency_is_detected():
    orders = [
        {
            "order_id": "1001",
            "customer_id": "C001",
            "amount": "100",
            "currency": "INVALID",
            "status": "completed",
            "created_at": "2026-09-01",
        }
    ]

    errors = validate_orders(orders)

    assert any("invalid currency" in error for error in errors)


def test_duplicate_order_id_is_detected():
    orders = [
        {
            "order_id": "1001",
            "customer_id": "C001",
            "amount": "100",
            "currency": "USD",
            "status": "completed",
            "created_at": "2026-09-01",
        },
        {
            "order_id": "1001",
            "customer_id": "C002",
            "amount": "200",
            "currency": "USD",
            "status": "pending",
            "created_at": "2026-09-02",
        },
    ]

    errors = validate_orders(orders)

    assert any("duplicate order_id" in error for error in errors)
