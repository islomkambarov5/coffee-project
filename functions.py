from dictionaris import *


def choosing_type_of_coffee(coffee: str):
    if coffee.lower() == 'эспрессо':
        return espresso
    elif coffee.lower() == 'латте':
        return latte
    elif coffee.lower() == 'капучино':
        return cappuccino


def checking_payment(coffee, coffee_info):
    payment = input(f"{coffee.title()} стоит ${coffee_info['price']}\n"
                    f"Сколько будете платить?\n")
    try:
        payment = int(payment)
    except:
        overall = 0
        payment = (' '.join(payment.split(', '))).split(' ')
        for price in range(0, len(payment) - 1, 2):
            overall += float(payment[price]) * float(currency[payment[price + 1]])
        payment = overall

    if payment >= coffee['price']:
        return True
    else:
        return False


def checking_storage(coffee: dict = None, show_storage_items=False):
    if coffee is not None and storage['milk'] - coffee['milk'] >= 0 and storage['water'] - coffee['water'] >= 0 and \
            storage['coffee'] - coffee['coffee'] >= 0:

        return True
    elif show_storage_items:
        print(
            f"Воде: {storage['water']} мл\n"
            f"Молоко: {storage['milk']} мл\n"
            f"Кофе: {storage['coffee']} гр\n"
            f"Доход: ${storage['profit']}"
        )
    else:
        return False


def making_coffee(coffee: dict):
    try:
        storage['milk'] -= coffee['milk']
        storage['water'] -= coffee['water']
        storage['coffee'] -= coffee['coffee']
        return True
    except:
        return False
