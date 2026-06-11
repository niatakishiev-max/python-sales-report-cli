import pytest

from sales_report import (
    calculate_revenue,
    calculate_total_revenue,
    calculate_total_quantity,
    build_product_report,
)


@pytest.mark.parametrize("price, quantity, expected", [
    (100, 2, 200),
    (50, 3, 150),
    (10.5, 2, 21.0),
])
def test_calculate_revenue(price, quantity, expected):
    sale = {
        "product": "test product",
        "price": price,
        "quantity": quantity
    }

    assert calculate_revenue(sale) == expected


def test_calculate_total_revenue():
    sales = [
        {"product": "хлеб", "price": 100, "quantity": 2},
        {"product": "молоко", "price": 50, "quantity": 3},
        {"product": "вода", "price": 10, "quantity": 5},
    ]

    assert calculate_total_revenue(sales) == 400


def test_calculate_total_quantity():
    sales = [
        {"product": "хлеб", "price": 100, "quantity": 2},
        {"product": "молоко", "price": 50, "quantity": 3},
        {"product": "вода", "price": 10, "quantity": 5},
    ]

    assert calculate_total_quantity(sales) == 10


def test_build_product_report():
    sales = [
        {"product": "хлеб", "price": 100, "quantity": 2},
        {"product": "молоко", "price": 50, "quantity": 3},
        {"product": "хлеб", "price": 100, "quantity": 1},
    ]

    expected = {
        "хлеб": {
            "quantity": 3,
            "revenue": 300
        },
        "молоко": {
            "quantity": 3,
            "revenue": 150
        }
    }

    assert build_product_report(sales) == expected
