import pytest

from sales_report import (
    calculate_revenue,
    calculate_total_revenue,
    calculate_total_quantity,
    build_product_report,
    get_float,
    get_int,
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


def test_calculate_total_revenue_empty_list():
    assert calculate_total_revenue([]) == 0


def test_calculate_total_quantity_empty_list():
    assert calculate_total_quantity([]) == 0


def test_build_product_report_empty_list():
    assert build_product_report([]) == {}
    assert build_product_report([]) == {}


def test_get_float_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda message: "10.5")

    assert get_float("Цена: ") == 10.5


def test_get_float_invalid_text(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda message: "abc")

    assert get_float("Цена: ") is None

    captured = capsys.readouterr()
    assert "Нужно ввести число" in captured.out


@pytest.mark.parametrize("user_input", [
    "0",
    "-5",
])
def test_get_float_not_positive(monkeypatch, capsys, user_input):
    monkeypatch.setattr("builtins.input", lambda message: user_input)

    assert get_float("Цена: ") is None

    captured = capsys.readouterr()
    assert "Число должно быть больше нуля" in captured.out


def test_get_int_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda message: "3")

    assert get_int("Количество: ") == 3


@pytest.mark.parametrize("user_input", [
    "abc",
    "2.5",
])
def test_get_int_invalid_text(monkeypatch, capsys, user_input):
    monkeypatch.setattr("builtins.input", lambda message: user_input)

    assert get_int("Количество: ") is None

    captured = capsys.readouterr()
    assert "Нужно ввести целое число" in captured.out


@pytest.mark.parametrize("user_input", [
    "0",
    "-1",
])
def test_get_int_not_positive(monkeypatch, capsys, user_input):
    monkeypatch.setattr("builtins.input", lambda message: user_input)

    assert get_int("Количество: ") is None

    captured = capsys.readouterr()
    assert "Число должно быть больше нуля" in captured.out
