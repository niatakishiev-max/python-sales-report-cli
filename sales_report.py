import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "sales.json"


def load_sales():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_sales():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(sales, f, ensure_ascii=False, indent=4)


sales = load_sales()


def add_sale():
    product = input("Товар: ").strip()

    if product == "":
        print("Название товара не может быть пустым")
        return

    price = get_float("Цена: ")

    if price is None:
        return

    quantity = get_int("Количество: ")

    if quantity is None:
        return

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity
    }

    sales.append(sale)

    save_sales()

    print("Продажа добавлена")


def get_float(message):
    try:
        value = float(input(message))
    except ValueError:
        print("Нужно ввести число")
        return None

    if value <= 0:
        print("Число должно быть больше нуля")
        return None

    return value


def get_int(message):
    try:
        value = int(input(message))
    except ValueError:
        print("Нужно ввести целое число")
        return None

    if value <= 0:
        print("Число должно быть больше нуля")
        return None

    return value


def show_sales():
    if len(sales) == 0:
        print("Продаж пока нет")
    else:
        for sale in sales:
            revenue = sale["price"] * sale["quantity"]

            print(
                sale["product"],
                "| цена:", sale["price"],
                "| количество:", sale["quantity"],
                "| выручка:", revenue
            )


def delete_sale():
    if len(sales) == 0:
        print("Продаж пока нет")
        return

    show_sales()

    index = get_int("Номер продажи для удаления: ")

    if index is None:
        return

    if index < 1 or index > len(sales):
        print("Неверный номер продажи")
        return

    sales.pop(index - 1)

    save_sales()

    print("Продажа удалена")


def show_total_revenue():
    total = 0

    for sale in sales:
        total += sale["price"] * sale["quantity"]

    print("Общая выручка:", total)


def show_total_quantity():
    total_quantity = 0

    for sale in sales:
        total_quantity += sale["quantity"]

    print("Всего продано товаров:", total_quantity)


def show_product_report():
    report = {}

    for sale in sales:
        product = sale["product"]
        revenue = sale["price"] * sale["quantity"]

        if product not in report:
            report[product] = {
                "quantity": 0,
                "revenue": 0
            }

        report[product]["quantity"] += sale["quantity"]
        report[product]["revenue"] += revenue

    if len(report) == 0:
        print("Продаж пока нет")
    else:
        for product, data in report.items():
            print(
                product,
                "| количество:", data["quantity"],
                "| выручка:", data["revenue"]
            )


def show_menu():
    print("\n1 - Добавить продажу")
    print("2 - Показать продажи")
    print("3 - Показать общую выручку")
    print("4 - Показать общее количество товаров")
    print("5 - Отчёт по товарам")
    print("6 - Удалить продажу")
    print("7 - Выход")


def main():
    while True:
        show_menu()

        choice = input("Выбери: ")

        if choice == "1":
            add_sale()

        elif choice == "2":
            show_sales()

        elif choice == "3":
            show_total_revenue()

        elif choice == "4":
            show_total_quantity()

        elif choice == "5":
            show_product_report()

        elif choice == "6":
            delete_sale()

        elif choice == "7":
            print("Выход")
            break

        else:
            print("Неверная команда")



if __name__ == "__main__":
    main()
