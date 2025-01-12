from functions import *

while True:
    command = input('Что вам нужно? (эспрессо/латте/капучино): ')

    if command.lower() in ['эспрессо', 'латте', 'капучино']:
        diction = choosing_type_of_coffee(command)

        if checking_payment(diction, diction):
            if checking_storage(diction) and making_coffee(diction):
                print(f"Вот ваш {command.lower()}")
            else:
                print(f'Извените, у нас недостаточтно ресурсов что-бы сделать ваш {command}')
        else:
            print("Недостаточно средств для оплаты")

    elif command.lower() == "отчет":
        checking_storage(show_storage_items=True)

    elif command == "off":
        print('Выключаюсь...')
        break
    else:
        print('Не понял вас')
