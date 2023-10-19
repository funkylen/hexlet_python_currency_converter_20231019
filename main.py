from online import get_currencies


# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 7. Вывод результата

online_response = get_currencies()


def convert(amount, from_ticker, to_ticker, currencies):
    from_currency = currencies.get(from_ticker)
    to_currency = currencies.get(to_ticker)

    coefficient = to_currency / from_currency
    return round(amount * coefficient, 2)


def input_currency(input_message, currencies):
    ticker = input(f"{input_message}: ").strip()

    currency = currencies.get(ticker, None)
    if currency is None:
        print(f'Ошибка при поиске валюты: {ticker}')
        exit()

    return ticker


current_currencies = {
    'RUB': 97.4545572753,
    'EUR': 0.9487101161,
    'USD': 1,
}

print("Привет, это программа Конвертер Валют!")

print("""
Для работы с программой требуется:
- выбрать исходную валюту 
- выбрать в какую валюту следует перевести
- ввести количество исходной валюты

Доступные валюты:
""")

for currency in current_currencies:
    print(f'- {currency}')

from_ticker = input_currency("Введите исходную валюту", current_currencies)
to_ticker = input_currency("Введите в какую валюту следует перевести", current_currencies)

amount_input = input("Введите количество валюты: ")
amount = int(amount_input)

result = convert(amount, from_ticker, to_ticker, current_currencies)

print(f'Результат: {amount} {from_ticker} = {result} {to_ticker}')
